import pygame

class Fight:

    def __init__(self, UF_game):

        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()

        self.fightr()
        self.fighty()
        self.fighto()

    def fightr(self):
        self.fight_r = pygame.image.load('images/fight.png').convert_alpha()

        self.fight_r_rect = self.fight_r.get_rect()
        self.fight_r_rect.left = self.screen_rect.left + 23
        self.fight_r_rect.bottom = self.screen_rect.bottom - 9

    def fighty(self):
        self.fight_y = pygame.image.load('images/fight3.png').convert_alpha()

        self.fight_y_rect = self.fight_y.get_rect()
        self.fight_y_rect.left = self.screen_rect.left + 23
        self.fight_y_rect.bottom = self.screen_rect.bottom - 9

    def fighto(self):
        self.fight_o = pygame.image.load('images/fight2.png').convert_alpha()

        self.fight_o_rect = self.fight_o.get_rect()
        self.fight_o_rect.left = self.screen_rect.left + 23
        self.fight_o_rect.bottom = self.screen_rect.bottom - 9

    def show_fightr(self):
        self.screen.blit(self.fight_r, self.fight_r_rect)

    def show_fighty(self):
        self.screen.blit(self.fight_y, self.fight_y_rect)

    def show_fighto(self):
        self.screen.blit(self.fight_o, self.fight_o_rect)
