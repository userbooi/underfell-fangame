import pygame

class Slash:

    def __init__(self, UF_game):
        self.screen = UF_game.screen

        self.make_slash1()
        self.make_slash2()
        self.make_slash3()
        self.make_slash4()
        self.make_slash5()

    def make_slash1(self):
        self.slash1 = pygame.image.load('images/slash1.png').convert_alpha()
        self.slash1_rect = self.slash1.get_rect()

        self.slash1_rect.x = 275
        self.slash1_rect.y = -155

    def make_slash2(self):
        self.slash2 = pygame.image.load('images/slash2.png').convert_alpha()
        self.slash2_rect = self.slash2.get_rect()

        self.slash2_rect.x = 275
        self.slash2_rect.y = -155

    def make_slash3(self):
        self.slash3 = pygame.image.load('images/slash3.png').convert_alpha()
        self.slash3_rect = self.slash3.get_rect()

        self.slash3_rect.x = 275
        self.slash3_rect.y = -155

    def make_slash4(self):
        self.slash4 = pygame.image.load('images/slash4.png').convert_alpha()
        self.slash4_rect = self.slash4.get_rect()

        self.slash4_rect.x = 275
        self.slash4_rect.y = -155

    def make_slash5(self):
        self.slash5 = pygame.image.load('images/slash5.png').convert_alpha()
        self.slash5_rect = self.slash5.get_rect()

        self.slash5_rect.x = 275
        self.slash5_rect.y = -155

    def show_slash1(self):
        self.screen.blit(self.slash1, self.slash1_rect)

    def show_slash2(self):
        self.screen.blit(self.slash2, self.slash2_rect)

    def show_slash3(self):
        self.screen.blit(self.slash3, self.slash3_rect)

    def show_slash4(self):
        self.screen.blit(self.slash4, self.slash4_rect)

    def show_slash5(self):
        self.screen.blit(self.slash5, self.slash5_rect)
