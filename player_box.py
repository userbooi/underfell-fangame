import pygame

class BattleBox:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.screen_rect = UF_game.screen.get_rect()
        self.stats = UF_game.stats

        self.make_box()

    def make_box(self):
        self.image = pygame.image.load('images/battlebox.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (810, 270)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.y += 50

        self.image2 = pygame.image.load('images/battlebox_white.png').convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (810, 270)).convert_alpha()
        self.rect2 = self.image2.get_rect()

        self.rect2.center = self.screen_rect.center
        self.rect2.y += 50

    def shrinks(self):
        if self.rect.width != 270:
            self.rect.width -= 10

            self.image = pygame.image.load('images/battlebox.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (self.rect.width, 270)).convert_alpha()
            self.rect = self.image.get_rect()

            self.rect.center = self.screen_rect.center
            self.rect.y += 50

    def shrink_a_bit1(self):
        if self.rect.width != 670:
            self.rect.width -= 10

            self.image = pygame.image.load('images/battlebox.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (self.rect.width, 270)).convert_alpha()
            self.rect = self.image.get_rect()

            self.rect.center = self.screen_rect.center
            self.rect.y += 50

    def shrink_a_bit2(self):
        if self.rect.width != 490:
            self.rect.width -= 10

            self.image = pygame.image.load('images/battlebox.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (self.rect.width, 270)).convert_alpha()
            self.rect = self.image.get_rect()

            self.rect.center = self.screen_rect.center
            self.rect.y += 50

    def shrink_to_left(self):
        if self.rect.width != 490:
            self.rect.width -= 10

            self.image = pygame.image.load('images/battlebox.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (self.rect.width, 270)).convert_alpha()
            self.rect = self.image.get_rect()

            self.rect.center = self.screen_rect.center
            self.rect.left = 95
            self.rect.y += 50

    def shrink_to_left_a_bit(self):
        left = self.rect.left
        bottom = self.rect.bottom

        if self.rect.width != 250:
            self.rect.width -= 2

            self.image = pygame.image.load('images/battlebox.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height)).convert_alpha()
            self.rect = self.image.get_rect()

            self.rect.center = self.screen_rect.center
            self.rect.left = left
            self.rect.y += 50
            self.rect.bottom = bottom

    def shrink_to_bottom(self):
        bottom = self.rect.bottom

        if self.rect.height != 120:
            self.rect.height -= 2

            self.image = pygame.image.load('images/battlebox.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height)).convert_alpha()
            self.rect = self.image.get_rect()

            self.rect.center = self.screen_rect.center
            self.rect.y += 50
            self.rect.bottom = bottom

    def return_size_width(self):
        self.rect.width += 10

        self.image = pygame.image.load('images/battlebox.png').convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.rect.width, 270)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.y += 50

    def return_size_width2(self):
        bottom = self.rect.bottom

        if self.rect.width != 270:
            self.rect.width += 2

            self.image = pygame.image.load('images/battlebox.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.width)).convert_alpha()
            self.rect = self.image.get_rect()

            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = bottom

    def return_size_height(self):
        bottom = self.rect.bottom

        if self.rect.height != 270:
            self.rect.height += 2

            self.image = pygame.image.load('images/battlebox.png').convert_alpha()

            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height)).convert_alpha()
            self.rect = self.image.get_rect()

            self.rect.bottom = bottom

    def blitme(self):
        if self.stats.turn != 'spared turn':
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.image2, self.rect2)
