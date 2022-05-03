def find_potential_columns(s):
    # process sql statement to find potential columns
    potential_columns = []
    words = s.split(' ')
    for i in range(len(words)-1):
        if words[i].endswith('id') and  words[i+1].startswith('text') and ',' not in words[i]  and '\n' not in words[i]:
            potential_columns.append(words[i])
    return potential_columns

def get_tablename(s):
    return s.split(' ')[2]   

def sqlite_table_schema(conn, name):
    cursor = conn.execute("SELECT sql FROM sqlite_master WHERE name=?;", [name])
    sql = cursor.fetchone()[0]
    cursor.close()
    return sql

class APVerifier:
    @classmethod
    def verify_MultiValueAttribute(cls, conn, sql, ap):
        isAP = True
        potential_columns = find_potential_columns(sql)
        table_name = get_tablename(sql)
        query = f"SELECT {', '.join(potential_columns)} FROM {table_name} LIMIT 10;"  # use limit 10 for now * TODO: may apply random sampling
        # print(query) # debug
        cursor = conn.execute(query)
        results = cursor.fetchall()
        for row in results:
            for column_value in row:
                if len(column_value.split(','))>1: 
                    # may use a repeat threshold (e.g. 10%) to check if it actually contains malti-value - tunable
                    return isAP # => multi-valued AP
        isAP = False # AP not detected
        return ap if isAP else ""

    @classmethod
    def verify_GenericPrimaryKey(cls, conn, sql, ap):
        return ap if ' id ' in sql.lower() else ""

    @classmethod
    def verify_ImpreciseDataType(cls, conn, sql, ap):
        return ap \
            if ' real,' in sql.lower() or ' real)' in sql.lower() or ' float,' in sql.lower() or ' float)' in sql.lower() \
            else ""

    @classmethod
    def verify_ValuesInDefinition(cls, conn, sql, ap):
        return ap if ' enum ' in sql.lower() or ' enum(' in sql.lower() else ''
    
    @classmethod
    def verify_MetadataTribbles(cls, conn, sql, ap):
        if not ap.split(" ")[-2].isalpha():
            ap =  ap.replace('MEDIUM RISK', 'HINT')
        else :
            ap = ''
        return ap 

