class BlockType:
    START = "�����"
    PROPERTY = "����"
    DESTINATION = "������"
    JAIL = "����"
    SOCIAL = "��ȸ�������"
    SPACE = "���ֿ���"

class Block:
    def __init__(self, block_type, name, position, price=0, toll=0, villas=0, hotels=0):
        self.block_type = block_type  # ��� ���� (�����, ����, ������, ���� ��)
        self.name = name  # ��� �̸�
        self.position = position  # ����� ��ġ
        self.owner = None  # ���� ����� ������

        # ���� ��Ͽ� �ش��ϴ� ����
        if self.block_type == BlockType.PROPERTY:
            self.price = price  # ���� ���� ����
            self.toll = toll  # ���� �����
            self.villas = villas  # ���� ��
            self.hotels = hotels  # ȣ�� ��

    def purchase_property(self, player):
        if self.block_type == BlockType.PROPERTY and not self.owner:  
            if player.money >= self.price:  
                player.money -= self.price  
                self.owner = player  
                player.properties.append(self)  
                print(f"{player.name}��(��) {self.name}��(��) �����߽��ϴ�.")
            else:
                print("���� �����Ͽ� ������ �� �����ϴ�.")

    def build_villa(self, player, villa_cost, new_toll):
        if self.block_type == BlockType.PROPERTY and self.owner == player:  
            if player.money >= villa_cost and self.villas < 4:  
                player.money -= villa_cost  
                self.villas += 1  
                self.toll = new_toll  # ���� ���� �� ��� ������Ʈ
                print(f"{player.name}��(��) {self.name}�� ���� �����ϴ�.")
            else:
                print("���� �� ���� �� �����ϴ�.")

    def build_hotel(self, player, hotel_cost, new_toll):
        if self.block_type == BlockType.PROPERTY and self.owner == player:  
            if player.money >= hotel_cost and self.villas == 4 and self.hotels < 1:  
                player.money -= hotel_cost  
                self.villas = 0  
                self.hotels = 1  
                self.toll = new_toll  # ȣ���� ���� �� ��� ������Ʈ
                print(f"{player.name}��(��) {self.name}�� ȣ���� �����ϴ�.")
            else:
                print("ȣ���� ���� �� �����ϴ�.")

# �η縶�� ���� Ŭ����
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

# �÷��̾� Ŭ����
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0  
        self.money = 100000 
        self.properties = []  

# �η縶�� ���� ����

# ���� ��� �߰�
def play():
    board = Board()
    board.add_block(Block(BlockType.START, "�����", 0))

    board.add_block(Block(BlockType.PROPERTY, "Ÿ������", 1, price=50000, toll=2000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "����¡", 2, price=80000, toll=4000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "���Ҷ�", 3, price=80000, toll=4000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "���ֵ�", 4, price=200000, toll=300000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "�̰�����", 5, price=100000, toll=6000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "ī�̷�", 6, price=100000, toll=6000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "�̽�ź��", 7, price=120000, toll=8000, villas=0, hotels=0))

    board.add_block(Block(BlockType.JAIL, "���ε�", 8))

    board.add_block(Block(BlockType.PROPERTY, "���׳�", 9, price=140000, toll=10000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "�����ϰ�", 10, price=160000, toll=12000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "����Ȧ��", 11, price=160000, toll=12000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "���ڵ� ������", 12, price=200000, toll=300000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "�븮��", 13, price=180000, toll=14000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "������", 14, price=160000, toll=12000, villas=0, hotels=0))
    board.add_block(Block(BlockType.PROPERTY, "��Ÿ��", 15, price=200000, toll=16000, villas=0, hotels=0))
    
    board.add_block(Block(BlockType.SOCIAL, "��ȸ�������", 16))

    board.add_block(Block(BlockType.PROPERTY, "�ο��뽺 ���̷���", 17, price=220000, toll=18000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "���Ŀ��", 18, price=240000, toll=20000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "�õ��", 19, price=240000, toll=20000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "�λ�", 20, price=500000, toll=600000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "�Ͽ���", 21, price=260000, toll=22000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "������", 22, price=260000, toll=22000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "�� �����ں���ȣ", 23, price=300000, toll=250000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "���帮��", 24, price=280000, toll=24000, buildings=0))
    
    board.add_block(Block(BlockType.SPACE, "���ֿ���", 25, price=200000, toll=200000, buildings=0))

    board.add_block(Block(BlockType.PROPERTY, "����", 26, price=300000, toll=26000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "�÷����ȣ", 27, price=450000, toll=300000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "�ĸ�", 28, price=320000, toll=28000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "�θ�", 29, price=320000, toll=28000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "����", 30, price=350000, toll=35000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "����", 31, price=350000, toll=35000, buildings=0))
    board.add_block(Block(BlockType.PROPERTY, "����", 32, price=1000000, toll=2000000, buildings=0))