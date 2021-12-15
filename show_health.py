import pygame
from pygame.font import Font

class health_number:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.location = UF_game.hb2
        self.location_rect = self.location.hb_rect
        self.settings = UF_game.settings

        self.stats = UF_game.stats
        self.text_color = (255, 255, 255)

        self.font = pygame.font.SysFont('arialblack', 30)

        self.health1()
        self.health2()

    def health1(self):
        number = str(self.stats.health)
        self.health_image = self.font.render(number, True, self.text_color, self.settings.bg_color).convert_alpha()

        self.hi_rect = self.health_image.get_rect()
        self.hi_rect.x = self.location_rect.x + 114
        self.hi_rect.y = self.location_rect.y - 9

    def health2(self):
        self.health2_image = self.font.render('/20', True, self.text_color, self.settings.bg_color).convert_alpha()
        self.hp = self.font.render('HP', True, self.text_color, self.settings.bg_color).convert_alpha()
        self.name = self.font.render('frisk', True, self.text_color, self.settings.bg_color).convert_alpha()
        self.lv = self.font.render('LV 1', True, self.text_color, self.settings.bg_color).convert_alpha()

        self.h2i_rect = self.health2_image.get_rect()
        self.h2i_rect.left = self.hi_rect.right
        self.h2i_rect.y = self.hi_rect.y

        self.hp_rect = self.hp.get_rect()
        self.hp_rect.top = self.h2i_rect.top
        self.hp_rect.right = self.location_rect.left - 20

        self.name_rect = self.name.get_rect()
        self.name_rect.top = self.h2i_rect.top
        self.name_rect.left = self.screen_rect.left + 25

        self.lv_rect = self.lv.get_rect()
        self.lv_rect.top = self.h2i_rect.top
        self.lv_rect.right = self.hp_rect.left - 100

    def show_health1(self):
        self.screen.blit(self.health_image, self.hi_rect)

    def show_other_health(self):
        self.screen.blit(self.health2_image, self.h2i_rect)
        self.screen.blit(self.hp, self.hp_rect)
        self.screen.blit(self.name, self.name_rect)
        self.screen.blit(self.lv, self.lv_rect)