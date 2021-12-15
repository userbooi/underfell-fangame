import pygame.font
import pygame

class Credit:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont('comicsansms', 30, False, True)
        self.credit_lines_color = (255, 255, 255)

        self.credit_lines_usable = []

        self.make_all_credit_lines()

    def make_all_credit_lines(self):
        credit_lines = ['Toby Fox', 'Toby Fox', 'Keno9988iii', 'DAVID0414', 'TeffyJeffy', 'userboiboi', 'userboiboi', '(press "z" to continue)']

        self.undertale_by = pygame.image.load('images/undertale_game_by.png').convert_alpha()
        self.undertale_by = pygame.transform.scale(self.undertale_by, (301, 27)).convert_alpha()
        self.undertale_by_rect = self.undertale_by.get_rect()

        self.undertale_by_rect.center = self.screen_rect.center
        self.undertale_by_rect.top = self.screen_rect.bottom

        pair = {}

        pair['surface'] = self.font.render(credit_lines[0], True, self.credit_lines_color, (0, 0, 0)).convert_alpha()
        pair['rect'] = pair['surface'].get_rect()

        pair['rect'].centerx = self.screen_rect.centerx
        pair['rect'].top = self.undertale_by_rect.bottom + 40

        self.credit_lines_usable.append(pair)

        self.music_by = pygame.image.load('images/music_from.png').convert_alpha()
        self.music_by = pygame.transform.scale(self.music_by, (213, 27)).convert_alpha()
        self.music_by_rect = self.music_by.get_rect()

        self.music_by_rect.centerx = self.screen_rect.centerx
        self.music_by_rect.top = self.credit_lines_usable[0]['rect'].bottom + 120

        for line2 in credit_lines[1:5]:
            pair2 = {}

            pair2['surface'] = self.font.render(line2, True, self.credit_lines_color, (0, 0, 0)).convert_alpha()
            pair2['rect'] = pair2['surface'].get_rect()

            if len(self.credit_lines_usable) == 1:
                pair2['rect'].y = self.music_by_rect.bottom + 40
                pair2['rect'].left = self.screen_rect.left + 200
            elif len(self.credit_lines_usable) == 2:
                pair2['rect'].y = self.music_by_rect.bottom + 40
                pair2['rect'].right = self.screen_rect.right - 200
            elif len(self.credit_lines_usable) == 3:
                pair2['rect'].y = self.music_by_rect.bottom + 80
                pair2['rect'].left = self.screen_rect.left + 200
            elif len(self.credit_lines_usable) == 4:
                pair2['rect'].y = self.music_by_rect.bottom + 80
                pair2['rect'].right = self.screen_rect.right - 200

            self.credit_lines_usable.append(pair2)

        self.sprite_by = pygame.image.load('images/sprite_by.png').convert_alpha()
        self.sprite_by = pygame.transform.scale(self.sprite_by, (145, 27)).convert_alpha()
        self.sprite_by_rect = self.sprite_by.get_rect()

        self.sprite_by_rect.centerx = self.screen_rect.centerx
        self.sprite_by_rect.top = self.credit_lines_usable[4]['rect'].bottom + 120

        pair3 = {}

        pair3['surface'] = self.font.render(credit_lines[5], True, self.credit_lines_color, (0, 0, 0)).convert_alpha()
        pair3['rect'] = pair3['surface'].get_rect()

        pair3['rect'].centerx = self.screen_rect.centerx
        pair3['rect'].top = self.sprite_by_rect.bottom + 40

        self.credit_lines_usable.append(pair3)

        self.programmed_by = pygame.image.load('images/programmed_by.png').convert_alpha()
        self.programmed_by = pygame.transform.scale(self.programmed_by, (229, 27)).convert_alpha()
        self.programmed_by_rect = self.programmed_by.get_rect()

        self.programmed_by_rect.centerx = self.screen_rect.centerx
        self.programmed_by_rect.top = self.credit_lines_usable[5]['rect'].bottom + 120

        pair4 = {}

        pair4['surface'] = self.font.render(credit_lines[6], True, self.credit_lines_color, (0, 0, 0)).convert_alpha()
        pair4['rect'] = pair4['surface'].get_rect()

        pair4['rect'].centerx = self.screen_rect.centerx
        pair4['rect'].top = self.programmed_by_rect.bottom + 40

        self.credit_lines_usable.append(pair4)

        self.saved_sans = pygame.image.load('images/saved_sans.png').convert_alpha()
        self.saved_sans = pygame.transform.scale(self.saved_sans, (210, 285)).convert_alpha()
        self.saved_sans_rect = self.saved_sans.get_rect()

        self.saved_sans_rect.centerx = self.screen_rect.centerx
        self.saved_sans_rect.top = self.credit_lines_usable[6]['rect'].bottom + 150

        pair5 = {}

        pair5['surface'] = self.font.render(credit_lines[7], True, self.credit_lines_color, (0, 0, 0)).convert_alpha()
        pair5['rect'] = pair5['surface'].get_rect()

        pair5['rect'].centerx = self.screen_rect.centerx
        pair5['rect'].top = self.saved_sans_rect.bottom + 80

        self.credit_lines_usable.append(pair5)

        self.y = float(self.undertale_by_rect.y)
        self.y2 = float(self.music_by_rect.y)
        self.y3 = float(self.credit_lines_usable[0]['rect'].y)
        self.y4 = float(self.credit_lines_usable[1]['rect'].y)
        self.y5 = float(self.credit_lines_usable[2]['rect'].y)
        self.y6 = float(self.credit_lines_usable[3]['rect'].y)
        self.y7 = float(self.credit_lines_usable[4]['rect'].y)
        self.y8 = float(self.credit_lines_usable[5]['rect'].y)
        self.y9 = float(self.credit_lines_usable[6]['rect'].y)
        self.y10 = float(self.sprite_by_rect.y)
        self.y11 = float(self.programmed_by_rect.y)
        self.y12 = float(self.saved_sans_rect.y)
        self.y13 = float(self.credit_lines_usable[7]['rect'].y)

    def move_all_lines_up(self):
        self.y -= 0.04
        self.y2 -= 0.04
        self.y3 -= 0.04
        self.y4 -= 0.04
        self.y5 -= 0.04
        self.y6 -= 0.04
        self.y7 -= 0.04
        self.y8 -= 0.04
        self.y9 -= 0.04
        self.y10 -= 0.04
        self.y11 -= 0.04
        self.y12 -= 0.04
        self.y13 -= 0.04

        self.undertale_by_rect.y = self.y
        self.music_by_rect.y = self.y2
        self.credit_lines_usable[0]['rect'].y = self.y3
        self.credit_lines_usable[1]['rect'].y = self.y4
        self.credit_lines_usable[2]['rect'].y = self.y5
        self.credit_lines_usable[3]['rect'].y = self.y6
        self.credit_lines_usable[4]['rect'].y = self.y7
        self.credit_lines_usable[5]['rect'].y = self.y8
        self.credit_lines_usable[6]['rect'].y = self.y9
        self.sprite_by_rect.y = self.y10
        self.programmed_by_rect.y = self.y11
        self.saved_sans_rect.y = self.y12
        self.credit_lines_usable[7]['rect'].y = self.y13

    def show_all_credit_lines(self):
        for line in self.credit_lines_usable:
            self.screen.blit(line['surface'], line['rect'])
        self.screen.blit(self.undertale_by, self.undertale_by_rect)
        self.screen.blit(self.music_by, self.music_by_rect)
        self.screen.blit(self.sprite_by, self.sprite_by_rect)
        self.screen.blit(self.programmed_by, self.programmed_by_rect)
        self.screen.blit(self.saved_sans, self.saved_sans_rect)
