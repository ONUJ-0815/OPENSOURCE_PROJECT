import pygame
from constant import *
from ground import *
from player import *
from log import *

pygame.font.init()



#시작화면
people = 2
start_button = pygame.image.load("Pictures/start_button.png")
start_button = pygame.transform.scale(start_button, (WIDTH * 3 / 16, HEIGHT * 5 / 64))
S_width, S_height = start_button.get_size()
S_x, S_y = WIDTH / 2 - S_width / 2, HEIGHT * 13 / 16 - S_height / 2

Start_Bg = pygame.image.load("Pictures/Start_bg.jpg")
Start_Bg = pygame.transform.scale(Start_Bg, (WIDTH, HEIGHT))

font1 = pygame.font.SysFont(None, 180)
Title = font1.render('BLUE_MARBLE', True, (0, 0, 0))
T_width, T_height = Title.get_size()

font2 = pygame.font.SysFont(None, 100)
People = font2.render(str(people), True, (0, 0, 0))
P_width, P_height = People.get_size()

Up = pygame.image.load("Pictures/arrow_up.png")
Up = pygame.transform.scale(Up, (70, 70))
U_width, U_height = Up.get_size()
U_x, U_y = WIDTH / 2 - P_width + 100, HEIGHT * 43 / 64

Down = pygame.image.load("Pictures/arrow_down.png")
Down = pygame.transform.scale(Down, (70, 70))
D_width, D_height = Down.get_size()
D_x, D_y = WIDTH / 2 - P_width - 110, HEIGHT * 43 / 64

class START_MENU:
    def __init__(self, window, board, users, dice, log_instance):
        self.window = window
        self.people = 2
        self.board = board
        self.users = users
        self.dice = dice
        self.log_instance = log_instance

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
                            self.users.make_Userlist(self.people)
                            for user in self.users.user_list:
                                user.positon = 0
                            return Loading(self.window, self.board, self.users, self.dice, self.log_instance)

        return self
    
    def draw(self):
        self.window.blit(Start_Bg, (0, 0))
        self.window.blit(Title, (WIDTH / 2 - T_width / 2, WIDTH / 4 - T_height / 2))

        people_text = font2.render(str(self.people), True, (0, 0, 0))
        (P_width, P_height) = people_text.get_size()
        self.window.blit(people_text, (WIDTH / 2 - P_width / 2, HEIGHT * 43 / 64))

        self.window.blit(Up, (U_x, U_y))
        self.window.blit(Down, (D_x, D_y))
        self.window.blit(start_button, (S_x, S_y))





#로딩화면
class Loading:
    def __init__(self, window, board, users, dice, log_instance):
        self.window = window
        self.board = board
        self.users = users
        self.dice = dice
        self.log_instance = log_instance

    def handle_events(self, events):
        return GAME_SCREEN(self.window, self.board, self.users, self.dice, self.log_instance)

    def draw_loading(self):
        Loading_BG = pygame.Rect(0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(self.window, BLACK, Loading_BG)
        #규칙 및 작동방법 설명
        context1 = font_RULE.render("이 게임은 오프라인 보드게임인 '부루마블'을 모티브로 제작되었습니다.", True, WHITE)
        Width1 = context1.get_width()
        context2 = font_RULE.render("게임을 진행하는 인원은 " + str(len(self.users)) + "명 입니다.", True, WHITE)
        Width2 = context2.get_width()
        context3 = font_RULE.render("스페이스 바를 누를 시 주사위가 굴러가며, t를 통해 차례를 다음 사람한테 넘길 수 있습니다.", True, WHITE)
        Width3 = context3.get_width()
        context4 = font_RULE.render("땅을 구매하시고 싶은 경우에는 그 땅에 위치한 뒤 B키를 통해 땅을 구매하며", True, WHITE)
        Width4 = context4.get_width()
        context5 = font_RULE.render("땅을 소유한 경우 B를 더 눌러 각각 빌라와 호텔을 건설할 수 있습니다.", True, WHITE)
        Width5 = context5.get_width()
        context6 = font_RULE.render("땅을 오른쪽 클릭 한 경우, 땅의 가격, 소유주 등의 정보를 표시할 수 있습니다.", True, WHITE)
        Width6 = context6.get_width()
        context7 = font_RULE.render("아이템은 아이템 창의 숫자 키를 눌러 사용할 수 있으며, 사용할 수 있을 때 표시됩니다.", True, WHITE)
        Width7 = context7.get_width()
        context8 = font_RULE.render("무인도: 3턴동안 움직일 수 없습니다. 더블이 나오면 탈출합니다", True, WHITE)
        Width8 = context8.get_width()
        context9 = font_RULE.render("우주여행: 내 다음턴에 원하는 곳을 좌클릭하면 이동합니다.", True, WHITE)
        Width9 = context9.get_width()
        context10 = font_RULE.render("사회복지기금: 접수처에 갈 시 기부를 하고 수령처에 가면 쌓인 기부금을 받을 수 있습니다", True, WHITE)
        Width10 = context10.get_width()
        context11 = font_RULE.render("황금열쇠: 다양한 아이템을 얻을 수 있습니다(벌칙도 존재합니다!)", True, WHITE)
        Width11 = context11.get_width()

        self.window.blit(context1, (WIDTH / 2 - Width1 / 2, HEIGHT * 22 / 64))
        self.window.blit(context2, (WIDTH / 2 - Width2 / 2, HEIGHT * 24 / 64))
        self.window.blit(context3, (WIDTH / 2 - Width3 / 2, HEIGHT * 26 / 64))
        self.window.blit(context4, (WIDTH / 2 - Width4 / 2, HEIGHT * 28 / 64))
        self.window.blit(context5, (WIDTH / 2 - Width5 / 2, HEIGHT * 30 / 64))
        self.window.blit(context6, (WIDTH / 2 - Width6 / 2, HEIGHT * 32 / 64))
        self.window.blit(context7, (WIDTH / 2 - Width7 / 2, HEIGHT * 34 / 64))
        self.window.blit(context8, (WIDTH / 2 - Width8 / 2, HEIGHT * 36 / 64))
        self.window.blit(context9, (WIDTH / 2 - Width9 / 2, HEIGHT * 38 / 64))
        self.window.blit(context10, (WIDTH / 2 - Width10 / 2, HEIGHT * 40 / 64))
        self.window.blit(context11, (WIDTH / 2 - Width11 / 2, HEIGHT * 42 / 64))
        
        pygame.display.flip()
        pygame.time.delay(5000)        






#게임화면
mid = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT * 2 / 13, HEIGHT * 2 / 13, HEIGHT * 9 / 13, HEIGHT * 9 / 13)
left = pygame.Rect(0, 0, (WIDTH - HEIGHT) / 2, HEIGHT)
right = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT, 0, (WIDTH - HEIGHT) / 2, HEIGHT)
Map = pygame.Rect(0, 0, WIDTH, HEIGHT)

