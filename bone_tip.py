import pygame
from pygame.sprite import Sprite

class BoneTip(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.bone_stem = UF_game.fullbone

        self.reset_posed_x = False
        self.reset_posed_y = False

        self.make_tip()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x2 = float(self.rect.x)
        self.y2 = float(self.rect.y)

    def make_tip(self):
        self.image = pygame.image.load('images/bone_tip.png')
        self.rect = self.image.get_rect()

    def update_top_bone_bl(self):
        if self.reset_posed_y == False:
            self.y = float(self.rect.y)
            self.reset_posed_y = True

        self.y += 0.5

        self.rect.y = self.y

    def update_right_bone_bl(self):
        if self.reset_posed_x == False:
            self.x = float(self.rect.x)
            self.reset_posed_x = True

        self.x -= 0.5

        self.rect.x = self.x

    def update_right_bone_in(self):
        if self.reset_posed_x == False:
            self.x = float(self.rect.x)
            self.reset_posed_x = True

        self.x -= 0.3

        self.rect.x = self.x

    def update_left_bone_in(self):
        if self.reset_posed_x == False:
            self.x2 = float(self.rect.x)
            self.reset_posed_x = True

        self.x2 += 0.3

        self.rect.x = self.x2

    def update_right_bone_in2(self):
        if self.reset_posed_x == False:
            self.x = float(self.rect.x)
            self.reset_posed_x = True

        self.x -= 0.47

        self.rect.x = self.x

    def update_left_bone_in2(self):
        if self.reset_posed_x == False:
            self.x2 = float(self.rect.x)
            self.reset_posed_x = True

        self.x2 += 0.47

        self.rect.x = self.x2

    def update_up_bones_going_left(self):
        if self.reset_posed_x is False:
            self.x = float(self.rect.x)
            self.reset_posed_x = True

        self.x -= 0.5

        self.rect.x = self.x

class BlueBoneTip(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.bone_stem = UF_game.fullbone

        self.reset_posed_x = False
        self.reset_posed_y = False

        self.make_tip()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def make_tip(self):
        self.image = pygame.image.load('images/blue_bone_tip.png')
        self.rect = self.image.get_rect()

class OrangeBoneTip(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.bone_stem = UF_game.fullbone

        self.reset_posed_x = False
        self.reset_posed_y = False

        self.make_tip()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def make_tip(self):
        self.image = pygame.image.load('images/orange_bone_tip.png')
        self.rect = self.image.get_rect()
