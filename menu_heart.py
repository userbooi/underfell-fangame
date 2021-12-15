import pygame

class MenuHeart:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.battle = UF_game.battle

        self.make_menu_heart()

    def make_menu_heart(self):
        self.menu_heart = pygame.image.load('images/sample_heart.png').convert_alpha()
        self.menu_heart = pygame.transform.scale(self.menu_heart, (27, 24)).convert_alpha()
        self.menu_heart_rect = self.menu_heart.get_rect()

        self.menu_heart_rect.top = self.battle.rect.top + 35
        self.menu_heart_rect.left = self.battle.rect.left + 28

    def show_menu_heart(self):
        self.screen.blit(self.menu_heart, self.menu_heart_rect)