User_Space1 = pygame.Rect(0, 0, (WIDTH - HEIGHT) / 2, HEIGHT / 4)
User_Space2 = pygame.Rect(0, HEIGHT * 3 / 4, (WIDTH - HEIGHT) / 2, HEIGHT / 4)
User_Space3 = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT, 0, (WIDTH - HEIGHT) / 2, HEIGHT / 4)
User_Space4 = pygame.Rect((WIDTH - HEIGHT) / 2 + HEIGHT, HEIGHT * 3 / 4, (WIDTH - HEIGHT) / 2, HEIGHT / 4)
Inform_Space = pygame.Rect(0, HEIGHT/4, (WIDTH - HEIGHT) / 2, HEIGHT / 2)
Item_Space = pygame.Rect((WIDTH-HEIGHT) / 2 + HEIGHT, HEIGHT / 4, (WIDTH - HEIGHT) / 2, HEIGHT / 2)

Villa_A = pygame.image.load("Pictures/Villa_A.png")
Villa_A = pygame.transform.scale(Villa_A, (HEIGHT/26, HEIGHT/26))
Villa_B = pygame.image.load("Pictures/Villa_B.png")
Villa_B = pygame.transform.scale(Villa_B, (HEIGHT/26, HEIGHT/26))
Villa_C = pygame.image.load("Pictures/Villa_C.png")
Villa_C = pygame.transform.scale(Villa_C, (HEIGHT/26, HEIGHT/26))
Villa_D = pygame.image.load("Pictures/Villa_D.png")
Villa_D = pygame.transform.scale(Villa_D, (HEIGHT/26, HEIGHT/26))
Hotel_A = pygame.image.load("Pictures/Hotel_A.png")
Hotel_A = pygame.transform.scale(Hotel_A, (HEIGHT/26, HEIGHT/26))
Hotel_B = pygame.image.load("Pictures/Hotel_B.png")
Hotel_B = pygame.transform.scale(Hotel_B, (HEIGHT/26, HEIGHT/26))
Hotel_C = pygame.image.load("Pictures/Hotel_C.png")
Hotel_C = pygame.transform.scale(Hotel_C, (HEIGHT/26, HEIGHT/26))
Hotel_D = pygame.image.load("Pictures/Hotel_D.png")
Hotel_D = pygame.transform.scale(Hotel_D, (HEIGHT/26, HEIGHT/26))


