import pygame
from coding.download_images import load_image


class Back(pygame.sprite.Sprite):
    image = load_image('back.png')

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = Back.image
        self.image = pygame.transform.scale(self.image, (100, 36))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def click(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return True
        return False
