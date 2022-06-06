import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memorize game")

# 시작 버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 게임 루프
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # 창 닫는 이벤트
            running = False
        

    screen.fill(BLACK)
    
    # 시작 화면 표시
    display_start_screen()

    # 화면 업데이트
    pygame.display.update()
    

# 게임 종료
pygame.quit()