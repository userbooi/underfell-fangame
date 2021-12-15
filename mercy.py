import pygame

class Mercy:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()

        self.mercyr()
        self.mercyy()
        self.mercyo()

    def mercyr(self):
        self.mercy_r = pygame.image.load('images/mercy.png').convert_alpha()

        self.mercy_r_rect = self.mercy_r.get_rect()
        self.mercy_r_rect.right = self.screen_rect.right - 23
        self.mercy_r_rect.bottom = self.screen_rect.bottom - 9

    def mercyy(self):
        self.mercy_y = pygame.image.load('images/mercy3.png').convert_alpha()

        self.mercy_y_rect = self.mercy_y.get_rect()
        self.mercy_y_rect.right = self.screen_rect.right - 23
        self.mercy_y_rect.bottom = self.screen_rect.bottom - 9

    def mercyo(self):
        self.mercy_o = pygame.image.load('images/mercy2.png').convert_alpha()

        self.mercy_o_rect = self.mercy_o.get_rect()
        self.mercy_o_rect.right = self.screen_rect.right - 23
        self.mercy_o_rect.bottom = self.screen_rect.bottom - 9

    def show_mercyr(self):
        self.screen.blit(self.mercy_r, self.mercy_r_rect)

    def show_mercyy(self):
        self.screen.blit(self.mercy_y, self.mercy_y_rect)

    def show_mercyo(self):
        self.screen.blit(self.mercy_o, self.mercy_o_rect)
