import pygame
from coding import sprite_group
from coding.download_images import load_image
import time


class TrashCan(pygame.sprite.Sprite):

    def __init__(self, x=490, y=410, angle=0, group=sprite_group.all_sprites):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image('closed_trash_can.png'), (75, 108))
        self.image = pygame.transform.rotate(self.image, angle)
        self.image_1 = pygame.transform.scale(load_image('open_trash_can.png'), (70, 90))
        self.rect = self.image.get_rect()
        self.rect_1 = self.image_1.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.normal_y = 410
        self.mass = 1
        self.velocity = 8
        self.start_time = 0
        self.time_result = 0
        self.position = True
        self.run = True
        self.open = True

    def update(self, flag_left, flag_right, isjump, switch, open_trash_can, hearts):
        if flag_left and self.rect.x > -15:
            self.rect.x -= 10
            if self.position:
                self.rect.x -= 110
                self.position = False

        if flag_right and 940 > self.rect.x:
            self.rect.x += 10
            if not self.position:
                self.rect.x += 110
                self.position = True

        if isjump:
            self.rect.y -= 0.5 * self.mass * (self.velocity ** 2)
            self.velocity -= 1
            if self.velocity < 0:
                self.mass = -1

            if self.velocity < -9:
                self.rect.y = self.normal_y
                self.velocity = 8
                self.mass = 1
                self.run = False

        if switch:
            self.image, self.image_1 = self.image_1, self.image
            if self.open:
                self.rect.y += 13
                self.normal_y += 13
                self.open = not self.open
                self.start_time = time.time()
            else:
                self.rect.y -= 13
                self.normal_y -= 13
                self.open = not self.open
                self.time_result += time.time() - self.start_time
                self.time_result = round(self.time_result, 1)
