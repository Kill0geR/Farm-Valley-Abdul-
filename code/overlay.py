import pygame
from settings import *


class Overlay:
    def __init__(self, player):
        # General setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # Imports
        overlay_path = '../graphics/overlay/'
        self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in
                           player.tools}
        self.seeds_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in
                           player.seeds}

        # Button properties
        self.quit_button_rect = pygame.Rect(SCREEN_WIDTH - 110, 10, 100, 40)  # Position und Größe des Quit-Buttons

    def display(self):
        # Tool
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom=OVERLAY_POSITIONS['tool'])
        self.display_surface.blit(tool_surf, tool_rect)

        font = pygame.font.Font(None, 36)
        tool_changer = font.render("Q", True, (255, 255, 255))
        tool_changer_rect = tool_changer.get_rect(midbottom=(55, SCREEN_HEIGHT - 85))
        self.display_surface.blit(tool_changer, tool_changer_rect)

        # Seeds
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS['seed'])
        self.display_surface.blit(seed_surf, seed_rect)

        tool_changer = font.render("E", True, (255, 255, 255))
        tool_changer_rect = tool_changer.get_rect(midbottom=(95, SCREEN_HEIGHT - 85))
        self.display_surface.blit(tool_changer, tool_changer_rect)

        # Title Text
        text_surf = font.render("Farm Valley (Abdul)", True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(self.display_surface.get_width() // 2, 30))
        self.display_surface.blit(text_surf, text_rect)

        # Quit button
        pygame.draw.rect(self.display_surface, (255, 0, 0), self.quit_button_rect)  # Roter Button
        quit_text = font.render("Quit", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect(center=self.quit_button_rect.center)
        self.display_surface.blit(quit_text, quit_text_rect)

