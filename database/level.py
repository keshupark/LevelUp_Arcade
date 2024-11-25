import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

def level_up(userid):
    SELECT_SQL = f"SELECT userid,level,EXP FROM member WHERE userid='{userid}';"
    cursor.execute(SELECT_SQL)
    row = cursor.fetchone()
    userid, level, EXP = row
        
    if EXP // 1000 != 0:
        up = EXP // 1000
        UPDATE_SQL = f"UPDATE member SET level='{up}' WHERE userid='{userid}';"
        cursor.execute(UPDATE_SQL)
        conn.commit()
        cursor.execute(SELECT_SQL)
        row = cursor.fetchone()
        userid, level, EXP = row
  
    print(f"현재 {userid}님의 레벨은 {level}, 경험치는 {EXP}입니다.")
    
def rsp_EXP_UP(userid):
    SELECT_SQL = f"SELECT userid,EXP FROM member WHERE userid='{userid}';"
    cursor.execute(SELECT_SQL)
    row = cursor.fetchone()
    userid, EXP = row
    EXP_plus=EXP+100
    UPDATE_SQL = f"UPDATE member SET EXP='{EXP_plus}' WHERE userid='{userid}';"
    cursor.execute(UPDATE_SQL)
    conn.commit()

def coin_game_EXP_UP(userid):
    SELECT_SQL = f"SELECT userid,EXP FROM member WHERE userid='{userid}';"
    cursor.execute(SELECT_SQL)
    row = cursor.fetchone()
    userid, EXP = row
    EXP_plus=EXP+300
    UPDATE_SQL = f"UPDATE member SET EXP='{EXP_plus}' WHERE userid='{userid}';"
    cursor.execute(UPDATE_SQL)
    conn.commit()
    
def break_blocks_EXP_UP(userid,score):
    SELECT_SQL = f"SELECT userid,EXP FROM member WHERE userid='{userid}';"
    cursor.execute(SELECT_SQL)
    row = cursor.fetchone()
    userid, EXP = row
    if score < 80:
        EXP_plus=EXP
        return print(f"게임에서 {score}점을 달성하여 경험치 획득에 실패하였습니다.")
    elif 80 <= score < 200:
        EXP_plus=EXP+100
    elif 200 <= score < 350:
        EXP_plus=EXP+200
    elif 350 <= score < 390:
        EXP_plus=EXP+300
    elif 390 <= score:
        EXP_plus=EXP+400
    UPDATE_SQL = f"UPDATE member SET EXP='{EXP_plus}' WHERE userid='{userid}';"
    cursor.execute(UPDATE_SQL)
    conn.commit()
    EXP_add=EXP_plus - EXP
    return print(f"게임에서 {score}점을 달성하여 경험치 {EXP_add}EXP를 얻었습니다.")

def category_quiz_EXP_UP(userid,quiz):
    SELECT_SQL = f"SELECT userid,EXP FROM member WHERE userid='{userid}';"
    cursor.execute(SELECT_SQL)
    row = cursor.fetchone()
    userid, EXP = row
    if quiz == 0:
        EXP_plus=EXP
        return print(f"게임에서 {quiz}점을 달성하여 경험치 획득에 실패하였습니다.")
    elif quiz == 1:
        EXP_plus=EXP+100
    elif quiz == 2:
        EXP_plus=EXP+200
    elif quiz == 3:
        EXP_plus=EXP+300

    UPDATE_SQL = f"UPDATE member SET EXP='{EXP_plus}' WHERE userid='{userid}';"
    cursor.execute(UPDATE_SQL)
    conn.commit()
    EXP_add=EXP_plus - EXP
    return print(f"게임에서 {quiz}문제를 맞아 경험치 {EXP_add}EXP를 얻었습니다.")