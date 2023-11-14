import pygame
import random

BOARD_SIZE = 40

class User:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.items = [6]  # 가지고 있는 아이템을 저장할 리스트
        self.dice = 0  # 주사위 숫자를 저장할 변수
        self.dice_rolls = 0 #주사위 두 번까지 굴릴수있게 추적(아이템에도 활용가능)
        self.money = 0
        self.turns = 0

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
    item_rarity = {'희귀', '영웅', '전설'}
    def Item_information(self, name, number, rarity, ):
        self.name = name
        self.

    def Item_dice(self):
        User.dice1 = random.randint(1, 6)
        User.dice2 = random.randint(1, 6)
        User.dice = pygame.math.Vector2(self.dice1, self.dice2)
        if User.dice1 == User.dice2:
            double = True
        else:
            double = False
        return double
    def Item_Lotto(self):
        self.name = '복권 당첨!'
        self.number = 1
        self.rarity = '레어'
        self.percentage = 


class BlockType:
    START = "출발점"
    PROPERTY = "토지"
    DESTINATION = "목적지"
    JAIL = "감옥"
    SOCIAL = "사회복지기금"
    SPACE = "우주여행"

class Block:
    def __init__(self, block_type, name, position, price=0, toll=0, villas=0, hotels=0):
        self.block_type = block_type  # 블록 종류 (출발점, 토지, 목적지, 감옥 등)
        self.name = name  # 블록 이름
        self.position = position  # 블록의 위치
        self.owner = None  # 토지 블록의 소유주

        # 토지 블록에 해당하는 정보
        if self.block_type == BlockType.PROPERTY:
            self.price = price  # 토지 구입 가격
            self.toll = toll  # 토지 통행료
            self.villas = villas  # 빌라 수
            self.hotels = hotels  # 호텔 수

    def purchase_property(self, player):
        if self.block_type == BlockType.PROPERTY and not self.owner:  
            if player.money >= self.price:  
                player.money -= self.price  
                self.owner = player  
                player.properties.append(self)  
                print(f"{player.name}이(가) {self.name}을(를) 구입했습니다.")
            else:
                print("돈이 부족하여 구매할 수 없습니다.")

    def build_villa(self, player, villa_cost, new_toll):
        if self.block_type == BlockType.PROPERTY and self.owner == player:  
            if player.money >= villa_cost and self.villas < 4:  
                player.money -= villa_cost  
                self.villas += 1  
                self.toll = new_toll  # 빌라를 지을 때 톨비 업데이트
                print(f"{player.name}이(가) {self.name}에 빌라를 짓습니다.")
            else:
                print("빌라를 더 지을 수 없습니다.")

    def build_hotel(self, player, hotel_cost, new_toll):
        if self.block_type == BlockType.PROPERTY and self.owner == player:  
            if player.money >= hotel_cost and self.villas == 4 and self.hotels < 1:  
                player.money -= hotel_cost  
                self.villas = 0  
                self.hotels = 1  
                self.toll = new_toll  # 호텔을 지을 때 톨비 업데이트
                print(f"{player.name}이(가) {self.name}에 호텔을 짓습니다.")
            else:
                print("호텔을 지을 수 없습니다.")

# 부루마블 보드 클래스
class Board:
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)

    def get_block_at_position(self, position):
        for block in self.blocks:
            if block.position == position:
                return block
        return None

# 도시 블록 추가
class play:
    def fill_board(self):
        board = Board()
        board.add_block(Block(BlockType.START, "출발지", 0))

        board.add_block(Block(BlockType.PROPERTY, "타이페이", 1, price=50000, toll=2000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "베이징", 2, price=80000, toll=4000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "마닐라", 3, price=80000, toll=4000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "제주도", 4, price=200000, toll=300000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "싱가포르", 5, price=100000, toll=6000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "카이로", 6, price=100000, toll=6000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "이스탄불", 7, price=120000, toll=8000, villas=0, hotels=0))

        board.add_block(Block(BlockType.JAIL, "무인도", 8))

        board.add_block(Block(BlockType.PROPERTY, "아테네", 9, price=140000, toll=10000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "코펜하겐", 10, price=160000, toll=12000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "스톡홀름", 11, price=160000, toll=12000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "콩코드 여객기", 12, price=200000, toll=300000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "취리히", 13, price=180000, toll=14000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "베를린", 14, price=160000, toll=12000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "오타와", 15, price=200000, toll=16000, villas=0, hotels=0))
    
        board.add_block(Block(BlockType.SOCIAL, "사회복지기금", 16))

        board.add_block(Block(BlockType.PROPERTY, "부에노스 아이레스", 17, price=220000, toll=18000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "상파울루", 18, price=240000, toll=20000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "시드니", 19, price=240000, toll=20000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "부산", 20, price=500000, toll=600000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "하와이", 21, price=260000, toll=22000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "리스본", 22, price=260000, toll=22000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "퀸 엘리자베스호", 23, price=300000, toll=250000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "마드리드", 24, price=280000, toll=24000, buildings=0))
    
        board.add_block(Block(BlockType.SPACE, "우주여행", 25, price=200000, toll=200000, buildings=0))

        board.add_block(Block(BlockType.PROPERTY, "도쿄", 26, price=300000, toll=26000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "컬럼비아호", 27, price=450000, toll=300000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "파리", 28, price=320000, toll=28000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "로마", 29, price=320000, toll=28000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "런던", 30, price=350000, toll=35000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "뉴욕", 31, price=350000, toll=35000, buildings=0))
        board.add_block(Block(BlockType.PROPERTY, "서울", 32, price=1000000, toll=2000000, buildings=0))
    

    
