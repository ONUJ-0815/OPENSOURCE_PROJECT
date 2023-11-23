import pygame
from constant import *
Item_Space = pygame.Rect((WIDTH-HEIGHT) / 2 + HEIGHT, HEIGHT / 4, (WIDTH - HEIGHT) / 2, HEIGHT / 2)
Font_size = 10
Max = 46

class Log_Info:
    def __init__(self):
        self.messages = []
        self.window = None

    def add_message(self, message):
        if len(self.messages) == Max:
            self.messages.pop(0)
        self.messages.append(message)


    def draw_log(self, window):
        self.window = window
        pygame.draw.rect(self.window, WHITE, Item_Space)
        font = pygame.font.Font("Jalnan.ttf", Font_size)
        font_height = font.get_height()
        i = 0
        for i, message in enumerate(reversed(self.messages)):
            text = font.render(message, True, BLACK)
            self.window.blit(text, ((WIDTH-HEIGHT)/2 + HEIGHT + 3, HEIGHT/4 + i * font_height))