import pygame
from pygame.sprite import Sprite

class BlastBeam(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.battlebox = UF_game.battle
        self.settings = UF_game.settings

        self.create_beam()

    def create_beam(self):
        self.image = pygame.image.load('images/blastbeam.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 600)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.battlebox.rect.centerx - 9
        self.rect.centery = self.screen_rect.centery + 20
