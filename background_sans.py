import pygame

class BgSans:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/sans_background.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (540, 750)).convert_alpha()
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

        self.image2 = pygame.image.load('images/background_sans_saved.png').convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (540, 750)).convert_alpha()
        self.image2_rect = self.image2.get_rect()
        self.image2_rect.center = self.screen_rect.center

        self.visability = False

    def draw_him(self):
        self.visability = True
        self.screen.blit(self.image, self.image_rect)

    def show_background_sans_saved(self):
        self.visability = True
        self.screen.blit(self.image2, self.image2_rect)