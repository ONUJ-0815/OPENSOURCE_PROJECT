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




#시작화면
people = 2
start_button = pygame.image.load("start_button.png")
start_button = pygame.transform.scale(start_button, (WIDTH * 3 / 16, HEIGHT * 5 / 64))
S_width, S_height = start_button.get_size()
S_x, S_y = WIDTH / 2 - S_width / 2, HEIGHT * 13 / 16 - S_height / 2

Start_Bg = pygame.image.load("Start_bg.jpg")
Start_Bg = pygame.transform.scale(Start_Bg, (WIDTH, HEIGHT))

font1 = pygame.font.SysFont(None, 180)
Title = font1.render('BLUE_MARBLE', True, (0, 0, 0))
T_width, T_height = Title.get_size()

font2 = pygame.font.SysFont(None, 100)
People = font2.render(str(people), True, (0, 0, 0))
P_width, P_height = People.get_size()

Up = pygame.image.load("arrow_up.png")
Up = pygame.transform.scale(Up, (70, 70))
U_width, U_height = Up.get_size()
U_x, U_y = WIDTH / 2 - P_width + 100, HEIGHT * 43 / 64

Down = pygame.image.load("arrow_down.png")
Down = pygame.transform.scale(Down, (70, 70))
D_width, D_height = Down.get_size()
D_x, D_y = WIDTH / 2 - P_width - 110, HEIGHT * 43 / 64

class START_MENU:
    def __init__(self, window):
        self.window = window
        self.people = 2

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.window.get_rect().collidepoint(pos):
                        if U_x < pos[0] < U_x + U_width and U_y < pos[1] < U_y + U_height and self.people <= 3:
                            self.people += 1
                        if D_x < pos[0] < D_x + D_width and D_y < pos[1] < D_y + D_height and self.people >= 3:
                            self.people -= 1
                        if S_x < pos[0] < S_x + S_width and S_y < pos[1] < S_y + S_height:
                            return GAME_SCREEN(self.window, self.people)

        return self
    
    def update(self):
        pass

    def draw(self):
        self.window.blit(Start_Bg, (0, 0))
        self.window.blit(Title, (WIDTH / 2 - T_width / 2, WIDTH / 4 - T_height / 2))

        people_text = font2.render(str(self.people), True, (0, 0, 0))
        (P_width, P_height) = people_text.get_size()
        self.window.blit(people_text, (WIDTH / 2 - P_width / 2, HEIGHT * 43 / 64))

        self.window.blit(Up, (U_x, U_y))
        self.window.blit(Down, (D_x, D_y))
        self.window.blit(start_button, (S_x, S_y))








#게임화면
mid = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT * 2 / 13, HEIGHT * 2 / 13, HEIGHT * 9 / 13, HEIGHT * 9 / 13)
left = pygame.Rect(0, 0, (WIDTH - HEIGHT) / 2, HEIGHT)
right = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT, 0, (WIDTH - HEIGHT) / 2, HEIGHT)
Board = pygame.Rect((WIDTH - HEIGHT) / 2, 0, HEIGHT, HEIGHT)

User_Space1 = pygame.Rect(0, 0, (WIDTH - HEIGHT) / 2, HEIGHT / 2)
User_Space2 = pygame.Rect(0, HEIGHT / 2, (WIDTH - HEIGHT) / 2, HEIGHT / 2)
User_Space3 = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT, 0, (WIDTH - HEIGHT) / 2, HEIGHT / 2)
User_Space4 = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT, HEIGHT / 2, (WIDTH - HEIGHT) / 2, HEIGHT / 2)

font3 = pygame.font.SysFont(None, 40)

