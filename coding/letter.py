import pygame
from coding import sprite_group
from coding.download_images import load_image


class Letter(pygame.sprite.Sprite):
    def __init__(self, name_letter, x, y):
        super().__init__(sprite_group.start_screen_sprites)
        self.image = load_image(f'letter\\{name_letter}.png')
        self.image = pygame.transform.scale(self.image, (100, 125))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
