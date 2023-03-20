import pygame
from coding import sprite_group
from coding.download_images import load_image


class Heart(pygame.sprite.Sprite):
    image = load_image('heart.png')

    def __init__(self, x=10, y=10, group=sprite_group.all_sprites):
        super().__init__(group)
        self.image = Heart.image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
