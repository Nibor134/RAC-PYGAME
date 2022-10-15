# Shoot 'em up game 
import pygame
import random
from os import path
import math
#import Startscreen
#from MainMenu import main_menu

#if Startscreen.full_game_state == 3: 
   #exit()
#if MainMenu == 2:
    #exit()
    
# Screen and graphics
def game():
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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
            if now - self.last_bullet > self.bullet_delay:
                self.last_bullet = now
                bullet = Bullets(self.rect.right, self.rect.centery)
                all_sprites.add(bullet)
                bullets.add(bullet)

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

    def show_go_screen():
        screen.blit(background, background_rect)
        draw_text(screen, 'GAME OVER!', 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, 'Arrow keys to move, Space to Fire', 22, WIDTH /2, HEIGHT / 2)
        draw_text(screen, 'Press key to continue', 18, WIDTH / 2, HEIGHT * 3 / 4)
        draw_text(screen, 'Your highscore   =', 20, 490 , 5)
        draw_text(screen, str(saved_highscore), 20, 590, 5)
        
        pygame.display.flip()
        waiting = True
        while waiting: 
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False 
                    return             

    # initialize score
    score = 0
    previous_score = 0
    highscore = 0
    saved_highscore = 0
    file = open('Highscores.txt', 'r')
    for line in file:
        if 'highscore: ' in line:
            highscore = int(line.replace('highscore: ', ''))
            saved_highscore = 0



    # Load All game graphics
    #Background
    background = pygame.image.load(path.join(img_dir, "space.png")).convert()
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
            show_go_screen()
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
            explosion = Explosion(hit.rect.center, 'small')
            all_sprites.add(explosion)

        # Check to see if enemie hit the player
        hits_player_enemie = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)
        for hit in hits_player_enemie:
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
                

        # Draw / render
        all_sprites.draw(screen)
        show_lives(screen, WIDTH - 1000, 5, player.lives, player_lives_img)
        draw_text(screen, str(score), 20, WIDTH / 2, 10)

        # Flip the display
        pygame.display.flip()

    pygame.quit()