import sys
from bluemarble_UI import *
from ground import *
from player import *

pygame.init()
board = Board.make_block()
users = Users()
dice = Dice(random.randint(1, 6), random.randint(1, 6))
def buy_ground (user, board):
    build = 0
    while(build == 0): 
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYUP and event.key == pygame.K_b and (board.blocks[int(user.position)].owner!=user) :
                board.blocks[int(user.position)].purchase_property(user)
            elif event.type == pygame.KEYUP and event.key == pygame.K_b and board.blocks[int(user.position)].owner == user and board.blocks[int(user.position)].villas==0:
                board.blocks[int(user.position)].build_villa(user)
            elif event.type == pygame.KEYUP and event.key == pygame.K_b and board.blocks[int(user.position)].owner == user and board.blocks[int(user.position)].villas==1:
                board.blocks[int(user.position)].build_hotel(user)
            elif event.type == pygame.KEYUP and event.key == pygame.K_1:
                if len(user.items)>=1:
                    item_num=user.items[0].number
                    if(item_num==1 or item_num==2):
                        while(1):
                            tgt=users.user_list[random.randint(0, 3)]
                            if(tgt!=user):
                                break
                            else:
                                pass
                        user.items[0].Use_item_tgt(user,item_num,tgt)
                        user.items.pop(0)
                    elif(item_num<=7):
                        user.items[0].Use_item(user,item_num)
                        user.items.pop(0)
            elif event.type == pygame.KEYUP and event.key == pygame.K_2:
                if len(user.items)>=2:
                    item_num=user.items[1].number
                    if(item_num==1 or item_num==2):
                        while(1):
                            tgt=users.user_list[random.randint(0, 3)]
                            if(tgt!=user):
                                break
                            else:
                                pass
                        user.items[1].Use_item_tgt(user,item_num,tgt)
                        user.items.pop(1)
                    elif(item_num<=7):
                        user.items[1].Use_item(user,item_num)
                        user.items.pop(1)
            elif event.type == pygame.KEYUP and event.key == pygame.K_3:
                if len(user.items)>=3:
                    item_num=user.items[2].number
                    if(item_num==1 or item_num==2):
                        while(1):
                            tgt=users.user_list[random.randint(0, 3)]
                            if(tgt!=user):
                                break
                            else:
                                pass
                        user.items[2].Use_item_tgt(user,item_num,tgt)
                        user.items.pop(2)
                    elif(item_num<=7):
                        user.items[2].Use_item(user,item_num)
                        user.items.pop(2)
            elif event.type == pygame.KEYUP and event.key == pygame.K_4:
                if len(user.items)>=4:
                    item_num=user.items[3].number
                    if(item_num==1 or item_num==2):
                        while(3):
                            tgt=users.user_list[random.randint(0, 3)]
                            if(tgt!=user):
                                break
                            else:
                                pass
                        user.items[3].Use_item_tgt(user,item_num,tgt)
                        user.items.pop(3)
                    elif(item_num<=7):
                        user.items[3].Use_item(user,item_num)
                        user.items.pop(3)
            elif event.type == pygame.KEYUP and event.key == pygame.K_5:
                if len(user.items)>=5:
                    item_num=user.items[4].number
                    if(item_num==1 or item_num==2):
                        while(1):
                            tgt=users.user_list[random.randint(0, 3)]
                            if(tgt!=user):
                                break
                            else:
                                pass
                        user.items[4].Use_item_tgt(user,item_num,tgt)
                        user.items.pop(4)
                    elif(item_num<=7):
                        user.items[4].Use_item(user,item_num)
                        user.items.pop(4)
            elif event.type == pygame.KEYUP and event.key == pygame.K_t:
                build+=1
                break 

