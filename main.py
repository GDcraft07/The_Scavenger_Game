import pygame
import config
from coding import download_images, start_screen
background = download_images.load_image('background_1.png')


pygame.init()
screen = pygame.display.set_mode(config.SIZE)
screen.fill(config.COLOR)


def main():
    start_screen.start_screen(screen, background)


if __name__ == "__main__":
    main()
