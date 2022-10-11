import pygame

# Enemy fighters
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