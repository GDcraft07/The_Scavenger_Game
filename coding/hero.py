import pygame
from coding import sprite_group
from coding.download_images import load_image


class Hero(pygame.sprite.Sprite):
    image = load_image('hero.png')

    def __init__(self, x=400, y=391, angle=0, group=sprite_group.all_sprites):
        super().__init__(group)
        self.image = Hero.image
        self.image = pygame.transform.scale(self.image, (150, 172))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.mass = 1
        self.velocity = 8
        self.position = True
        self.run = True

    def update(self, flag_left, flag_right, isjump, switch, open_trash_can, hearts):
        if flag_left and self.rect.x > 0:
            self.rect.x -= 10
            if self.position:
                self.image = pygame.transform.flip(self.image, True, False)
                self.position = False

        if flag_right and 850 > self.rect.x:
            self.rect.x += 10
            if not self.position:
                self.image = pygame.transform.flip(self.image, True, False)
                self.position = True

        if isjump:
            self.rect.y -= 0.5 * self.mass * (self.velocity ** 2)
            self.velocity -= 1
            if self.velocity < 0:
                self.mass = -1

            if self.velocity < -9:
                self.rect.y = 391
                self.velocity = 8
                self.mass = 1
                self.run = False
