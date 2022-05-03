import sqlite3
path = './exp/'
database = "synthetic.sqlite"
conn = sqlite3.connect(path + database) 

c = conn.cursor()
sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                    user_id text PRIMARY KEY,
                                    name text
                                ); """
c.execute(sql_create_users_table)

sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users_following (
                                    user_id text PRIMARY KEY,
                                    follows text
                                ); """
c.execute(sql_create_users_table)

# test foreign key does not exist constraint

sql_create_t1_table = """ CREATE TABLE IF NOT EXISTS T1 (
                                    t1 text PRIMARY KEY,
                                    t2 text
                                ); """
c.execute(sql_create_t1_table)

sql_create_t2_table = """ CREATE TABLE IF NOT EXISTS T2 (
                                    t2 text PRIMARY KEY,
                                    a text,
                                    b text
                                ); """
c.execute(sql_create_t2_table)
          
                   
conn.commit()

insert_sql = ''' INSERT INTO users(user_id, name)
            VALUES(?,?) '''
rows = [('u1', "user1"), \
        ('u2', "user2"), \
        ('u3', "user3"), \
        ('u4', "user4"), \
        ('u5', "user5")]

insert_sql = ''' INSERT INTO users_following(user_id, follows)
            VALUES(?,?) '''
rows = [('u1', "u2, u3"), \
        ('u2', "u3"), \
        ('u3', ""), \
        ('u4', "u3, u1, u2"), \
        ('u5', "u3")]

cur = conn.cursor()
for row in rows:
    cur.execute(insert_sql, row)

conn.commit()
conn.close()


try:
    conn = sqlite3.connect(path + database)
    c = conn.cursor()
    c.execute('''SELECT * FROM users;''')
    for row in c.fetchall():
        print(row)

except sqlite3.Error as error:
    print("Failed to execute the above query", error)
finally:
    if conn:
        conn.close()          



