
import pygame, sys
from button import Button
import random
import math
from os import path

#Game initiation
pygame.init()
pygame.mixer.init
pygame.mixer.music.load('SpaceMenu.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()


SCREEN = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Space Invaders")
BLACK = (0, 0, 0)
BG = pygame.image.load("Lib/img/space.png")
BG_G = pygame.image.load("Lib/img/BG_still.jpg")
HS = pygame.image.load("Lib/img/Startmenu.jpg")
BG = pygame.transform.scale(BG, (1500, 1000))
BG_G = pygame.transform.scale(BG_G, (1000, 500))
HS = pygame.transform.scale(HS, (1000, 500))
rect = HS.get_rect()
rect = rect.move((0, 0))
rect2 = BG_G.get_rect()
rect2 = rect2.move((0, 0))

file = open('Highscores.txt', 'r')
for line in file:
    if 'highscore: ' in line:
        highscore = int(line.replace('highscore: ', ''))
        saved_highscore = 0

def draw_text(surf, text, size, x, y):
            font = pygame.font.Font(get_font, size)
            text_surface = font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surf.blit(text_surface, text_rect)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Lib/img/NeoTechItalic-WyKZY.ttf", size)

def play_game():
    pygame.mixer.music.load('SpaceGame.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    global highscore
    while True:
        img_dir = path.join(path.dirname(__file__), "img")

        WIDTH = 1000
        HEIGHT = 500
        FPS = 60

        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0 , 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)

        # intialize game and create window
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(10)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #pygame.mixer.music.load('hit.mp3')
        #pygame.mixer.music.load('loselife.mp3')
        pygame.display.set_caption("Space liberators")
        clock = pygame.time.Clock()

        # Display text in game over screen, Font use in game, location
        font_name = pygame.font.match_font('impact')
        def draw_text(surf, text, size, x, y):
            font = pygame.font.Font(font_name, size)
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            surf.blit(text_surface, text_rect)

        # Create player
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.transform.scale(player_img, (80,60))
                self.image.set_colorkey(BLACK)
                self.rect = self.image.get_rect()
                self.radius = 24
                # Make the hitbox visible ---> 
                # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
                self.rect.centerx = WIDTH / 100
                self.rect.bottom = HEIGHT / 2
                self.speedx = 0
                self.speedy = 0
                self.bullet_delay = 250
                self.last_bullet = pygame.time.get_ticks()
                self.lives = 3
                
            def update(self):
                # Player movement with arrow keys
                self.speedx = 0
                self.speedy = 0
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_LEFT]:
                    self.speedx = -5
                if keystate[pygame.K_RIGHT]:
                    self.speedx = 5
                if keystate[pygame.K_UP]:
                    self.speedy = -5
                if keystate[pygame.K_DOWN]:
                    self.speedy = 5
                self.rect.x += self.speedx
                self.rect.y += self.speedy
                if keystate[pygame.K_SPACE]:
                    self.shoot()

            # Creating Borders for the player so it can't go of the screen
                if self.rect.right > WIDTH:
                    self.rect.right = WIDTH
                if self.rect.left < 0:
                    self.rect.left = 0
                if self.rect.top < 0:
                    self.rect.top = 0
                if self.rect.bottom > HEIGHT:
                    self.rect.bottom = HEIGHT

            # Shoot bullets button
            def shoot(self):
                now = pygame.time.get_ticks()
                pygame.mixer.music.set_volume(1)
                if now - self.last_bullet > self.bullet_delay:
                    self.last_bullet = now
                    bullet = Bullets(self.rect.right, self.rect.centery)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    pygame.mixer.Channel(7).play(pygame.mixer.Sound('Shoot.mp3'))

        # Enemie fighters
        class Enemies(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = enemie_img
                self.image = pygame.transform.scale(enemie_img, (55,45))
                self.image.set_colorkey(BLACK)
                self.rect = self.image.get_rect()
                self.radius = int(self.rect.width * .85 / 2)
                # Make the hitbox visible --->
                # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
                self.rect.x = random.randrange(990, 1000)
                self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
                self.speedy = random.randrange(-3, 3)
                self.speedx = random.randrange(-12, -5)

            # killing and spawning new enemies when they go of the screen
            def update(self):
                self.rect.x += self.speedx
                self.rect.y += self.speedy
                if self.rect.top < -30 or self.rect.left < WIDTH - 1030  or self.rect.right > WIDTH + 50 or self.rect.bottom > 530:
                    self.kill()
                    new_enemies = Enemies()
                    all_sprites.add(new_enemies)
                    enemies.add(new_enemies)

        # Creating indestructable meteors that the player has to dodge
        class Meteors(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image_original = random.choice(meteor_images)
                self.image_original = pygame.transform.scale(self.image_original, (80,71))
                self.image_original.set_colorkey(BLACK)
                self.image = self.image_original.copy()
                self.rect = self.image.get_rect()
                self.radius = int(self.rect.width * 0.7 / 2)
                # Make the hitbox visible --->
                # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
                self.rect.x = random.randrange(990, 1000)
                self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
                self.speedy = random.randrange(-1, 1)
                self.speedx = random.randrange(-12, -5)
                self.rotation = 0
                self.rotation_speed = random.randrange(-8, 8)
                self.last_update = pygame.time.get_ticks()

            # Rotate the meteors for better looks
            def rotate(self):
                now = pygame.time.get_ticks()
                if now - self.last_update > 50:
                    self.last_update = now
                    self.rotation = (self.rotation + self.rotation_speed) % 360
                    new_image = pygame.transform.rotate(self.image_original, self.rotation)
                    old_center = self.rect.center
                    self.image = new_image
                    self.rect = self.image.get_rect()
                    self.rect.center = old_center
                
            # killing and spawning a new meteor when they go of the screen
            def update(self):
                self.rotate()
                self.rect.x += self.speedx
                self.rect.y += self.speedy
                if self.rect.top < -50 or self.rect.left < WIDTH - 1100  or self.rect.right > WIDTH + 100 or self.rect.bottom > 530:
                    self.kill()
                    new_meteors = Meteors()
                    all_sprites.add(new_meteors)
                    meteor.add(new_meteors)
                    
        # bullets
        class Bullets(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = bullet_img
                self.image.set_colorkey(BLACK)
                self.rect = self.image.get_rect()
                self.rect.bottom = y
                self.rect.centerx = x
                self.speedy = 0
                self.speedx = 10

            def update(self):
                self.rect.x += self.speedx
                # Remove the bullet if it is no longer on the screen
                if self.rect.right > 1000:
                    self.kill()
                    
        class Explosion(pygame.sprite.Sprite):
            def __init__(self, center, size):
                pygame.sprite.Sprite.__init__(self)
                self.size = size
                self.image = explosion_img[self.size][0]
                self.rect = self.image.get_rect()
                self.rect.center = center
                self.frame = 0
                self.last_update = pygame.time.get_ticks()
                self.frame_rate = 80

            def update(self): 
                now = pygame.time.get_ticks()
                if now - self.last_update > self.frame_rate:
                    self.last_update = now
                    self.frame += 1
                    if self.frame == len(explosion_img[self.size]):
                        self.kill()
                    else: 
                        center = self.rect.center
                        self.image = explosion_img[self.size][self.frame]
                        self.rect = self.image.get_rect()
                        self.rect.center = center


        # Show how many lives the player has left in the top left corner using images
        def show_lives(surf, x, y, lives, img):
            for i in range(lives):
                img_rect = img.get_rect()
                img_rect.x = x + 30 * i
                img_rect.y = y
                surf.blit(img, img_rect)

        # Function to pop up game over screen when player dies, Controls
        #def show_score_screen():
            #Startscreen.full_game_state == 0       

        # initialize score
        score = 0
        previous_score = 0
        saved_highscore = 0
        file = open('Highscores.txt', 'r')
        for line in file:
            if 'highscore: ' in line:
                highscore = int(line.replace('highscore: ', ''))
                saved_highscore = 0

        # Load All game graphics
        #Background
        background = pygame.image.load(path.join(img_dir, "Background.png")).convert()
        background_rect = background.get_rect()
        bg_width = background.get_width()
        scroll = 0
        tiles = math.ceil(WIDTH / bg_width) + 1

        # Player and Enemies and meteors
        player_img = pygame.image.load(path.join(img_dir, "Player 1.png")).convert()
        player_lives_img = pygame.transform.scale(player_img, (40, 29))
        player_lives_img.set_colorkey(BLACK)
        enemie_img = pygame.image.load(path.join(img_dir, "enemyRed2.png")).convert()
        bullet_img = pygame.image.load(path.join(img_dir, "laserRed07.png")).convert()

        # Random meteor image
        meteor_images = []
        meteor_list = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_big3.png', 'meteorBrown_big4.png']
        for img in meteor_list:
            meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

        # Making an image loop so an explosion is visible when something dies
        explosion_img = {}
        explosion_img['big'] = []
        explosion_img['small'] = []
        explosion_img['player'] = []
        for i in range (9):
            filename = 'explosie{}.png'.format(i)
            img = pygame.image.load(path.join(img_dir, filename)).convert()
            img.set_colorkey(BLACK)
            img_big = pygame.transform.scale(img, (75, 75))
            explosion_img['big'].append(img_big)
            img_small = pygame.transform.scale(img, (32, 32))
            explosion_img['small'].append(img_small)

        # All sprites 
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        enemies = pygame.sprite.Group() 
        for i in range(8):
            enemies_jets = Enemies()
            all_sprites.add(enemies_jets)
            enemies.add(enemies_jets) 
        player = Player()
        all_sprites.add(player)
        meteor = pygame.sprite.Group()
        for i in range(3):
            meteors = Meteors()
            all_sprites.add(meteors)
            meteor.add(meteors)

        # Game loop
        running = True
        game_over = False
        while running:
            if game_over:
                game_over = False 
                all_sprites = pygame.sprite.Group()
                bullets = pygame.sprite.Group()
                enemies = pygame.sprite.Group() 
                for i in range(8):
                    enemies_jets = Enemies()
                    all_sprites.add(enemies_jets)
                    enemies.add(enemies_jets) 
                player = Player()
                all_sprites.add(player)
                meteor = pygame.sprite.Group()
                for i in range(3):
                    meteors = Meteors()
                    all_sprites.add(meteors)
                    meteor.add(meteors)    
            # keep loop running at the right speed
            clock.tick(FPS)

            # Moving background
            for i in range (0, tiles):
                screen.blit(background, (i * bg_width + scroll, 0))

            scroll -= 2
            if abs(scroll) > bg_width:
                scroll = 0

            # Process input (events)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
            
            previous_score = score
        
            # update
            all_sprites.update()
            # Check to see if bullet hits an enemie
            hits_bullet_enemie = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits_bullet_enemie:
                pygame.mixer.music.set_volume(1)
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('hit.mp3'))
                score +=1
                if (previous_score//50) < (score//50):
                    print('add more', previous_score//50, score//50)
                    more_enemies = Enemies()
                    enemies.add(more_enemies)
                    all_sprites.add(more_enemies)
                # Spawn new enemies when killed by bullet
                new_enemies = Enemies()
                all_sprites.add(new_enemies)
                enemies.add(new_enemies)
                # Explosion
                explosion = Explosion(hit.rect.center, 'big')
                all_sprites.add(explosion)

            # Check to see if bullet hit meteor
            hits_bullet_meteor = pygame.sprite.groupcollide(meteor, bullets, False, True)
            for hit in hits_bullet_meteor:
                pygame.mixer.music.set_volume(1)
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('hit.mp3'))
                explosion = Explosion(hit.rect.center, 'small')
                all_sprites.add(explosion)

            # Check to see if enemie hit the player
            hits_player_enemie = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)
            for hit in hits_player_enemie:
                pygame.mixer.music.set_volume(1)
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('loselife.mp3'))
                player.lives -=1
                player.rect.centerx = WIDTH / 100
                player.rect.bottom = HEIGHT / 2
                # Respawn an enemie when it hit the player
                new_enemies = Enemies()
                all_sprites.add(new_enemies)
                enemies.add(new_enemies)

            # Check to see if meteor hit the player
            hits_player_meteors = pygame.sprite.spritecollide(player, meteor, True, pygame.sprite.collide_circle)
            if hits_player_meteors:

                player.rect.centerx = WIDTH / 100
                player.rect.bottom = HEIGHT / 2
                player.lives -= 1
                # Respawn a meteor when it hit the player
                new_meteors = Meteors()
                all_sprites.add(new_meteors)
                meteor.add(new_meteors)
            
            elif player.lives == 0:
                pygame.mixer.Channel(8).play(pygame.mixer.Sound('death.mp3'))
                game_over = True
                previous_score = score
                if score > highscore:
                    highscore = score
                if highscore > saved_highscore:
                    file = open('Highscores.txt','w')
                    file.write('highscore: ' + str(highscore))
                    file.close
                    saved_highscore = highscore
                score = 0
                show_go_screen()
            
                    

            # Draw / render
            all_sprites.draw(screen)
            show_lives(screen, WIDTH - 1000, 5, player.lives, player_lives_img)
            draw_text(screen, str(score), 20, WIDTH / 2, 10)

            # Flip the display
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()    
        pygame.quit()
        pygame.display.update() 

def highscores():
    global highscore  
    while True:
        SCREEN.blit(HS, (0, 0))
        HIGHSCORE_MOUSE_POS = pygame.mouse.get_pos()
        left, middle, right = pygame.mouse.get_pressed()
        file = open('Highscores.txt', 'r')
        for line in file:
            if 'highscore: ' in line:
                highscore = str(line.replace('highscore: ', '')) 
        str(highscore)
        HIGHSCORE_TEXT = get_font(70).render("Your Highscore is ", True, "White")

        HIGHSCORE_RECT = HIGHSCORE_TEXT.get_rect(center=(500, 130))
        SCREEN.blit(HIGHSCORE_TEXT, HIGHSCORE_RECT)

        HIGHSCORE_BACK = Button(image=None, pos=(500, 400), 
            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")
        HIGHSCORE_SCORE = Button(image=None, pos=(500, 250), 
            text_input=str(highscore), font=get_font(100), base_color="RED", hovering_color="Green")

        HIGHSCORE_BACK.changeColor(HIGHSCORE_MOUSE_POS)
        HIGHSCORE_BACK.update(SCREEN)

        HIGHSCORE_SCORE.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()     
            if event.type == pygame.MOUSEBUTTONDOWN:                    
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:  
                    if HIGHSCORE_BACK.checkForInput(HIGHSCORE_MOUSE_POS):
                        main_menu()
        pygame.display.update()

def show_go_screen():
    global highscore
    pygame.mixer.music.load('SpaceMenu.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    waiting = True
    while waiting: 
        file = open('Highscores.txt', 'r')
        for line in file:
            if 'highscore: ' in line:
                highscore = str(line.replace('highscore: ', '')) 
        str(highscore)
        GO_SCREEN_MOUSE_POS = pygame.mouse.get_pos()
        left, middle, right = pygame.mouse.get_pressed()    
        SCREEN.blit(HS, (0, 0))
        GAMEOVER_TEXT = get_font(80).render("GAME OVER ", True, "#ff0000")
        MANUAL_TEXT = get_font(40).render("Arrow keys to move, Space to Fire ", True, "White")
        HS_TEXT = get_font(40).render("Press SPACE to continue ", True, "White")
        HS2_TEXT = get_font(40).render("Your highscore   = ", True, "White")
        SCORE_TEXT = get_font(40).render(str(highscore), True, "#ff0000")

        GAMEOVER_RECT = GAMEOVER_TEXT.get_rect(center=(500, 150))
        MANUAL_RECT = MANUAL_TEXT.get_rect(center=(500, 300))
        HS_RECT = HS_TEXT.get_rect(center=(500, 400))
        HS2_RECT = HS2_TEXT.get_rect(center=(450, 250))
        SCORE_RECT = SCORE_TEXT.get_rect(center=(700, 250))

        SCREEN.blit(GAMEOVER_TEXT, GAMEOVER_RECT)
        SCREEN.blit(MANUAL_TEXT, MANUAL_RECT)
        SCREEN.blit(HS_TEXT, HS_RECT)
        SCREEN.blit(HS2_TEXT, HS2_RECT)
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)

        

        GO_SCREEN_BACK = Button(image=None, pos=(500, 450), 
        text_input="BACK TO MAIN MENU", font=get_font(25), base_color="White", hovering_color="Green")
        
        GO_SCREEN_BACK.changeColor(GO_SCREEN_MOUSE_POS)
        GO_SCREEN_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False         
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    if GO_SCREEN_BACK.checkForInput(GO_SCREEN_MOUSE_POS):
                        main_menu()
                        
        pygame.display.update()
   
def options_menu():
    while True:
        SCREEN.blit(HS, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        left, middle, right = pygame.mouse.get_pressed()
        OPTIONS_TEXT = get_font(40).render("options ", True, "White")
        OPTIONS_TEXT2 = get_font(40).render("Arrow keys to move, Space to Fire ", True, "White")
        #OPTIONS_TEXT = get_font(40).render("options ", True, "White")
        #OPTIONS_TEXT = get_font(40).render("options ", True, "White")

        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 130))
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(500, 200))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)

        OPTIONS_BACK = Button(image=None, pos=(500, 400), 
            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        OPTIONS_MUSICON = Button(image=None, pos=(700, 250), 
            text_input="MUSIC ON", font=get_font(25), base_color="White", hovering_color="Green") 

        OPTIONS_MUSICOFF = Button(image=None, pos=(700, 300), 
            text_input="MUSIC OFF", font=get_font(25), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_MUSICON.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MUSICON.update(SCREEN)
        OPTIONS_MUSICOFF.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MUSICOFF.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        if OPTIONS_MUSICON.checkForInput(OPTIONS_MOUSE_POS):
                            pygame.mixer.music.unpause()
                        if OPTIONS_MUSICOFF.checkForInput(OPTIONS_MOUSE_POS):
                            pygame.mixer.music.pause()	
                        if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                            main_menu()
        pygame.display.update()

def main_menu():
    while True:

        SCREEN.blit(BG_G, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        left, middle, right = pygame.mouse.get_pressed()
        MENU_TEXT = get_font(75).render("MAIN MENU", True, "Purple")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Lib/img/Play Button.png"), pos=(333, 250), 
                            text_input="PLAY", font=get_font(35), base_color="#fcd4f4", hovering_color="Purple")
        HIGHSCORE_BUTTON = Button(image=pygame.image.load("Lib/img/Play Button.png"), pos=(666, 250), 
                            text_input="HIGHSCORE", font=get_font(35), base_color="#fcd4f4", hovering_color="Purple")
        QUIT_BUTTON = Button(image=pygame.image.load("Lib/img/Play Button.png"), pos=(655, 400), 
                            text_input="QUIT", font=get_font(35), base_color="#fcd4f4", hovering_color="Purple")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Lib/img/Play Button.png"), pos=(333, 400), 
                            text_input="OPTIONS", font=get_font(35), base_color="#fcd4f4", hovering_color="Purple")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, HIGHSCORE_BUTTON, QUIT_BUTTON, OPTIONS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.mixer.music.set_volume(1)
                        pygame.mixer.Channel(6).play(pygame.mixer.Sound('Select.mp3'))
                        play_game()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.mixer.music.set_volume(1)
                        pygame.mixer.Channel(6).play(pygame.mixer.Sound('Select.mp3'))
                        options_menu()
                    if HIGHSCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.mixer.music.set_volume(1)
                        pygame.mixer.Channel(6).play(pygame.mixer.Sound('Select.mp3'))
                        highscores()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
        pygame.display.update()   
main_menu()
