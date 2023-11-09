import pygame
import sys

WHITE = (255, 255, 255)
SKYBLUE = (135, 206, 235)
BLACK = (0, 0, 0)
MID = (105, 186, 255)

WIDTH = 1240
HEIGHT = 960
Ground_Line = 3

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)








#협업으로 인해 삭제 예정
class User:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.items = []  # 가지고 있는 아이템을 저장할 리스트
        self.dice = 0  # 주사위 숫자를 저장할 변수
        self.dice_rolls = 0 #주사위 두 번까지 굴릴수있게 추적(아이템에도 활용가능)

class Ground:
    def __init__(self, position):
        self.position = position

    def draw(self, surface):
        if self.position == 0:
            self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13, HEIGHT*11/13, HEIGHT*2/13, HEIGHT*2/13)
            pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
        if 1 <= self.position <= 9:
            self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13 - self.position*HEIGHT/13, HEIGHT*11/13, HEIGHT/13, HEIGHT*2/13)
            pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
        if self.position == 10:
            self.rect = pygame.Rect((WIDTH-HEIGHT)/2, HEIGHT*11/13, HEIGHT*2/13, HEIGHT*2/13)
            pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
        if 11 <= self.position <= 19:
            self.rect = pygame.Rect((WIDTH-HEIGHT)/2, HEIGHT*11/13 - (self.position - 10)*HEIGHT/13, HEIGHT*2/13, HEIGHT/13)
            pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
        if self.position == 20:
            self.rect = pygame.Rect((WIDTH-HEIGHT)/2, 0, HEIGHT*2/13, HEIGHT*2/13)
            pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
        if 21 <= self.position <= 29:
            self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*2/13 + (self.position - 21)*HEIGHT/13, 0, HEIGHT/13, HEIGHT*2/13)
            pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
        if self.position == 30:
            self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13, 0, HEIGHT*2/13, HEIGHT*2/13)
            pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
        if 31 <= self.position <= 39:
            self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13, HEIGHT*2/13 + (self.position - 31)*HEIGHT/13, HEIGHT*2/13, HEIGHT/13)
            pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)

