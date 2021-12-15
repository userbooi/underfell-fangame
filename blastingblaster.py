import pygame
from pygame.sprite import Sprite

class FellBlasted(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.battlebox = UF_game.battle

        self.blasting_blaster()

    def blasting_blaster(self):
        self.image = pygame.image.load('images/fellblasterblast.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (166, 196)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 583
        self.rect.y = 75
