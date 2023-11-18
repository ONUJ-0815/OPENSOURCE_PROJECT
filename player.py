import pygame
import random

BOARD_SIZE = 40

class User:
    def __init__(self, name = None, money = None):
        self.name = name
        self.position = 0
        self.items = [6]  # 가지고 있는 아이템을 저장할 리스트
        self.dice = 0  # 주사위 숫자를 저장할 변수
        self.dice_rolls = 0 #주사위 두 번까지 굴릴수있게 추적(아이템에도 활용가능)
        self.money = 0
        self.turns = 0
        self.SE = ''

    def roll_dice(self):
        # 이 부분에 턴 시작 + 턴 추가
        # 주사위를 굴린 후 나온 숫자를 self.dice에 저장
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.dice = pygame.math.Vector2(self.dice1, self.dice2)
        print(self.dice1 , self.dice2)
        self.move(sum(self.dice))

        if self.dice1 == self.dice2 and self.dice_rolls < 2:
            print("더블! 한번 더!")
            self.dice_rolls += 1
            self.roll_dice()

        elif self.dice_rolls >= 2:
            self.dice_rolls = 0
            self.dice1 = 0
            self.dice2 = 0
        # 이 부분에 턴 끝나는 명령어 추가

    def roll_dice_event(self):
        #이벤트 전용 다이스굴리기
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.dice = pygame.math.Vector2(self.dice1, self.dice2)
        if (self.dice1 == self.dice2):
            double = True
        elif (self.dice1 != self.dice2):
            double = False

    def move(self, moving):
        # 입력된 숫자만큼 이동
        self.position += moving
        if self.position >= BOARD_SIZE:  # 보드의 크기에 따라 설정
            self.position -= BOARD_SIZE
    
    def locate(self):
        print(self.name + "님의 현재 위치:", self.position, "번째 칸")

    def use_item(self, item):
        # 아이템 사용
        if item in self.items:
            self.items.remove(item)
            # 아이템 사용에 따른 동작을 추가

    def add_item(self, item):
        # 아이템 획득
        self.items.append(item)

    def item_list(self):
        if len(self.items) == 0:
            print("보유중인 아이템이 없습니다!")
        else:
            print(self.name + "님이 보유중인 아이템:", *self.items)

class Item:
    lotto_money = 1000000
    item_number = list(range(1,20))
    item_rarity = {"희귀", "영웅", "전설"}
    def __init__(self, name, number, rarity, percent):
        self.name = name
        self.number = number
        self.rarity = rarity
        self.percent = percent

    def Logic_dice(self):
        User.dice1 = random.randint(1, 6)
        User.dice2 = random.randint(1, 6)
        User.dice = pygame.math.Vector2(self.dice1, self.dice2)
        double = User.dice1 == User.dice2
        return double
    
    def Item_Lotto(self, user):
        print("복권에 당첨되었습니다! {Item.lotto_money}원 획득!")
        user.money += self.lotto_money

    def Item_Froze(self, user, enemy):
        print("{user.name}님이{enemy.name}님에게 {self.name}아이템을 사용하였습니다!")
        enemy.SE = "얼음"

    def Item_Steal(self, user, enemy, block):
        print("{user.name}님이 {enemy.name}님의 \"{block.name}\"을(를) 빼앗았습니다!")
        block.owner = user
    
    def Item_dice_Onemore(self, user):
        print("{user.name}님이 \"{self.name}\"아이템 사용!")
        Item.Logic_dice(self)
        user.move(user, sum(user.dice))

    def Item_3block(self, user):
        print("{user.name}님이 \"{self.name}\"아이템 사용! 3칸 이동합니다")
        User.move(user, 3)

    def Item_ReStart(self, user):
        print("{user.name}님이 \"{self.name}\"아이템 사용! 출발지로 이동합니다")
        moving = BOARD_SIZE = user.position
        User.move(user, moving)

class Penalty:
    fine_money = 200000
    def __init__(self, name, number, rarity, percent):
        self.name = name
        self.number = number
        self.rarity = rarity
        self.percent = percent

    def Penalty_Tax(self, user):
        print("{user.name}님이 세금 납부!")
        user.money -= self.fine_money
    
    def Penalty_LossBlock(self, user, block):
        print("{user.name}님이 {block.name}의 소유권 상실!")
        block.owner = None
    
    def Penalty_Drifting(self, user):
        print("{user.name}님이 무인도에 표류되었어요!")
        if user.position <= 10:
            moving = 10 - user.position
        elif user.position > 10:
            moving = BOARD_SIZE - (user.position - 10)
        User.move(user, moving)
    
