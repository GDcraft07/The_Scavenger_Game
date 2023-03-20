import sys
import pygame
from coding import back, sprite_group
import main


def rule_screen():
    screen = pygame.display.set_mode((800, 300))
    text = ['Правила игры "Мусорщик"',
            '1) Управление:',
            '-Хотьба персонажа - стрелки вправо и влево',
            '-Прыжок - Space',
            '-Открытие / Закрытие бака - "B"',
            '2) Цель игры:',
            'Целью игры являеться собрать наибольшое количество мусора падающего с неба.',
            'У вас всего лишь три жизни. Если мусор касается вас, пола или закрытого бака',
            'вы теряете жизнь. Если же бак открыт и вы ловите мусор, вам начисляются баллы.',
            'Однако есть усложнение: чем дольше вы держите бак открытым тем меньше вам баллов начисляется.',
            'Удачи!']

    font = pygame.font.Font(None, 20)
    text_coord = 5
    for line in text:
        string_rendered = font.render(line, True, pygame.Color(255, 255, 255))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    back_button = back.Back(690, 10, sprite_group.rule_screen_sprites)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if back_button.click(event):
                screen = pygame.display.set_mode((1000, 563))
                main.main()

        screen.fill((0, 0, 0))
        text_coord = 10
        for line in text:
            string_rendered = font.render(line, True, pygame.Color(255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        sprite_group.rule_screen_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(60)
