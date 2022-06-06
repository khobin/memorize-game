import pygame

# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memorize game")


# 게임 루프
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # 창 닫는 이벤트
            running = False



# 게임 종료
pygame.quit()