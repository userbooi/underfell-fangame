import pygame
from time import time

class SANNESS:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.heart = ai_game.heart
        self.box = ai_game.battle
        self.slam = ai_game.slam
        self.stats = ai_game.stats

        self.last_time = None
        self.last_time2 = None
        self.last_time3 = None
        self.last_time4 = None
        self.last_time5 = None
        self.last_time6 = None
        self.fade_delay = None
        self.fade_value = 0
        self.times_moved = 0

        self.make_sans_closed()
        self.make_sans_no_glow()
        self.make_sans_no_glow_drop1()
        self.make_sans_no_glow_drop2()
        self.make_crazy_sans_glow_slamdown()
        self.make_normal_sans_slamdown()
        self.make_normal_sans_slamup()
        self.make_normal_sans_slamleft()
        self.make_crazy_sans_glow_slamup()
        self.make_sans_glow()
        self.make_sans_no_glow_shrug()
        self.make_sans_normal()
        self.make_shocked_sans()
        self.make_downed_sans()
        self.make_pleased_sans()
        self.make_tired_killed_sans()
        self.make_almost_dead_sans()
        self.make_dead_sans()
        self.make_normal_eyes_closed_sans()
        self.make_normal_sans_confused()
        self.make_normal_sans_glow()
        self.make_normal_sans_look_right()
        self.make_normal_sans_no_glow()
        self.make_normal_sans_a_bit_tired()
        self.make_normal_sans_tired_shrug()
        self.make_confused_sans_a_bit_tired()
        self.make_normal_sans_quite_tired()
        self.make_normal_sans_very_tired()
        self.make_normal_sans_sleeping()
        self.make_normal_sans_a_bit_tired2()
        self.make_normal_sans_a_bit_tired_eyes_closed()
        self.make_angry_sans_eyes_closed()
        self.make_angry_crazy_sans_no_glow()
        self.make_angry_crazy_sans_glow()
        self.make_angry_crazy_sans_glow_with_gaster()
        self.make_angry_crazy_sans_glow_with_gaster_slamup()
        self.make_angry_crazy_sans_glow_with_gaster_slamdown()
        self.make_angry_crazy_sans_glow_with_gaster_slamright()
        self.make_difficult_angry_crazy_sans_glow_with_gaster_slamdown()
        self.make_a_bit_tired_angry_crazy_sans_glow_with_gaster()
        self.make_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamright()
        self.make_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamup()
        self.make_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamdown()
        self.make_tired_angry_crazy_sans_glow_with_gaster()
        self.make_quite_tired_angry_crazy_sans_glow_with_gaster()
        self.make_really_tired_angry_crazy_sans_glow_with_gaster()
        self.make_really_tired_normal_sans()
        self.make_really_tired_normal_sans_smile()
        self.make_happy_sans_red()
        self.make_happy_sans_white()
        self.make_fade()
        self.sd_warning()

        self.x = float(self.rect10.x)

    def sd_warning(self):
        self.screen.blit(self.heart.warning, self.heart.warning_rect)

    def make_sans_closed(self):
        self.image = pygame.image.load('images/sans_eyes_closed.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (210, 285)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = -5

    def make_sans_no_glow(self):
        self.image2_ = pygame.image.load('images/crazy_sans_no_glow.png').convert_alpha()
        self.image2_ = pygame.transform.scale(self.image2_, (210, 285)).convert_alpha()
        self.rect2_ = self.image2_.get_rect()

        self.rect2_.centerx = self.screen_rect.centerx
        self.rect2_.y = -5

    def make_crazy_sans_glow_slamdown(self):
        self.image3 = pygame.image.load('images/crazy_sans_slamdown.png').convert_alpha()
        self.image3 = pygame.transform.scale(self.image3, (210, 285)).convert_alpha()
        self.rect3 = self.image3.get_rect()

        self.rect3.centerx = self.screen_rect.centerx
        self.rect3.y = -5

    def make_normal_sans_slamdown(self):
        self.image18 = pygame.image.load('images/normal_sans_slamdown.png').convert_alpha()
        self.image18 = pygame.transform.scale(self.image18, (210, 285)).convert_alpha()
        self.rect18 = self.image18.get_rect()

        self.rect18.centerx = self.screen_rect.centerx
        self.rect18.y = -5

    def make_crazy_sans_glow_slamup(self):
        self.image17 = pygame.image.load('images/crazy_sans_slamup.png').convert_alpha()
        self.image17 = pygame.transform.scale(self.image17, (210, 285)).convert_alpha()
        self.rect17 = self.image17.get_rect()

        self.rect17.centerx = self.screen_rect.centerx
        self.rect17.y = -5

    def make_normal_sans_slamup(self):
        self.image19 = pygame.image.load('images/normal_sans_slamup.png').convert_alpha()
        self.image19 = pygame.transform.scale(self.image19, (210, 285)).convert_alpha()
        self.rect19 = self.image19.get_rect()

        self.rect19.centerx = self.screen_rect.centerx
        self.rect19.y = -5

    def make_normal_sans_slamleft(self):
        self.image20 = pygame.image.load('images/normal_sans_slamright.png')
        self.image20 = pygame.transform.scale(self.image20, (260, 285))
        self.rect20 = self.image20.get_rect()

        self.rect20.centerx = self.screen_rect.centerx + 25
        self.rect20.y = -5

    def make_sans_glow(self):
        self.image4 = pygame.image.load('images/crazy_sans.png').convert_alpha()
        self.image4 = pygame.transform.scale(self.image4, (210, 285)).convert_alpha()
        self.rect4 = self.image4.get_rect()

        self.rect4.centerx = self.screen_rect.centerx
        self.rect4.y = -5

    def make_sans_no_glow_drop1(self):
        self.image5 = pygame.image.load('images/crazy_sans_no_glow_drop1.png').convert_alpha()
        self.image5 = pygame.transform.scale(self.image5, (210, 285)).convert_alpha()
        self.rect5 = self.image5.get_rect()

        self.rect5.centerx = self.screen_rect.centerx
        self.rect5.y = -5

    def make_sans_no_glow_drop2(self):
        self.image6 = pygame.image.load('images/crazy_sans_no_glow_drop2.png').convert_alpha()
        self.image6 = pygame.transform.scale(self.image6, (210, 285)).convert_alpha()
        self.rect6 = self.image6.get_rect()

        self.rect6.centerx = self.screen_rect.centerx
        self.rect6.y = -5

    def make_sans_no_glow_shrug(self):
        self.image7 = pygame.image.load('images/sans_no_glow_shrug.png').convert_alpha()
        self.image7 = pygame.transform.scale(self.image7, (245, 285)).convert_alpha()
        self.rect7 = self.image7.get_rect()

        self.rect7.centerx = self.screen_rect.centerx
        self.rect7.y = 0

    def make_sans_normal(self):
        self.image8 = pygame.image.load('images/underfell_sans.png').convert_alpha()
        self.image8 = pygame.transform.scale(self.image8, (210, 285)).convert_alpha()
        self.rect8 = self.image8.get_rect()

        self.rect8.centerx = self.screen_rect.centerx
        self.rect8.y = -5

    def make_shocked_sans(self):
        self.image9 = pygame.image.load('images/shocked_sans.png').convert_alpha()
        self.image9 = pygame.transform.scale(self.image9, (210, 285)).convert_alpha()
        self.rect9 = self.image9.get_rect()

        self.rect9.centerx = self.screen_rect.centerx
        self.rect9.y = -5

    def make_downed_sans(self):
        self.image10 = pygame.image.load('images/sans_down.png').convert_alpha()
        self.image10 = pygame.transform.scale(self.image10, (235, 285)).convert_alpha()
        self.rect10 = self.image10.get_rect()

        self.rect10.centerx = self.screen_rect.centerx
        self.rect10.y = -5

    def make_pleased_sans(self):
        self.image11 = pygame.image.load('images/pleased_sans.png').convert_alpha()
        self.image11 = pygame.transform.scale(self.image11, (235, 285)).convert_alpha()
        self.rect11 = self.image11.get_rect()

        self.rect11.centerx = self.screen_rect.centerx
        self.rect11.y = -5

    def make_tired_killed_sans(self):
        self.image12 = pygame.image.load('images/killed_sans_tired.png').convert_alpha()
        self.image12 = pygame.transform.scale(self.image12, (235, 285)).convert_alpha()
        self.rect12 = self.image12.get_rect()

        self.rect12.centerx = self.screen_rect.centerx
        self.rect12.y = -5

    def make_almost_dead_sans(self):
        self.image13 = pygame.image.load('images/killed_sans_about_dead.png').convert_alpha()
        self.image13 = pygame.transform.scale(self.image13, (235, 285)).convert_alpha()
        self.rect13 = self.image13.get_rect()

        self.rect13.centerx = self.screen_rect.centerx
        self.rect13.y = -5

    def make_dead_sans(self):
        self.image14 = pygame.image.load('images/killed_sans_dead.png').convert_alpha()
        self.image14 = pygame.transform.scale(self.image14, (235, 285)).convert_alpha()
        self.rect14 = self.image14.get_rect()

        self.rect14.centerx = self.screen_rect.centerx
        self.rect14.y = -5

    def make_normal_eyes_closed_sans(self):
        self.image15 = pygame.image.load('images/normal_sans_closed_eyes.png').convert_alpha()
        self.image15 = pygame.transform.scale(self.image15, (210, 285)).convert_alpha()
        self.rect15 = self.image15.get_rect()

        self.rect15.centerx = self.screen_rect.centerx
        self.rect15.y = -5

    def make_normal_sans_confused(self):
        self.image16 = pygame.image.load('images/normal_sans_confused.png').convert_alpha()
        self.image16 = pygame.transform.scale(self.image16, (210, 285)).convert_alpha()
        self.rect16 = self.image16.get_rect()

        self.rect16.centerx = self.screen_rect.centerx
        self.rect16.y = -5

    def make_normal_sans_glow(self):
        self.image21 = pygame.image.load('images/normal_sans_glow.png').convert_alpha()
        self.image21 = pygame.transform.scale(self.image21, (210, 285)).convert_alpha()
        self.rect21 = self.image21.get_rect()

        self.rect21.centerx = self.screen_rect.centerx
        self.rect21.y = -5

    def make_normal_sans_look_right(self):
        self.image22 = pygame.image.load('images/normal_sans_look_right.png').convert_alpha()
        self.image22 = pygame.transform.scale(self.image22, (210, 285)).convert_alpha()
        self.rect22 = self.image22.get_rect()

        self.rect22.centerx = self.screen_rect.centerx
        self.rect22.y = -5

    def make_normal_sans_no_glow(self):
        self.image23 = pygame.image.load('images/no_glow_normal_sans.png').convert_alpha()
        self.image23 = pygame.transform.scale(self.image23, (210, 285)).convert_alpha()
        self.rect23 = self.image23.get_rect()

        self.rect23.centerx = self.screen_rect.centerx
        self.rect23.y = -5

    def make_normal_sans_a_bit_tired(self):
        self.image24 = pygame.image.load('images/normal_sans_tired.png').convert_alpha()
        self.image24 = pygame.transform.scale(self.image24, (210, 285)).convert_alpha()
        self.rect24 = self.image24.get_rect()

        self.rect24.centerx = self.screen_rect.centerx
        self.rect24.y = -5

    def make_normal_sans_tired_shrug(self):
        self.image25 = pygame.image.load('images/tired_sans_shrug.png').convert_alpha()
        self.image25 = pygame.transform.scale(self.image25, (245, 285)).convert_alpha()
        self.rect25 = self.image25.get_rect()

        self.rect25.centerx = self.screen_rect.centerx
        self.rect25.y = -5

    def make_confused_sans_a_bit_tired(self):
        self.image26 = pygame.image.load('images/confused_sans_a_bit_tired.png').convert_alpha()
        self.image26 = pygame.transform.scale(self.image26, (210, 285)).convert_alpha()
        self.rect26 = self.image26.get_rect()

        self.rect26.centerx = self.screen_rect.centerx
        self.rect26.y = -5

    def make_normal_sans_quite_tired(self):
        self.image27 = pygame.image.load('images/normal_sans_quite_tired.png').convert_alpha()
        self.image27 = pygame.transform.scale(self.image27, (210, 285)).convert_alpha()
        self.rect27 = self.image27.get_rect()

        self.rect27.centerx = self.screen_rect.centerx
        self.rect27.y = -5

    def make_normal_sans_very_tired(self):
        self.image28 = pygame.image.load('images/normal_sans_very_tired.png').convert_alpha()
        self.image28 = pygame.transform.scale(self.image28, (210, 285)).convert_alpha()
        self.rect28 = self.image28.get_rect()

        self.rect28.centerx = self.screen_rect.centerx
        self.rect28.y = -5

    def make_normal_sans_sleeping(self):
        self.image29 = pygame.image.load('images/normal_sans_sleeping.png').convert_alpha()
        self.image29 = pygame.transform.scale(self.image29, (210, 285)).convert_alpha()
        self.rect29 = self.image29.get_rect()

        self.rect29.centerx = self.screen_rect.centerx
        self.rect29.y = -5

    def make_normal_sans_a_bit_tired2(self):
        self.image30 = pygame.image.load('images/normal_sans_tired2.png').convert_alpha()
        self.image30 = pygame.transform.scale(self.image30, (210, 285)).convert_alpha()
        self.rect30 = self.image30.get_rect()

        self.rect30.centerx = self.screen_rect.centerx
        self.rect30.y = -5

    def make_normal_sans_a_bit_tired_eyes_closed(self):
        self.image31 = pygame.image.load('images/normal_sans_a_bit_tired_eyes_closed.png').convert_alpha()
        self.image31 = pygame.transform.scale(self.image31, (210, 285)).convert_alpha()
        self.rect31 = self.image31.get_rect()

        self.rect31.centerx = self.screen_rect.centerx
        self.rect31.y = -5

    def make_angry_sans_eyes_closed(self):
        self.image32 = pygame.image.load('images/angry_sans_eyes_closed.png').convert_alpha()
        self.image32 = pygame.transform.scale(self.image32, (210, 285)).convert_alpha()
        self.rect32 = self.image32.get_rect()

        self.rect32.centerx = self.screen_rect.centerx
        self.rect32.y = -5

    def make_angry_crazy_sans_no_glow(self):
        self.image33 = pygame.image.load('images/angry_crazy_sans_no_glow.png').convert_alpha()
        self.image33 = pygame.transform.scale(self.image33, (210, 285)).convert_alpha()
        self.rect33 = self.image33.get_rect()

        self.rect33.centerx = self.screen_rect.centerx
        self.rect33.y = -5

    def make_angry_crazy_sans_glow(self):
        self.image34 = pygame.image.load('images/angry_crazy_sans_glow.png').convert_alpha()
        self.image34 = pygame.transform.scale(self.image34, (210, 285)).convert_alpha()
        self.rect34 = self.image34.get_rect()

        self.rect34.centerx = self.screen_rect.centerx
        self.rect34.y = -5

    def make_angry_crazy_sans_glow_with_gaster(self):
        self.image35 = pygame.image.load('images/angry_crazy_sans_glow_with_gaster.png').convert_alpha()
        self.image35 = pygame.transform.scale(self.image35, (370, 285)).convert_alpha()
        self.rect35 = self.image35.get_rect()

        self.rect35.centerx = self.screen_rect.centerx - 20
        self.rect35.y = -5

    def make_angry_crazy_sans_glow_with_gaster_slamup(self):
        self.image36 = pygame.image.load('images/angry_crazy_sans_glow_with_gaster_slamup.png').convert_alpha()
        self.image36 = pygame.transform.scale(self.image36, (370, 285)).convert_alpha()
        self.rect36 = self.image36.get_rect()

        self.rect36.centerx = self.screen_rect.centerx - 20
        self.rect36.y = -5

    def make_angry_crazy_sans_glow_with_gaster_slamdown(self):
        self.image37 = pygame.image.load('images/angry_crazy_sans_glow_with_gaster_slamdown.png').convert_alpha()
        self.image37 = pygame.transform.scale(self.image37, (370, 285)).convert_alpha()
        self.rect37 = self.image37.get_rect()

        self.rect37.centerx = self.screen_rect.centerx - 20
        self.rect37.y = -5

    def make_angry_crazy_sans_glow_with_gaster_slamright(self):
        self.image38 = pygame.image.load('images/angry_crazy_sans_glow_with_gaster_slamright.png').convert_alpha()
        self.image38 = pygame.transform.scale(self.image38, (370, 285)).convert_alpha()
        self.rect38 = self.image38.get_rect()

        self.rect38.centerx = self.screen_rect.centerx - 20
        self.rect38.y = -5

    def make_difficult_angry_crazy_sans_glow_with_gaster_slamdown(self):
        self.image39 = pygame.image.load(
            'images/difficult_angry_crazy_sans_glow_with_gaster_slamdown.png').convert_alpha()
        self.image39 = pygame.transform.scale(self.image39, (370, 285)).convert_alpha()
        self.rect39 = self.image39.get_rect()

        self.rect39.centerx = self.screen_rect.centerx - 20
        self.rect39.y = -5

    def make_a_bit_tired_angry_crazy_sans_glow_with_gaster(self):
        self.image40 = pygame.image.load('images/a_bit_tired_angry_crazy_sans_glow_with_gaster.png').convert_alpha()
        self.image40 = pygame.transform.scale(self.image40, (370, 285)).convert_alpha()
        self.rect40 = self.image40.get_rect()

        self.rect40.centerx = self.screen_rect.centerx - 20
        self.rect40.y = -5

    def make_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamright(self):
        self.image41 = pygame.image.load(
            'images/a_bit_tired_angry_crazy_sans_glow_with_gaster_slamright.png').convert_alpha()
        self.image41 = pygame.transform.scale(self.image41, (370, 285)).convert_alpha()
        self.rect41 = self.image41.get_rect()

        self.rect41.centerx = self.screen_rect.centerx - 20
        self.rect41.y = -5

    def make_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamup(self):
        self.image42 = pygame.image.load(
            'images/a_bit_tired_angry_crazy_sans_glow_with_gaster_slamup.png').convert_alpha()
        self.image42 = pygame.transform.scale(self.image42, (370, 285)).convert_alpha()
        self.rect42 = self.image42.get_rect()

        self.rect42.centerx = self.screen_rect.centerx - 20
        self.rect42.y = -5

    def make_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamdown(self):
        self.image43 = pygame.image.load(
            'images/a_bit_tired_angry_crazy_sans_glow_with_gaster_slamdown.png').convert_alpha()
        self.image43 = pygame.transform.scale(self.image43, (370, 285)).convert_alpha()
        self.rect43 = self.image43.get_rect()

        self.rect43.centerx = self.screen_rect.centerx - 20
        self.rect43.y = -5

    def make_tired_angry_crazy_sans_glow_with_gaster(self):
        self.image44 = pygame.image.load('images/tired_angry_crazy_sans_glow_with_gaster.png').convert_alpha()
        self.image44 = pygame.transform.scale(self.image44, (370, 285)).convert_alpha()
        self.rect44 = self.image44.get_rect()

        self.rect44.centerx = self.screen_rect.centerx - 20
        self.rect44.y = -5

    def make_quite_tired_angry_crazy_sans_glow_with_gaster(self):
        self.image45 = pygame.image.load('images/quite_tired_angry_crazy_sans_glow_with_gaster.png').convert_alpha()
        self.image45 = pygame.transform.scale(self.image45, (370, 285)).convert_alpha()
        self.rect45 = self.image45.get_rect()

        self.rect45.centerx = self.screen_rect.centerx - 20
        self.rect45.y = -5

    def make_really_tired_angry_crazy_sans_glow_with_gaster(self):
        self.image46 = pygame.image.load('images/really_tired_angry_crazy_sans_glow_with_gaster.png').convert_alpha()
        self.image46 = pygame.transform.scale(self.image46, (370, 285)).convert_alpha()
        self.rect46 = self.image46.get_rect()

        self.rect46.centerx = self.screen_rect.centerx - 20
        self.rect46.y = -5

    def make_really_tired_normal_sans(self):
        self.image47 = pygame.image.load('images/really_tired_sans.png').convert_alpha()
        self.image47 = pygame.transform.scale(self.image47, (210, 285)).convert_alpha()
        self.rect47 = self.image47.get_rect()

        self.rect47.centerx = self.screen_rect.centerx
        self.rect47.y = -5

    def make_really_tired_normal_sans_smile(self):
        self.image48 = pygame.image.load('images/really_tired_sans_smile.png').convert_alpha()
        self.image48 = pygame.transform.scale(self.image48, (210, 285)).convert_alpha()
        self.rect48 = self.image48.get_rect()

        self.rect48.centerx = self.screen_rect.centerx
        self.rect48.y = -5

    def make_happy_sans_red(self):
        self.image49 = pygame.image.load('images/happy_sans.png').convert_alpha()
        self.image49 = pygame.transform.scale(self.image49, (210, 285)).convert_alpha()
        self.rect49 = self.image49.get_rect()

        self.rect49.centerx = self.screen_rect.centerx
        self.rect49.y = -5

    def make_happy_sans_white(self):
        self.image50 = pygame.image.load('images/saved_sans.png').convert_alpha()
        self.image50 = pygame.transform.scale(self.image50, (210, 285)).convert_alpha()
        self.rect50 = self.image50.get_rect()

        self.rect50.centerx = self.screen_rect.centerx
        self.rect50.y = -5

        self.fade2 = pygame.Surface((self.rect50.width, self.rect50.height)).convert()
        self.fade2.set_alpha(175)

    def make_fade(self):
        self.fade = pygame.Surface((self.rect12.width + 10, self.rect12.height)).convert()

    def increase_fade(self):
        if self.fade_delay is None:
            self.fade_delay = time()
        if time() - self.fade_delay >= 0.01:
            self.fade.fill((0, 0, 0))
            self.fade_value += 8
            self.fade_delay = None
        self.fade.set_alpha(self.fade_value)
        
    def shake_sans(self):
        if self.rect10.x >= 310 and self.times_moved == 0:
            self.x -= 1.8
            self.rect10.x = self.x
        else:
            if self.times_moved == 0:
                self.times_moved = 1
            if self.rect10.x <= 440 and self.times_moved == 1:
                self.x += 0.7
                self.rect10.x = self.x
            else:
                if self.times_moved == 1:
                    self.times_moved = 2
                if self.rect10.x >= 335 and self.times_moved == 2:
                    self.x -= 0.4
                    self.rect10.x = self.x
                else:
                    if self.times_moved == 2:
                        self.times_moved = 3
                    if self.rect10.x <= 400 and self.times_moved == 3:
                        self.x += 0.2
                        self.rect10.x = self.x
                    else:
                        if self.times_moved == 3:
                            self.times_moved = 4
                        if self.rect10.x >= 383 and self.times_moved == 4:
                            self.x -= 0.05
                            self.rect10.x = self.x
                        else:
                            self.stats.kill_dia += 1

    def sans_waking_up(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time <= 2.25 and self.last_time2 is None:
            self.screen.blit(self.image28, self.rect28)
        else:
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 <= 2.25 and self.last_time3 is None:
                self.screen.blit(self.image27, self.rect27)
            else:
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 <= 1.25 and self.last_time4 is None:
                    self.screen.blit(self.image24, self.rect24)
                else:
                    if self.last_time4 is None:
                        self.last_time4 = time()
                    if time() - self.last_time4 <= 0.5:
                        self.screen.blit(self.image30, self.rect30)
                    else:
                        self.stats.dia += 1

    def show_closed(self):
        self.screen.blit(self.image, self.rect)

    def show_craze_no_glow(self):
        self.screen.blit(self.image2_, self.rect2_)

    def show_craze_glow_slamdown(self):
        self.screen.blit(self.image3, self.rect3)
        self.slam.slam = 'down'
        self.heart.heart_direction = 'up'

    def show_craze_glow_slamup(self):
        self.screen.blit(self.image17, self.rect17)
        self.slam.slam = 'up'
        self.heart.heart_direction = 'down'

    def show_normal_sans_slamdown(self):
        self.screen.blit(self.image18, self.rect18)
        self.slam.slam = 'down'
        self.heart.heart_direction = 'up'

    def show_normal_sans_slamup(self):
        self.screen.blit(self.image19, self.rect19)
        self.slam.slam = 'up'
        self.heart.heart_direction = 'down'

    def show_normal_sans_slamright(self):
        self.screen.blit(self.image20, self.rect20)
        self.slam.slam = 'right'
        self.heart.heart_direction = 'right'

    def show_normal_sans_slamleft(self):
        if self.last_time is None:
            self.last_time = time()
            self.screen.blit(self.image20, self.rect20)
            self.slam.slam = 'left'
        if time() - self.last_time <= 0.4:
            self.screen.blit(self.image20, self.rect20)
        else:
            self.screen.blit(self.image8, self.rect8)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.0001:
                self.stats.sans_amount += 1
                self.heart.heart_direction = 'left'
                self.last_time = None
                self.last_time2 = None

    def show_angry_crazy_sans_glow_with_gaster_slamup(self):
        self.last_time = time()
        self.screen.blit(self.image36, self.rect36)
        self.slam.slam = 'up'
        self.heart.heart_direction = 'down'

    def show_craze_glow(self):
        self.screen.blit(self.image4, self.rect4)

    def show_craze_no_glow_drop1(self):
        self.screen.blit(self.image5, self.rect5)

    def show_craze_no_glow_drop2(self):
        self.screen.blit(self.image6, self.rect6)

    def show_craze_no_glow_shrug(self):
        self.screen.blit(self.image7, self.rect7)

    def show_normal_sans(self):
        self.screen.blit(self.image8, self.rect8)

    def show_shocked_sans(self):
        self.screen.blit(self.image9, self.rect9)

    def show_downed_sans(self):
        self.screen.blit(self.image10, self.rect10)

    def show_pleased_sans(self):
        self.screen.blit(self.image11, self.rect11)

    def show_killed_tired_sans(self):
        self.screen.blit(self.image12, self.rect12)

    def show_almost_dead_sans(self):
        self.screen.blit(self.image13, self.rect13)

    def show_dead_sans(self):
        self.screen.blit(self.image14, self.rect14)

    def show_normal_eyes_closed_sans(self):
        self.screen.blit(self.image15, self.rect15)

    def show_normal_confused_sans(self):
        self.screen.blit(self.image16, self.rect16)

    def show_normal_sans_glow(self):
        self.screen.blit(self.image21, self.rect21)

    def show_normal_sans_look_right(self):
        self.screen.blit(self.image22, self.rect22)

    def show_normal_sans_no_glow(self):
        self.screen.blit(self.image23, self.rect23)

    def show_normal_sans_a_bit_tired(self):
        self.screen.blit(self.image24, self.rect24)

    def show_normal_sans_tired_shrug(self):
        self.screen.blit(self.image25, self.rect25)

    def show_confused_sans_a_bit_tired(self):
        self.screen.blit(self.image26, self.rect26)

    def show_normal_sans_quite_tired(self):
        self.screen.blit(self.image27, self.rect27)

    def show_normal_sans_very_tired(self):
        self.screen.blit(self.image28, self.rect28)

    def show_normal_sans_sleeping(self):
        self.screen.blit(self.image29, self.rect29)

    def show_normal_sans_a_bit_tired2(self):
        self.screen.blit(self.image30, self.rect30)

    def show_normal_sans_a_bit_tired_eyes_closed(self):
        self.screen.blit(self.image31, self.rect31)

    def show_angry_sans_eyes_closed(self):
        self.screen.blit(self.image32, self.rect32)

    def show_angry_crazy_sans_no_glow(self):
        self.screen.blit(self.image33, self.rect33)

    def show_angry_crazy_sans_glow(self):
        self.screen.blit(self.image34, self.rect34)

    def show_angry_crazy_sans_glow_with_gaster(self):
        self.screen.blit(self.image35, self.rect35)

    def show_angry_crazy_sans_glow_with_gaster_slamdown(self):
        self.screen.blit(self.image37, self.rect37)
        self.slam.slam = 'down'
        self.heart.heart_direction = 'up'

    def show_angry_crazy_sans_glow_with_gaster_slamleft(self):
        if self.last_time is None:
            self.last_time = time()
            self.screen.blit(self.image38, self.rect38)
            self.slam.slam = 'left'
        if time() - self.last_time <= 0.4:
            self.screen.blit(self.image38, self.rect38)
        else:
            self.screen.blit(self.image34, self.rect34)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.0001:
                self.stats.sans_amount += 1
                self.heart.heart_direction = 'left'
                self.last_time = None
                self.last_time2 = None

    def show_difficult_angry_crazy_sans_with_gaster_slamdown(self):
        self.screen.blit(self.image39, self.rect38)

    def show_a_bit_tired_angry_crazy_sans_glow_with_gaster(self):
        self.screen.blit(self.image40, self.rect40)

    def show_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamleft(self):
        if self.last_time is None:
            self.last_time = time()
            self.screen.blit(self.image41, self.rect41)
            self.slam.slam = 'left'
        if time() - self.last_time <= 0.4:
            self.screen.blit(self.image41, self.rect41)
        else:
            self.screen.blit(self.image40, self.rect40)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.0001:
                self.stats.sans_amount += 1
                self.heart.heart_direction = 'left'
                self.last_time = None
                self.last_time2 = None

    def show_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamup(self):
        self.heart.heart_direction = 'down'
        self.slam.slam = 'up'
        self.screen.blit(self.image42, self.rect42)

    def show_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamdown(self):
        self.heart.heart_direction = 'up'
        self.slam.slam = 'down'
        self.screen.blit(self.image43, self.rect43)

    def show_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamright(self):
        self.heart.heart_direction = 'right'
        self.slam.slam = 'right'
        self.screen.blit(self.image41, self.rect41)

    def show_tired_angry_crazy_sans_glow_with_gaster(self):
        self.screen.blit(self.image44, self.rect44)

    def show_quite_tired_angry_crazy_sans_glow_with_gaster(self):
        self.screen.blit(self.image45, self.rect45)

    def show_really_tired_angry_crazy_sans_glow_with_gaster(self):
        self.screen.blit(self.image46, self.rect46)

    def show_really_tired_normal_sans(self):
        self.screen.blit(self.image47, self.rect47)

    def show_really_tired_normal_sans_smile(self):
        self.screen.blit(self.image48, self.rect48)

    def show_happy_sans_red(self):
        self.screen.blit(self.image49, self.rect49)

    def show_happy_sans_white(self):
        self.screen.blit(self.image50, self.rect50)
        self.screen.blit(self.fade2, (self.rect50.centerx - 105, self.rect50.centery - 142.5))

    def show_fade(self):
        self.screen.blit(self.fade, (380, -5))