class GAME_SCREEN:
    def __init__(self, window, people):
        self.window = window
        self.people = people

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

        return self

    def draw(self):
        people = self.people
        pygame.draw.rect(self.window, SKYBLUE, Board)
        pygame.draw.rect(self.window, MID, mid)
        pygame.draw.rect(self.window, WHITE, left)
        pygame.draw.rect(self.window, WHITE, right)
        pygame.draw.rect(self.window, BLACK, User_Space1, 3)
        pygame.draw.rect(self.window, BLACK, User_Space2, 3)
        pygame.draw.rect(self.window, BLACK, User_Space3, 3)
        pygame.draw.rect(self.window, BLACK, User_Space4, 3)
        if people == 2:
            User1 = font3.render("User 1", True, (0, 0, 0))
            self.window.blit(User1, (0, 0))
            User4 = font3.render("User 2", True, (0, 0, 0))
            self.window.blit(User4, ((WIDTH - HEIGHT) / 2 + HEIGHT, HEIGHT / 2))
        if people == 3:
            User1 = font3.render("User 1", True, (0, 0, 0))
            self.window.blit(User1, (0, 0))
            User2 = font3.render("User 2", True, (0, 0, 0))
            self.window.blit(User2, (0, HEIGHT / 2))
            User4 = font3.render("User 3", True, (0, 0, 0))
            self.window.blit(User4, ((WIDTH - HEIGHT) / 2 + HEIGHT, HEIGHT / 2))
        if people == 4:
            User1 = font3.render("User 1", True, (0, 0, 0))
            self.window.blit(User1, (0, 0))
            User2 = font3.render("User 2", True, (0, 0, 0))
            self.window.blit(User2, (0, HEIGHT / 2))
            User3 = font3.render("User 3", True, (0, 0, 0))
            self.window.blit(User3, ((WIDTH - HEIGHT) / 2 + HEIGHT, 0))
            User4 = font3.render("User 4", True, (0, 0, 0))
            self.window.blit(User4, ((WIDTH - HEIGHT) / 2 + HEIGHT, HEIGHT / 2))
        j = 1
        ground = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT * 11 / 13, HEIGHT * 11 / 13, HEIGHT * 2 / 13, HEIGHT * 2 / 13)
        pygame.draw.rect(self.window, WHITE, ground, Ground_Line)
        while j < 10:
            ground = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT * 11 / 13 - j * HEIGHT / 13, HEIGHT * 11 / 13, HEIGHT / 13, HEIGHT * 2 / 13)
            pygame.draw.rect(self.window, WHITE, ground, Ground_Line)
            j = j + 1
        ground = pygame.Rect((WIDTH - HEIGHT) / 2, HEIGHT * 11 / 13, HEIGHT * 2 / 13, HEIGHT * 2 / 13)
        pygame.draw.rect(self.window, WHITE, ground, Ground_Line)
        j = j + 1
        while j < 20:
            ground = pygame.Rect((WIDTH - HEIGHT) / 2, HEIGHT * 11 / 13 - (j - 10) * HEIGHT / 13, HEIGHT * 2 / 13, HEIGHT / 13)
            pygame.draw.rect(self.window, WHITE, ground, Ground_Line)
            j = j + 1
        ground = pygame.Rect((WIDTH - HEIGHT) / 2, 0, HEIGHT * 2 / 13, HEIGHT * 2 / 13)
        pygame.draw.rect(self.window, WHITE, ground, Ground_Line)
        j = j + 1
        while j < 30:
            ground = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT * 2 / 13 + (j - 21) * HEIGHT / 13, 0, HEIGHT / 13,
                                 HEIGHT * 2 / 13)
            pygame.draw.rect(self.window, WHITE, ground, Ground_Line)
            j = j + 1
        ground = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT * 11 / 13, 0, HEIGHT * 2 / 13, HEIGHT * 2 / 13)
        pygame.draw.rect(self.window, WHITE, ground, Ground_Line)
        j = j + 1
        while j < 40:
            ground = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT * 11 / 13, HEIGHT * 2 / 13 + (j - 31) * HEIGHT / 13, HEIGHT * 2 / 13, HEIGHT / 13)
            pygame.draw.rect(self.window, WHITE, ground, Ground_Line)
            j = j + 1
        
        pygame.display.flip()

    def update(self):
        pass








#땅 정보
Info_Window = pygame.Rect((WIDTH - HEIGHT)/2 + HEIGHT*3/26, HEIGHT*3/26, HEIGHT * 10 / 13, HEIGHT * 10 / 13)
Info_Tit = pygame.Rect((WIDTH - HEIGHT)/2 + HEIGHT*3/26, HEIGHT*3/26, HEIGHT * 10/13, HEIGHT*1/26)
X_button = pygame.image.load("X_button.png")
X_button = pygame.transform.scale(X_button, (HEIGHT*1/26, HEIGHT*1/26))

class Ground_Info:
    def __init__(self, window, position):
        self.window = window
        self.position = position

    def draw(self):
        pygame.draw.rect(self.window, WHITE, Info_Window)
        pygame.draw.rect(self.window, YELLOW, Info_Tit)
        self.window.blit(X_button, ((WIDTH - HEIGHT)/2 + HEIGHT*11/13, HEIGHT*3/26))






#아이템 사용
class Use_Item:
    def __init(self, window, Item):
        self.window = window
        self.Item_num = Item
