import pygame
import random
from log import *

BOARD_SIZE = 40
NUMBERS_OF_ITEMS = 7
NUMBERS_OF_BURSTS = 5

log_instance = Log_Info()

class User:
    def __init__(self, name = None):
        self.name = name
        self.position = 0
        self.items = []  # 가지고 있는 아이템을 저장할 리스트
        self.dice = 0  # 주사위 숫자를 저장할 변수
        self.dice_rolls = 0 #주사위 두 번까지 굴릴수있게 추적(아이템에도 활용가능)
        self.money = 3000000
        self.turns = 0
        self.SE = True
        self.dice1=0
        self.dice2=0
        self.double=False
        self.properties = []
        self.jail_turn = 0
        self.ppt=0
        self.time = 0
        self.ifadd = 0

    def get_total_money(self):
        pro_price=0
        for propertie in self.properties:
            land_price=propertie.price
            villa_price=propertie.villas*propertie.villa_cost
            hotel_price=propertie.hotels*propertie.hotel_cost
            pro_price+=land_price+villa_price+hotel_price
        self.ppt=pro_price
    
    def roll_dice(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.dice = pygame.math.Vector2(self.dice1, self.dice2)
        print(self.name)
        print(self.dice1 , self.dice2)
        if (self.dice1 == self.dice2):
            double = True
            return double
        elif (self.dice1 != self.dice2):
            double = False
            return double

    def move(self, moving):
        # 현재 위치 저장
        Slocate = self.position
        # 입력된 숫자만큼 이동
        self.position += moving
        if self.position >= BOARD_SIZE:  # 보드의 크기에 따라 설정
            self.position -= BOARD_SIZE
        # 나중 위치 저장
        Elocate = self.position

        if Elocate < Slocate:
            self.money += 200000
    def add_item(self):
    # 아이템 획득
        item_or_burst = random.randint(1, 2)
        if item_or_burst == 1:
            self.items.append(ITEM_LIST[random.randint(2, NUMBERS_OF_ITEMS)])
            self.ifadd = 1
        elif item_or_burst == 2:
            WhatBurst = random.randint(1, NUMBERS_OF_BURSTS)
            if WhatBurst == 1:
                Burst.Burst_Fine(self)
            elif WhatBurst == 2:
                self.properties = sorted(self.properties, key=lambda x: x.price)
                if len(self.properties) != 0:
                    lossblock = self.properties[0]
                    Burst.Burst_LossBlock(self, lossblock)
                else:
                    log_instance.add_message("보유한 땅이 없습니다.")
            elif WhatBurst == 3:
                Burst.Burst_Drifting(self)
            elif WhatBurst == 4:
                Burst.Burst_Lotto(self)
    
    def locate(self):
        log_instance.add_message(self.name + "님의 현재 위치:", self.position, "번째 칸")

    def use_item(self, item):
        # 아이템 사용
        if item in self.items:
            self.items.remove(item)
            # 아이템 사용에 따른 동작을 추가

    def item_list(self):
        if len(self.items) == 0:
            log_instance.add_message("보유중인 아이템이 없습니다!")
        else:
            log_instance.add_message(self.name + "님이 보유중인 아이템:", *self.items)
class Users:
        def __init__(self):
            self.user_list = []
        def player_rank(self):
            rank=1
            self.Rank = []
            for user in self.user_list:
                user.get_total_money()
            self.user_list = sorted(self.user_list, key=lambda user: user.money + user.ppt, reverse=True)
            for user in self.user_list:
                if user.SE == True:
                    log_instance.add_message(f"순위: {rank}, 이름: {user.name}, 재산: {int(user.ppt+user.money)} 토지재산: {int(user.ppt)} 현금재산: {int(user.money)}")
                    rank+=1
                    self.Rank.append(user)
            self.user_list = sorted(self.user_list, key=lambda user: user.time,reverse=True)
            for user in self.user_list:
                if user.SE==False:
                    log_instance.add_message(f"순위: {rank}, 이름: {user.name}, 재산: {int(user.ppt+user.money)} 토지재산: {int(user.ppt)} 현금재산: {int(user.money)}")
                    rank+=1
                    self.Rank.append(user)
            return self.Rank
        def add_user(self, user):
            self.user_list.append(user)

        def make_Userlist(self, players):
            for i in range(1, players+1):
                self.add_user(User(f"{i}P"))
        def __len__(self):
            return len(self.user_list)
class Item:
    item_number = list(range(1,20))
    item_rarity = {"희귀", "영웅", "전설"}
    def __init__(self, name, number, rarity):
        self.name = name
        self.number = number
        self.rarity = rarity
    def Item_Frozen(self,user,enemy):
        enemy.SE = "얼음"

    def Item_Steal(self, user, enemy, block):
        log_instance.add_message(f"{user.name}님이 {enemy.name}님의 \"{block.name}\"을(를) 빼앗았습니다!")
        block.owner = user
    
    def Item_dice_Onemore(self, user):
        idx1 = random.randint(1,6)
        idx2 = random.randint(1,6)
        dice = Dice(idx1, idx2)
        dice.roll_dice(user)
        user.move(sum(int(dice.dice)))
        

    def Item_3block(self, user):
        log_instance.add_message(f"{user.name}님이 \"{self.name}\"아이템 사용! 3칸 이동합니다")
        User.move(user, 3)

    def Item_ReStart(self, user):
        log_instance.add_message(f"{user.name}님이 \"{self.name}\"아이템 사용! 출발지로 이동합니다")
        moving = BOARD_SIZE - user.position
        User.move(user, moving)
    
    def Item_Musk(self, user):
        log_instance.add_message(f"{user.name}님이 \"{self.name}\"아이템 사용! 우주여행으로 이동합니다")
        moving = 30 - user.position
        User.move(user, moving)

    def Item_receive(self, user):
        log_instance.add_message(f"{user.name}님이 \"{self.name}\"아이템 사용! 사회복지기금(수령처)으로 이동합니다")
        moving = 20 - user.position
        User.move(user, moving)

    def Use_item_tgt(self,user,number,tgt):
        if number==2:
            if(len(tgt.properties)!=0):
                self.Item_Steal(user, tgt,tgt.properties[0])
                user.properties.append(tgt.properties[0])
                tgt.properties.pop(0)
            else:
                print("상대토지가없어요")

    def Use_item(self,user,number):
        if number==3:
            self.Item_dice_Onemore(user)
        if number==4:
            self.Item_3block(user)
        if number==5:
            self.Item_ReStart(user)
        if number==6:
            self.Item_Musk(user)
        if number==7:
            self.Item_receive(user)
class Burst:
    def __init__(self, name, number, rarity):
        self.name = name
        self.number = number
        self.rarity = rarity

    def Burst_Fine(user):
        log_instance.add_message(f"{user.name}님이 세금 납부!")
        user.money -= 200000
    
    def Burst_LossBlock(user, block):
        log_instance.add_message(f"{user.name}님이 {block.name}의 소유권 상실!")
        block.owner = None
    
    def Burst_Drifting(user):
        log_instance.add_message(f"{user.name}님이 무인도에 표류되었어요!")
        if user.position <= 10:
            moving = 10 - user.position
        elif user.position > 10:
            moving = BOARD_SIZE - (user.position - 10)
        User.move(user, moving)

    def Burst_Lotto(user):
        log_instance.add_message("복권에 당첨되었습니다! 1000000원 획득!")
        user.money += 1000000

    def Burst_Donate(user):
        log_instance.add_message(f"{user.name}님이 기부 당첨!")
        if user.position <= 38:
            moving = 38 - user.position
        elif user.position > 38:
            moving = BOARD_SIZE - (user.position - 38)
        User.move(user, moving)

ITEM_LIST = []
BURST_LIST = []
ITEM_LIST.extend([0, Item("얼음!", 1, "영웅"), Item("도시 강탈", 2, "전설"), Item("주사위 한번 더!", 3, "희귀"), Item("세 보 앞으로", 4, "희귀"), Item("새출발", 5, "영웅"), Item("우주 여행 무료 티켓", 6, "희귀"),Item("기부받기", 7, "영웅") ])
BURST_LIST.extend([0, Burst("벌금 납부", 1, "희귀"), Burst("쿠데타", 2, "전설"), Burst("무인도 표류", 3, "영웅"), Burst("복권 당첨!", 4, "희귀"), Burst("강제 기부", 5, "영웅")]) 

class Dice:
    def __init__(self, idx1, idx2):
        self.image1 = pygame.image.load(f"Pictures/{idx1}.png")
        self.image1 = pygame.transform.scale(self.image1, (WIDTH/10, HEIGHT/10))
        self.image2 = pygame.image.load(f"Pictures/{idx2}.png")
        self.image2 = pygame.transform.scale(self.image2, (WIDTH/10, HEIGHT/10))
        self.dice1 = 0
        self.dice2 = 0
        self.dice = 0
        self.angle = 0
        self.idx1 = idx1
        self.idx2 = idx2
        
        
    def roll_dice(self, user):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.image1 = pygame.image.load(f"Pictures/{self.dice1}.png")
        self.image1 = pygame.transform.scale(self.image1, (WIDTH/12, HEIGHT/10))
        self.image2 = pygame.image.load(f"Pictures/{self.dice2}.png")
        self.image2 = pygame.transform.scale(self.image2, (WIDTH/12, HEIGHT/10))
        self.dice = pygame.math.Vector2(self.dice1, self.dice2)
        log_instance.add_message(f"{user.name}")
        log_instance.add_message(f"{self.dice1} , {self.dice2}")
        if (self.dice1 == self.dice2):
            double = True
            self.roll = True
            return double
        elif (self.dice1 != self.dice2):
            double = False
            self.roll = True
            return double
    