import sqlite3
import database.member as member, database.ranking as ranking, database.level as level, game.break_blocks as break_blocks, game.rsp as rsp, game.coin_game as coin_game, game.category_quiz as quiz_game

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS member(
        idx integer primary key autoincrement,
        userid text not null,
        userpw text not null,
        level integer not null,
        EXP integer not null
    );"""

cursor.execute(CREATE_SQL)
conn.commit()
program = 0

while program == 0:
    print("-----------------------------------------------------------------------------------------")
    print(" _                          _  _    _                                           _")
    print("| |                        | || |  | |            /\\                           | |")
    print("| |       ___ __   __  ___ | || |  | | _ __      /  \\    _ __   ___   __ _   __| |  ___")
    print("| |      / _ \\\\ \\ / / / _ \\| || |  | || '_ \\    / /\\ \\  | '__| / __| / _` | / _` | / _ \\")
    print("| |____ |  __/ \\ V / |  __/| || |__| || |_) |  / ____ \\ | |   | (__ | (_| || (_| ||  __/")
    print("|______| \\___|  \\_/   \\___||_| \\____/ | .__/  /_/    \\_\\|_|    \\___| \\__,_| \\__,_| \\___|")
    print("                                      | |")
    print("                                      |_|")
    print("\n                   보안프로그래밍 9조 - 김용섭, 박혜수, 이현성, 함유진\n")
    print("-----------------------------------------------------------------------------------------")
    print("0) 프로그램 종료")
    print("1) 로그인")
    print("2) 회원 탈퇴")
    print("3) 회원 가입")
    choice = int(input("메뉴 선택 : "))

    if choice == 0:
        pick_ok = 0
        while pick_ok == 0:
            print("-----------------------------------------------------------------------------------------")
            print("정말 로그아웃 하시겠습니까?")
            pick = input("n or y : ")
            if (pick == 'y'):
                pick_ok = 1
            elif (pick == 'n'):
                print("-----------------------------------------------------------------------------------------")
                print("메인 페이지로 돌아갑니다.")
                pick_ok = 1
            else:
                print("-----------------------------------------------------------------------------------------")
                print("다시 선택해주세요.")
        program = 1
        
    elif choice == 1:
        menu_page = 0
        while menu_page == 0:
            login_good = 0
            while login_good == 0:
                print("-----------------------------------------------------------------------------------------")
                print("\n                                      Login page\n")
                print("-----------------------------------------------------------------------------------------")
                userid = input("ID : ")
                userpw = input("Password : ")
                
                if (member.login_ok(userid,userpw)):
                    print(f"로그인 성공! {userid}님, 환영합니다!")
                    login_good = 1
                else:
                    print(f"로그인 실패!")
            game_page = 0
            while game_page == 0:
                print("-----------------------------------------------------------------------------------------")
                print("\n                                       Menu page\n")
                print("-----------------------------------------------------------------------------------------")
                print("0) 로그아웃 및 메인 페이지 이동")
                print("1) 순위 확인")
                print("2) 게임 진행")
                menu = int(input("메뉴 선택 : "))
                if menu == 0:
                    game_page = 1
                    menu_page = 1
                    
                elif menu == 1:
                    print("-----------------------------------------------------------------------------------------")
                    print("Ranking")
                    ranking.ranking()
                    
                elif menu == 2:
                    game_menu = 0
                    while game_menu == 0:
                        print("-----------------------------------------------------------------------------------------")
                        print("\n                                       Game page\n")
                        print("-----------------------------------------------------------------------------------------")
                        level.level_up(userid)
                        print("0)메뉴 페이지 이동 1)동전 던지기 2)카테고리 퀴즈 3)가위바위보 4)벽돌 깨기")
                        game = int(input("게임 선택 : "))
                        if game == 0:
                            print("-----------------------------------------------------------------------------------------")
                            print("게임 페이지 이동")
                            game_menu = 1
                            
                        elif game == 1:
                            print("-----------------------------------------------------------------------------------------")
                            print("동전 던지기")
                            if (coin_game.coin_game()):
                                level.coin_game_EXP_UP(userid)
                            
                        elif game == 2:
                            print("-----------------------------------------------------------------------------------------")
                            print("카테고리 퀴즈 맞추기")
                            quiz = quiz_game.quiz_game()
                            print("-----------------------------------------------------------------------------------------")
                            level.category_quiz_EXP_UP(userid,quiz)
                            
                        elif game == 3:
                            print("-----------------------------------------------------------------------------------------")
                            print("가위바위보")
                            if (rsp.main(userid)):
                                level.rsp_EXP_UP(userid)
                                print("-----------------------------------------------------------------------------------------")
                                print("게임에서 승리하여 경험치 100EXP를 얻었습니다.")
                            else:
                                print("-----------------------------------------------------------------------------------------")
                                print("게임에서 무승부 또는 패배하여 경험치를 얻지 못하였습니다.")
                        elif game == 4:
                            print("-----------------------------------------------------------------------------------------")
                            print("벽돌 깨기")
                            score = break_blocks.main()
                            print("-----------------------------------------------------------------------------------------")
                            level.break_blocks_EXP_UP(userid,score)
                        else:
                            print("잘못된 선택입니다.")
                            
                else:
                    print("잘못된 선택입니다.")
                    
    elif choice == 2:
        member_out_good = 0
        while member_out_good == 0:
            print("-----------------------------------------------------------------------------------------")
            print("\n                              Account Deletion page\n")
            print("-----------------------------------------------------------------------------------------")
            out_userid = input("ID : ")
            out_userpw = input("Password : ")
            
            if (member.member_out_ok(out_userid,out_userpw)):
                print(f"회원정보 삭제 성공! {out_userid}님, 안녕히가세요!")
                member_out_good = 1
            else:
                print(f"회원정보 삭제 실패!")
                
    elif choice == 3:
        member_good = 0
        while member_good == 0:
            print("-----------------------------------------------------------------------------------------")
            print("\n                                    Sign Up Page\n")
            print("-----------------------------------------------------------------------------------------")            
            new_userid = input("ID : ")
            new_userpw = input("Password : ")
        
            if(member.new_member(new_userid,new_userpw)):
                print("회원가입 성공!")
                member_good = 1
            else:
                print("중복된 아이디! 회원가입 실패!")    
        
    else:
        print("-----------------------------------------------------------------------------------------")
        print("잘못된 선택입니다.")