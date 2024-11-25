import pygame
import sys

def main():
    # 초기화
    pygame.init()

    # 화면 크기 설정
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("벽돌깨기 게임")

    # 색상 정의
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 225, 0)
    BLUE = (0, 0, 255)

    # 공 설정
    ball_speed = [4, -4]
    ball_radius = 10
    ball_pos = [screen_width // 2, screen_height // 2]

    # 패들 설정
    paddle_width = 100
    paddle_height = 15
    paddle_speed = 8
    paddle_pos = [screen_width // 2 - paddle_width // 2, screen_height - 30]

    # 벽돌 설정
    brick_rows = 5
    brick_cols = 8
    brick_width = screen_width // brick_cols
    brick_height = 20
    bricks = []

    for row in range(brick_rows):
        for col in range(brick_cols):
            bricks.append(pygame.Rect(col * brick_width, row * brick_height, brick_width - 2, brick_height - 2))

    # 점수 초기화
    score = 0
    score_increment = 10  # 벽돌 하나당 얻는 점수

    # 폰트 설정
    font = pygame.font.Font(None, 36)  # 크기 36의 기본 폰트

    # 게임 루프
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)
        
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 패들 움직임
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
            paddle_pos[0] -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_pos[0] < screen_width - paddle_width:
            paddle_pos[0] += paddle_speed
        
        # 공 움직임
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]
        
        # 공의 벽 충돌
        if ball_pos[0] <= 0 or ball_pos[0] >= screen_width:
            ball_speed[0] = -ball_speed[0]
        if ball_pos[1] <= 0:
            ball_speed[1] = -ball_speed[1]
        if ball_pos[1] >= screen_height:
            print("Game Over!")
            running = False
        
        # 패들과 공 충돌
        paddle_rect = pygame.Rect(paddle_pos[0], paddle_pos[1], paddle_width, paddle_height)
        if paddle_rect.collidepoint(ball_pos[0], ball_pos[1] + ball_radius):
            ball_speed[1] = -ball_speed[1]
        
        # 벽돌과 공 충돌
        ball_rect = pygame.Rect(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius, ball_radius * 2, ball_radius * 2)
        for brick in bricks[:]:
            if brick.colliderect(ball_rect):
                bricks.remove(brick)
                ball_speed[1] = -ball_speed[1]
                score += score_increment  # 점수 증가
                break
        
        # 공 그리기
        pygame.draw.circle(screen, RED, ball_pos, ball_radius)
        
        # 패들 그리기
        pygame.draw.rect(screen, BLUE, paddle_rect)
        
        # 벽돌 그리기
        for brick in bricks:
            pygame.draw.rect(screen, WHITE, brick)
        
        # 점수 텍스트 렌더링
        score_text = font.render(f"Score: {score}", True, GREEN)
        screen.blit(score_text, (10, 10))  # 화면 왼쪽 위에 표시
        
        # 화면 업데이트
        pygame.display.flip()
        clock.tick(60)

    # 게임 종료 시 GUI 창 닫기
    pygame.quit()
    return score # 선택창으로 돌아가기
