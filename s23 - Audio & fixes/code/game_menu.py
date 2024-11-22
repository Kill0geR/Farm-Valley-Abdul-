import pygame
import sys
from settings import *
from main import *
import os


class GameMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image = pygame.image.load("../background/stardew_valley_2.jpeg")
        pygame.display.set_caption('Farm Valley')
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick() / 1000

    def get_font(self, size):
        return pygame.font.Font("../font/LycheeSoda.ttf", size)

    def set_background(self, image):
        size = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(size, (0, 0))

    def set_playground(self, image, zoom=0.8):
        new_width = int(image.get_width() * zoom)
        new_height = int(image.get_height() * zoom)
        size = pygame.transform.scale(image, (new_width, new_height))
        position = ((SCREEN_WIDTH - new_width) // 2, (SCREEN_HEIGHT - new_height) // 2)
        self.screen.blit(size, position)

    def run(self):
        while True:
            menu_mouse = pygame.mouse.get_pos()

            self.screen.fill((0, 0, 0))
            self.set_background(self.image)

            text = self.get_font(100).render("Farm Valley", True, "#38883F")
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, 100))
            self.screen.blit(text, rect)

            name = self.get_font(50).render("Made by: Abdulrahman Ajloni", True, "#FFFFFF")
            rect_name = text.get_rect(center=((SCREEN_WIDTH // 2)+20, 900))
            self.screen.blit(name, rect_name)

            play_button = Button(image=pygame.image.load("../play_rect/Play Rect.png"), pos=(SCREEN_WIDTH // 2, 250),
                                 text_input="PLAY", font=self.get_font(75), base_color="#B0CFAE",
                                 hovering_color="White")

            play_button.changeColor(menu_mouse)
            play_button.update(self.screen)

            quit_button = Button(image=pygame.image.load("../play_rect/Play Rect.png"), pos=(SCREEN_WIDTH // 2, 500),
                                 text_input="QUIT", font=self.get_font(75), base_color="#B0CFAE",
                                 hovering_color="White")

            quit_button.changeColor(menu_mouse)
            quit_button.update(self.screen)

            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_button.checkForInput(menu_mouse):
                            start_game = Game()
                            start_game.run()

                        elif quit_button.checkForInput(menu_mouse):
                            pygame.quit()
                            sys.exit()
            except SystemError:
                pass

            pygame.display.update()


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
