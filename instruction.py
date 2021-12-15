import pygame
from pygame.font import Font

class Instructions:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = UF_game.settings

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('comicsansms', 30)

        self.instruc()

    def instruc(self):
        instruction1 = 'This game was made with python and by one guy. This is his first'
        instruction2 = 'game. Credits will be at the end of the game, hope you can make it'
        instruction3 = 'that far! The controls for the game is "z" to continue/select,'
        instruction4 = 'arrow keys to maneuver through the attacks and the selection menu'
        instruction5 = 'in the game. use "ESC" key to go from the game to the start menu'
        instruction6 = 'and also to exit the game when in the start menu. Use "x" to go'
        instruction7 = 'from inside your selection back to the menu. Remember, UnderFell'
        instruction8 = 'sans is a mercy boss fight, you get the real ending by sparing him'
        instruction9 = "in case you didn't know, when a attack is blue, don't move and "
        instruction10 = "when it is orange, move"
        instruction11 = 'Enjoy!'
        to_start = '(if you are ready, press "z" to start)'

        self.instr1 = self.font.render(instruction1, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr1_rect = self.instr1.get_rect()

        self.instr1_rect.centerx = self.screen_rect.centerx
        self.instr1_rect.top = self.screen_rect.top + 20

        self.instr2 = self.font.render(instruction2, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr2_rect = self.instr2.get_rect()

        self.instr2_rect.centerx = self.screen_rect.centerx
        self.instr2_rect.top = self.instr1_rect.bottom + 15

        self.instr3 = self.font.render(instruction3, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr3_rect = self.instr3.get_rect()

        self.instr3_rect.centerx = self.screen_rect.centerx
        self.instr3_rect.top = self.instr2_rect.bottom + 15

        self.instr4 = self.font.render(instruction4, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr4_rect = self.instr4.get_rect()

        self.instr4_rect.centerx = self.screen_rect.centerx
        self.instr4_rect.top = self.instr3_rect.bottom + 15

        self.instr5 = self.font.render(instruction5, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr5_rect = self.instr5.get_rect()

        self.instr5_rect.centerx = self.screen_rect.centerx
        self.instr5_rect.top = self.instr4_rect.bottom + 15

        self.instr6 = self.font.render(instruction6, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr6_rect = self.instr6.get_rect()

        self.instr6_rect.centerx = self.screen_rect.centerx
        self.instr6_rect.top = self.instr5_rect.bottom + 15

        self.instr7 = self.font.render(instruction7, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr7_rect = self.instr7.get_rect()

        self.instr7_rect.centerx = self.screen_rect.centerx
        self.instr7_rect.top = self.instr6_rect.bottom + 15

        self.instr8 = self.font.render(instruction8, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr8_rect = self.instr8.get_rect()

        self.instr8_rect.centerx = self.screen_rect.centerx
        self.instr8_rect.top = self.instr7_rect.bottom + 15

        self.instr9 = self.font.render(instruction9, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr9_rect = self.instr9.get_rect()

        self.instr9_rect.centerx = self.screen_rect.centerx
        self.instr9_rect.top = self.instr8_rect.bottom + 15

        self.instr10 = self.font.render(instruction10, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr10_rect = self.instr10.get_rect()

        self.instr10_rect.centerx = self.screen_rect.centerx
        self.instr10_rect.top = self.instr9_rect.bottom + 15

        self.instr11 = self.font.render(instruction11, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.instr11_rect = self.instr11.get_rect()

        self.instr11_rect.centerx = self.screen_rect.centerx
        self.instr11_rect.top = self.instr10_rect.bottom + 15

        self.to_start = self.font.render(to_start, True, self.text_color, self.settings.bg_battle_text).convert_alpha()
        self.to_start_rect = self.to_start.get_rect()

        self.to_start_rect.centerx = self.screen_rect.centerx
        self.to_start_rect.bottom = self.screen_rect.bottom - 30

    def show_instruc1(self):
        self.screen.blit(self.instr1, self.instr1_rect)

    def show_instruc2(self):
        self.screen.blit(self.instr2, self.instr2_rect)

    def show_instruc3(self):
        self.screen.blit(self.instr3, self.instr3_rect)

    def show_instruc4(self):
        self.screen.blit(self.instr4, self.instr4_rect)

    def show_instruc5(self):
        self.screen.blit(self.instr5, self.instr5_rect)

    def show_instruc6(self):
        self.screen.blit(self.instr6, self.instr6_rect)

    def show_instruc7(self):
        self.screen.blit(self.instr7, self.instr7_rect)

    def show_instruc8(self):
        self.screen.blit(self.instr8, self.instr8_rect)

    def show_instruc9(self):
        self.screen.blit(self.instr9, self.instr9_rect)

    def show_instruc10(self):
        self.screen.blit(self.instr10, self.instr10_rect)

    def show_instruc11(self):
        self.screen.blit(self.instr11, self.instr11_rect)

    def show_continue_prompt(self):
        self.screen.blit(self.to_start, self.to_start_rect)
