from player import *
from bluemarble_UI import *

class BlockType:
    START = "출발점"
    JAIL = "감옥"
    RECEIVE_TAX = "사회복지기금(수령처)"
    PAY_TAX = "사회복지기금(접수처)"
    SPACE = "우주여행"
    GOLD_KEY = "황금열쇠"
    PROPERTY = "토지"
    tax = 0
    def inJail(self, user):
        from player import move
        if(user.dice1 != user.dice2):
            if(self.count != 3):
                user.turns+=1
                self.count+=1
            elif(self.count == 3):
                move(sum(user.dice1, user.dice2))
        else:
            move(sum(user.dice1, user.dice2))
    def space_Travel(self, user):
        user.position = wantPosition #wantPosition은 UI에서 입력받아서 넣으면 됨



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
    def make_block():
        board = Board()
        board.add_block(Block(BlockType.START, "출발지", 0))

        board.add_block(Block(BlockType.PROPERTY, "타이페이", 1, price=50000, toll=2000, villas=0, hotels=0))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 2, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "베이징", 3, price=80000, toll=4000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "마닐라", 4, price=80000, toll=4000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "제주도", 5, price=200000, toll=300000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "싱가포르", 6, price=100000, toll=6000, villas=0, hotels=0))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 7, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "카이로", 8, price=100000, toll=6000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "이스탄불", 9, price=120000, toll=8000, villas=0, hotels=0))

        board.add_block(Block(BlockType.JAIL, "무인도", 10))

        board.add_block(Block(BlockType.PROPERTY, "아테네", 11, price=140000, toll=10000, villas=0, hotels=0))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 12, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "코펜하겐", 13, price=160000, toll=12000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "스톡홀름", 14, price=160000, toll=12000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "콩코드 여객기", 15, price=200000, toll=300000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "취리히", 16, price=180000, toll=14000, villas=0, hotels=0))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 17, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "베를린", 18, price=160000, toll=12000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "오타와", 19, price=200000, toll=16000, villas=0, hotels=0))
    
        board.add_block(Block(BlockType.RECEIVE_TAX, "사회복지기금(수령처)", 20))

        board.add_block(Block(BlockType.PROPERTY, "부에노스 아이레스", 21, price=220000, toll=18000, villas=0, hotels=0))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 22, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "상파울루", 23, price=240000, toll=20000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "시드니", 24, price=240000, toll=20000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "부산", 25, price=500000, toll=600000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "하와이", 26, price=260000, toll=22000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "리스본", 27, price=260000, toll=22000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "퀸 엘리자베스호", 28, price=300000, toll=250000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "마드리드", 29, price=280000, toll=24000, villas=0, hotels=0))
    
        board.add_block(Block(BlockType.SPACE, "우주여행", 30, price=200000, toll=200000, villas=0, hotels=0))

        board.add_block(Block(BlockType.PROPERTY, "도쿄", 31, price=300000, toll=26000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "컬럼비아호", 32, price=450000, toll=300000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "파리", 33, price=320000, toll=28000,villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "로마", 34, price=320000, toll=28000, villas=0, hotels=0))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 35, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "런던", 36, price=350000, toll=35000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "뉴욕", 37, price=350000, toll=35000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PAY_TAX, "사회복지기금(접수처)", 38, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "서울", 39, price=1000000, toll=2000000, villas=0, hotels=0))
        return board
    def draw(self, surface):
        for block in self.blocks:
            if block.position == 0:
                self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13, HEIGHT*11/13, HEIGHT*2/13, HEIGHT*2/13)
                pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
            if 1 <= block.position <= 9:
                self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13 - block.position*HEIGHT/13, HEIGHT*11/13, HEIGHT/13, HEIGHT*2/13)
                pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
            if block.position == 10:
                self.rect = pygame.Rect((WIDTH-HEIGHT)/2, HEIGHT*11/13, HEIGHT*2/13, HEIGHT*2/13)
                pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
            if 11 <= block.position <= 19:
                self.rect = pygame.Rect((WIDTH-HEIGHT)/2, HEIGHT*11/13 - (block.position - 10)*HEIGHT/13, HEIGHT*2/13, HEIGHT/13)
                pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
            if block.position == 20:
                self.rect = pygame.Rect((WIDTH-HEIGHT)/2, 0, HEIGHT*2/13, HEIGHT*2/13)
                pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
            if 21 <= block.position <= 29:
                self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*2/13 + (block.position - 21)*HEIGHT/13, 0, HEIGHT/13, HEIGHT*2/13)
                pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
            if block.position == 30:
                self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13, 0, HEIGHT*2/13, HEIGHT*2/13)
                pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
            if 31 <= block.position <= 39:
                self.rect = pygame.Rect((WIDTH-HEIGHT)/2 + HEIGHT*11/13, HEIGHT*2/13 + (block.position - 31)*HEIGHT/13, HEIGHT*2/13, HEIGHT/13)
                pygame.draw.rect(surface, WHITE, self.rect, Ground_Line)
