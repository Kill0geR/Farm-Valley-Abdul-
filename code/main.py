import pygame
import sys
from settings import *
from level import Level
from game_menu import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Farm Valley')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        cursor_image = pygame.image.load("../Cursors/Cursors/leaf.png").convert_alpha()
        cursor_image = pygame.transform.scale(cursor_image, (32, 32))

        pygame.mouse.set_visible(False)
        while True:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            quit_button_rect = pygame.Rect(SCREEN_WIDTH - 110, 10, 100, 40)
                            if quit_button_rect.collidepoint(event.pos):
                                pygame.quit()
                                sys.exit()

                dt = self.clock.tick() / 1000
                self.level.run(dt)

                mouse_pos = pygame.mouse.get_pos()

                self.screen.blit(cursor_image, mouse_pos)

                pygame.display.update()
            except SystemError:
                pass


if __name__ == '__main__':
    game = GameMenu()
    game.run()
