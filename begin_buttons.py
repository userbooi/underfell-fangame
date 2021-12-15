import pygame

class Begin:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = UF_game.settings
        self.visibility = False
        self.moved = False

        self.start_button()

        self.x = float(self.start_rect.x)

    def start_button(self):

        self.start = pygame.image.load('images/start.png').convert_alpha()
        self.start = pygame.transform.scale(self.start, (218, 50)).convert_alpha()
        self.start_rect = self.start.get_rect()

        self.start_rect.center = self.screen_rect.center

    def move_title(self):
        if self.start_rect.x <= 445:
            self.x += 0.6

            self.start_rect.x = self.x
        else:
            self.moved = True

    def draw_start_button(self):
        self.visibility = True
        self.screen.blit(self.start, self.start_rect)
