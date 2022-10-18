# Shoot 'em up game
import pygame
import random
from os import path
import math

# Screen and graphics
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
pygame.display.set_caption("Shoot 'em up")
clock = pygame.time.Clock()

# Create player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50,38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 100
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.lives = 3
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    
        

        

    # Player movement with keys
    def update(self):
        
        self.rect.center = pygame.mouse.get_pos()
        #hierboven de functie die ervoor zorgt dat de spaceship de positie van de muis volgt
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

    
    #Deze class zorgt ervoor dat wanneer er een bullet is afgeschoten dat er dan weer een nieuwe bullet sprite word teruggegeven

    def create_bullet(self):
        return bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

# Hier de bullet code
class bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50,10))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(center = (pos_x, pos_y))

    def update(self):
        self.rect.x += 5



       # Creating Borders for the player so it can't go of the screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Enemie fighters
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemie_img
        self.image = pygame.transform.scale(enemie_img, (45,38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
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
            new_enemies = Mob()
            all_sprites.add(new_enemies)
            mobs.add(new_enemies)




# Load All game graphics
#Background
background = pygame.image.load(path.join(img_dir, "space.png")).convert()
background_rect = background.get_rect()
bg_width = background.get_width()
scroll = 0
tiles = math.ceil(WIDTH / bg_width) + 1
# Player and Enemies
player_img = pygame.image.load(path.join(img_dir, "playership.png")).convert()
enemie_img = pygame.image.load(path.join(img_dir, "enemyRed1.png")).convert()

# All sprites 
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group() 
for i in range(14):
    Enemies = Mob()
    all_sprites.add(Enemies)
    mobs.add(Enemies) 
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
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
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # update
    all_sprites.update()

    # Check to see if enemie hit the player
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    if hits:
        player.rect.centerx = WIDTH / 100
        player.rect.bottom = HEIGHT / 2
        player.lives -= 1
        
    elif player.lives == 0:
         running = False
        #Hieronder is voor het creeren van de kogels 
    if event.type == pygame.MOUSEBUTTONDOWN:
        bullet_group.add(player.create_bullet())


    #Bullet groep

    bullet_group = pygame.sprite.Group()
        

    #draw / render
    all_sprites.draw(screen)
    #Door wat hieronder staat zouden de schoten moeten werken maar het werkt niet.
    bullet_group.draw(screen)
    bullet_group.update()
    
    # flip the display
    pygame.display.flip()

pygame.quit()