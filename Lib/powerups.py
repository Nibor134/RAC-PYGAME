



class Pow(pygame.sprite.Sprite):

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self) 
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_imgages[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 0
        self.speedx = 3

    def update(self):
        self.rect.x += self.speedx
        # Remove the bullet if it is no longer on the screen
        if self.rect.top > HEIGHT:
            self.kill()