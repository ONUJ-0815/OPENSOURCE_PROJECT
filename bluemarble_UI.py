import pygame
import sys

pygame.font.init()

WHITE = (255, 255, 255)
SKYBLUE = (135, 206, 235)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
MID = (105, 186, 255)

WIDTH = 1240
HEIGHT = 960
Ground_Line = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)





class Base:
    def __init__(self):
        pass
    
    def handle_events(self, event):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()





people = 2
start_button = pygame.image.load("start_button.png")
start_button = pygame.transform.scale(start_button, (WIDTH*3/16, HEIGHT*5/64))
S_width, S_height = start_button.get_size()
S_x, S_y = WIDTH/2 - S_width/2, HEIGHT*13/16 - S_height/2

Start_Bg = pygame.image.load("Start_bg.jpg")
Start_Bg = pygame.transform.scale(Start_Bg, (WIDTH, HEIGHT))

font1 = pygame.font.SysFont(None, 180)
Title = font1.render('BLUE_MARBLE',True, (0, 0, 0))
T_width, T_height = Title.get_size()

font2 = pygame.font.SysFont(None, 100)
People = font2.render(str(people), True, (0, 0, 0))
P_width, P_height = People.get_size()

Up = pygame.image.load("arrow_up.png")
Up = pygame.transform.scale(Up, (70, 70))
U_width, U_height = Up.get_size()
U_x, U_y = WIDTH/2 - P_width + 100, HEIGHT*43/64

Down = pygame.image.load("arrow_down.png")
Down = pygame.transform.scale(Down, (70, 70))
D_width, D_height = Down.get_size()
D_x, D_y = WIDTH/2 - P_width - 110, HEIGHT*43/64

class START_MENU(Base):
    def __init__(self):
        # 생성자
        pass

    def handle_events(self, event):
        super().handle_events(event)
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
                            return GAME_SCREEN
                        
    def draw(self, screen):
        screen.fill((0, 0, 255))
        screen.blit(Start_Bg, (0,0))
        screen.blit(Title,(WIDTH/2 - T_width/2, WIDTH/4 - T_height/2))
        screen.blit(People, ((WIDTH/2 - P_width/2), HEIGHT*43/64))
        screen.blit(Up, (U_x, U_y))
        screen.blit(Down, (D_x, D_y))
        screen.blit(start_button, (S_x, S_y))





mid = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*2/13, HEIGHT*2/13, HEIGHT*9/13, HEIGHT*9/13)
left = pygame.Rect(0, 0, (WIDTH-HEIGHT)/2, HEIGHT)
right = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT, 0, (WIDTH-HEIGHT)/2, HEIGHT)

User_Space1 = pygame.Rect(0, 0, (WIDTH-HEIGHT)/2, HEIGHT/2)
User_Space2 = pygame.Rect(0, HEIGHT/2, (WIDTH-HEIGHT)/2, HEIGHT/2)
User_Space3 = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT, 0, (WIDTH-HEIGHT)/2, HEIGHT/2)
User_Space4 = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT, HEIGHT/2, (WIDTH-HEIGHT)/2, HEIGHT/2)

font3 = pygame.font.SysFont(None, 40)

class GAME_SCREEN(Base):
    def __init__(self):
        #생성자
        pass

    def handle_events(self, events):
        super().handle_events(events)

    def draw(self, screen, people):
        pygame.draw.rect(screen, MID, mid)
        pygame.draw.rect(screen, WHITE, left)
        pygame.draw.rect(screen, WHITE, right)
        pygame.draw.rect(screen, BLACK, User_Space1, 3)
        pygame.draw.rect(screen, BLACK, User_Space2, 3)
        pygame.draw.rect(screen, BLACK, User_Space3, 3)
        pygame.draw.rect(screen, BLACK, User_Space4, 3)
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
        j = 1
        ground = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13, HEIGHT*11/13, HEIGHT*2/13, HEIGHT*2/13)
        pygame.draw.rect(screen, WHITE, ground, Ground_Line)
        while j < 10:
            ground = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13 - j*HEIGHT/13, HEIGHT*11/13, HEIGHT/13, HEIGHT*2/13)
            pygame.draw.rect(screen, WHITE, ground, Ground_Line)
            j = j + 1
        ground = pygame.Rect((WIDTH-HEIGHT)/2, HEIGHT*11/13, HEIGHT*2/13, HEIGHT*2/13)
        pygame.draw.rect(screen, WHITE, ground, Ground_Line)
        j = j + 1
        while j < 20:
            ground = pygame.Rect((WIDTH-HEIGHT)/2, HEIGHT*11/13 - (j - 10)*HEIGHT/13, HEIGHT*2/13, HEIGHT/13)
            pygame.draw.rect(screen, WHITE, ground, Ground_Line)
            j = j + 1
        ground = pygame.Rect((WIDTH-HEIGHT)/2, 0, HEIGHT*2/13, HEIGHT*2/13)
        pygame.draw.rect(screen, WHITE, ground, Ground_Line)
        j = j + 1
        while j < 30:
            ground = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*2/13 + (j - 21)*HEIGHT/13, 0, HEIGHT/13, HEIGHT*2/13)
            pygame.draw.rect(screen, WHITE, ground, Ground_Line)
            j = j + 1
        ground = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13, 0, HEIGHT*2/13, HEIGHT*2/13)
        pygame.draw.rect(screen, WHITE, ground, Ground_Line)
        j = j + 1
        while j < 40:
            ground = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13, HEIGHT*2/13 + (j - 31)*HEIGHT/13, HEIGHT*2/13, HEIGHT/13)
            pygame.draw.rect(screen, WHITE, ground, Ground_Line)
            


X_button = pygame.image.load("X_button.png")
X_button = pygame.transform.scale(X_button, (WIDTH*1/16, HEIGHT*1/16))
X_width, X_height = X_button.get_size()

class Ground_Info(Base):
    def __init__(self):
        pass

    def handle_events(self, events):
        super().handle_events(events)

    def draw(self):
        Info = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*1/13, HEIGHT*2/13, HEIGHT*10/13, HEIGHT*9/13)
        Tit = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*1/13, HEIGHT*2/13, HEIGHT*10/13, HEIGHT*1/13)
        screen.blit(X_button, ())
        pygame.draw.rect(screen, WHITE, Info)
        pygame.draw.rect(screen, YELLOW, Tit)





class PygameWindow:
    def __init__(self):
        pygame.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_screen = START_MENU(self.screen)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.current_screen = self.current_screen.handle_events(event)

            self.current_screen.update()
            self.current_screen.draw()

            pygame.display.flip()
            self.clock.tick(60)
