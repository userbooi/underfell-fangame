import pygame

class Warning:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.battle = UF_game.battle

        self.make_blue_warning()
        self.make_orange_warning()

    def make_blue_warning(self):
        self.blue_w = pygame.image.load('images/blue_bone_warning.png')
        self.blue_w = pygame.transform.scale(self.blue_w, (25, 100))
        self.blue_w_rect = self.blue_w.get_rect()

        self.blue_w_rect.top = self.battle.rect.top + 85

    def make_orange_warning(self):
        self.orange_w = pygame.image.load('images/orange_bone_warning.png')
        self.orange_w = pygame.transform.scale(self.orange_w, (25, 100))
        self.orange_w_rect = self.blue_w.get_rect()

        self.orange_w_rect.top = self.battle.rect.top + 85

    def make_warnings_40(self):
        self.blue_w_rect.x = 333
        self.orange_w_rect.x = 333

    def show_blue_warning(self):
        self.screen.blit(self.blue_w, self.blue_w_rect)

    def show_orange_warning(self):
        self.screen.blit(self.orange_w, self.orange_w_rect)
