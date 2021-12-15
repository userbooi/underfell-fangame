import pygame

class Bg_heart:

    def __init__(self, UF_game):

        self.screen = UF_game.screen
        self.begin = UF_game.start
        self.location = self.begin.start
        self.location_rect = self.begin.start_rect

        self.bg_heart = pygame.image.load('images/starting_heart.png').convert_alpha()
        self.bg_heart = pygame.transform.scale(self.bg_heart, (44, 50)).convert_alpha()
        self.bg_heart_rect = self.bg_heart.get_rect()

        self.bg_heart_rect.left = self.location_rect.left - 4
        self.bg_heart_rect.top = self.location_rect.top

        self.visability = False

    def draw_bg_heart(self):
        self.visability = True
        self.screen.blit(self.bg_heart, self.bg_heart_rect)