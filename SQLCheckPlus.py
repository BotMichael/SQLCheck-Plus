import sqlite3
from APFinder import APFinder
from APVerifier import APVerifier

def sqlite_table_schema(conn, name):
    cursor = conn.execute("SELECT sql FROM sqlite_master WHERE name=?;", [name])
    sql = cursor.fetchone()[0]
    cursor.close()
    return sql

def extract_schema_from_sqlite2(path, sqlite3dbName):
    try:
        conn = sqlite3.connect(path + sqlite3dbName)
        sql_query = """SELECT name FROM sqlite_master 
        WHERE type='table';"""
        cursor = conn.cursor()
        cursor.execute(sql_query)
        tables = []
        for t in cursor.fetchall():
            tables.append(sqlite_table_schema(conn, t[0]))
    except sqlite3.Error as error:
        print("Failed to execute the above query", error)
    finally:
        if conn:
            conn.close()          
    return ';\n'.join(tables).replace('"', '') + ";" 


class SQLCheckPlus:
    def __init__(self, APs, sqlite_path, sqlite_filename, threshold):
        self.APlist = []
        self.conn = sqlite3.connect(sqlite_path + sqlite_filename)

        sqls = extract_schema_from_sqlite2(sqlite_path, sqlite_filename).lower().split(';\n')
        sql_map = dict()
        
        _APS = []
        for i, sql in enumerate(sqls):
            sql_map[sql.split(' ')[2]] = i
            _APS.append([sql, ''])

        for sql, aps in APs:
            idx = sql_map[sql.split(' ')[2]] 
            _APS[idx][1] = aps

        for sql, aps in _APS:
            ap_result = self.process(sql, aps, threshold)
            if ap_result:
                # if 'medium' in ''.join(ap_result).lower():
                #     print(sql, ap_result)
                self.APlist.append((sql, ap_result))
    
    def examineSQLAP(self, sql, threshold):
        return APFinder.findAP(self.conn, sql, threshold)

    def verifyAP(self, sql, ap):
        isAP = ap
        if ap=='':
            # sqlcheck does not report AP for this sql statement
            pass 
        elif "Multi-Valued Attribute" in ap:
            isAP = APVerifier.verify_MultiValueAttribute(self.conn, sql, ap)
        elif "Generic Primary Key" in ap:
            isAP = APVerifier.verify_GenericPrimaryKey(self.conn, sql, ap)
        elif "Metadata Tribbles" in ap:
            # print(ap)
            isAP = APVerifier.verify_MetadataTribbles(self.conn, sql, ap)
            # print(sql, isAP)
        elif "Imprecise Data Type" in ap:
            isAP = APVerifier.verify_ImpreciseDataType(self.conn, sql, ap)
        elif "Values In Definition" in ap:
            isAP = APVerifier.verify_ValuesInDefinition(self.conn, sql, ap) 
        elif "(QUERY ANTI-PATTERN)" in ap:
            # SQLCheck+ targets schema related APs only
            isAP = ''

        return isAP

    def process(self, sql, aps, threshold):
        '''
        verify each SQLCheck reported AP, return true APs
        '''
        result = self.examineSQLAP(sql, threshold)
        
        for ap in aps:
            isAP = self.verifyAP(sql, ap)
            if isAP:
                result.append(isAP)
        return result

    def getAPReport(self):
        return self.APlist

    def getAPstats(self):
        high = medium = low = hint = 0
        _aps = []
        for sql, aps in self.APlist:
            for ap in aps:
                # print(sql, ap)
                if 'HIGH RISK' in ap:
                    high += 1
                elif 'MEDIUM RISK' in ap:
                    medium += 1 
                elif 'LOW RISK' in ap:
                    low += 1 
                elif 'hint' in ap.lower():
                    hint += 1 
            _aps += aps
        ap_stats = \
f'''
==================== Summary ===================
All Anti-Patterns and Hints  :: {high + medium + low + hint}
>  High Risk   :: {high}
>  Medium Risk :: {medium}
>  Low Risk    :: {low}
>  Hints       :: {hint}

''' 
# \
#  + '\n'.join(_aps)

        return ap_stats
        