class PygameWindow:
    def __init__(self):
        pygame.init() 
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_screen = START_MENU(self.screen, board, users, dice, log_instance)
        
    

    def run_game(self):
        current_user_index = 0
        game_turn=0
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if type(self.current_screen) ==GAME_SCREEN:
                    user = users.user_list[current_user_index]  # 현재 사용자
                    if(user.SE):
                        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                            if user.position != 10 and user.position !=30:
                                if dice.roll_dice(user) == True:
                                    user.move(sum(dice.dice))
                                    log_instance.add_message(" ")
                                    log_instance.add_message("더블! 한번더!")
                                    self.current_screen.draw(board)
                                    pygame.display.flip()
                                    buy_ground(user, board)
                                    if board.blocks[int(user.position)].owner!=user and board.blocks[int(user.position)].owner !=None:
                                        board.blocks[int(user.position)].pay_toll(user)
                                        board.blocks[int(user.position)].owner.money += board.blocks[int(user.position)].toll
                                    break
                                else:
                                    user.move(sum(dice.dice))
                                    self.current_screen.draw(board)
                                    pygame.display.flip()
                                    buy_ground(user, board)
                                if board.blocks[int(user.position)].owner!=user and board.blocks[int(user.position)].owner !=None:
                                    board.blocks[int(user.position)].pay_toll(user)
                                    board.blocks[int(user.position)].owner.money += board.blocks[int(user.position)].toll
                            if user.position == 2 or user.position==7 or user.position == 12 or user.position == 17 or user.position == 22 or user.position == 35:
                                user.add_item()
                            if user.position == 30:
                                log_instance.add_message(" ")
                                log_instance.add_message("(다음 턴에 여행 가능)")
                                log_instance.add_message("우주여행 도착!")
                                log_instance.add_message(f"({user.name})")
                                move=0
                                while(move==0):
                                    events = pygame.event.get()
                                    for event in events:
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            if event.button == 1:
                                                x, y = pygame.mouse.get_pos()
                                                wantposition = board.get_block_at_position(self.current_screen.Ground_Click(x, y)).position
                                                user.position = wantposition
                                                buy_ground(user, board)
                                                if board.blocks[int(user.position)].owner!=user and board.blocks[int(user.position)].owner !=None:
                                                    board.blocks[int(user.position)].pay_toll(user)
                                                    board.blocks[int(user.position)].owner.money += board.blocks[int(user.position)].toll
                                                move+=1
                                                self.current_screen.draw(board)
                                                pygame.display.flip()
                                                buy_ground(user, board)
                                
                            
                            if user.position == 10 and user.jail_turn == 0:
                                user.jail_turn += 1
                                log_instance.add_message(" ")
                                log_instance.add_message(f"표류된 턴 : {user.jail_turn}")
                                log_instance.add_message("무인도에 도착!")
                                log_instance.add_message(f"({user.name})")
                            elif user.position == 10 and user.jail_turn == 3:
                                if dice.roll_dice(user) == True:
                                    user.move(sum(dice.dice))
                                    log_instance.add_message("")
                                    log_instance.add_message("더블! 한번더!")
                                    log_instance.add_message(f"({user.name})")
                                    break
                                user.move(sum(dice.dice))
                                user.jail_turn = 0
                            elif user.position == 10:
                                if dice.roll_dice(user) == True:
                                    user.move(sum(dice.dice))
                                    log_instance.add_message(" ")
                                    log_instance.add_message("더블! 탈출 성공")
                                    log_instance.add_message(f"({user.name})")
                                else:
                                    user.jail_turn += 1
                                    log_instance.add_message(" ")
                                    log_instance.add_message(f"표류된 턴 : {user.jail_turn}")
                                    log_instance.add_message(f"({user.name})")

                            if user.position == 20:
                                log_instance.add_message(" ")
                                log_instance.add_message(f"+{board.blocks[20].price}")
                                log_instance.add_message("복지금 수령처 도착!")
                                log_instance.add_message(f"({user.name})")
                                if board.blocks[20].price != 0:
                                    user.money += board.blocks[20].price
                                    board.blocks[20].price = 0
                            
                    
                            if user.SE:
                                users.user_list[current_user_index].turns += 1
                                current_user_index = (current_user_index + 1) % (len(self.current_screen.users))
                                if users.user_list[0].turns==users.user_list[len(users.user_list)-1].turns:
                                    game_turn+=1
                                    log_instance.add_message(" ")
                                    log_instance.add_message(f"게임턴: {game_turn}")
                                    log_instance.add_message(f"({user.name})") 
                                if game_turn==20:
                                    self.current_screen = Ending(self.screen, users)
                    if user.SE == False:
                        users.user_list[current_user_index].turns += 1
                        current_user_index = (current_user_index + 1) % (len(self.current_screen.users))
                        if users.user_list[0].turns==users.user_list[len(users.user_list)-1].turns:
                            game_turn+=1
                            log_instance.add_message(" ")
                            log_instance.add_message(f"게임턴: {game_turn}")
                    count = 0
                    for user in users.user_list:
                        if user.SE == False: 
                            count += 1
                        if count == len(users.user_list)-1:
                            self.current_screen = Ending(self.screen, users)
                if type(self.current_screen)==Ending:
                    if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        pygame.quit()
                        sys.exit()

                          

                        
            if type(self.current_screen)==START_MENU:          
                self.current_screen.draw()
                pygame.display.flip()
                self.current_screen = self.current_screen.handle_events(events)
            if type(self.current_screen) == Loading:
                self.current_screen.draw_loading()
                pygame.display.flip()
                self.current_screen = self.current_screen.handle_events(events)
            if type(self.current_screen)==GAME_SCREEN:
                
                self.current_screen.draw(board)                
                pygame.display.flip()
                for user in self.current_screen.users.user_list:
                    if user.ifadd == 1:
                        pygame.time.delay(3000)
                        user.ifadd = 0
                self.current_screen = self.current_screen.handle_events(events)
                self.clock.tick(60)
            elif type(self.current_screen) == Ending:
                self.current_screen.draw()
                pygame.display.flip()
            self.clock.tick(60)

            

            

if __name__ == "__main__":
    window = PygameWindow()
    window.run_game()
pygame.quit()