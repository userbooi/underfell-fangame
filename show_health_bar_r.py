import pygame

class HealthBar2():

    def __init__(self, UF_game):

        self.screen = UF_game.screen
        self.settings = UF_game.settings
        self.BB = UF_game.battle
        self.hb_color = self.settings.health_bar_color2

        self.hb_rect = pygame.Rect(0, 0, 100, 30)
        self.hb_rect.center = self.BB.rect.center
        self.hb_rect.y += 190

    def draw_bar(self):
        pygame.draw.rect(self.screen, self.hb_color, self.hb_rect)