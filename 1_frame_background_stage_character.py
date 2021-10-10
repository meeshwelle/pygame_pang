#This file is the bone structure for building any other pygame
import pygame, os
####################기본 초기화 (반드시 해야하는것들)########################
pygame.init() #mandatory to initialize

#화면 크키 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Pang Pang") #Game Name

#FPS
clock = pygame.time.Clock()
###########################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환return
image_path = os.path.join(current_path, "images") #images folder 위치 반환

#배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 높이 위에 캐릭터를 두기 위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

#Event Loop - is game running?
running = True
while running:
    dt = clock.tick(30) #화면의 초당 프레임 수
    # print("fps: " + str(clock.get_fps()))
    
    #2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): #this line is mandatory when using a pygame (어떤 이벤트가 발생하면)
        if event.type == pygame.QUIT: #When the tab closes
            running = False

    #3. 게임 케릭터 위치 정의

    #4. 충돌처리
    
    #5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # as while True loops, 계속 화면 update해줌 frame by frame

#pygame done
pygame.quit()