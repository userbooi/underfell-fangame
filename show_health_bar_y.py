import pygame

class HealthBar():

    def __init__(self, UF_game):

        self.screen = UF_game.screen
        self.settings = UF_game.settings
        self.BB = UF_game.battle
        self.hb_color = self.settings.health_bar_color
        self.hbr = UF_game.hb2
        self.make_bar()

    def make_bar(self):
        self.hb_rect = pygame.Rect(0, 0, self.settings.health_bar_width, self.settings.health_bar_height)
        self.hb_rect.center = self.BB.rect.center
        self.hb_rect.left = self.hbr.hb_rect.left
        self.hb_rect.top = self.hbr.hb_rect.top

    def draw_bar(self):
        pygame.draw.rect(self.screen, self.hb_color, self.hb_rect)