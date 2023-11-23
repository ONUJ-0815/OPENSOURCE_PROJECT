import pygame

WHITE = (255, 255, 255)
SKYBLUE = (135, 206, 235)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
MID = (105, 186, 255)
NAME = (98, 106, 223)
NAME_LINE = (51, 62, 220)


WIDTH = 1240
HEIGHT = 960
Ground_Line = 3

pygame.font.init()

font3 = pygame.font.SysFont(None, 40)
font_GOTHIC = "malgungothic"
font_JALNAN = "Jalnan.ttf"
font_Info = pygame.font.Font(font_JALNAN, 20)
font_Max = pygame.font.SysFont(font_GOTHIC, 13)
font_RULE_TITLE = pygame.font.Font(font_JALNAN, 80)
font_RULE = pygame.font.Font(font_JALNAN, 20)