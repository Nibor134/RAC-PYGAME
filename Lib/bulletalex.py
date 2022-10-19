
# Shoot bullets button
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_bullet > self.bullet_delay:
            self.last_bullet = now
            bullet = Bullets(self.rect.right, self.rect.centery)
            all_sprites.add(bullet)
            bullets.add(bullet)

#Class for bullet position, speed and drawing the custom made bullet
class Bullets(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = bullet.png
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 0
        self.speedx = 10

#Function for updating the bullet
    def update(self):
        self.rect.x += self.speedx
        # Remove the bullet if it is no longer on the screen
        if self.rect.right > 1000:
            self.kill()

bullets = pygame.sprite.Group()
all_sprites.update()