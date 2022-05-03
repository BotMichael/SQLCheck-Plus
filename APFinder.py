def get_tablename(s):
    return s.split(' ')[2]  
def get_columns(cursor):
    return list(map(lambda x: x[0], cursor.description)) 

# def get_column_map(sql):
#     sql = sql.replace('\n', ' ')
#     i = sql.index('(')
#     j = sql.index(')')
#     sql2 = (sql[i+1:j]).split(', ')
#     cols = []
#     for each in sql2:
#         if each.split(' ')[0] and f" {each.split(' ')[0]} " in sql:
#             cols.append(each.split(' ')[0])
#     return cols

from collections import defaultdict
def find_MultiValueAttribute_AP(conn, sql, sep = ", ", threshold = 0.15, limit = None):
    '''
    for each text column, check if values separated by ', ' (or other separator) is repeated in more than 10% of the rows
    '''
    if limit:
        limit = f'LIMIT {limit}'
    else:
        limit = ''

    table_name = get_tablename(sql)
    cursor = conn.execute(f"SELECT * FROM {table_name} {limit};") 

    cnt = 0
    value_counter = defaultdict(dict)
    for row in cursor.fetchall():
        cnt += 1
        for i, col in enumerate(row):
            try:
                if type(col)==str and ("\n" in col or len(col)>50):
                    # it's likely the column stores a paragraph of text
                    continue
                words = col.split(sep) # may create overhead when text is long
            except:
                # may have wrong type problem
                continue

            if len(words) > 1:


                for word in words: 
                    # if not " " in word:
                    if word not in value_counter[i]:
                        value_counter[i][word] = 0
                    value_counter[i][word] += 1
   
    column_map = get_columns(cursor)
    cursor.close()

    max_frq = 0

    potential_cols = []
    for col, word_freq in value_counter.items():
        for freq in word_freq.values():
            max_frq = max(max_frq, freq)
            if freq >= max(threshold * cnt, 10):
                potential_cols.append(col)
                
                # print(word_freq)

                break

    print('stop at max freq: ', max_frq, 'threshold: ',  max(threshold * cnt, 10)) #debug

    
    potential_cols = [column_map[i] for i in potential_cols if not 'text' in column_map[i].lower()] # xx_text columns tend to report false-positives
    if potential_cols:
        AP_report_msg = \
f'''(HINT) (LOGICAL_DATABASE_DESIGN ANTI-PATTERN) Multi-Valued Attribute
[In {', '.join(potential_cols)} column(s), values separated by '{sep}' has exceeded the threshold {threshold}]
'''
    else:
        AP_report_msg = ''

    return AP_report_msg

def find_PrimaryKeyDoesNotExist_AP(sql):
    AP_report_msg = ''
    if 'primary key' not in sql.lower():
        AP_report_msg = \
f'''(HIGH RISK) (LOGICAL_DATABASE_DESIGN ANTI-PATTERN) No Primary Key
[No Primary key has been defined in the table]
'''

    return AP_report_msg

def find_ForeignKeyDoesNotExist_AP(conn, sql, limit = 10):
    if limit:
        limit = f'LIMIT {limit}'
    else:
        limit = ''
    table_name = get_tablename(sql)
    cursor = conn.execute(f"SELECT * FROM {table_name} {limit};") 
    column_names = get_columns(cursor)

    flag = False
    ap_col = []
    counter = 0
    cnt_cols = []
    for col in column_names:
        col = col.lower()
        # if col.endswith("id") and len(col)>2:
        if ('_id' in col or col.endswith("id") ) and len(col)>2:
            if '_' in col:
                added = False
                for each in col.split('_')[:-1]:
                    if each not in table_name.lower().split('_') and \
                        each+'s' not in table_name.lower().split('_') :
                        ap_col.append(col)
                        added = True
                        break
                if not added:
                    cnt_cols.append(col)
            else:
                # print( col[:-2] , table_name.lower())
                if col[:-2] not in table_name.lower().split('_') and \
                    col[:-2]+'s' not in table_name.lower().split('_'):
                    ap_col.append(col)
                else:
                    cnt_cols.append(col)
    if len(cnt_cols)>=2:
        ap_col += cnt_cols 
    # print(table_name, ap_col, cnt_cols)

    AP_report_msg = ''
    if ap_col and 'foreign key' not in sql.lower():
        AP_report_msg = \
f'''(HIGH RISK) (LOGICAL_DATABASE_DESIGN ANTI-PATTERN) No Foreign Key
[{', '.join(ap_col)} column(s) have been identified as potential foreign keys from other table but no referential integrity constraints have been established.]
'''
    return AP_report_msg




class APFinder:
    @classmethod
    def findAP(cls, conn, sql, threshold)->bool:
        ap_list = []
        MultiValueAttribute_AP = find_MultiValueAttribute_AP(conn, sql, threshold=threshold)
        PrimaryKeyDoesNotExist_AP = find_PrimaryKeyDoesNotExist_AP(sql)

        ForeignKeyDoesNotExist_AP = find_ForeignKeyDoesNotExist_AP(conn, sql)

        if MultiValueAttribute_AP:
            ap_list.append(MultiValueAttribute_AP)
        
        if PrimaryKeyDoesNotExist_AP:
            ap_list.append(PrimaryKeyDoesNotExist_AP)

        if ForeignKeyDoesNotExist_AP:
            ap_list.append(ForeignKeyDoesNotExist_AP)


        #TODO: foreign key


        

        return ap_list