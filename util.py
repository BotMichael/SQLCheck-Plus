import sqlite3

def sqlite_table_schema(conn, name):
    cursor = conn.execute("SELECT sql FROM sqlite_master WHERE name=?;", [name])
    sql = cursor.fetchone()[0]
    cursor.close()
    return sql

def extract_schema_from_sqlite(path, sqlite3dbName):
    try:
        # print(path + sqlite3dbName)
        conn = sqlite3.connect(path + sqlite3dbName)
        # Getting all tables from sqlite_master
        sql_query = """SELECT name FROM sqlite_master 
        WHERE type='table';"""
        # Creating cursor object using connection object
        cursor = conn.cursor()
        cursor.execute(sql_query)

        tables = []
        for t in cursor.fetchall():
            tables.append(sqlite_table_schema(conn, t[0]))

    except sqlite3.Error as error:
        print("Failed to execute the above query", error)
    finally:
        # Inside Finally Block, If connection is
        # open, we need to close it
        if conn:
            # using close() method, we will close 
            # the connection
            conn.close()          
            # After closing connection object, we 
            # will print "the sqlite connection is 
            # closed"
            # print(f"[Done] The sqlite connection for {sqlite3dbName} is closed")
    # path = './sql-schema/'
    with open(path + sqlite3dbName[:-7] + '.sql', 'w') as f_write_schema:
        f_write_schema.write( ';\n'.join(tables).replace('"', '') + ";" )
    return path + sqlite3dbName[:-7] + '.sql'



def test_connection(path, sqlite3dbName):
    try:
        conn = sqlite3.connect(path+sqlite3dbName)
        # Getting all tables from sqlite_master
        sql_query = """
        SELECT * FROM Player 
        LIMIT 10;
        """
        # Creating cursor object using connection object
        cursor = conn.cursor()
        cursor.execute(sql_query)

        results = []
        for t in cursor.fetchall():
            results.append(t)
        print(results)

    except sqlite3.Error as error:
        print("Failed to execute the above query", error)
    finally:
        if conn:
            conn.close()          
            



def get_SQL_Statement(ap_report):
    statement = ap_report.split(';')[0].split('Statement: ')[1]
    return statement + ';'

def get_SQL_APs(ap_report, path, filename):
    aps = [i.rstrip('\n')+"\n" for i in ap_report.split(f"[{path}{filename}]: ")[1:] ]
    return aps

def get_APs(path, filename, sqlitename):
    with open(path + filename, 'r') as f:
        SQLs = []
        flag = False
        for line in f:
            if line.startswith("SQL Statement:"):
                flag = True
                SQLs.append("")
            if line.startswith('---') or line.startswith('==='):
                flag = False
            if flag:
                SQLs[-1] += line
                


        # path = './exp/'
        # filename = 'The-History-of-Baseball.sql'
        filename = sqlitename
        ap = []
        for ap_report in SQLs:
            ap.append( (get_SQL_Statement(ap_report), get_SQL_APs(ap_report, path, filename)) )

        return ap

from SQLCheckPlus import SQLCheckPlus
def get_sqlcheck_aps(APs, sqlite_path, sqlite_filename, threshold):
    return SQLCheckPlus(APs, sqlite_path, sqlite_filename, threshold)
