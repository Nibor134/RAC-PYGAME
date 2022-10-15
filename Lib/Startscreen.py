import pygame
from os import path
pygame.init()
import Menubutton

img_dir = path.join(path.dirname(__file__), "img")

# Size Window
WIDTH = 1000
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))

#Display Title, Icon Game, Buttons
pygame.display.set_caption('Space Liberators')
icon = pygame.image.load(path.join(img_dir, "player 1.png"))
play_button_image = pygame.image.load(path.join(img_dir, "play_button.png")).convert_alpha()
highscore_button_image = pygame.image.load(path.join(img_dir, "highscore_button.png")).convert_alpha()
exit_button_image = pygame.image.load(path.join(img_dir, "exit_button.png")).convert_alpha()

#play_button_image = pygame.image.load(path.join(img_dir, "play_button.png"))
#highscore_button_image = pygame.image.load(path.join(img_dir, "highscore_button.png"))
#exit_button_image = pygame.image.load(path.join(img_dir, "exit_button.png"))

#Background Image, Scale Size
background = pygame.image.load(path.join(img_dir, "Startmenu.jpg")).convert()
background = pygame.transform.scale(background,(WIDTH,HEIGHT))
background_rect = background.get_rect()

#Manual scale
#play_button = pygame.transform.scale(play_button,(100,100))
#highscore_button = pygame.transform.scale(highscore_button,(100,100))
#exit_button = pygame.transform.scale(exit_button,(100,100))

# Display Title Icon
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Colors 
GREY  = (192, 192, 192)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Define fonts, size, text
#font = pygame.font.match_font('arial', 50)
font = pygame.font.SysFont('impact',50)

def draw_text(text,font, WHITE, x,y): 
    title = font.render(text, True, WHITE)
    screen.blit(title,(x,y))    

# Test shape on screen
#test_surface = pygame.Surface((200,200))
#test_surface.fill('Red')

play_button = Menubutton.Button((WIDTH / 4), 250, play_button_image, 0.4)
highscore_button = Menubutton.Button((WIDTH / 2.15), 250, highscore_button_image, 0.4)
exit_button = Menubutton.Button((WIDTH / 1.5), 250, exit_button_image, 0.4)

# Game Window Loop, # Show background, Buttons, Title
running = True
full_game_state = 0

while running: 
    screen.blit(background, background_rect)
    draw_text('Space Liberators',font, WHITE, 340 ,125)
    draw_text('Arrow keys to move, Space to Fire',font, WHITE, 190, 405)
    if play_button.draw(screen):
        full_game_state = 1
        running = False
        print('Play')
    if highscore_button.draw(screen):
        full_game_state = 2
        running = False
        print('Highscore')
    if exit_button.draw(screen): 
        full_game_state = 3
        running = False
        
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            full_game_state = 3
    pygame.display.update
    
    # Manual position buttons on screen 
    #screen.blit(play_button,((WIDTH / 4),250)) 
    #screen.blit(highscore_button,((WIDTH / 2.15),250))
    #screen.blit(exit_button,((WIDTH / 1.5),250)) 

    pygame.display.update()       
    clock.tick(60)