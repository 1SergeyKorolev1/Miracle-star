import pygame
import time
import random
pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Miracle-star")
pygame.display.set_icon(pygame.image.load('image/logo/ico.png'))

BG = pygame.transform.scale(pygame.image.load('image/background/fon.jpg'), (WIDTH, HEIGHT))

STAR_WIDTH = 10
STAR_HEIGHT = 17
# PLAYER_WIDTH = 40
# PLAYER_HEIGHT = 40
PLAYER_RADIUS = 15

PLAYER_TURN = 3
STAR_TURN = 3

FONT = pygame.font.SysFont('comicsans', 30)