class GAME_SCREEN:
    def __init__(self, window, board, users, dice, log_instance):
        self.window = window
        self.board = board
        self.click_ground = 0
        self.winner = None
        self.Trgt_Block = None
        self.users = users
        self.dice = dice
        self.log_instance = log_instance
        self.Player_A = pygame.image.load("Pictures/Player_A.png")
        self.Player_A = pygame.transform.scale(self.Player_A, (HEIGHT/26, HEIGHT/26))
        self.Player_B = pygame.image.load("Pictures/Player_B.png")
        self.Player_B = pygame.transform.scale(self.Player_B, (HEIGHT/26, HEIGHT/26))
        self.Player_C = pygame.image.load("Pictures/Player_C.png")
        self.Player_C = pygame.transform.scale(self.Player_C, (HEIGHT/26, HEIGHT/26))
        self.Player_D = pygame.image.load("Pictures/Player_D.png")
        self.Player_D = pygame.transform.scale(self.Player_D, (HEIGHT/26, HEIGHT/26))        

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    clicked_block_position = self.Ground_Click(pos[0], pos[1])
                    if clicked_block_position is not None:
                        self.Trgt_Block = self.board.get_block_at_position(clicked_block_position)
                        if self.Trgt_Block is not None:
                            self.click_ground = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return Ending(self.window, self.users)
                if event.key == pygame.K_d:
                    return GAME_SCREEN(self.window, self.board, self.users, self.dice, self.log_instance)
        return self

    def draw(self, board):
        #맵 표시
        pygame.draw.rect(self.window, SKYBLUE, Map)
        pygame.draw.rect(self.window, MID, mid)
        pygame.draw.rect(self.window, WHITE, left)
        pygame.draw.rect(self.window, WHITE, right)
        pygame.draw.rect(self.window, BLACK, Inform_Space)
        pygame.draw.rect(self.window, WHITE, Item_Space)

        #주사위 구현
        if self.dice.dice1 >=1 and self.dice.dice1 <=6:
            d1width, d1height = self.dice.image1.get_width(), self.dice.image1.get_height()
            self.window.blit(self.dice.image1, (WIDTH/2 - d1width, HEIGHT/2 - d1height/2))
            
        if self.dice.dice2 >=1 and self.dice.dice2 <=6:
            d1width, d1height = self.dice.image2.get_width(), self.dice.image2.get_height()
            self.window.blit(self.dice.image2, (WIDTH/2, HEIGHT/2 - d1height/2))

        #땅 객체 표현
        board.draw_board(self.window)

        #땅 이름 표시, 특수칸 배경 채우기
        for block in self.board.blocks:
            limited_name = block.name[:3]
            limited_name = font_Info.render(limited_name, True, BLACK)
            alpha_value = 150
            if block.position == 0:
                B_Width, B_Height = block.rect.width, block.rect.height
                Start = pygame.image.load("Pictures/Start.png")
                Start = pygame.transform.scale(Start, (B_Width, B_Height))
                Start.set_alpha(alpha_value)
                self.window.blit(Start, (block.rect.left, block.rect.top))
            if 1 <= block.position <= 9:
                B_Width, B_Height = block.rect.w, block.rect.h
                N_Width = limited_name.get_width()
                N_Height = limited_name.get_height()
                name_block = pygame.Rect(block.rect.left, block.rect.centery - B_Height/4, B_Width, B_Height/4)
                pygame.draw.rect(self.window, NAME, name_block)
                name_Line = pygame.Rect(block.rect.left, block.rect.centery - B_Height/4, B_Width, B_Height/4)
                pygame.draw.rect(self.window, NAME_LINE, name_Line, 3)
                self.window.blit(limited_name, (block.rect.centerx - N_Width/2, block.rect.centery - N_Height - 5))
            if block.position == 10:
                B_Width, B_Height = block.rect.w, block.rect.h
                Jail = pygame.image.load("Pictures/jail.png")
                Jail = pygame.transform.scale(Jail, (B_Width, B_Height))
                self.window.blit(Jail, (block.rect.left, block.rect.top))
            if 11 <= block.position <= 19:
                B_Width, B_Height = block.rect.w, block.rect.h
                limited_name = block.name[:3]
                limited_name = font_Info.render(limited_name, True, BLACK)
                limited_name = pygame.transform.rotate(limited_name, 90)
                N_Width = limited_name.get_width()
                N_Height = limited_name.get_height()
                name_block = pygame.Rect(block.rect.centerx, block.rect.top, B_Width/4, B_Height)
                pygame.draw.rect(self.window, NAME, name_block)
                name_Line = pygame.Rect(block.rect.centerx, block.rect.top, B_Width/4, B_Height)
                pygame.draw.rect(self.window, NAME_LINE, name_Line, 3)
                self.window.blit(limited_name, (block.rect.centerx + 5, block.rect.centery - N_Height/2))
            if block.position == 20:
                B_Width, B_Height = block.rect.w, block.rect.h
                Pay = pygame.image.load("Pictures/pay.png")
                Pay = pygame.transform.scale(Pay, (B_Width, B_Height))
                self.window.blit(Pay, (block.rect.left, block.rect.top))
            if 21 <= block.position <= 29:
                B_Width, B_Height = block.rect.w, block.rect.h
                N_Width = limited_name.get_width()
                N_Height = limited_name.get_height()
                name_block = pygame.Rect(block.rect.left, block.rect.centery, B_Width, B_Height/4)
                pygame.draw.rect(self.window, NAME, name_block)
                name_Line = pygame.Rect(block.rect.left, block.rect.centery, B_Width, B_Height/4)
                pygame.draw.rect(self.window, NAME_LINE, name_Line, 3)
                self.window.blit(limited_name, (block.rect.centerx - N_Width/2, block.rect.centery + 5))
            if block.position == 30:
                B_Width, B_Height = block.rect.w, block.rect.h
                Travel = pygame.image.load("Pictures/Travel.png")
                Travel = pygame.transform.scale(Travel, (B_Width, B_Height))
                Travel.set_alpha(alpha_value)
                self.window.blit(Travel, (block.rect.left, block.rect.top))
            if block.position == 38:
                B_Width, B_Height = block.rect.w, block.rect.h
                Bank = pygame.image.load("Pictures/bank.png")
                Bank = pygame.transform.scale(Bank, (B_Width, B_Height))
                self.window.blit(Bank, (block.rect.left, block.rect.top))
            if 31 <= block.position <= 39:
                B_Width, B_Height = block.rect.w, block.rect.h
                limited_name = block.name[:3]
                limited_name = font_Info.render(limited_name, True, BLACK)
                limited_name = pygame.transform.rotate(limited_name, 270)
                N_Width = limited_name.get_width()
                N_Height = limited_name.get_height()
                name_block = pygame.Rect(block.rect.centerx - B_Width/4, block.rect.top, B_Width/4, B_Height)
                pygame.draw.rect(self.window, NAME, name_block)
                name_Line = pygame.Rect(block.rect.centerx - B_Width/4, block.rect.top, B_Width/4, B_Height)
                pygame.draw.rect(self.window, NAME_LINE, name_Line, 3)
                self.window.blit(limited_name, (block.rect.centerx - B_Width/4 + 5, block.rect.centery - N_Height/2))
        
        #황금열쇠
        for block in self.board.blocks:
            if block.block_type == BlockType.GOLD_KEY:
                B_Width, B_Height = block.rect.w, block.rect.h
                bg = pygame.Rect(block.rect.left, block.rect.top, B_Width, B_Height)
                pygame.draw.rect(self.window, BLACK, bg)
                if block.position < 10:
                    B_Width, B_Height = block.rect.w, block.rect.h
                    GoldenKey = pygame.image.load("Pictures/Golden_Key.png")
                    GoldenKey = pygame.transform.rotate(GoldenKey, 180)
                    GoldenKey = pygame.transform.scale(GoldenKey, (B_Width, B_Height))
                    self.window.blit(GoldenKey, (block.rect.left, block.rect.top))
                elif block.position < 20:
                    B_Width, B_Height = block.rect.w, block.rect.h
                    GoldenKey = pygame.image.load("Pictures/Golden_Key.png")
                    GoldenKey = pygame.transform.rotate(GoldenKey, 90)
                    GoldenKey = pygame.transform.scale(GoldenKey, (B_Width, B_Height))
                    self.window.blit(GoldenKey, (block.rect.left, block.rect.top))
                elif block.position < 30:
                    B_Width, B_Height = block.rect.w, block.rect.h
                    GoldenKey = pygame.image.load("Pictures/Golden_Key.png")
                    GoldenKey = pygame.transform.scale(GoldenKey, (B_Width, B_Height))
                    self.window.blit(GoldenKey, (block.rect.left, block.rect.top))
                elif block.position < 40:
                    B_Width, B_Height = block.rect.w, block.rect.h
                    GoldenKey = pygame.image.load("Pictures/Golden_Key.png")
                    GoldenKey = pygame.transform.rotate(GoldenKey, 270)
                    GoldenKey = pygame.transform.scale(GoldenKey, (B_Width, B_Height))
                    self.window.blit(GoldenKey, (block.rect.left, block.rect.top))

        #말 UI, 유저 스페이스 색상 표시
        pygame.draw.rect(self.window, WHITE, User_Space1)
        pygame.draw.rect(self.window, WHITE, User_Space2)
        pygame.draw.rect(self.window, WHITE, User_Space3)
        pygame.draw.rect(self.window, WHITE, User_Space4)
        
        if len(self.users) == 2:
            pygame.draw.rect(self.window, RED, User_Space1, 10)
            pygame.draw.rect(self.window, BLUE, User_Space4, 10)
            
            Block_A = board.get_block_at_position(self.users.user_list[0].position)
            if self.users.user_list[0].position == 0 or self.users.user_list[0].position == 10 or self.users.user_list[0].position == 20 or self.users.user_list[0].position == 30 :
                self.window.blit(self.Player_A, (Block_A.rect.centerx - HEIGHT/26, Block_A.rect.centery - HEIGHT/26))
            elif 0 < self.users.user_list[0].position < 10:
                self.window.blit(self.Player_A, (Block_A.rect.left, Block_A.rect.centery)) 
            elif 11 <= self.users.user_list[0].position < 20:
                self.window.blit(self.Player_A, (Block_A.rect.left, Block_A.rect.top))
            elif 21 <= self.users.user_list[0].position < 30:
                self.window.blit(self.Player_A, (Block_A.rect.left, Block_A.rect.top))
            else:
                self.window.blit(self.Player_A, (Block_A.rect.centerx, Block_A.rect.top))
            
            Block_B = board.get_block_at_position(self.users.user_list[1].position)
            if self.users.user_list[1].position == 0 or self.users.user_list[1].position == 10 or self.users.user_list[1].position == 20 or self.users.user_list[1].position == 30 :
                self.window.blit(self.Player_B, (Block_B.rect.centerx, Block_B.rect.centery))
            elif 0 <= self.users.user_list[1].position <= 10:
                self.window.blit(self.Player_B, (Block_B.rect.centerx, Block_B.rect.centery + HEIGHT / 26)) 
            elif 11<= self.users.user_list[1].position <= 20:
                self.window.blit(self.Player_B, (Block_B.rect.centerx - HEIGHT/26, Block_B.rect.centery))
            elif 21 <= self.users.user_list[1].position <= 30:
                self.window.blit(self.Player_B, (Block_B.rect.centerx, Block_B.rect.centery - HEIGHT/26))
            else:
                self.window.blit(self.Player_B, (Block_B.rect.centerx + HEIGHT/26, Block_B.rect.centery))
        elif len(self.users) == 3:
            pygame.draw.rect(self.window, RED, User_Space1, 10)
            pygame.draw.rect(self.window, BLUE, User_Space2, 10)
            pygame.draw.rect(self.window, YELLOW, User_Space4, 10)     
            
            Block_A = board.get_block_at_position(self.users.user_list[0].position)
            Block_A = board.get_block_at_position(self.users.user_list[0].position)
            if self.users.user_list[0].position == 0 or self.users.user_list[0].position == 10 or self.users.user_list[0].position == 20 or self.users.user_list[0].position == 30 :
                self.window.blit(self.Player_A, (Block_A.rect.centerx - HEIGHT/26, Block_A.rect.centery - HEIGHT/26))
            elif 0 < self.users.user_list[0].position < 10:
                self.window.blit(self.Player_A, (Block_A.rect.left, Block_A.rect.centery)) 
            elif 11<= self.users.user_list[0].position < 20:
                self.window.blit(self.Player_A, (Block_A.rect.left, Block_A.rect.top))
            elif 21 <= self.users.user_list[0].position < 30:
                self.window.blit(self.Player_A, (Block_A.rect.left, Block_A.rect.top))
            else:
                self.window.blit(self.Player_A, (Block_A.rect.centerx, Block_A.rect.top))
            
            Block_B = board.get_block_at_position(self.users.user_list[1].position)
            if self.users.user_list[1].position == 0 or self.users.user_list[1].position == 10 or self.users.user_list[1].position == 20 or self.users.user_list[1].position == 30 :
                self.window.blit(self.Player_B, (Block_B.rect.centerx - HEIGHT/26, Block_B.rect.centery))
            elif 0 < self.users.user_list[1].position < 10:
                self.window.blit(self.Player_B, (Block_B.rect.left, Block_B.rect.centery + HEIGHT / 26)) 
            elif 11<= self.users.user_list[1].position <= 20:
                self.window.blit(self.Player_B, (Block_B.rect.left, Block_B.rect.top))
            elif 21 <= self.users.user_list[1].position <= 30:
                self.window.blit(self.Player_B, (Block_B.rect.left, Block_B.rect.centery + HEIGHT / 26))
            else:
                self.window.blit(self.Player_B, (Block_B.rect.centerx, Block_B.rect.centery))
            
            Block_C = board.get_block_at_position(self.users.user_list[2].position)
            if self.users.user_list[2].position == 0 or self.users.user_list[2].position == 10 or self.users.user_list[2].position == 20 or self.users.user_list[2].position == 30 :
                self.window.blit(self.Player_C, (Block_C.rect.centerx, Block_C.rect.centery))
            elif 0 <= self.users.user_list[2].position <= 10:
                self.window.blit(self.Player_C, (Block_C.rect.centerx, Block_C.rect.centery + HEIGHT / 26)) 
            elif 11<= self.users.user_list[2].position <= 20:
                self.window.blit(self.Player_C, (Block_C.rect.centerx - HEIGHT/26, Block_C.rect.centery))
            elif 21 <= self.users.user_list[2].position <= 30:
                self.window.blit(self.Player_C, (Block_C.rect.centerx, Block_C.rect.centery - HEIGHT/26))
            else:
                self.window.blit(self.Player_C, (Block_C.rect.centerx + HEIGHT/26, Block_C.rect.centery))
        elif len(self.users) == 4:
            pygame.draw.rect(self.window, RED, User_Space1, 10)
            pygame.draw.rect(self.window, BLUE, User_Space2, 10)
            pygame.draw.rect(self.window, YELLOW, User_Space3, 10)
            pygame.draw.rect(self.window, GREEN, User_Space4, 10)
            if self.users.user_list[0].SE != False:
                Block_A = board.get_block_at_position(self.users.user_list[0].position)
                if self.users.user_list[0].position == 0 or self.users.user_list[0].position == 10 or self.users.user_list[0].position == 20 or self.users.user_list[0].position == 30 :
                    self.window.blit(self.Player_A, (Block_A.rect.centerx - HEIGHT/26, Block_A.rect.centery - HEIGHT/26))
                elif 0 <= self.users.user_list[0].position <= 10:
                    self.window.blit(self.Player_A, (Block_A.rect.left, Block_A.rect.centery)) 
                elif 11<= self.users.user_list[0].position <= 20:
                    self.window.blit(self.Player_A, (Block_A.rect.left, Block_A.rect.top))
                elif 21 <= self.users.user_list[0].position <= 30:
                    self.window.blit(self.Player_A, (Block_A.rect.left, Block_A.rect.top))
                else:
                    self.window.blit(self.Player_A, (Block_A.rect.centerx, Block_A.rect.top))
            if self.users.user_list[1].SE != False: 
                Block_B = board.get_block_at_position(self.users.user_list[1].position)
                if self.users.user_list[1].position == 0 or self.users.user_list[1].position == 10 or self.users.user_list[1].position == 20 or self.users.user_list[1].position == 30 :
                    self.window.blit(self.Player_B, (Block_B.rect.centerx - HEIGHT/26, Block_B.rect.centery))
                elif 0 <= self.users.user_list[1].position <= 10:
                    self.window.blit(self.Player_B, (Block_B.rect.left, Block_B.rect.centery + HEIGHT / 26)) 
                elif 11<= self.users.user_list[1].position <= 20:
                    self.window.blit(self.Player_B, (Block_B.rect.left, Block_B.rect.centery))
                elif 21 <= self.users.user_list[1].position <= 30:
                    self.window.blit(self.Player_B, (Block_B.rect.left, Block_B.rect.centery - HEIGHT / 26))
                else:
                    self.window.blit(self.Player_B, (Block_B.rect.centerx, Block_B.rect.centery))
            if self.users.user_list[2].SE != False:    
                Block_C = board.get_block_at_position(self.users.user_list[2].position)
                if self.users.user_list[2].position == 0 or self.users.user_list[2].position == 10 or self.users.user_list[2].position == 20 or self.users.user_list[2].position == 30 :
                    self.window.blit(self.Player_C, (Block_C.rect.centerx, Block_C.rect.centery - HEIGHT/26))
                elif 0 <= self.users.user_list[2].position <= 10:
                    self.window.blit(self.Player_C, (Block_C.rect.centerx, Block_C.rect.centery)) 
                elif 11<= self.users.user_list[2].position <= 20:
                    self.window.blit(self.Player_C, (Block_C.rect.centerx - HEIGHT / 26, Block_C.rect.top))
                elif 21 <= self.users.user_list[2].position <= 30:
                    self.window.blit(self.Player_C, (Block_C.rect.centerx, Block_C.rect.top))
                else:
                    self.window.blit(self.Player_C, (Block_C.rect.centerx + HEIGHT /26, Block_C.rect.top))
            if self.users.user_list[3].SE != False:
                Block_D = board.get_block_at_position(self.users.user_list[3].position)
                if self.users.user_list[3].position == 0 or self.users.user_list[3].position == 10 or self.users.user_list[3].position == 20 or self.users.user_list[3].position == 30 :
                    self.window.blit(self.Player_D, (Block_D.rect.centerx, Block_D.rect.centery))
                elif 0 <= self.users.user_list[3].position <= 10:
                    self.window.blit(self.Player_D, (Block_D.rect.centerx, Block_D.rect.centery + HEIGHT / 26)) 
                elif 11<= self.users.user_list[3].position <= 20:
                    self.window.blit(self.Player_D, (Block_D.rect.centerx - HEIGHT/26, Block_D.rect.centery))
                elif 21 <= self.users.user_list[3].position <= 30:
                    self.window.blit(self.Player_D, (Block_D.rect.centerx, Block_D.rect.centery - HEIGHT/26))
                else:
                    self.window.blit(self.Player_D, (Block_D.rect.centerx + HEIGHT/26, Block_D.rect.centery))

        #땅 소유 확인을 위한 색깔 대입    
        for block in self.board.blocks:
            if block.owner == None:
                pass
            elif block.owner.name == '1P':
                pygame.draw.rect(self.window, RED, block.rect, 2)
            elif block.owner.name == '2P':
                pygame.draw.rect(self.window, BLUE, block.rect, 2)
            elif block.owner.name == '3P':
                pygame.draw.rect(self.window, YELLOW, block.rect, 2)
            elif block.owner.name == '4P':
                pygame.draw.rect(self.window, GREEN, block.rect, 2)
            
        #유저 정보(이름, 돈, 아이템, 순위)
        if len(self.users) == 2:
            User_A = font3.render(self.users.user_list[0].name, True, BLACK)
            name_height = User_A.get_height()
            name_width = User_A.get_width()
            A_asset = font_Max.render("현재 잔액: " + str(self.users.user_list[0].money), True, BLACK)
            F_size = A_asset.get_height()
            A_Items_tit = font_Max.render("아이템 리스트: ", True, BLACK)
            i = 0
            for i, item in enumerate(self.users.user_list[0].items):
                if isinstance(item, Item):
                    A_Items_List = font_Max.render(item.name + " ", True, BLACK)
                    self.window.blit(A_Items_List, (20, name_height + 2 * F_size + 30 + (F_size + 5) * i))
            self.window.blit(User_A, (10, 10))
            self.window.blit(A_asset, (10, 10 + name_height + 5))
            self.window.blit(A_Items_tit, (10, 10 + name_height + F_size+ 10))

            User_D = font3.render(self.users.user_list[1].name, True, (0, 0, 0))
            name_height = User_D.get_height()
            D_asset = font_Max.render("현재 잔액: " + str(self.users.user_list[1].money), True, BLACK)
            F_size = D_asset.get_height()
            D_Items_tit = font_Max.render("아이템 리스트: ", True, BLACK)
            i = 0
            for i, item in enumerate(self.users.user_list[1].items):
                if isinstance(item, Item):
                    D_Items_List = font_Max.render(item.name + " ", True, BLACK)
                    self.window.blit(D_Items_List, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, name_height + 2 * F_size + 30 + (F_size + 5) * i + HEIGHT * 3 / 4))
            self.window.blit(User_D, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, HEIGHT * 3 / 4 + 10))
            self.window.blit(D_asset, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, HEIGHT * 3 / 4 + 10 + name_height + 5))
            self.window.blit(D_Items_tit, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, HEIGHT * 3 / 4 + 10 + name_height + F_size+ 10))
        elif len(self.users) == 3:
            User_A = font3.render(self.users.user_list[0].name, True, BLACK)
            name_height = User_A.get_height()
            A_asset = font_Max.render("현재 잔액: " + str(self.users.user_list[0].money), True, BLACK)
            F_size = A_asset.get_height()
            A_Items_tit = font_Max.render("아이템 리스트: ", True, BLACK)
            i = 0
            for i, item in enumerate(self.users.user_list[0].items):
                if isinstance(item, Item):
                    A_Items_List = font_Max.render(item.name + " ", True, BLACK)
                    self.window.blit(A_Items_List, (20, name_height + 2 * F_size + 30 + (F_size + 5) * i))
            self.window.blit(User_A, (10, 10))
            self.window.blit(A_asset, (10, 10 + name_height + 5))
            self.window.blit(A_Items_tit, (10, 10 + name_height + F_size+ 10))
            
            User_B = font3.render(self.users.user_list[1].name, True, (0, 0, 0))
            name_height = User_B.get_height()
            B_asset = font_Max.render("현재 잔액: " + str(self.users.user_list[1].money), True, BLACK)
            F_size = B_asset.get_height()
            B_Items_tit = font_Max.render("아이템 리스트: ", True, BLACK)
            i = 0
            for i, item in enumerate(self.users.user_list[1].items):
                if isinstance(item, Item):
                    B_Items_List = font_Max.render(item.name + " ", True, BLACK)
                    self.window.blit(B_Items_List, (20, name_height + 2 * F_size + 30 + (F_size + 5) * i + HEIGHT* 3 / 4))
            self.window.blit(User_B, (10, HEIGHT * 3 / 4 + 10))
            self.window.blit(B_asset, (10, HEIGHT * 3 / 4 + 10 + name_height + 5))
            self.window.blit(B_Items_tit, (10, HEIGHT * 3 / 4 + 10 + name_height + F_size+ 10))
            
            User_D = font3.render(self.users.user_list[2].name, True, (0, 0, 0))
            name_height = User_D.get_height()
            D_asset = font_Max.render("현재 잔액: " + str(self.users.user_list[2].money), True, BLACK)
            F_size = D_asset.get_height()
            D_Items_tit = font_Max.render("아이템 리스트: ", True, BLACK)
            i = 0
            for i, item in enumerate(self.users.user_list[2].items):
                if isinstance(item, Item):
                    D_Items_List = font_Max.render(item.name + " ", True, BLACK)
                    self.window.blit(D_Items_List, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, name_height + 2 * F_size + 30 + (F_size + 5) * i + HEIGHT * 3 / 4))
            self.window.blit(User_D, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, HEIGHT * 3 / 4 + 10))
            self.window.blit(D_asset, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, HEIGHT * 3 / 4 + 10 + name_height + 5))
            self.window.blit(D_Items_tit, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, HEIGHT * 3 / 4 + 10 + name_height + F_size+ 10))
        elif len(self.users) == 4:
            User_A = font3.render(self.users.user_list[0].name, True, BLACK)
            name_height = User_A.get_height()
            A_asset = font_Max.render("현재 잔액: " + str(self.users.user_list[0].money), True, BLACK)
            F_size = A_asset.get_height()
            A_Items_tit = font_Max.render("아이템 리스트: ", True, BLACK)
            i = 0
            for i, item in enumerate(self.users.user_list[0].items):
                if isinstance(item, Item):
                    A_Items_List = font_Max.render(item.name + " ", True, BLACK)
                    self.window.blit(A_Items_List, (20, name_height + 2 * F_size + 30 + (F_size + 5) * i))
            self.window.blit(User_A, (10, 10))
            self.window.blit(A_asset, (10, 10 + name_height + 5))
            self.window.blit(A_Items_tit, (10, 10 + name_height + F_size+ 10))
            
            User_B = font3.render(self.users.user_list[1].name, True, (0, 0, 0))
            name_height = User_B.get_height()
            B_asset = font_Max.render("현재 잔액: " + str(self.users.user_list[1].money), True, BLACK)
            F_size = B_asset.get_height()
            B_Items_tit = font_Max.render("아이템 리스트: ", True, BLACK)
            i = 0
            for i, item in enumerate(self.users.user_list[1].items):
                if isinstance(item, Item):
                    B_Items_List = font_Max.render(item.name + " ", True, BLACK)
                    self.window.blit(B_Items_List, (20, name_height + 2 * F_size + 30 + (F_size + 5) * i + HEIGHT* 3 / 4))
            self.window.blit(User_B, (10, HEIGHT * 3 / 4 + 10))
            self.window.blit(B_asset, (10, HEIGHT * 3 / 4 + 10 + name_height + 5))
            self.window.blit(B_Items_tit, (10, HEIGHT * 3 / 4 + 10 + name_height + F_size+ 10))
            
            User_C = font3.render(self.users.user_list[2].name, True, (0, 0, 0))
            name_height = User_C.get_height()
            C_asset = font_Max.render("현재 잔액: " + str(self.users.user_list[2].money), True, BLACK)
            F_size = C_asset.get_height()
            C_Items_tit = font_Max.render("아이템 리스트: ", True, BLACK)
            i = 0
            for i, item in enumerate(self.users.user_list[2].items):
                if isinstance(item, Item):
                    C_Items_List = font_Max.render(item.name + " ", True, BLACK)
                    self.window.blit(C_Items_List, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10 , name_height + 2 * F_size + 30 + (F_size + 5) * i))
            self.window.blit(User_C, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, 10))
            self.window.blit(C_asset, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, 10 + name_height + 5))
            self.window.blit(C_Items_tit, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, 10 + name_height + F_size+ 10))
            
            User_D = font3.render(self.users.user_list[3].name, True, (0, 0, 0))
            name_height = User_D.get_height()
            D_asset = font_Max.render("현재 잔액: " + str(self.users.user_list[3].money), True, BLACK)
            F_size = D_asset.get_height()
            D_Items_tit = font_Max.render("아이템 리스트: ", True, BLACK)
            i = 0
            for i, item in enumerate(self.users.user_list[3].items):
                if isinstance(item, Item):
                    D_Items_List = font_Max.render(item.name, True, BLACK)
                    self.window.blit(D_Items_List, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, name_height + 2 * F_size + 30 + (F_size + 5) * i + HEIGHT * 3 / 4))
            self.window.blit(User_D, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, HEIGHT * 3 / 4 + 10))
            self.window.blit(D_asset, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, HEIGHT * 3 / 4 + 10 + name_height + 5))
            self.window.blit(D_Items_tit, ((WIDTH - HEIGHT) / 2 + HEIGHT + 10, HEIGHT * 3 / 4 + 10 + name_height + F_size+ 10))

        #땅 정보
        if self.click_ground == 1:
            info = Ground_Info(self.window)
            info.draw_info(self.Trgt_Block)
        
        #빌라 호텔 생성
        for block in self.board.blocks:
            if block.owner != None:
                if block.position < 10:
                    if block.villas == 1:
                        if block.owner.name == '1P':
                            self.window.blit(Villa_A, (block.rect.left, block.rect.top))
                        elif block.owner.name == '2P':
                            self.window.blit(Villa_B, (block.rect.left, block.rect.top))
                        elif block.owner.name == '3P':
                            self.window.blit(Villa_C, (block.rect.left, block.rect.top))
                        else:
                            self.window.blit(Villa_D, (block.rect.left, block.rect.top))
                    if block.hotels == 1:
                        if block.owner.name == '1P':
                            self.window.blit(Hotel_A, (block.rect.centerx, block.rect.top))
                        elif block.owner.name == '2P':
                            self.window.blit(Hotel_B, (block.rect.centerx, block.rect.top))
                        elif block.owner.name == '3P':
                            self.window.blit(Hotel_C, (block.rect.centerx, block.rect.top))
                        else:
                            self.window.blit(Hotel_D, (block.rect.centerx, block.rect.top))
                elif block.position < 20:
                    if block.villas == 1:
                        if block.owner.name == '1P':
                            self.window.blit(Villa_A, (block.rect.centerx + HEIGHT/26, block.rect.top))
                        elif block.owner.name == '2P':
                            self.window.blit(Villa_B, (block.rect.centerx + HEIGHT/26, block.rect.top))
                        elif block.owner.name == '3P':
                            self.window.blit(Villa_C, (block.rect.centerx + HEIGHT/26, block.rect.top))
                        else:
                            self.window.blit(Villa_D, (block.rect.centerx + HEIGHT/26, block.rect.top))
                    if block.hotels == 1:
                        if block.owner.name == '1P':
                            self.window.blit(Hotel_A, (block.rect.centerx + HEIGHT/26, block.rect.centery))
                        elif block.owner.name == '2P':
                            self.window.blit(Hotel_B, (block.rect.centerx + HEIGHT/26, block.rect.centery))
                        elif block.owner.name == '3P':
                            self.window.blit(Hotel_C, (block.rect.centerx + HEIGHT/26, block.rect.centery))
                        else:
                            self.window.blit(Hotel_D, (block.rect.centerx + HEIGHT/26, block.rect.centery))
                elif block.position < 30:
                    if block.villas == 1:
                        if block.owner.name == '1P':
                            self.window.blit(Villa_A, (block.rect.centerx, block.rect.bottom - HEIGHT/26))
                        elif block.owner.name == '2P':
                            self.window.blit(Villa_B, (block.rect.centerx, block.rect.bottom - HEIGHT/26))
                        elif block.owner.name == '3P':
                            self.window.blit(Villa_C, (block.rect.centerx, block.rect.bottom - HEIGHT/26))
                        else:
                            self.window.blit(Villa_D, (block.rect.centerx, block.rect.bottom - HEIGHT/26))
                    if block.hotels == 1:
                        if block.owner.name == '1P':
                            self.window.blit(Hotel_A, (block.rect.left, block.rect.bottom - HEIGHT/26))
                        elif block.owner.name == '2P':
                            self.window.blit(Hotel_B, (block.rect.left, block.rect.bottom - HEIGHT/26))
                        elif block.owner.name == '3P':
                            self.window.blit(Hotel_C, (block.rect.left, block.rect.bottom - HEIGHT/26))
                        else:
                            self.window.blit(Hotel_D, (block.rect.left, block.rect.bottom - HEIGHT/26))
                else:
                    if block.villas == 1:
                        if block.owner.name == '1P':
                            self.window.blit(Villa_A, (block.rect.left, block.rect.centery))
                        elif block.owner.name == '2P':
                            self.window.blit(Villa_B, (block.rect.left, block.rect.centery))
                        elif block.owner.name == '3P':
                            self.window.blit(Villa_C, (block.rect.left, block.rect.centery))
                        else:
                            self.window.blit(Villa_D, (block.rect.left, block.rect.centery))
                    if block.hotels == 1:
                        if block.owner.name == '1P':
                            self.window.blit(Hotel_A, (block.rect.left, block.rect.top))
                        elif block.owner.name == '2P':
                            self.window.blit(Hotel_B, (block.rect.left, block.rect.top))
                        elif block.owner.name == '3P':
                            self.window.blit(Hotel_C, (block.rect.left, block.rect.top))
                        else:
                            self.window.blit(Hotel_D, (block.rect.left, block.rect.top))
        
        #황금열쇠 획득 이펙트
        for users in self.users.user_list:
            if users.ifadd == 1:
                UGET_ITEM = font_RULE_TITLE.render("아이템 획득", True, BLACK)
                g_width, g_height = UGET_ITEM.get_width(), UGET_ITEM.get_height()
                self.window.blit(UGET_ITEM, (WIDTH/2 - g_width/2, HEIGHT/2 - g_height*2))
                font_Item = pygame.font.Font(font_JALNAN, 60)
                itemget = font_Item.render(users.items[len(users.items) - 1].name , True, BLACK)
                i_width = itemget.get_width()
                self.window.blit(itemget, (WIDTH/2 - i_width/2, HEIGHT*3/4))

        self.log_instance.draw_log(self.window)

        pygame.display.flip()



    def Ground_Click(self, x, y):
        for blocks in self.board.blocks:
            if blocks.rect.collidepoint(x, y):
                return blocks.position
        return None





