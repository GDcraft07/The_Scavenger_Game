import sys
import pygame
from coding import hero, sprite_group, trash_can, add_garbage, heart, back, garbage
import config
import main

heros = hero.Hero()
trush_can = trash_can.TrashCan()


def main_screen(screen, background):
    clock = pygame.time.Clock()
    left, right, isjump, running, switch = [False] * 5
    sprite_group.person.add(heros)
    heart_1 = heart.Heart()
    heart_2 = heart.Heart(x=70)
    heart_3 = heart.Heart(x=130)
    hearts = [heart_1, heart_2, heart_3]
    back_button = back.Back(890, 10, sprite_group.all_sprites)
    sprite_group.trush_can.add(trush_can)
    add_garbage.AddGarbage(4).add()
    sprite_group.all_sprites.add([heros, trush_can])

    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_SPACE:
                    isjump = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_b:
                    switch = True
            if back_button.click(event):
                garbage.Garbage().hero_dead(False)
                main.main()

        sprite_group.all_sprites.update(left, right, isjump, switch, trush_can.open, hearts)

        if not heros.run and not trush_can.run:
            isjump = False
            heros.run = True
            trush_can.run = True
        switch = False
        screen.blit(background, (0, 0))
        sprite_group.all_sprites.draw(screen)
        clock.tick(config.FPS)
        pygame.display.flip()

    pygame.quit()