#임시 땅
Ground1 = Ground(0)
Ground2 = Ground(1)
Ground3 = Ground(2)
Ground4 = Ground(3)
Ground5 = Ground(4)
Ground6 = Ground(5)
Ground7 = Ground(6)
Ground8 = Ground(7)
Ground9 = Ground(8)
Ground10 = Ground(9)
Ground11 = Ground(10)
Ground12 = Ground(11)
Ground13 = Ground(12)
Ground14 = Ground(13)
Ground15 = Ground(14)
Ground16 = Ground(15)
Ground17 = Ground(16)
Ground18 = Ground(17)
Ground19 = Ground(18)
Ground20 = Ground(19)
Ground21 = Ground(20)
Ground22 = Ground(21)
Ground23 = Ground(22)
Ground24 = Ground(23)
Ground25 = Ground(24)
Ground26 = Ground(25)
Ground27 = Ground(26)
Ground28 = Ground(27)
Ground29 = Ground(28)
Ground30 = Ground(29)
Ground31 = Ground(30)
Ground32 = Ground(31)
Ground33 = Ground(32)
Ground34 = Ground(33)
Ground35 = Ground(34)
Ground36 = Ground(35)
Ground37 = Ground(36)
Ground38 = Ground(37)
Ground39 = Ground(38)
Ground40 = Ground(39)









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
                if screen.get_rect().collidepoint(pos):
                    if (U_x < pos[0] < U_x + U_width and U_y < pos[1] < U_y + U_height and people <= 3):
                        people += 1
                    if (D_x < pos[0] < D_x + D_width and D_y < pos[1] < D_y + D_height and people >= 3):
                        people -= 1
                    if(S_x < pos[0] < S_x + S_width and S_y < pos[1] < S_y + S_height):
                        Press_Start = False
                

    screen.fill((0, 0, 255))

    Start_Bg = pygame.image.load("Start_bg.jpg")
    Start_Bg = pygame.transform.scale(Start_Bg, (WIDTH, HEIGHT))
    screen.blit(Start_Bg, (0,0))

    font1 = pygame.font.SysFont(None, 180)
    Title = font1.render('BLUE_MARBLE',True, (0, 0, 0))
    T_width, T_height = Title.get_size()
    screen.blit(Title,(WIDTH/2 - T_width/2, WIDTH/4 - T_height/2))

    font2 = pygame.font.SysFont(None, 100)
    People = font2.render(str(people), True, (0, 0, 0))
    P_width, P_height = People.get_size()
    screen.blit(People, ((WIDTH/2 - P_width/2), HEIGHT*43/64))

    Up = pygame.image.load("arrow_up.png")
    Up = pygame.transform.scale(Up, (70, 70))
    U_width, U_height = Up.get_size()
    U_x, U_y = WIDTH/2 - P_width + 100, HEIGHT*43/64
    screen.blit(Up, (U_x, U_y))

    Down = pygame.image.load("arrow_down.png")
    Down = pygame.transform.scale(Down, (70, 70))
    D_width, D_height = Down.get_size()
    D_x, D_y = WIDTH/2 - P_width - 110, HEIGHT*43/64
    screen.blit(Down, (D_x, D_y))

    start_button = pygame.image.load("start_button.png")
    start_button = pygame.transform.scale(start_button, (WIDTH*3/16, HEIGHT*5/64))
    S_width, S_height = start_button.get_size()
    S_x, S_y = WIDTH/2 - S_width/2, HEIGHT*13/16 - S_height/2
    screen.blit(start_button, (S_x, S_y))

    pygame.display.flip()









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
    mid = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*2/13, HEIGHT*2/13, HEIGHT*9/13, HEIGHT*9/13)
    left = pygame.Rect(0, 0, (WIDTH-HEIGHT)/2, HEIGHT)
    right = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT, 0, (WIDTH-HEIGHT)/2, HEIGHT)
    pygame.draw.rect(screen, MID, mid)
    pygame.draw.rect(screen, WHITE, left)
    pygame.draw.rect(screen, WHITE, right)

    Ground1.draw(screen)
    Ground2.draw(screen)
    Ground3.draw(screen)
    Ground4.draw(screen)
    Ground5.draw(screen)
    Ground6.draw(screen)
    Ground7.draw(screen)
    Ground8.draw(screen)
    Ground9.draw(screen)
    Ground10.draw(screen)
    Ground11.draw(screen)
    Ground12.draw(screen)
    Ground13.draw(screen)
    Ground14.draw(screen)
    Ground15.draw(screen)
    Ground16.draw(screen)
    Ground17.draw(screen)
    Ground18.draw(screen)
    Ground19.draw(screen)
    Ground20.draw(screen)
    Ground21.draw(screen)
    Ground22.draw(screen)
    Ground23.draw(screen)
    Ground24.draw(screen)
    Ground25.draw(screen)
    Ground26.draw(screen)
    Ground27.draw(screen)
    Ground28.draw(screen)
    Ground29.draw(screen)
    Ground30.draw(screen)
    Ground31.draw(screen)
    Ground32.draw(screen)
    Ground33.draw(screen)
    Ground34.draw(screen)
    Ground35.draw(screen)
    Ground36.draw(screen)
    Ground37.draw(screen)
    Ground38.draw(screen)
    Ground39.draw(screen)
    Ground40.draw(screen)

    User_Space1 = pygame.Rect(0, 0, (WIDTH-HEIGHT)/2, HEIGHT/2)
    User_Space2 = pygame.Rect(0, HEIGHT/2, (WIDTH-HEIGHT)/2, HEIGHT/2)
    User_Space3 = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT, 0, (WIDTH-HEIGHT)/2, HEIGHT/2)
    User_Space4 = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT, HEIGHT/2, (WIDTH-HEIGHT)/2, HEIGHT/2)
    pygame.draw.rect(screen, BLACK, User_Space1, 3)
    pygame.draw.rect(screen, BLACK, User_Space2, 3)
    pygame.draw.rect(screen, BLACK, User_Space3, 3)
    pygame.draw.rect(screen, BLACK, User_Space4, 3)

    font3 = pygame.font.SysFont(None, 40)
    if people == 2:
        User1 = font3.render("User 1", True, (0, 0, 0))
        screen.blit(User1, (0, 0))

        User4 = font3.render("User 2", True, (0, 0, 0))
        screen.blit(User4, ((WIDTH-HEIGHT)/2 + HEIGHT, HEIGHT/2))

    if people == 3:
        User1 = font3.render("User 1", True, (0, 0, 0))
        screen.blit(User1, (0, 0))
    
        User2 = font3.render("User 2", True, (0, 0, 0))
        screen.blit(User2, (0, HEIGHT/2))

        User4 = font3.render("User 3", True, (0, 0, 0))
        screen.blit(User4, ((WIDTH-HEIGHT)/2 + HEIGHT, HEIGHT/2))

    if people == 4:
        User1 = font3.render("User 1", True, (0, 0, 0))
        screen.blit(User1, (0, 0))
    
        User2 = font3.render("User 2", True, (0, 0, 0))
        screen.blit(User2, (0, HEIGHT/2))

        User3 = font3.render("User 3", True, (0, 0, 0))
        screen.blit(User3, ((WIDTH-HEIGHT)/2 + HEIGHT, 0))

        User4 = font3.render("User 4", True, (0, 0, 0))
        screen.blit(User4, ((WIDTH-HEIGHT)/2 + HEIGHT, HEIGHT/2))

    pygame.display.flip()


pygame.quit()
sys.exit()
