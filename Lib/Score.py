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

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Space liberators")
clock = pygame.time.Clock()
img_dir = path.join(path.dirname(__file__), "img")

BG = pygame.image.load("Lib/img/space.png")
HS = pygame.image.load("Lib/img/Startmenu.jpg")
HS = pygame.transform.scale(HS, (1000, 500))
rect = HS.get_rect()
rect = rect.move((0, 0))

pygame.display.flip()

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
        screen.blit(HS, (0, 0))
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
                draw_text(screen, 'Your highscore   =', 20, 490 , 5)
                draw_text(screen, str(highscore), 20, 590, 5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HIGHSCORE_BACK.checkForInput(HIGHSCORE_MOUSE_POS):
                    main_menu() 

        pygame.display.update()

pygame.quit()

