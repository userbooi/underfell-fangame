import pygame
from fight import Fight

class Act:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.fight = Fight(UF_game)

        self.actr()
        self.acty()
        self.acto()

    def actr(self):
        self.act_r = pygame.image.load('images/act.png').convert_alpha()

        self.act_r_rect = self.act_r.get_rect()
        self.act_r_rect.left = self.fight.fight_r_rect.right + 23
        self.act_r_rect.bottom = self.screen_rect.bottom - 9

    def acty(self):
        self.act_y = pygame.image.load('images/act3.png').convert_alpha()

        self.act_y_rect = self.act_y.get_rect()
        self.act_y_rect.left = self.fight.fight_r_rect.right + 23
        self.act_y_rect.bottom = self.screen_rect.bottom - 9

    def acto(self):
        self.act_o = pygame.image.load('images/act2.png').convert_alpha()

        self.act_o_rect = self.act_o.get_rect()
        self.act_o_rect.left = self.fight.fight_r_rect.right + 23
        self.act_o_rect.bottom = self.screen_rect.bottom - 9

    def show_actr(self):
        self.screen.blit(self.act_r, self.act_r_rect)

    def show_acty(self):
        self.screen.blit(self.act_y, self.act_y_rect)

    def show_acto(self):
        self.screen.blit(self.act_o, self.act_o_rect)
