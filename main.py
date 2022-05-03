import sqlite3
from SQLCheckPlus import SQLCheckPlus
import util
import sys
import os


if __name__=='__main__':
    # -----------------------SQLCheck+ Extractor-----------------------
    
   
    threshold = float(sys.argv[2]) if len(sys.argv)==3 else 0.15

    sqlite_filename = sys.argv[1].split("/")[-1]
    path = '/'.join(sys.argv[1].split("/")[:-1])+'/'
    sqlite_path = path
    filename = util.extract_schema_from_sqlite(path, sqlite_filename)
    # print(filename)

    path = '/'.join(filename.split("/")[:-1])+'/'
    filename = filename.split("/")[-1]
    input_name = path + filename
    sqlfilename = filename
    sqlcheck_filename = 'SQLCheck_'+ filename.split('.')[0] + '.txt'
    sqlcheckPlus_filename = 'SQLCheckPlus_'+ filename.split('.')[0] + '.txt'
    output_name = path + sqlcheck_filename



    os.system(f"sqlcheck.exe -f {input_name} > {output_name}")

    print(f"[SQLCheck Done] Collected SQLCheck AP report in {output_name}")

    sqlcheck_aps = util.get_APs(path, sqlcheck_filename, sqlfilename)

    # for each in sqlcheck_aps:
    #     print(each) # debug


    # -----------------------SQLCheck+ Analyzer-----------------------
# TODO: 
    sqlcheckPlus_instance = util.get_sqlcheck_aps(sqlcheck_aps, sqlite_path, sqlite_filename, threshold)
    sqlcheckPlus_aps = sqlcheckPlus_instance.getAPReport()
    ap_stats = sqlcheckPlus_instance.getAPstats()


    sep = \
    '''\n-------------------------------------------------\n'''

    with open( path + sqlcheckPlus_filename, 'w') as sqlcheckPlus_f:
        sqlcheckPlus_f.write("AP Report Summary")

        for each in sqlcheckPlus_aps:
            sql, aps = each
            sqlcheckPlus_f.write(sep + "SQL Statement: " + sql + '\n' + ''.join(aps))

        sqlcheckPlus_f.write(ap_stats)
    
    SQLCheckPlus_output_filename =  path + sqlcheckPlus_filename
    print(f"[SQLCheckPlus Done] Results written to {SQLCheckPlus_output_filename}")

    
