import pygame
import sys

WHITE = (255, 255, 255)
SKYBLUE = (135, 206,)
WIDTH = 720
HEIGHT = 720
Ground_Line = 3

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)








#협업으로 인해 수정 필요
class User:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.items = []  # 가지고 있는 아이템을 저장할 리스트
        self.dice = 0  # 주사위 숫자를 저장할 변수
        self.dice_rolls = 0 #주사위 두 번까지 굴릴수있게 추적(아이템에도 활용가능)

class Ground:
    def __init__(self, x, y, width, height, position):
        self.rect = pygame.Rect(x, y, width, height)
        self.position = position


    def draw(self, surface, x, y):
        self.rect = pygame.Rect(x, y)
        pygame.draw.rect(surface, SKYBLUE, self.rect, Ground_Line)

#땅 구분(임시)
Start = Ground(WIDTH*9/11, HEIGHT*9/11, WIDTH*2/11, HEIGHT*2/11, 0)
Seoul = Ground(WIDTH*9/11, HEIGHT*8/11, WIDTH*2/11, HEIGHT*1/11, 1)
#...










people = 2
#시작화면
Press_Start = True
while Press_Start:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1):
                pos = pygame.mouse.get_pos()
                print(pos)
                if screen.get_rect().collidepoint(pos):
                    if (U_x < pos[0] < U_x + U_width and U_y < pos[1] < U_y + U_height and people <= 3):
                        people += 1
                        print(people)
                    if (D_x < pos[0] < D_x + D_width and D_y < pos[1] < D_y + D_height and people >= 3):
                        people -= 1
                        print(people)
                    if(S_x < pos[0] < S_x + S_width and S_y < pos[1] < S_y + S_height):
                        print(S_x, S_width, S_y, S_height)
                        print(pos)
                        Press_Start = False
                

    screen.fill((0, 0, 255))
    Start_Bg = pygame.image.load("Start_bg.jpg")
    Start_Bg = pygame.transform.scale(Start_Bg, (WIDTH, HEIGHT))
    screen.blit(Start_Bg, (0,0))

    font1 = pygame.font.SysFont(None, 80)
    Title = font1.render('BLUE_MARBLE',True, (0, 0, 0))
    T_width, T_height = Title.get_size()
    screen.blit(Title,(WIDTH/2 - T_width/2, WIDTH/4 - T_height/2))

    font2 = pygame.font.SysFont(None, 80)
    People = font2.render(str(people), True, (0, 0, 0))
    P_width, P_height = People.get_size()
    screen.blit(People, ((WIDTH/2 - P_width/2), HEIGHT*43/64))

    Up = pygame.image.load("arrow_up.png")
    Up = pygame.transform.scale(Up, (50, 50))
    U_width, U_height = Up.get_size()
    U_x, U_y = WIDTH/2 - P_width + 55, HEIGHT*43/64
    screen.blit(Up, (U_x, U_y))

    Down = pygame.image.load("arrow_down.png")
    Down = pygame.transform.scale(Down, (50, 50))
    D_width, D_height = Down.get_size()
    D_x, D_y = WIDTH/2 - P_width - 50, HEIGHT*43/64
    screen.blit(Down, (D_x, D_y))

    start_button = pygame.image.load("start_button.png")
    start_button = pygame.transform.scale(start_button, (WIDTH*5/16, HEIGHT*3/32))
    S_width, S_height = start_button.get_size()
    S_x, S_y = WIDTH/2 - S_width/2, HEIGHT*13/16 - S_height/2
    screen.blit(start_button, (S_x, S_y))

    pygame.display.flip()








Players = []

#게임화면
playing = True
while playing:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            playing = False
    screen.fill((135, 206, 235))

    #땅그리는 건 좀 더 확인해봄
    #Seoul.draw(screen, WIDTH*9/11, HEIGHT*9/11)
    #Start.draw(screen, WIDTH*9/11, HEIGHT*8/11)

    for _ in range(people):
        player = User(people)
        Players.append(player)

    pygame.display.flip()


pygame.quit()
sys.exit()