#땅 정보
class Ground_Info:
    def __init__(self, window):
        self.window = window

    def draw_info(self, block):
        pygame.draw.rect(self.window, WHITE, Inform_Space)
        
        Name_tit = font_Info.render("토지 이름: ", True, BLACK)
        
        if block.position == 20 or block.position == 21 or block.position == 28 or block.position == 38:
            Name_txt = font_Max.render(block.name, True, BLACK)
        else:
            Name_txt = font_Info.render(block.name, True, BLACK)
        
        price_tit, price_txt, toll_tit, toll_txt, Owner_tit, Owner_txt, villa_tit, villa_txt, hotel_tit, hotel_txt = [None] * 10
        
        if block.price != 0:
            price_tit = font_Info.render("토지 가격: ", True, BLACK)
            price_txt = font_Info.render(str(block.price), True, BLACK)
            
        if block.block_type == BlockType.PROPERTY:
            toll_tit = font_Info.render("통행세: ", True, BLACK)
            toll_txt = font_Info.render(str(int(block.toll)), True, BLACK)
            
            if block.owner != None:
                Owner_tit = font_Info.render("토지 소유주: ", True, BLACK)
                Owner_txt = font_Info.render(str(block.owner.name), True, BLACK)
                villa_tit = font_Info.render("빌라 수: ", True, BLACK)
                villa_txt = font_Info.render(str(block.villas), True, BLACK)
                hotel_tit = font_Info.render("호텔 수: ", True, BLACK)
                hotel_txt = font_Info.render(str(block.hotels), True, BLACK)
                
        F_HEIGHT = Name_tit.get_height()

        self.window.blit(Name_tit, (0, HEIGHT/4))
        self.window.blit(Name_txt, (10, HEIGHT/4 + F_HEIGHT))

        if price_tit:
            self.window.blit(price_tit, (0, HEIGHT/4 + F_HEIGHT * 4))
        if price_txt:
            self.window.blit(price_txt, (10, HEIGHT/4 + F_HEIGHT * 5))
            
        if toll_tit:
            self.window.blit(toll_tit, (0, HEIGHT/4 + F_HEIGHT * 6))
        if toll_txt:
            self.window.blit(toll_txt, (10, HEIGHT/4 + F_HEIGHT * 7))
            
        if Owner_tit:
            self.window.blit(Owner_tit, (0, HEIGHT/4 + F_HEIGHT * 2))
        if Owner_txt:
            self.window.blit(Owner_txt, (10, HEIGHT/4 + F_HEIGHT * 3))
            
        if villa_tit:
            self.window.blit(villa_tit, (0, HEIGHT/4 + F_HEIGHT * 8))
        if villa_txt:
            self.window.blit(villa_txt, (10, HEIGHT/4 + F_HEIGHT * 9))
            
        if hotel_tit:
            self.window.blit(hotel_tit, (0, HEIGHT/4 + F_HEIGHT * 10))
        if hotel_txt:
            self.window.blit(hotel_txt, (10, HEIGHT/4 + F_HEIGHT * 11))




