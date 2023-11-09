import pygame
import random

BOARD_SIZE = 40

class User:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.items = []  # 가지고 있는 아이템을 저장할 리스트
        self.dice = 0  # 주사위 숫자를 저장할 변수
        self.dice_rolls = 0 #주사위 두 번까지 굴릴수있게 추적(아이템에도 활용가능)

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

# 테스트코드

user1 = User("준호")
user2 = User("지웅")
user3 = User("인호")
user4 = User("현호")

user1.item_list()

user1.add_item(1)

user1.item_list()

user1.add_item(3)

user1.item_list()

user1.locate()

user1.roll_dice()

user1.locate()

user1.move(3)

user1.locate()
