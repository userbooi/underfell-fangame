import pygame


class Player_heart:

    def __init__(self, UF_game):
        self.fall = 0
        self.screen = UF_game.screen
        self.screen_rect = UF_game.screen.get_rect()
        self.battlebox = UF_game.battle
        self.setting = UF_game.settings
        self.stats = UF_game.stats
        self.slam = UF_game.slam
        self.platformrs = pygame.sprite.Group()
        self.platformys = pygame.sprite.Group()

        self.make_red_heart()
        self.make_blue_heart()
        self.make_blue_heart_left()
        self.make_blue_heart_right()
        self.make_blue_heart_down()
        self.warnings()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.jump = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.y2 = float(self.blue_rect.y)
        self.x2 = float(self.blue_rect.x)
        self.y3 = float(self.rect2.y)
        self.x3 = float(self.rect2.x)
        self.y4 = float(self.rect3.y)
        self.x4 = float(self.rect3.x)
        self.x5 = float(self.rect4.x)
        self.y5 = float(self.rect4.y)
        self.add = 0
        self.heart_direction = 'up'

    def make_red_heart(self):
        self.image = pygame.image.load('images/playerheart.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = self.battlebox.rect.center

    def make_blue_heart_left(self):
        self.image2 = pygame.image.load('images/playerheart_blue.png').convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (32, 32)).convert_alpha()
        self.image2 = pygame.transform.rotozoom(self.image2, -90, 1).convert_alpha()
        self.rect2 = self.image2.get_rect()

        self.rect2.center = self.battlebox.rect.center

    def make_blue_heart_right(self):
        self.image3 = pygame.image.load('images/playerheart_blue.png').convert_alpha()
        self.image3 = pygame.transform.scale(self.image3, (32, 32)).convert_alpha()
        self.image3 = pygame.transform.rotozoom(self.image3, 90, 1).convert_alpha()
        self.rect3 = self.image3.get_rect()

        self.rect3.center = self.battlebox.rect.center

    def make_blue_heart_down(self):
        self.image4 = pygame.image.load('images/playerheart_blue.png').convert_alpha()
        self.image4 = pygame.transform.scale(self.image4, (32, 32)).convert_alpha()
        self.image4 = pygame.transform.rotozoom(self.image4, 180, 1)
        self.rect4 = self.image4.get_rect()

        self.rect4.center = self.battlebox.rect.center

    def make_blue_heart(self):
        self.blue_image = pygame.image.load('images/playerheart_blue.png').convert_alpha()
        self.blue_image = pygame.transform.scale(self.blue_image, (32, 32)).convert_alpha()
        self.blue_rect = self.blue_image.get_rect()

        self.blue_rect.center = self.battlebox.rect.center

    def warnings(self):
        self.warning = pygame.image.load('images/warning.png').convert_alpha()
        self.warning = pygame.transform.scale(self.warning, (270, 80)).convert_alpha()

        self.warning_rect = self.warning.get_rect()
        self.warning_rect.center = self.battlebox.rect.center
        self.warning_rect.y += 80

    def gravity(self):
        if self.heart_direction == 'down':
            if self.rect.top == self.battlebox.rect.top:
                self.add = 0
                self.fall = 0.05
            if self.rect.top != self.battlebox.rect.top and self.jump is True:
                if self.add == 0:
                    self.fall = 0.019
                if self.fall >= 0.019:
                    self.add += 1
                    self.fall += 0.0015
            if self.rect.top > self.battlebox.rect.top:
                self.y -= self.fall
                self.y2 -= self.fall
                self.y3 -= self.fall
                self.y4 -= self.fall
                self.y5 -= self.fall
                if self.jump == False and self.fall <= self.setting.heart_speed + 0.43:
                    self.fall += 0.0021
                else:
                    self.jump = True
            else:
                self.rect.top = self.battlebox.rect.top
                self.blue_rect.top = self.battlebox.rect.top
                self.rect2.top = self.battlebox.rect.top
                self.rect3.top = self.battlebox.rect.top
                self.rect4.top = self.battlebox.rect.top
        elif self.heart_direction == 'up':
            if pygame.sprite.spritecollideany(self, self.platformrs) or pygame.sprite.spritecollideany(self, self.platformys):
                for platformr in self.platformrs:
                    if self.rect.bottom == platformr.rect.bottom - 15:
                        self.add = 0
                        self.fall = 0.05
                for platformr in self.platformrs:
                    if self.rect.bottom < platformr.rect.bottom - 15:
                        self.y += self.fall
                        self.y2 += self.fall
                        self.y3 += self.fall
                        self.y4 += self.fall
                        self.y5 += self.fall
                        if self.jump == False and self.fall <= self.setting.heart_speed + 0.43:
                            self.fall += 0.0021
                        else:
                            self.jump = True
                    else:
                        self.rect.bottom = platformr.rect.bottom - 15
                        self.blue_rect.bottom = platformr.rect.bottom - 15
                        self.rect2.bottom = platformr.rect.bottom - 15
                        self.rect3.bottom = platformr.rect.bottom - 15
                        self.rect4.bottom = platformr.rect.bottom - 15
            else:
                if self.rect.bottom == self.battlebox.rect.bottom:
                    self.add = 0
                    self.fall = 0.05
                if self.rect.bottom != self.battlebox.rect.bottom and self.jump == True:
                    if self.add == 0:
                        self.fall = 0.019
                    if self.fall >= 0.019:
                        self.add += 1
                        self.fall += 0.0015
                if self.rect.bottom < self.battlebox.rect.bottom:
                    self.y += self.fall
                    self.y2 += self.fall
                    self.y3 += self.fall
                    self.y4 += self.fall
                    self.y5 += self.fall
                    if self.jump == False and self.fall <= self.setting.heart_speed + 0.43:
                        self.fall += 0.0021
                    else:
                        self.jump = True
                else:
                    self.rect.bottom = self.battlebox.rect.bottom
                    self.blue_rect.bottom = self.battlebox.rect.bottom
                    self.rect2.bottom = self.battlebox.rect.bottom
                    self.rect3.bottom = self.battlebox.rect.bottom
                    self.rect4.bottom = self.battlebox.rect.bottom
        elif self.heart_direction == 'left':
            if self.rect.left == self.battlebox.rect.left:
                self.add = 0
                self.fall = 0.05
            if self.rect.left != self.battlebox.rect.left and self.jump == True:
                if self.add == 0:
                    self.fall = 0.019
                if self.fall >= 0.019:
                    self.add += 1
                    self.fall += 0.0015
            if self.rect.left > self.battlebox.rect.left:
                self.x -= self.fall
                self.x2 -= self.fall
                self.x3 -= self.fall
                self.x4 -= self.fall
                self.x5 -= self.fall
                if self.jump == False and self.fall <= self.setting.heart_speed + 0.43:
                    self.fall += 0.0021
                else:
                    self.jump = True
            else:
                self.rect.left = self.battlebox.rect.left
                self.blue_rect.left = self.battlebox.rect.left
                self.rect2.left = self.battlebox.rect.left
                self.rect3.left = self.battlebox.rect.left
                self.rect4.left = self.battlebox.rect.left
        elif self.heart_direction == 'right':
            if self.rect.right == self.battlebox.rect.right:
                self.add = 0
                self.fall = 0.05
            if self.rect.right != self.battlebox.rect.right and self.jump == True:
                if self.add == 0:
                    self.fall = 0.019
                if self.fall >= 0.019:
                    self.add += 1
                    self.fall += 0.0015
            if self.rect.right < self.battlebox.rect.right:
                self.x += self.fall
                self.x2 += self.fall
                self.x3 += self.fall
                self.x4 += self.fall
                self.x5 += self.fall
                if self.jump == False and self.fall <= self.setting.heart_speed + 0.43:
                    self.fall += 0.0021
                else:
                    self.jump = True
            else:
                self.rect.right = self.battlebox.rect.right
                self.blue_rect.right = self.battlebox.rect.right
                self.rect2.right = self.battlebox.rect.right
                self.rect3.right = self.battlebox.rect.right
                self.rect4.right = self.battlebox.rect.right

    def gravity_instant(self):
        if self.heart_direction == 'up':
            if self.rect.bottom < self.battlebox.rect.bottom or self.blue_rect.bottom < self.battlebox.rect.bottom or self.rect2.bottom < self.battlebox.rect.bottom or self.rect3.bottom < self.battlebox.rect.bottom:
                self.y += 4
                self.y2 += 4
                self.y3 += 4
                self.y4 += 4
                self.y5 += 4
            else:
                self.rect.bottom = self.battlebox.rect.bottom
                self.blue_rect.bottom = self.battlebox.rect.bottom
                self.rect2.bottom = self.battlebox.rect.bottom
                self.rect3.bottom = self.battlebox.rect.bottom
                self.rect4.bottom = self.battlebox.rect.bottom
        elif self.heart_direction == 'down':
            if self.rect.top > self.battlebox.rect.top or self.blue_rect.top > self.battlebox.rect.top or self.rect2.top > self.battlebox.rect.top or self.rect3.top < self.battlebox.rect.top:
                self.y -= 4
                self.y2 -= 4
                self.y3 -= 4
                self.y4 -= 4
                self.y5 -= 4
            else:
                self.rect.top = self.battlebox.rect.top
                self.blue_rect.top = self.battlebox.rect.top
                self.rect2.top = self.battlebox.rect.top
                self.rect3.top = self.battlebox.rect.top
                self.rect4.top = self.battlebox.rect.top

        elif self.heart_direction == 'left':
            if self.rect.left > self.battlebox.rect.left or self.blue_rect.left > self.battlebox.rect.left or self.rect2.left > self.battlebox.rect.left or self.rect3.left > self.battlebox.rect.left:
                self.x -= 4
                self.x2 -= 4
                self.x3 -= 4
                self.x4 -= 4
                self.x5 -= 4
            else:
                self.rect.left = self.battlebox.rect.left
                self.blue_rect.left = self.battlebox.rect.left
                self.rect2.left = self.battlebox.rect.left
                self.rect3.left = self.battlebox.rect.left
                self.rect4.left = self.battlebox.rect.left
        elif self.heart_direction == 'right':
            if self.rect.right < self.battlebox.rect.right or self.blue_rect.right < self.battlebox.rect.right:
                self.x += 4
                self.x2 += 4
                self.x3 += 4
                self.x4 += 4
                self.x5 += 4
            else:
                self.rect.right = self.battlebox.rect.right
                self.blue_rect.right = self.battlebox.rect.right
                self.rect2.right = self.battlebox.rect.right
                self.rect3.right = self.battlebox.rect.right
                self.rect4.right = self.battlebox.rect.right

    def update_red(self):
        if self.moving_right and self.rect.right < self.battlebox.rect.right:
            self.x += self.setting.heart_speed
            self.x2 += self.setting.heart_speed
            self.x3 += self.setting.heart_speed
            self.x4 += self.setting.heart_speed
            self.x5 += self.setting.heart_speed
        if self.moving_left and self.rect.left > self.battlebox.rect.left:
            self.x -= self.setting.heart_speed
            self.x2 -= self.setting.heart_speed
            self.x3 -= self.setting.heart_speed
            self.x4 -= self.setting.heart_speed
            self.x5 -= self.setting.heart_speed
        if self.moving_up and self.rect.top > self.battlebox.rect.top:
            self.y -= self.setting.heart_speed
            self.y2 -= self.setting.heart_speed
            self.y3 -= self.setting.heart_speed
            self.y4 -= self.setting.heart_speed
            self.y5 -= self.setting.heart_speed
        if self.moving_down and self.rect.bottom < self.battlebox.rect.bottom:
            self.y += self.setting.heart_speed
            self.y2 += self.setting.heart_speed
            self.y3 += self.setting.heart_speed
            self.y4 += self.setting.heart_speed
            self.y5 += self.setting.heart_speed

        self.rect.x = self.x
        self.rect.y = self.y
        self.blue_rect.x = self.x2
        self.blue_rect.y = self.y2
        self.rect2.x = self.x3
        self.rect2.y = self.y3
        self.rect3.x = self.x4
        self.rect3.y = self.y4
        self.rect4.x = self.x5
        self.rect4.y = self.y5

    def update_blue(self):
        if self.moving_right:
            if self.heart_direction == 'up' and self.rect.right < self.battlebox.rect.right and self.blue_rect.right < self.battlebox.rect.right:
                self.x += self.setting.heart_speed
                self.x2 += self.setting.heart_speed
                self.x3 += self.setting.heart_speed
                self.x4 += self.setting.heart_speed
                self.x5 += self.setting.heart_speed
            elif self.heart_direction == 'left' and self.rect.right < self.battlebox.rect.right and self.blue_rect.right < self.battlebox.rect.right and self.jump == False:
                self.x += self.setting.heart_speed + 0.43
                self.x2 += self.setting.heart_speed + 0.43
                self.x3 += self.setting.heart_speed + 0.43
                self.x4 += self.setting.heart_speed + 0.43
                self.x5 += self.setting.heart_speed + 0.43
            elif self.heart_direction == 'down' and self.rect.right < self.battlebox.rect.right and self.blue_rect.right < self.battlebox.rect.right:
                self.x += self.setting.heart_speed
                self.x2 += self.setting.heart_speed
                self.x3 += self.setting.heart_speed
                self.x4 += self.setting.heart_speed
                self.x5 += self.setting.heart_speed
        if self.moving_left:
            if self.heart_direction == 'up' and self.rect.left > self.battlebox.rect.left and self.blue_rect.left > self.battlebox.rect.left:
                self.x -= self.setting.heart_speed
                self.x2 -= self.setting.heart_speed
                self.x3 -= self.setting.heart_speed
                self.x4 -= self.setting.heart_speed
                self.x5 -= self.setting.heart_speed
            elif self.heart_direction == 'right' and self.rect.left > self.battlebox.rect.left and self.blue_rect.left > self.battlebox.rect.left and self.jump == False:
                self.x -= self.setting.heart_speed + 0.43
                self.x2 -= self.setting.heart_speed + 0.43
                self.x3 -= self.setting.heart_speed + 0.43
                self.x4 -= self.setting.heart_speed + 0.43
                self.x5 -= self.setting.heart_speed + 0.43
            elif self.heart_direction == 'down' and self.rect.left > self.battlebox.rect.left and self.blue_rect.left > self.battlebox.rect.left:
                self.x -= self.setting.heart_speed
                self.x2 -= self.setting.heart_speed
                self.x3 -= self.setting.heart_speed
                self.x4 -= self.setting.heart_speed
                self.x5 -= self.setting.heart_speed
        if self.moving_up:
            if self.heart_direction == 'up' and self.rect.top > self.battlebox.rect.top and self.blue_rect.top > self.battlebox.rect.top and self.jump == False:
                self.y -= self.setting.heart_speed + 0.43
                self.y2 -= self.setting.heart_speed + 0.43
                self.y3 -= self.setting.heart_speed + 0.43
                self.y4 -= self.setting.heart_speed + 0.43
                self.y5 -= self.setting.heart_speed + 0.43
            elif self.heart_direction == 'left' and self.rect.top > self.battlebox.rect.top and self.blue_rect.top > self.battlebox.rect.top:
                self.y -= self.setting.heart_speed
                self.y2 -= self.setting.heart_speed
                self.y3 -= self.setting.heart_speed
                self.y4 -= self.setting.heart_speed
                self.y5 -= self.setting.heart_speed
            elif self.heart_direction == 'right' and self.rect.top > self.battlebox.rect.top and self.blue_rect.top > self.battlebox.rect.top:
                self.y -= self.setting.heart_speed
                self.y2 -= self.setting.heart_speed
                self.y3 -= self.setting.heart_speed
                self.y4 -= self.setting.heart_speed
                self.y5 -= self.setting.heart_speed
        if self.moving_down:
            if self.heart_direction == 'left' and self.rect.bottom < self.battlebox.rect.bottom and self.blue_rect.bottom < self.battlebox.rect.bottom:
                self.y += self.setting.heart_speed
                self.y2 += self.setting.heart_speed
                self.y3 += self.setting.heart_speed
                self.y4 += self.setting.heart_speed
                self.y5 += self.setting.heart_speed
            elif self.heart_direction == 'right' and self.rect.bottom < self.battlebox.rect.bottom and self.blue_rect.bottom < self.battlebox.rect.bottom:
                self.y += self.setting.heart_speed
                self.y2 += self.setting.heart_speed
                self.y3 += self.setting.heart_speed
                self.y4 += self.setting.heart_speed
                self.y5 += self.setting.heart_speed
            elif self.heart_direction == 'down' and self.rect.bottom < self.battlebox.rect.bottom and self.blue_rect.bottom < self.battlebox.rect.bottom and self.jump != True:
                self.y += self.setting.heart_speed + 0.43
                self.y2 += self.setting.heart_speed + 0.43
                self.y3 += self.setting.heart_speed + 0.43
                self.y4 += self.setting.heart_speed + 0.43
                self.y5 += self.setting.heart_speed + 0.43

        self.rect.x = self.x
        self.rect.y = self.y
        self.blue_rect.x = self.x2
        self.blue_rect.y = self.y2
        self.rect2.x = self.x3
        self.rect2.y = self.y3
        self.rect3.x = self.x4
        self.rect3.y = self.y4
        self.rect4.x = self.x5
        self.rect4.y = self.y5

    def reset_pos(self):
        self.rect.center = self.battlebox.rect.center
        self.blue_rect.center = self.battlebox.rect.center
        self.rect2.center = self.battlebox.rect.center
        self.rect3.center = self.battlebox.rect.center
        self.rect4.center = self.battlebox.rect.center
        self.rect4.center = self.battlebox.rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.y2 = float(self.blue_rect.y)
        self.x2 = float(self.blue_rect.x)
        self.x3 = float(self.rect2.x)
        self.y3 = float(self.rect2.y)
        self.x4 = float(self.rect3.x)
        self.y4 = float(self.rect3.y)
        self.x5 = float(self.rect4.x)
        self.y5 = float(self.rect4.y)

    def blitred(self):
        self.screen.blit(self.image, self.rect)

    def blitblue(self):
        if self.heart_direction == 'up':
            self.screen.blit(self.blue_image, self.blue_rect)
        elif self.heart_direction == 'left':
            self.screen.blit(self.image2, self.rect2)
        elif self.heart_direction == 'right':
            self.screen.blit(self.image3, self.rect3)
        elif self.heart_direction == 'down':
            self.screen.blit(self.image4, self.rect4)
