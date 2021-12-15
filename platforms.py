import pygame
from pygame.sprite import Sprite
from time import time

class PlatformRed(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.stats = UF_game.stats
        self.battle = UF_game.battle
        self.heart = UF_game.heart
        self.last_time = None

        self.times_moved = 0
        self.make_red_platform()

        self.x = float(self.rect.x)

    def make_red_platform(self):
        self.image = pygame.image.load('images/platform_red.png').convert_alpha()
        self.rect = self.image.get_rect()

    def locate_battle_rect_left(self):
        self.x = self.battle.rect.left
        self.rect.left = self.x
        self.rect.y = self.battle.rect.bottom - 120

    def move_plat_to_battle_center1(self):
        if self.rect.centerx <= self.battle.rect.centerx:
            self.x += 1
            self.rect.x = self.x
            if self.stats.platform_color == 'red':
                if self.rect.colliderect(self.heart):
                    self.heart.x += 2
                    self.heart.x2 += 2
                    self.heart.x3 += 2
                    self.heart.x4 += 2
    def move_plat_to_battle_center2(self):
        if self.rect.centerx <= self.battle.rect.centerx:
            self.x += 1
            self.rect.x = self.x

    def test_move1(self):
        if self.rect.centerx >= self.battle.rect.centerx - 25 and self.times_moved == 0:
            self.x -= 0.25
            self.rect.x = self.x
            if self.stats.platform_color == 'red':
                if self.rect.colliderect(self.heart):
                    self.heart.x -= 0.25
                    self.heart.x2 -= 0.25
                    self.heart.x3 -= 0.25
                    self.heart.x4 -= 0.25
        else:
            if self.times_moved == 0:
                self.times_moved = 1
            if self.rect.centerx <= self.battle.rect.centerx + 50 and self.times_moved == 1:
                self.x += 0.25
                self.rect.x = self.x
                if self.stats.platform_color == 'red':
                    if self.rect.colliderect(self.heart):
                        self.heart.x += 0.25
                        self.heart.x2 += 0.25
                        self.heart.x3 += 0.25
                        self.heart.x4 += 0.25
            else:
                if self.times_moved == 1:
                    self.times_moved = 2
                if self.rect.centerx >= self.battle.rect.centerx - 50 and self.times_moved == 2:
                    self.x -= 0.25
                    self.rect.x = self.x
                    if self.stats.platform_color == 'red':
                        if self.rect.colliderect(self.heart):
                            self.heart.x -= 0.25
                            self.heart.x2 -= 0.25
                            self.heart.x3 -= 0.25
                            self.heart.x4 -= 0.25
                else:
                    if self.times_moved == 2:
                        self.times_moved = 3
                    if self.rect.centerx <= self.battle.rect.centerx + 50 and self.times_moved == 3:
                        self.x += 0.25
                        self.rect.x = self.x
                        if self.stats.platform_color == 'red':
                            if self.rect.colliderect(self.heart):
                                self.heart.x += 0.25
                                self.heart.x2 += 0.25
                                self.heart.x3 += 0.25
                                self.heart.x4 += 0.25
                    else:
                        if self.times_moved == 3:
                            self.times_moved = 4
                        if self.rect.centerx >= self.battle.rect.centerx and self.times_moved == 4:
                            self.x -= 0.25
                            self.rect.x = self.x
                            if self.stats.platform_color == 'red':
                                if self.rect.colliderect(self.heart):
                                    self.heart.x -= 0.25
                                    self.heart.x2 -= 0.25
                                    self.heart.x3 -= 0.25
                                    self.heart.x4 -= 0.25
                        else:
                            if self.last_time is None:
                                self.last_time = time()
                            if time() - self.last_time >= 1.2:
                                self.times_moved = 0
                                self.stats.sans_amount += 1
                                self.last_time = None
    def test_move2(self):
        if self.rect.centerx >= self.battle.rect.centerx - 25 and self.times_moved == 0:
            self.x -= 0.25
            self.rect.x = self.x
        else:
            if self.times_moved == 0:
                self.times_moved = 1
            if self.rect.centerx <= self.battle.rect.centerx + 50 and self.times_moved == 1:
                self.x += 0.25
                self.rect.x = self.x
            else:
                if self.times_moved == 1:
                    self.times_moved = 2
                if self.rect.centerx >= self.battle.rect.centerx - 50 and self.times_moved == 2:
                    self.x -= 0.25
                    self.rect.x = self.x
                else:
                    if self.times_moved == 2:
                        self.times_moved = 3
                    if self.rect.centerx <= self.battle.rect.centerx + 50 and self.times_moved == 3:
                        self.x += 0.25
                        self.rect.x = self.x
                    else:
                        if self.times_moved == 3:
                            self.times_moved = 4
                        if self.rect.centerx >= self.battle.rect.centerx and self.times_moved == 4:
                            self.x -= 0.25
                            self.rect.x = self.x

    def move_platform_left1(self):
        if self.rect.centerx >= self.battle.rect.centerx - 125 and self.times_moved == 0:
            self.x -= 0.05
            self.rect.x = self.x
            if self.stats.platform_color == 'red':
                if self.rect.colliderect(self.heart):
                    self.heart.x -= 0.05
                    self.heart.x2 -= 0.05
                    self.heart.x3 -= 0.05
                    self.heart.x4 -= 0.05
    def move_platform_left2(self):
        if self.rect.centerx >= self.battle.rect.centerx - 125 and self.times_moved == 0:
            self.x -= 0.05
            self.rect.x = self.x

    def move_platform_left_right1(self):
        if self.times_moved == 0:
            self.times_moved = 1
        if self.rect.centerx <= self.battle.rect.centerx + 125 and self.times_moved == 1:
            self.x += 0.05
            self.rect.x = self.x
            if self.stats.platform_color == 'red':
                if self.rect.colliderect(self.heart):
                    self.heart.x += 0.05
                    self.heart.x2 += 0.05
                    self.heart.x3 += 0.05
                    self.heart.x4 += 0.05
        else:
            if self.times_moved == 1:
                self.times_moved = 2
            if self.rect.centerx >= self.battle.rect.centerx - 125 and self.times_moved == 2:
                self.x -= 0.05
                self.rect.x = self.x
                if self.stats.platform_color == 'red':
                    if self.rect.colliderect(self.heart):
                        self.heart.x -= 0.05
                        self.heart.x2 -= 0.05
                        self.heart.x3 -= 0.05
                        self.heart.x4 -= 0.05
            else:
                self.times_moved = 0
    def move_platform_left_right2(self):
        if self.times_moved == 0:
            self.times_moved = 1
        if self.rect.centerx <= self.battle.rect.centerx + 250 and self.times_moved == 1:
            self.x += 0.05
            self.rect.x = self.x
        else:
            if self.times_moved == 1:
                self.times_moved = 2
            if self.rect.centerx >= self.battle.rect.centerx - 250 and self.times_moved == 2:
                self.x -= 0.05
                self.rect.x = self.x
            else:
                self.times_moved = 0

class PlatformYellow(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.stats = UF_game.stats
        self.battle = UF_game.battle
        self.heart = UF_game.heart
        self.last_time = None

        self.times_moved = 0
        self.make_yellow_platform()

        self.x = float(self.rect.x)

    def make_yellow_platform(self):
        self.image = pygame.image.load('images/platform_yellow.png').convert_alpha()
        self.rect = self.image.get_rect()

    def locate_battle_rect_left(self):
        self.x = self.battle.rect.left
        self.rect.left = self.x
        self.rect.y = self.battle.rect.bottom - 120

    def move_plat_to_battle_center1(self):
        if self.rect.centerx <= self.battle.rect.centerx:
            self.x += 1
            self.rect.x = self.x
            if self.stats.platform_color == 'red':
                if self.rect.colliderect(self.heart):
                    self.heart.x += 2
                    self.heart.x2 += 2
                    self.heart.x3 += 2
                    self.heart.x4 += 2
    def move_plat_to_battle_center2(self):
        if self.rect.centerx <= self.battle.rect.centerx:
            self.x += 1
            self.rect.x = self.x

    def test_move1(self):
        if self.rect.centerx >= self.battle.rect.centerx - 25 and self.times_moved == 0:
            self.x -= 0.25
            self.rect.x = self.x
            if self.stats.platform_color == 'red':
                if self.rect.colliderect(self.heart):
                    self.heart.x -= 0.25
                    self.heart.x2 -= 0.25
                    self.heart.x3 -= 0.25
                    self.heart.x4 -= 0.25
        else:
            if self.times_moved == 0:
                self.times_moved = 1
            if self.rect.centerx <= self.battle.rect.centerx + 50 and self.times_moved == 1:
                self.x += 0.25
                self.rect.x = self.x
                if self.stats.platform_color == 'red':
                    if self.rect.colliderect(self.heart):
                        self.heart.x += 0.25
                        self.heart.x2 += 0.25
                        self.heart.x3 += 0.25
                        self.heart.x4 += 0.25
            else:
                if self.times_moved == 1:
                    self.times_moved = 2
                if self.rect.centerx >= self.battle.rect.centerx - 50 and self.times_moved == 2:
                    self.x -= 0.25
                    self.rect.x = self.x
                    if self.stats.platform_color == 'red':
                        if self.rect.colliderect(self.heart):
                            self.heart.x -= 0.25
                            self.heart.x2 -= 0.25
                            self.heart.x3 -= 0.25
                            self.heart.x4 -= 0.25
                else:
                    if self.times_moved == 2:
                        self.times_moved = 3
                    if self.rect.centerx <= self.battle.rect.centerx + 50 and self.times_moved == 3:
                        self.x += 0.25
                        self.rect.x = self.x
                        if self.stats.platform_color == 'red':
                            if self.rect.colliderect(self.heart):
                                self.heart.x += 0.25
                                self.heart.x2 += 0.25
                                self.heart.x3 += 0.25
                                self.heart.x4 += 0.25
                    else:
                        if self.times_moved == 3:
                            self.times_moved = 4
                        if self.rect.centerx >= self.battle.rect.centerx and self.times_moved == 4:
                            self.x -= 0.25
                            self.rect.x = self.x
                            if self.stats.platform_color == 'red':
                                if self.rect.colliderect(self.heart):
                                    self.heart.x -= 0.25
                                    self.heart.x2 -= 0.25
                                    self.heart.x3 -= 0.25
                                    self.heart.x4 -= 0.25
                        else:
                            if self.last_time is None:
                                self.last_time = time()
                            if time() - self.last_time >= 1.2:
                                self.times_moved = 0
                                self.last_time = None
    def test_move2(self):
        if self.rect.centerx >= self.battle.rect.centerx - 25 and self.times_moved == 0:
            self.x -= 0.25
            self.rect.x = self.x
        else:
            if self.times_moved == 0:
                self.times_moved = 1
            if self.rect.centerx <= self.battle.rect.centerx + 50 and self.times_moved == 1:
                self.x += 0.25
                self.rect.x = self.x
            else:
                if self.times_moved == 1:
                    self.times_moved = 2
                if self.rect.centerx >= self.battle.rect.centerx - 50 and self.times_moved == 2:
                    self.x -= 0.25
                    self.rect.x = self.x
                else:
                    if self.times_moved == 2:
                        self.times_moved = 3
                    if self.rect.centerx <= self.battle.rect.centerx + 50 and self.times_moved == 3:
                        self.x += 0.25
                        self.rect.x = self.x
                    else:
                        if self.times_moved == 3:
                            self.times_moved = 4
                        if self.rect.centerx >= self.battle.rect.centerx and self.times_moved == 4:
                            self.x -= 0.25
                            self.rect.x = self.x

    def move_platform_left1(self):
        if self.rect.centerx >= self.battle.rect.centerx - 125 and self.times_moved == 0:
            self.x -= 0.05
            self.rect.x = self.x
            if self.stats.platform_color == 'red':
                if self.rect.colliderect(self.heart):
                    self.heart.x -= 0.05
                    self.heart.x2 -= 0.05
                    self.heart.x3 -= 0.05
                    self.heart.x4 -= 0.05
    def move_platform_left2(self):
        if self.rect.centerx >= self.battle.rect.centerx - 125 and self.times_moved == 0:
            self.x -= 0.05
            self.rect.x = self.x

    def move_platform_left_right1(self):
        if self.times_moved == 0:
            self.times_moved = 1
        if self.rect.centerx <= self.battle.rect.centerx + 125 and self.times_moved == 1:
            self.x += 0.05
            self.rect.x = self.x
            if self.stats.platform_color == 'red':
                if self.rect.colliderect(self.heart):
                    self.heart.x += 0.05
                    self.heart.x2 += 0.05
                    self.heart.x3 += 0.05
                    self.heart.x4 += 0.05
        else:
            if self.times_moved == 1:
                self.times_moved = 2
            if self.rect.centerx >= self.battle.rect.centerx - 125 and self.times_moved == 2:
                self.x -= 0.05
                self.rect.x = self.x
                if self.stats.platform_color == 'red':
                    if self.rect.colliderect(self.heart):
                        self.heart.x -= 0.05
                        self.heart.x2 -= 0.05
                        self.heart.x3 -= 0.05
                        self.heart.x4 -= 0.05
            else:
                self.times_moved = 0
    def move_platform_left_right2(self):
        if self.times_moved == 0:
            self.times_moved = 1
        if self.rect.centerx <= self.battle.rect.centerx + 125 and self.times_moved == 1:
            self.x += 0.05
            self.rect.x = self.x
        else:
            if self.times_moved == 1:
                self.times_moved = 2
            if self.rect.centerx >= self.battle.rect.centerx - 125 and self.times_moved == 2:
                self.x -= 0.05
                self.rect.x = self.x
            else:
                self.times_moved = 0
