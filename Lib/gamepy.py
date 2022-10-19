
import pygame
import random

WIDTH = 360 
HEIGHT = 480 
FPS = 60 

#Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# initialize pygame and create window 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game ")
Clock = pygame.time.Clock()

# Game Loop

Running = True 
while running : 

    #Below here the three parts that go into the game loop
    #Process input (events)
    #Update
    #Draw / Render 
    screen.fill(BLACK)
    pygame.display.flip()