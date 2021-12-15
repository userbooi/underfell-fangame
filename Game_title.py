import pygame, time

class Title:

    def __init__(self, UF_game):

        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()

        self.UNDERFELL()
        self.sans_fight()
        self.credits()

        self.y = float(self.title_image_rect.y)
        self.y2 = float(self.title2_image_rect.y)
        self.y3 = float(self.credit_rect.y)

    def sans_fight(self):
        self.title2_image = pygame.image.load('images/title2.png').convert_alpha()
        self.title2_image = pygame.transform.scale(self.title2_image, (500, 50)).convert_alpha()
        self.title2_image_rect = self.title2_image.get_rect()
        self.title2_image_rect.center = self.screen_rect.center

    def UNDERFELL(self):
        self.title_image = pygame.image.load('images/UNDERFELL.png').convert_alpha()
        self.title_image = pygame.transform.scale(self.title_image, (800, 125)).convert_alpha()
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.center = self.screen_rect.center

    def credits(self):
        self.credit = pygame.image.load('images/credits.png').convert_alpha()
        self.credit = pygame.transform.scale(self.credit, (452, 133)).convert_alpha()
        self.credit_rect = self.credit.get_rect()

        self.credit_rect.center = self.screen_rect.center

    def animate_title(self):
        if self.title_image_rect.y >= 60:
            self.y -= 0.6
            self.title_image_rect.y = self.y
        else:
            pass

    def animate_title2(self):
        if self.title2_image_rect.y >= self.title_image_rect.bottom + 10:
            self.y2 -= 0.6
            self.title2_image_rect.y = self.y2
        else:
            pass

    def animate_credit(self):
        if self.title2_image_rect.y >= self.title2_image_rect.bottom + 10:
            self.y3 -= 0.6
            self.credit_rect.y = self.y3
        else:
            pass

    def slow_up_titles(self):
        self.y -= 0.04
        self.y2 -= 0.04
        self.y3 -= 0.04

        self.title_image_rect.y = self.y
        self.title2_image_rect.y = self.y2
        self.credit_rect.y = self.y3

    def draw_title(self):
        self.screen.blit(self.title_image, self.title_image_rect)

    def draw_title2(self):
        self.screen.blit(self.title2_image, self.title2_image_rect)

    def show_credit(self):
        self.screen.blit(self.credit, self.credit_rect)
