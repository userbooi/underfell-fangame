import pygame
from pygame.sprite import Sprite

class Attacks(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.bone_down_visibility = False
        self.set_loco_now = False
        self.battlebox = UF_game.battle
        self.heart = UF_game.heart

        self.slam_down_bones()

        self.x = float(self.rect.x)

    def slam_down_bones(self):
        self.image = pygame.image.load('images/single_bone.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (23, 80)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.battlebox.rect.x
        self.rect.bottom = self.battlebox.rect.bottom - 12

    def move_bone_right_slow(self):
        if self.set_loco_now is False:
            self.x = float(self.rect.x)
            self.set_loco_now = True

        self.x += 0.08
        self.rect.x = self.x
