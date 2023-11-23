from player import *
from constant import *
class BlockType:
    START = "출발점"
    JAIL = "감옥"
    RECEIVE_TAX = "사회복지기금(수령처)"
    PAY_TAX = "사회복지기금(접수처)"
    SPACE = "우주여행"
    GOLD_KEY = "황금열쇠"
    PROPERTY = "토지"
    TOURLAND = "관광지"
    tax = 0



class Block:
    def __init__(self, block_type, name, position, price=0, toll=0, villas=0, hotels=0,villa_cost=0,hotel_cost=0):
        self.block_type = block_type  # 블록 종류 (출발점, 토지, 목적지, 감옥 등)
        self.name = name  # 블록 이름
        self.position = position  # 블록의 위치
        self.owner = None  # 토지 블록의 소유주
        self.price = price  # 토지 구입 가격
        self.toll = toll  # 토지 통행료
        self.villas = villas  # 빌라 수
        self.hotels = hotels  # 호텔 수
        self.villa_cost=villa_cost
        self.hotel_cost=hotel_cost

    def purchase_property(self, player):
        if self.block_type == BlockType.TOURLAND and not self.owner or self.block_type == BlockType.PROPERTY and not self.owner:  
            if player.money >= self.price:  
                player.money -= self.price  
                self.owner = player  
                player.properties.append(self)
                log_instance.add_message(" ")
                log_instance.add_message("구입했습니다.")
                log_instance.add_message(f"{self.name}을(를)")
                log_instance.add_message(f"({player.name})") 
            else:
                log_instance.add_message(" ")
                print("돈이 부족하여 구매할 수 없습니다.")

    def pay_toll(self, user):
        building_money = 0
        total_money = user.money + building_money
        my_properties = []
        i = 0
        if total_money <= self.toll:
            my_properties = sorted(user.properties, key=lambda x: x.price)
            while(total_money <= self.toll and my_properties!=[]):
                total_money = user.money + building_money
                if len(my_properties) != 0:
                    if my_properties[i].hotels == 1:
                        building_money += my_properties[i].hotel_cost
                        my_properties[i].hotels=0
                        log_instance.add_message(" ")
                        log_instance.add_message(f"+{my_properties[i].hotel_cost}")
                        log_instance.add_message(f"{self.name}호텔 매각 ")
                        log_instance.add_message(f"({user.name})")
                    elif my_properties[i].villas == 1:
                        building_money += my_properties[i].villa_cost
                        my_properties[i].villas=0
                        log_instance.add_message(" ")
                        log_instance.add_message(f"+{my_properties[i].villa_cost}")
                        log_instance.add_message(f"{self.name}빌라 매각")
                        log_instance.add_message(f"({user.name})")
                    else:
                        building_money += my_properties[i].price
                        my_properties[i].owner = None
                        log_instance.add_message(" ")
                        log_instance.add_message(f"+{my_properties[i].price}")
                        log_instance.add_message(f"{self.name}토지 매각")
                        log_instance.add_message(f"({user.name})")
                        my_properties.pop(i)
            if len(my_properties)==0 and total_money < self.toll:
                log_instance.add_message(" ")
                log_instance.add_message("파산했습니다.")
                log_instance.add_message(f"({user.name})")
                user.SE=False
                user.time=user.turns
                
            user.money = total_money - self.toll
            self.owner.money += self.toll
                
        else:
            user.money-=self.toll
            log_instance.add_message(" ")
            log_instance.add_message("지불하였습니다.")
            log_instance.add_message(f"통행료{self.toll}원을")
            log_instance.add_message(f"{self.name}에서")
            log_instance.add_message(f"({user.name})")
    

    def build_villa(self, player):
        if self.block_type == BlockType.PROPERTY and self.owner == player:  
            if player.money >= self.villa_cost and self.villas==0 :  
                player.money -= self.villa_cost  
                self.villas = 1  
                self.toll = self.villa_cost/100*600  # 빌라를 지을 때 톨비 업데이트
                log_instance.add_message(" ")
                log_instance.add_message("빌라를 지었습니다.")
                log_instance.add_message(f"{self.name}에")
                log_instance.add_message(f"({player.name})")
            else:
                log_instance.add_message(" ")
                log_instance.add_message("빌라를 더 지을 수 없습니다.")

    def build_hotel(self, player):
        if self.block_type == BlockType.PROPERTY and self.villas == 1 and self.owner == player:  
            if player.money >=self.hotel_cost and self.hotels==0:  
                player.money -= self.hotel_cost    
                self.hotels = 1  
                self.toll = self.hotel_cost/100*600  # 호텔을 지을 때 톨비 업데이트
                log_instance.add_message(" ")
                log_instance.add_message("호텔를 지었습니다.")
                log_instance.add_message(f"{self.name}에")
                log_instance.add_message(f"({player.name})님이")
            else:
                log_instance.add_message(" ")
                log_instance.add_message("호텔을 지을 수 없습니다.")
    
    def draw_block(self, surface):
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

        board.add_block(Block(BlockType.PROPERTY, "타이페이", 1, price=50000, toll=2000, villas=0, hotels=0,villa_cost=90000,hotel_cost=250000))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 2, price=0, toll=0, villas=0, hotels=0,))
        board.add_block(Block(BlockType.PROPERTY, "베이징", 3, price=80000, toll=4000, villas=0, hotels=0,villa_cost=180000,hotel_cost=450000))
        board.add_block(Block(BlockType.PROPERTY, "마닐라", 4, price=80000, toll=4000, villas=0, hotels=0,villa_cost=180000,hotel_cost=450000))
        board.add_block(Block(BlockType.TOURLAND, "제주도", 5, price=200000, toll=300000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "싱가포르", 6, price=100000, toll=6000, villas=0, hotels=0,villa_cost=270000,hotel_cost=550000))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 7, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "카이로", 8, price=100000, toll=6000, villas=0, hotels=0,villa_cost=270000,hotel_cost=550000))
        board.add_block(Block(BlockType.PROPERTY, "이스탄불", 9, price=120000, toll=8000, villas=0, hotels=0,villa_cost=300000,hotel_cost=600000))

        board.add_block(Block(BlockType.JAIL, "무인도", 10))

        board.add_block(Block(BlockType.PROPERTY, "아테네", 11, price=140000, toll=10000, villas=0, hotels=0,villa_cost=450000,hotel_cost=750000))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 12, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "코펜하겐", 13, price=160000, toll=12000, villas=0, hotels=0,villa_cost=500000,hotel_cost=900000))
        board.add_block(Block(BlockType.PROPERTY, "스톡홀름", 14, price=160000, toll=12000, villas=0, hotels=0,villa_cost=500000,hotel_cost=900000))
        board.add_block(Block(BlockType.TOURLAND, "콩코드 여객기", 15, price=200000, toll=300000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "취리히", 16, price=180000, toll=14000, villas=0, hotels=0,villa_cost=500000,hotel_cost=950000))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 17, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "베를린", 18, price=160000, toll=12000, villas=0, hotels=0,villa_cost=500000,hotel_cost=950000))
        board.add_block(Block(BlockType.PROPERTY, "오타와", 19, price=200000, toll=16000, villas=0, hotels=0,villa_cost=550000,hotel_cost=1000000))
    
        board.add_block(Block(BlockType.RECEIVE_TAX, "사회복지기금(수령처)", 20))

        board.add_block(Block(BlockType.PROPERTY, "부에노스 아이레스", 21, price=220000, toll=18000, villas=0, hotels=0,villa_cost=700000,hotel_cost=1050000))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 22, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "상파울루", 23, price=240000, toll=20000, villas=0, hotels=0,villa_cost=750000,hotel_cost=1100000))
        board.add_block(Block(BlockType.PROPERTY, "시드니", 24, price=240000, toll=20000, villas=0, hotels=0,villa_cost=750000,hotel_cost=1100000))
        board.add_block(Block(BlockType.TOURLAND, "부산", 25, price=500000, toll=600000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "하와이", 26, price=260000, toll=22000, villas=0, hotels=0,villa_cost=800000,hotel_cost=1150000))
        board.add_block(Block(BlockType.PROPERTY, "리스본", 27, price=260000, toll=22000, villas=0, hotels=0,villa_cost=800000,hotel_cost=1150000))
        board.add_block(Block(BlockType.TOURLAND, "퀸 엘리자베스호", 28, price=300000, toll=250000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "마드리드", 29, price=280000, toll=24000, villas=0, hotels=0,villa_cost=850000,hotel_cost=1200000))
    
        board.add_block(Block(BlockType.SPACE, "우주여행", 30, price=200000, toll=200000, villas=0, hotels=0))

        board.add_block(Block(BlockType.PROPERTY, "도쿄", 31, price=300000, toll=26000, villas=0, hotels=0,villa_cost=900000,hotel_cost=1270000))
        board.add_block(Block(BlockType.TOURLAND, "컬럼비아호", 32, price=450000, toll=300000, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "파리", 33, price=320000, toll=28000,villas=0, hotels=0,villa_cost=1000000,hotel_cost=1400000))
        board.add_block(Block(BlockType.PROPERTY, "로마", 34, price=320000, toll=28000, villas=0, hotels=0,villa_cost=1000000,hotel_cost=1400000))
        board.add_block(Block(BlockType.GOLD_KEY, "황금열쇠", 35, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.PROPERTY, "런던", 36, price=350000, toll=35000, villas=0, hotels=0,villa_cost=1100000,hotel_cost=1500000))
        board.add_block(Block(BlockType.PROPERTY, "뉴욕", 37, price=350000, toll=35000, villas=0, hotels=0,villa_cost=1100000,hotel_cost=1500000))
        board.add_block(Block(BlockType.PAY_TAX, "사회복지기금(접수처)", 38, price=0, toll=0, villas=0, hotels=0))
        board.add_block(Block(BlockType.TOURLAND, "서울", 39, price=1000000, toll=2000000, villas=0, hotels=0))
        return board
    
    def draw_board(self, surface):
        for block in self.blocks:
            block.draw_block(surface)