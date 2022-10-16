from turtle import Screen
import pygame, sys
from os import path
from button import Button
#from MainMenu import main_menu


WIDTH = 1000
HEIGHT = 500
FPS = 60
pygame.init()
pygame.mixer.init()


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Lib/img/Cyberpunk.ttf", size)

SCREEN = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Space liberators")
clock = pygame.time.Clock()
img_dir = path.join(path.dirname(__file__), "img")

BG = pygame.image.load("Lib/img/space.png")
HS = pygame.image.load("Lib/img/Startmenu.jpg")
HS = pygame.transform.scale(HS, (1000, 500))
rect = HS.get_rect()
rect = rect.move((0, 0))


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Display text in game over screen, Font use in game, location
font_name = pygame.font.match_font('impact')

def highscores():
    while True:
        SCREEN.blit(HS, (0, 0))
        HIGHSCORE_MOUSE_POS = pygame.mouse.get_pos()

        HIGHSCORE_TEXT = get_font(25).render("This is the Highscore screen.", True, "White")
        HIGHSCORE_RECT = HIGHSCORE_TEXT.get_rect(center=(500, 130))
        SCREEN.blit(HIGHSCORE_TEXT, HIGHSCORE_RECT)

        HIGHSCORE_BACK = Button(image=None, pos=(500, 150), 
            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        HIGHSCORE_BACK.changeColor(HIGHSCORE_MOUSE_POS)
        HIGHSCORE_BACK.update(SCREEN)
        #pygame.display.update()
        def draw_text(surf, text, size, x, y):
            font = pygame.font.Font(font_name, size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surf.blit(text_surface, text_rect)

        file = open('Highscores.txt', 'r')
        for line in file:
            if 'highscore: ' in line:
                highscore = str(line.replace('highscore: ', '')) 
                draw_text(SCREEN, 'Your highscore   =', 20, 490 , 5)
                draw_text(SCREEN, str(highscore), 20, 590, 5)
        
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.quit()
                #sys.exit()

        pygame.display.update()

pygame.quit()

