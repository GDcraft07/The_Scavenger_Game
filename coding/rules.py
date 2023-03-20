import pygame
from coding import sprite_group
from coding.download_images import load_image


class Rules(pygame.sprite.Sprite):
    image = load_image('rules.png')

    def __init__(self):
        super().__init__(sprite_group.start_screen_sprites)
        self.image = Rules.image
        self.image = pygame.transform.scale(self.image, (175, 119))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 412
        self.rect.y = 220

    def click(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            return True
        return False
