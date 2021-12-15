import pygame
from pygame.font import Font
from pygame.sprite import Sprite

class InsideText(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.mh = UF_game.mh
        self.battle = UF_game.battle
        self.settings = UF_game.settings

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('arialblack', 35)

        self.fighttext()
        self.acttext()
        self.itemtext()
        self.mercytext()
        self.used_items()

    def fighttext(self):
        self.ftext = self.font.render('sans', True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.ftext_rect = self.ftext.get_rect()

        self.ftext_rect.left = self.mh.menu_heart_rect.right + 12
        self.ftext_rect.top = self.mh.menu_heart_rect.top - 16

    def used_items(self):
        self.image = self.font.render('used', True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.rect = self.image.get_rect()

    def acttext(self):
        name = 'sans'
        options = ['check', 'reason']
        self.act_options_pair = []

        self.name = self.font.render(name, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.name_rect = self.name.get_rect()

        self.name_rect.left = self.mh.menu_heart_rect.right + 12
        self.name_rect.top = self.mh.menu_heart_rect.top - 16

        for option in options:
            pair = {}
            pair['surface'] = self.font.render(option, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
            pair['rect'] = pair['surface'].get_rect()

            if option == 'check':
                pair['rect'].left = self.mh.menu_heart_rect.right + 12
                pair['rect'].top = self.mh.menu_heart_rect.top - 16
            elif option == 'reason':
                pair['rect'].right = self.battle.rect.right - 150
                pair['rect'].top = self.mh.menu_heart_rect.top - 16

            self.act_options_pair.append(pair)

    def itemtext(self):
        page_names = ['Page 1', 'Page 2']
        item_names = ['Pie    ', 'I. Noodles', 'I. Noodles', 'F. Steak', 'L. Hero', 'L. Hero', 'L. Hero', 'L. Hero']
        noodles = 1
        lhero = 1
        self.item_options = []
        self.page_number = []

        for page_name in page_names:
            pairp = {}
            pairp['surface'] = self.font.render(page_name, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
            pairp['rect'] = pairp['surface'].get_rect()

            pairp['rect'].right = self.battle.rect.right - 35
            pairp['rect'].bottom = self.battle.rect.bottom - 20

            self.page_number.append(pairp)

        for item in item_names:
            pairi = {}
            pairi['surface'] = self.font.render(item, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
            pairi['rect'] = pairi['surface'].get_rect()

            if item_names.index(item) == 0:
                pairi['rect'].left = self.mh.menu_heart_rect.right + 12
                pairi['rect'].top = self.mh.menu_heart_rect.top - 16
            elif item_names.index(item) == 4 and lhero == 1:
                pairi['rect'].left = self.mh.menu_heart_rect.right + 12
                pairi['rect'].top = self.mh.menu_heart_rect.top - 16
                lhero = 2
            elif item_names.index(item) == 1 and noodles == 1:
                pairi['rect'].right = self.battle.rect.right - 150
                pairi['rect'].top = self.mh.menu_heart_rect.top - 16
                noodles = 2
            elif item_names.index(item) == 4 and lhero == 2:
                pairi['rect'].right = self.battle.rect.right - 215
                pairi['rect'].top = self.mh.menu_heart_rect.top - 16
                lhero = 3
            elif item_names.index(item) == 1 and noodles == 2:
                pairi['rect'].left = self.mh.menu_heart_rect.right + 12
                pairi['rect'].bottom = self.battle.rect.bottom - 110
            elif item_names.index(item) == 4 and lhero == 3:
                pairi['rect'].left = self.mh.menu_heart_rect.right + 12
                pairi['rect'].bottom = self.battle.rect.bottom - 110
                lhero = 4
            elif item_names.index(item) == 3:
                pairi['rect'].right = self.battle.rect.right - 190
                pairi['rect'].bottom = self.battle.rect.bottom - 110
            elif item_names.index(item) == 4 and lhero == 4:
                pairi['rect'].right = self.battle.rect.right - 215
                pairi['rect'].bottom = self.battle.rect.bottom - 110

            self.item_options.append(pairi)

    def mercytext(self):
        self.spare = self.font.render('spare', True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.spare_rect = self.spare.get_rect()

        self.spare_rect.left = self.mh.menu_heart_rect.right + 12
        self.spare_rect.top = self.mh.menu_heart_rect.top - 16

    def show_fighttext(self):
        self.screen.blit(self.ftext, self.ftext_rect)

    def show_act_name(self):
        self.screen.blit(self.name, self.name_rect)

    def show_act_options(self):
        self.screen.blit(self.act_options_pair[0]['surface'], self.act_options_pair[0]['rect'])
        self.screen.blit(self.act_options_pair[1]['surface'], self.act_options_pair[1]['rect'])

    def show_page_number_1(self):
        self.screen.blit(self.page_number[0]['surface'], self.page_number[0]['rect'])

    def show_page_number_2(self):
        self.screen.blit(self.page_number[1]['surface'], self.page_number[1]['rect'])

    def show_item_1(self):
        self.screen.blit(self.item_options[0]['surface'], self.item_options[0]['rect'])

    def show_item_2(self):
        self.screen.blit(self.item_options[1]['surface'], self.item_options[1]['rect'])

    def show_item_3(self):
        self.screen.blit(self.item_options[2]['surface'], self.item_options[2]['rect'])

    def show_item_4(self):
        self.screen.blit(self.item_options[3]['surface'], self.item_options[3]['rect'])

    def show_item_5(self):
        self.screen.blit(self.item_options[4]['surface'], self.item_options[4]['rect'])

    def show_item_6(self):
        self.screen.blit(self.item_options[5]['surface'], self.item_options[5]['rect'])

    def show_item_7(self):
        self.screen.blit(self.item_options[6]['surface'], self.item_options[6]['rect'])

    def show_item_8(self):
        self.screen.blit(self.item_options[7]['surface'], self.item_options[7]['rect'])

    def show_mercy(self):
        self.screen.blit(self.spare, self.spare_rect)
