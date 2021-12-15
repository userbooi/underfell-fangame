import pygame
from act import Act

class Item:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.act = Act(UF_game)

        self.itemr()
        self.itemy()
        self.itemo()

    def itemr(self):
        self.item_r = pygame.image.load('images/item.png').convert_alpha()

        self.item_r_rect = self.item_r.get_rect()
        self.item_r_rect.left = self.act.act_r_rect.right + 23
        self.item_r_rect.bottom = self.screen_rect.bottom - 9

    def itemy(self):
        self.item_y = pygame.image.load('images/item3.png').convert_alpha()

        self.item_y_rect = self.item_y.get_rect()
        self.item_y_rect.left = self.act.act_y_rect.right + 23
        self.item_y_rect.bottom = self.screen_rect.bottom - 9

    def itemo(self):
        self.item_o = pygame.image.load('images/item2.png').convert_alpha()

        self.item_o_rect = self.item_o.get_rect()
        self.item_o_rect.left = self.act.act_y_rect.right + 23
        self.item_o_rect.bottom = self.screen_rect.bottom - 9

    def show_itemr(self):
        self.screen.blit(self.item_r, self.item_r_rect)

    def show_itemy(self):
        self.screen.blit(self.item_y, self.item_y_rect)

    def show_itemo(self):
        self.screen.blit(self.item_o, self.item_o_rect)
