import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

def login_ok(userid, userpw):
    SELECT_SQL = f"SELECT * FROM member WHERE userid='{userid}' AND userpw='{userpw}';"
    cursor.execute(SELECT_SQL)
    user_list = cursor.fetchall()
    if user_list and user_list[0][1] == userid and user_list[0][2] == userpw:
        return True, userid
    else:
        return False
    
def new_member(new_userid, new_userpw):
    SELECT_SQL = f"SELECT * FROM member WHERE userid='{new_userid}';"
    cursor.execute(SELECT_SQL)
    user_list = cursor.fetchall()
    if user_list and user_list[0][1] == new_userid:
        return False
    else:
        INSERT_SQL = f"INSERT INTO member(userid,userpw,level,EXP) VALUES ('{new_userid}','{new_userpw}',0,0);"
        cursor.execute(INSERT_SQL)
        conn.commit()
        return True
    
def member_out_ok(out_userid, out_userpw):
    SELECT_SQL = f"SELECT * FROM member WHERE userid='{out_userid}';"
    cursor.execute(SELECT_SQL)
    user_list = cursor.fetchall()
    if user_list and user_list[0][1] == out_userid and user_list[0][2] == out_userpw:
        DELETE_SQL = f"DELETE FROM member WHERE userid='{out_userid}' AND userpw='{out_userpw}';"
        cursor.execute(DELETE_SQL)
        conn.commit()
        return True
    else:
        return False
    