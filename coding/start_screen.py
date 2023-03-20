import sys
import pygame

import main
from coding import sprite_group, play_button, main_screen, rules, rule_screen, hero, trash_can, letter,\
    download_images, read_update_bd, delet_button


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(screen, background):
    image = download_images.load_image('background_2.jpg')
    clock = pygame.time.Clock()
    play_button_object = play_button.PlayButton()
    rule_button = rules.Rules()
    deletbutton = delet_button.DeletButton()
    hero.Hero(100, 250, 45, sprite_group.start_screen_sprites)
    trash_can.TrashCan(675, 275, 315, sprite_group.start_screen_sprites)
    letters = ['m', 'y', 'c', 'o', 'p', "sh'", 'u', 'k']
    font = pygame.font.Font(None, 50)
    best_game = font.render(f'Лучший результат: {read_update_bd.read_table()}', True, pygame.color.Color(255, 0, 0))
    start_x = 40
    start_y = 50
    for let in letters:
        letter.Letter(let, start_x, start_y)
        start_x += 115

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_screen.main_screen(screen, background)

            elif play_button_object.click(event):
                main_screen.main_screen(screen, background)

            elif rule_button.click(event):
                rule_screen.rule_screen()

            elif deletbutton.click(event):
                read_update_bd.update_table('0')
                main.main()

        screen.blit(image, (0, 0))
        screen.blit(best_game, (10, 503))
        sprite_group.start_screen_sprites.draw(screen)
        pygame.display.set_caption('Мусорщик')
        pygame.display.set_icon(download_images.load_image('hero.png'))
        pygame.display.flip()
        clock.tick(60)