Podium = pygame.image.load("Pictures/Podium.png")
Po_Width, Po_Height = Podium.get_width(), Podium.get_height()
Podium = pygame.transform.scale(Podium, (2*Po_Width, 2*Po_Height))
Po_Width, Po_Height = Podium.get_width(), Podium.get_height()
class Ending:
    def __init__(self, window, user):
        self.window = window
        self.user = user
        self.rank = self.user.player_rank()

    def draw(self):
        background = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        background.fill((0, 0, 0, 200))
        self.window.blit(background, (0, 0))
        self.window.blit(Podium, (WIDTH / 2 - Po_Width/2, HEIGHT/2 - Po_Height/2))
        if len(self.user.user_list) == 2:
            First = font_RULE_TITLE.render(str(self.rank[0].name), True, WHITE)
            First_width, First_height = First.get_width(), First.get_height()
            Second = font_RULE_TITLE.render(str(self.rank[1].name), True, WHITE)
            Second_width, Second_height = Second.get_width(), Second.get_height()
            self.window.blit(First, (WIDTH/2 - First_width/2 - 10, HEIGHT/2 - First_height*2 + 30))
            self.window.blit(Second, (WIDTH/2 + Second_width + 15, HEIGHT/2 - Second_height))
        if len(self.user.user_list) == 3:
            First = font_RULE_TITLE.render(str(self.rank[0].name), True, WHITE)
            First_width, First_height = First.get_width(), First.get_height()
            Second = font_RULE_TITLE.render(str(self.rank[1].name), True, WHITE)
            Second_width, Second_height = Second.get_width(), Second.get_height()
            Third = font_RULE_TITLE.render(str(self.rank[2].name), True, WHITE)
            Third_width, Third_height = Third.get_width(), Third.get_height()
            self.window.blit(First, (WIDTH/2 - First_width/2 - 10, HEIGHT/2 - First_height*2 + 30))
            self.window.blit(Second, (WIDTH/2 + Second_width + 15, HEIGHT/2 - Second_height))
            self.window.blit(Third, (WIDTH/2 - 2 * Third_width - 20, HEIGHT/2 - Third_height/2))
        if len(self.user.user_list) == 4:
            First = font_RULE_TITLE.render(str(self.rank[0].name), True, WHITE)
            First_width, First_height = First.get_width(), First.get_height()
            Second = font_RULE_TITLE.render(str(self.rank[1].name), True, WHITE)
            Second_width, Second_height = Second.get_width(), Second.get_height()
            Third = font_RULE_TITLE.render(str(self.rank[2].name), True, WHITE)
            Third_width, Third_height = Third.get_width(), Third.get_height()
            self.window.blit(First, (WIDTH/2 - First_width/2 - 10, HEIGHT/2 - First_height*2 + 30))
            self.window.blit(Second, (WIDTH/2 + Second_width + 15, HEIGHT/2 - Second_height))
            self.window.blit(Third, (WIDTH/2 - 2 * Third_width - 20, HEIGHT/2 - Third_height/2))