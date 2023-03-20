import sys
import pygame
import random
from coding import back, sprite_group, read_update_bd, main_screen, particle
import main


def terminate():
    pygame.quit()
    sys.exit()


def final_screen(screen, result, amount):
    time = main_screen.trush_can.time_result
    main_screen.trush_can.time_result = 0
    best_socers = read_update_bd.read_table()
    clock = pygame.time.Clock()
    if result < 0:
        result = 0
    if list(sprite_group.rule_screen_sprites):
        for i in sprite_group.rule_screen_sprites:
            i.kill()
    back_button = back.Back(890, 10, sprite_group.rule_screen_sprites)
    font = pygame.font.Font(None, 100)
    game_over = font.render('Game Over', True, pygame.color.Color(255, 0, 0))
    font_letter = pygame.font.Font(None, 50)
    the_amount_of_garbage_caught = font_letter.render(f'Количество пойманного мусора: {round(amount / 5)}',
                                                      True, pygame.color.Color(0, 255, 0))
    time_with_an_open_trash_can = font_letter.render(f'Время с открытым мусорным ведром: {time} сек.', True,
                                                     pygame.color.Color(255, 0, 0))
    total_result = font_letter.render(f'Итоговый счет: {result}', True,
                                      pygame.color.Color(random.randrange(100, 255), random.randrange(100, 255),
                                                         random.randrange(100, 255)))
    best = pygame.surface.Surface((10, 10))
    x_pos = 0
    best.fill((0, 0, 0))
    flag = False
    if float(result) > float(best_socers):
        font_best = pygame.font.Font(None, 90)
        read_update_bd.update_table(result)
        best = font_best.render('Новый рекорд', True, pygame.color.Color(255, 215, 0))
        for _ in range(6):
            particle.create_particles((random.randrange(100, 900), random.randrange(50, 350)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if back_button.click(event):
                main.main()

        screen.fill((0, 0, 0))
        screen.blit(game_over, (300, 10))
        screen.blit(the_amount_of_garbage_caught, (30, 100))
        screen.blit(time_with_an_open_trash_can, (30, 160))
        screen.blit(total_result, (300, 300))
        screen.blit(best, (250, 463))
        pygame.draw.rect(screen, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)),
                         (x_pos, 280, 1000, 90))
        if x_pos <= 1000:
            x_pos += 5
        sprite_group.rule_screen_sprites.draw(main.screen)
        sprite_group.particles.draw(main.screen)
        sprite_group.particles.update()
        pygame.display.flip()
        clock.tick(60)
