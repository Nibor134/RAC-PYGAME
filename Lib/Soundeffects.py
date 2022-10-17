import pygame
from os import path
Audio_dir = path.join(path.dirname(__file__), "Audio")

pygame.mixer.init()

SpaceMenu_sound = pygame.mixer.Sound('Lib/Audio/SpaceMenu.mp3')
SpaceGame_sound = pygame.mixer.Sound('Lib/Audio/SpaceGame.mp3')
Hit_sound = pygame.mixer.Sound('Lib/Audio/hit.mp3')
Select_sound = pygame.mixer.Sound('Lib/Audio/select.mp3')
Loselife_sound = pygame.mixer.Sound('Lib/Audio/loselife.mp3')
Death_sound = pygame.mixer.Sound('Lib/Audio/death.mp3')
shoot_sound = pygame.mixer.Sound('Lib/Audio/Shoot.mp3')


background = pygame.image.load(path.join(img_dir, "space.png")).convert()