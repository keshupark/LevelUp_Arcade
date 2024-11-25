import random

def main(userid):
    print(f"{userid}님, 가위바위보 게임을 시작합니다.")
    print("가위(0), 바위(1), 보(2) 중 하나를 선택하세요.")

    # 컴퓨터의 선택
    a = random.randint(0, 2)

    # 사용자 입력
    b = int(input(f"{userid}님의 선택: "))
    print("-----------------------------------------------------------------------------------------")
    # 컴퓨터의 선택 출력
    if a == 0:
        print("컴퓨터는 가위를 냈습니다.")
    elif a == 1:
        print("컴퓨터는 바위를 냈습니다.")
    else:
        print("컴퓨터는 보를 냈습니다.")
    print("-----------------------------------------------------------------------------------------")
    # 결과 판정
    if b == 0:  # 사용자: 가위
        if a == 0:
            print("비겼습니다.")
            return False
        elif a == 1:
            print("컴퓨터가 이겼습니다.")
            return False
        else:
            print(f"{userid}님이 이겼습니다.")
            return True
    elif b == 1:  # 사용자: 바위
        if a == 0:
            print(f"{userid}님이 이겼습니다.")
            return True
        elif a == 1:
            print("비겼습니다.")
            return False
        else:
            print("컴퓨터가 이겼습니다.")
            return False
    elif b == 2:  # 사용자: 보
        if a == 0:
            print("컴퓨터가 이겼습니다.")
            return False
        elif a == 1:
            print(f"{userid}님이 이겼습니다.")
            return True
        else:
            print("비겼습니다.")
            return False
    else:
        print("잘못된 입력입니다. 0, 1, 2 중에서 선택하세요.")
        return False
