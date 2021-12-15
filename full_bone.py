import pygame
from pygame.sprite import Sprite

class FullBone(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.battlebox = UF_game.battle

        self.reset_posed_x = False
        self.reset_posed_y = False

        self.full_bone()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x2 = float(self.rect.x)
        self.y2 = float(self.rect.y)

    def full_bone(self):
        self.image = pygame.image.load('images/full_bone.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 310)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = self.battlebox.rect.right
        self.rect.centery = self.battlebox.rect.centery

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

class BlueBoneStem(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.battlebox = UF_game.battle

        self.reset_posed_x = False
        self.reset_posed_y = False

        self.full_bone()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def full_bone(self):
        self.image = pygame.image.load('images/blue_bone_stem.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 310)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = self.battlebox.rect.right
        self.rect.centery = self.battlebox.rect.centery

class OrangeBoneStem(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.battlebox = UF_game.battle

        self.reset_posed_x = False
        self.reset_posed_y = False

        self.full_bone()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def full_bone(self):
        self.image = pygame.image.load('images/orange_bone_stem.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 310)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = self.battlebox.rect.right
        self.rect.centery = self.battlebox.rect.centery
