import pygame, sys
from fullgame import game
#from fullgame import show_go_screen
from Score import highscores
from button import Button

  
pygame.init()

SCREEN = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Lib/img/space.png")
HS = pygame.image.load("Lib/img/Startmenu.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Lib/img/Cyberpunk.ttf", size)

def play():
    while True:
        game()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)
        
        PLAY_BACK = Button(image=None, pos=(500, 160), 
                text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def highscore():
    while True:
        SCREEN.blit(HS, (0, 0))
        HIGHSCORE_MOUSE_POS = pygame.mouse.get_pos()
        highscores()       
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HIGHSCORE_BACK.checkForInput(HIGHSCORE_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("MAIN MENU", True, "#940076")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Lib/img/Quit Rect.png"), pos=(500, 200), 
                            text_input="PLAY", font=get_font(40), base_color="#fcd4f4", hovering_color="Purple")
        HIGHSCORE_BUTTON = Button(image=pygame.image.load("Lib/img/highscore Rect.png"), pos=(500, 300), 
                            text_input="HIGHSCORE", font=get_font(40), base_color="#fcd4f4", hovering_color="Purple")
        QUIT_BUTTON = Button(image=pygame.image.load("Lib/img/Quit Rect.png"), pos=(500, 400), 
                            text_input="QUIT", font=get_font(40), base_color="#fcd4f4", hovering_color="Purple")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, HIGHSCORE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if HIGHSCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    highscore()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()