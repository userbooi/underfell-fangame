import pygame
from pygame.font import Font

class BattleText:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.battle = UF_game.battle
        self.settings = UF_game.settings
        self.stats = UF_game.stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('arialblack', 30)
        self.star_font = pygame.font.SysFont('arialblack', 50)

        self.stared = self.star_font.render('*', True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.star_rect = self.stared.get_rect()

        self.star_rect.left = self.battle.rect.left + 20
        self.star_rect.top = self.battle.rect.top + 14

        self.T1()
        self.T2()
        self.T3()
        self.T4()
        self.T5()
        self.T6()
        self.T7()
        self.T8()
        self.T9()
        self.TDE()
        self.TDE2()
        self.CT()
        self.RT()
        self.IT()

    def T1(self):
        t1 = 'The battle has just begun, stay'
        t2 = 'determined'

        self.text1 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text1_rect = self.text1.get_rect()

        self.text1_rect.left = self.star_rect.right + 8
        self.text1_rect.top = self.battle.rect.top + 18

        self.text12 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text12_rect = self.text12.get_rect()

        self.text12_rect.top = self.text1_rect.bottom
        self.text12_rect.left = self.text1_rect.left

    def T2(self):
        t1 = 'remember, he only does one'
        t2 = 'damage'

        self.text5 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text5_rect = self.text5.get_rect()

        self.text5_rect.left = self.star_rect.right + 8
        self.text5_rect.top = self.battle.rect.top + 18

        self.text52 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text52_rect = self.text52.get_rect()

        self.text52_rect.top = self.text5_rect.bottom
        self.text52_rect.left = self.text5_rect.left

    def T3(self):
        t1 = "he can's keep fighting forever,"
        t2 = 'keep sparing'

        self.text6 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text6_rect = self.text6.get_rect()

        self.text6_rect.left = self.star_rect.right + 8
        self.text6_rect.top = self.battle.rect.top + 18

        self.text62 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text62_rect = self.text62.get_rect()

        self.text62_rect.top = self.text6_rect.bottom
        self.text62_rect.left = self.text6_rect.left

    def T4(self):
        t1 = "sans looks a bit tired..."
        t2 = ''

        self.text7 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text7_rect = self.text7.get_rect()

        self.text7_rect.left = self.star_rect.right + 8
        self.text7_rect.top = self.battle.rect.top + 18

        self.text72 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text72_rect = self.text72.get_rect()

        self.text72_rect.top = self.text7_rect.bottom
        self.text72_rect.left = self.text7_rect.left

    def T5(self):
        t1 = "sans looks a quite tired..."
        t2 = ''

        self.text8 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text8_rect = self.text8.get_rect()

        self.text8_rect.left = self.star_rect.right + 8
        self.text8_rect.top = self.battle.rect.top + 18

        self.text82 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text82_rect = self.text82.get_rect()

        self.text82_rect.top = self.text8_rect.bottom
        self.text82_rect.left = self.text8_rect.left

    def T6(self):
        t1 = "sans looks.... sleepy?"
        t2 = ''

        self.text9 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text9_rect = self.text9.get_rect()

        self.text9_rect.left = self.star_rect.right + 8
        self.text9_rect.top = self.battle.rect.top + 18

        self.text92 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text92_rect = self.text92.get_rect()

        self.text92_rect.top = self.text9_rect.bottom
        self.text92_rect.left = self.text9_rect.left

    def T7(self):
        t1 = "sans fell a sleep....."
        t2 = ''

        self.text10 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text10_rect = self.text10.get_rect()

        self.text10_rect.left = self.star_rect.right + 8
        self.text10_rect.top = self.battle.rect.top + 18

        self.text102 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text102_rect = self.text102.get_rect()

        self.text102_rect.top = self.text10_rect.bottom
        self.text102_rect.left = self.text10_rect.left

    def T8(self):
        t1 = "sans looks very tired."
        t2 = 'keep sparing until he gives in!'

        self.text11 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text11_rect = self.text11.get_rect()

        self.text11_rect.left = self.star_rect.right + 8
        self.text11_rect.top = self.battle.rect.top + 18

        self.text112 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text112_rect = self.text112.get_rect()

        self.text112_rect.top = self.text11_rect.bottom
        self.text112_rect.left = self.text11_rect.left

    def T9(self):
        t1 = "he is accepting it."
        t2 = 'continue'

        self.text121 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text121_rect = self.text121.get_rect()

        self.text121_rect.left = self.star_rect.right + 8
        self.text121_rect.top = self.battle.rect.top + 18

        self.text122 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text122_rect = self.text122.get_rect()

        self.text122_rect.top = self.text121_rect.bottom
        self.text122_rect.left = self.text121_rect.left

    def CT(self):
        t1 = 'Sans, 1 Attack and 1 Defense'
        t2 = 'The most pathetic enemy, can only deal 1'
        t3 = 'damage'

        self.text3 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text3_rect = self.text3.get_rect()

        self.text3_rect.left = self.star_rect.right + 8
        self.text3_rect.top = self.battle.rect.top + 18

        self.text32 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text32_rect = self.text32.get_rect()

        self.text32_rect.top = self.text3_rect.bottom + 45
        self.text32_rect.left = self.text3_rect.left

        self.text33 = self.font.render(t3, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text33_rect = self.text33.get_rect()

        self.text33_rect.top = self.text32_rect.bottom
        self.text33_rect.left = self.text3_rect.left

    def RT(self):
        t1 = 'You try to explain to Sans that you are'
        t2 = 'doing this to save the underground.'
        t3 = "He doesn't even care."

        self.text4 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text4_rect = self.text4.get_rect()

        self.text4_rect.left = self.star_rect.right + 8
        self.text4_rect.top = self.battle.rect.top + 18

        self.text42 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text42_rect = self.text42.get_rect()

        self.text42_rect.top = self.text4_rect.bottom
        self.text42_rect.left = self.text4_rect.left

        self.text43 = self.font.render(t3, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text43_rect = self.text43.get_rect()

        self.text43_rect.top = self.text42_rect.bottom + 45
        self.text43_rect.left = self.text4_rect.left

    def IT(self):
        ate_texts = ['You ate the Pie', 'You ate the Instant Noodles', 'You ate the Face Steak', 'You ate the Legendary Hero']
        last_text = "Your health is maxed out!"
        self.texts = []

        for text in ate_texts:
            pair = {}
            pair['surface'] = self.font.render(text, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
            pair['rect'] = pair['surface'].get_rect()

            pair['rect'].top = self.battle.rect.top + 18
            pair['rect'].left = self.star_rect.right + 8

            self.texts.append(pair)

        self.maxed_out_text = self.font.render(last_text, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.maxed_out_rect = self.maxed_out_text.get_rect()

        self.maxed_out_rect.top = self.texts[0]['rect'].bottom + 45
        self.maxed_out_rect.left = self.star_rect.right + 8

    def TDE(self):
        t1 = 'You won! You gained 99999 EXP! Your'
        t2 = 'LV increased! You got 1000000 gold!'

        self.text2 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text2_rect = self.text2.get_rect()

        self.text2_rect.left = self.star_rect.right + 8
        self.text2_rect.top = self.battle.rect.top + 18

        self.text22 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text22_rect = self.text22.get_rect()

        self.text22_rect.top = self.text2_rect.bottom
        self.text22_rect.left = self.text2_rect.left

    def TDE2(self):
        t1 = 'You won! You gained 0 EXP! You'
        t2 = 'got 0 gold'

        self.text13 = self.font.render(t1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text13_rect = self.text13.get_rect()

        self.text13_rect.left = self.star_rect.right + 8
        self.text13_rect.top = self.battle.rect.top + 18

        self.text132 = self.font.render(t2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.text132_rect = self.text132.get_rect()

        self.text132_rect.top = self.text13_rect.bottom
        self.text132_rect.left = self.text13_rect.left

    def show_T1(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text1, self.text1_rect)
        self.screen.blit(self.text12, self.text12_rect)

    def show_T2(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text5, self.text5_rect)
        self.screen.blit(self.text52, self.text52_rect)

    def show_T3(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text6, self.text6_rect)
        self.screen.blit(self.text62, self.text62_rect)

    def show_T4(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text7, self.text7_rect)
        self.screen.blit(self.text72, self.text72_rect)

    def show_T5(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text8, self.text8_rect)
        self.screen.blit(self.text82, self.text82_rect)

    def show_T6(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text9, self.text9_rect)
        self.screen.blit(self.text92, self.text92_rect)

    def show_T7(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text10, self.text10_rect)
        self.screen.blit(self.text102, self.text102_rect)

    def show_T8(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text11, self.text11_rect)
        self.screen.blit(self.text112, self.text112_rect)

    def show_T9(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text121, self.text121_rect)
        self.screen.blit(self.text122, self.text122_rect)

    def show_TDE(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text2, self.text2_rect)
        self.screen.blit(self.text22, self.text22_rect)

    def show_TDE2(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.text13, self.text13_rect)
        self.screen.blit(self.text132, self.text132_rect)

    def show_AT(self):
        if self.stats.turn == 'checked':
            self.screen.blit(self.stared, self.star_rect)
            self.screen.blit(self.text3, self.text3_rect)
            self.screen.blit(self.text32, self.text32_rect)
            self.screen.blit(self.text33, self.text33_rect)
        elif self.stats.turn == 'reasoned':
            self.screen.blit(self.stared, self.star_rect)
            self.screen.blit(self.text4, self.text4_rect)
            self.screen.blit(self.text42, self.text42_rect)
            self.screen.blit(self.text43, self.text43_rect)

    def show_IT(self):
        self.screen.blit(self.stared, self.star_rect)
        self.screen.blit(self.maxed_out_text, self.maxed_out_rect)
        if self.stats.turn == 'ate pie':
            self.screen.blit(self.texts[0]['surface'], self.texts[0]['rect'])
        elif self.stats.turn == 'ate noodles':
            self.screen.blit(self.texts[1]['surface'], self.texts[1]['rect'])
        elif self.stats.turn == 'ate steak':
            self.screen.blit(self.texts[2]['surface'], self.texts[2]['rect'])
        elif self.stats.turn == 'ate lhero':
            self.screen.blit(self.texts[3]['surface'], self.texts[3]['rect'])
