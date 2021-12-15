import pygame

class Arrow:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.battle = UF_game.battle

        self.arrow_direction = None

        self.make_up_arrow()
        self.make_down_arrow()

    def make_up_arrow(self):
        self.arrow_image = pygame.image.load('images/warning_arrow.png').convert_alpha()
        self.arrow_image = pygame.transform.scale(self.arrow_image, (100, 200)).convert_alpha()
        self.arrow_rect = self.arrow_image.get_rect()

        self.arrow_rect.center = self.battle.rect.center

    def make_down_arrow(self):
        self.arrow_image_down = pygame.image.load('images/warning_arrow.png').convert_alpha()
        self.arrow_image_down = pygame.transform.scale(self.arrow_image_down, (100, 200))
        self.arrow_image_down = pygame.transform.rotozoom(self.arrow_image_down, 180, 1)
        self.arrow_rect_down = self.arrow_image_down.get_rect()

        self.arrow_rect_down.center = self.battle.rect.center

    def show_arrow_up(self):
        self.arrow_direction = 'up'
        self.screen.blit(self.arrow_image, self.arrow_rect)

    def show_arrow_down(self):
        self.arrow_direction = 'down'
        self.screen.blit(self.arrow_image_down, self.arrow_rect_down)
