import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

def ranking():
    SELECT_SQL = 'SELECT userid,level,EXP FROM member ORDER BY level DESC LIMIT 10;'
    cursor.execute(SELECT_SQL)
    row = cursor.fetchall()
    i=1
    for rows in row:
        userid, level, EXP = rows
        print(f'{i}등 - {userid} : {level}Level, {EXP}EXP')
        i+=1

