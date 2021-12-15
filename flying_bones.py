import pygame
from pygame.sprite import Sprite

class FlyingBones(Sprite):
    def __init__(self, UF_game):
        super().__init__()
        self.flyingbone_right_spin_degree = 0

        self.heart = UF_game.heart
        self.battle = UF_game.battle

        self.make_flying_bone()

    def make_flying_bone(self):
        self.before_image = pygame.image.load('images/flying_bone.png').convert_alpha()
        self.before_rect = self.before_image.get_rect()

        self.image = self.before_image.convert_alpha()
        self.rect = self.image.get_rect()

    def turn_flyingbone_right(self):
        self.flyingbone_right_spin_degree += 0.5
        self.image = pygame.transform.rotozoom(self.before_image, self.flyingbone_right_spin_degree, 1)
        self.rect = self.image.get_rect()
        self.rect.y = self.heart.rect.y
        self.rect.left = self.battle.rect.right + 15

class FlyingBonesLeft(Sprite):
    def __init__(self, UF_game):
        super().__init__()
        self.flyingbone_left_spin_degree = 0

        self.heart = UF_game.heart
        self.battle = UF_game.battle

        self.make_flying_bone()

    def make_flying_bone(self):
        self.before_image = pygame.image.load('images/flying_bone.png').convert_alpha()
        self.before_rect = self.before_image.get_rect()

        self.image = self.before_image.convert_alpha()
        self.rect = self.image.get_rect()

    def turn_flyingbone_left(self):
        self.flyingbone_left_spin_degree += 0.5
        self.image = pygame.transform.rotozoom(self.before_image, self.flyingbone_left_spin_degree, 1)
        self.rect = self.image.get_rect()
        self.rect.y = self.heart.rect.y
        self.rect.right = self.battle.rect.left - 15

class FlyingBonesTop(Sprite):
    def __init__(self, UF_game):
        super().__init__()
        self.flyingbone_top_spin_degree = 0

        self.heart = UF_game.heart
        self.battle = UF_game.battle

        self.make_flying_bone()

    def make_flying_bone(self):
        self.before_image = pygame.image.load('images/flying_bone.png').convert_alpha()
        self.before_rect = self.before_image.get_rect()

        self.image = self.before_image.convert_alpha()
        self.rect = self.image.get_rect()

    def turn_flyingbone_top(self):
        self.flyingbone_top_spin_degree += 0.5
        self.image = pygame.transform.rotozoom(self.before_image, 90 + self.flyingbone_top_spin_degree, 1)
        self.rect = self.image.get_rect()
        self.rect.x = self.heart.rect.x
        self.rect.bottom = self.battle.rect.top - 15

class FlyingBonesBottom(Sprite):
    def __init__(self, UF_game):
        super().__init__()
        self.flyingbone_bottom_spin_degree = 0

        self.heart = UF_game.heart
        self.battle = UF_game.battle

        self.make_flying_bone()

    def make_flying_bone(self):
        self.before_image = pygame.image.load('images/flying_bone.png').convert_alpha()
        self.before_rect = self.before_image.get_rect()

        self.image = self.before_image.convert_alpha()
        self.rect = self.image.get_rect()

    def turn_flyingbone_bottom(self):
        self.flyingbone_bottom_spin_degree += 0.5
        self.image = pygame.transform.rotozoom(self.before_image, 90 + self.flyingbone_bottom_spin_degree, 1)
        self.rect = self.image.get_rect()
        self.rect.x = self.heart.rect.x
        self.rect.top = self.battle.rect.bottom + 15

