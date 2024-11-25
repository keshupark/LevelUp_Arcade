import csv
import os

def load_quiz_data(file_path):
    """
    CSV 파일에서 퀴즈 데이터를 읽어와 딕셔너리로 변환.
    """
    quiz_data = {}
    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:  # BOM 제거
            reader = csv.DictReader(file)
            for row in reader:
                category = row["category"]
                question = row["question"]
                answer = row["answer"]
                if category not in quiz_data:
                    quiz_data[category] = []
                quiz_data[category].append({"question": question, "answer": answer})
    except FileNotFoundError:
        print(f"파일 '{file_path}'을(를) 찾을 수 없습니다. 파일 이름과 경로를 확인하세요.")
    except Exception as e:
        print(f"데이터 로드 중 오류가 발생했습니다: {e}")
    return quiz_data

def quiz_game():
    """
    퀴즈 게임 실행 함수.
    """
    # 현재 스크립트 위치에서 quiz data.csv 파일 경로를 지정
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "quiz_data.csv")  # 공백 포함된 이름

    # 파일 경로로 퀴즈 데이터 로드
    quiz_data = load_quiz_data(file_path)
    if not quiz_data:
        print("퀴즈 데이터를 불러올 수 없습니다. 게임을 종료합니다.")
        return

    while True:  # 게임 반복
        print("=== 단답형 퀴즈 게임 ===")

        # 카테고리 선택
        print("\n카테고리를 선택하세요:")
        categories = list(quiz_data.keys())
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")

        try:
            choice = int(input("카테고리 번호를 입력하세요: "))
            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
            else:
                print("잘못된 선택입니다. 게임을 종료합니다.")
                return
        except ValueError:
            print("숫자를 입력해야 합니다. 게임을 종료합니다.")
            return

        print(f"\n'{selected_category}' 카테고리 퀴즈를 시작합니다!\n")

        # 퀴즈 진행
        score = 0
        for quiz in quiz_data[selected_category]:
            print(f"문제: {quiz['question']}")
            user_answer = input("정답을 입력하세요: ").strip()
            if user_answer.lower() == quiz['answer'].lower():  # 대소문자 무시 비교
                print("정답입니다!\n")
                score += 1
            else:
                print(f"틀렸습니다. 정답은 '{quiz['answer']}'입니다.\n")

        # 결과 출력
        print(f"총 {len(quiz_data[selected_category])}문제 중 {score}문제를 맞히셨습니다!")
        
        return score
        break  # while 루프 종료

# 게임 실행