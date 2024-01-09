import time
import random
import pygame
from start_pack import app_operation, draw

pygame.font.init()
pygame.init()

app_operation = app_operation.app_operation
draw = draw.draw

# ____________________Дисплей (настройки)____________________________
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Miracle-star")
pygame.display.set_icon(pygame.image.load('image/logo/ico.png'))

BG = pygame.transform.scale(pygame.image.load('image/background/fon.jpg'), (WIDTH, HEIGHT))

# __________________Игрок и Враги (размеры)____________________
STAR_WIDTH = 15
STAR_HEIGHT = 15
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
PLAYER_RADIUS = 15

# ________________Смещение игрока/врага за одно нажатие_________________
PLAYER_TURN = 3
STAR_TURN = 3

# __________________Основной шрифт_____________________
FONT = pygame.font.SysFont('comicsans', 30)

# _______переменные основного цикла, времени,
# тика добавления звезд(врагов), список существующих звезд и Хита ____________
run = True
clock = pygame.time.Clock()
start_time = time.time()
star_add_increment = 1000
star_count = 0
stars = []
hit = False

# __________Игрок на сцене___________
# player = pygame.Rect(200, start_pack.HEIGHT - start_pack.PLAYER_HEIGHT, start_pack.PLAYER_WIDTH,
# start_pack.PLAYER_HEIGHT)
# player = pygame.draw.circle(WIN, 'blue', (WIDTH / 2, HEIGHT - PLAYER_RADIUS), PLAYER_RADIUS, width=0)
player_image = pygame.image.load('image/player/world.png')
player_image_transform = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
player = player_image_transform.get_rect(center=(WIDTH//2, HEIGHT-PLAYER_HEIGHT//2))
# player = pygame.transform.scale(pygame.image.load('image/player/world.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
