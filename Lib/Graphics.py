import pygame
import math
from lib.Display_settings import WIDTH
from os import path

# Screen and graphics
img_dir = path.join(path.dirname(__file__), "img")

class Graphicsbgrnd():
    # Load All game graphics
    # Background 
    background = pygame.image.load(path.join(img_dir, "Galaxyback.png")).convert()
    background_rect = background.get_rect()
    bg_width = background.get_width()
    scroll = 0
    tiles = math.ceil(WIDTH / bg_width) + 1

class GraphicsPE():
#  Player and Enemies
    player_img = pygame.image.load(path.join(img_dir, "playerShip1_blue.png")).convert()
    enemie_img = pygame.image.load(path.join(img_dir, "enemyRed1.png")).convert()
