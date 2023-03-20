import pygame
from random import randint, randrange
from coding import sprite_group, add_garbage, count, main_screen, fin_screen
from coding.download_images import load_image
import main
import time


class Garbage(pygame.sprite.Sprite):
    life_of_hearts = [True, True, True]
    count = 0

    def __init__(self, number=1, x=0, y=0):
        super().__init__(sprite_group.all_sprites)
        sprite_group.garbage_group.add(self)
        self.image = load_image(f'garbage\\garbage_{number}.png')
        self.image = pygame.transform.scale(self.image, (40, 66))
        self.image = pygame.transform.rotate(self.image, randint(1, 360))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.speedy = randrange(1, 3)
        self.speedx = randrange(-3, 3)
        self.point = count.Count()

    def count_add(self):
        Garbage.count += 5

    def hero_dead(self, bools=True):
        if not main_screen.trush_can.open:
            main_screen.trush_can.image, main_screen.trush_can.image_1 = main_screen.trush_can.image_1, \
                                                                         main_screen.trush_can.image
            main_screen.trush_can.rect.y -= 13
            main_screen.trush_can.normal_y -= 13
            main_screen.trush_can.open = not main_screen.trush_can.open
            main_screen.trush_can.time_result += time.time() - main_screen.trush_can.start_time
            main_screen.trush_can.time_result = round(main_screen.trush_can.time_result, 1)
        self.point.accrual_of_points(Garbage.count)
        amount_garbage = Garbage.count
        Garbage.count = 0
        self.point.deduction_of_points(main_screen.trush_can.time_result)
        main_screen.heros.rect.y = 391
        main_screen.trush_can.rect.y = main_screen.trush_can.normal_y
        Garbage.life_of_hearts = [True, True, True]
        for element in sprite_group.all_sprites:
            element.kill()
        if bools:
            fin_screen.final_screen(main.screen, self.point.return_points(), amount_garbage)
            self.point.clearing_points()

    def heart_lost(self, hearts):
        if Garbage.life_of_hearts[2]:
            hearts[2].kill()
            Garbage.life_of_hearts[2] = False
        elif Garbage.life_of_hearts[1]:
            hearts[1].kill()
            Garbage.life_of_hearts[1] = False
        elif Garbage.life_of_hearts[0]:
            hearts[0].kill()
            self.hero_dead()

    def update(self, flag_left, flag_right, isjump, switch, open_trash_can, hearts):
        if pygame.sprite.spritecollideany(self, sprite_group.person, pygame.sprite.collide_rect_ratio(.7))\
                or self.rect.y >= 497:
            self.kill()
            add_garbage.AddGarbage(4).add()
            self.heart_lost(hearts)
        if not pygame.sprite.spritecollideany(self, sprite_group.trush_can):
            self.rect = self.rect.move(self.speedx, self.speedy)
            if self.rect.x <= 0 or self.rect.x >= 940:
                self.speedx = -self.speedx
        else:
            self.kill()
            add_garbage.AddGarbage().add()
            if open_trash_can:
                self.heart_lost(hearts)
            else:
                self.count_add()
