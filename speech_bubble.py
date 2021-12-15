import pygame

class Bubble:

    def __init__(self, UF_game):

        self.screen = UF_game.screen
        self.sans = UF_game.Sanness
        self.sans_rect = self.sans.rect
        self.texts = UF_game.text
        self.stats = UF_game.stats

        with open('data/data.txt', 'r') as d:
            self.data = d.read()
            self.data = self.data.split(' ')

        self.update_bubble_height()
        self.update_bubble_width()
        self.speech_bubble()
        self.bubble_stem()

    def update_bubble_height(self):
        if self.data[0] == 'beat_the_first_attack':
            if self.stats.sans_health == 1:
                if self.stats.dia == 1:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 5:
                    self.heights = self.texts.diaAF1_rect.height + self.texts.diaAF2_rect.height + 45
                elif self.stats.dia == 6:
                    self.heights = self.texts.dia61_rect.height + self.texts.dia62_rect.height + 45
                elif self.stats.dia == 9:
                    self.heights = self.texts.dia131_rect.height + self.texts.dia132_rect.height + 45
                elif self.stats.dia == 10:
                    self.heights = self.texts.dia141_rect.height + self.texts.dia142_rect.height + self.texts.dia143_rect.height + 45
                elif self.stats.dia == 12:
                    self.heights = self.texts.dia151_rect.height + self.texts.dia152_rect.height + 45
                elif self.stats.dia == 13:
                    self.heights = self.texts.dia161_rect.height + self.texts.dia162_rect.height + 45
                elif self.stats.dia == 14:
                    self.heights = self.texts.dia171_rect.height + self.texts.dia172_rect.height + 45
                elif self.stats.dia == 15:
                    self.heights = self.texts.dia181_rect.height + self.texts.dia182_rect.height + 45
                elif self.stats.dia == 16:
                    self.heights = self.texts.dia181_rect.height + self.texts.dia182_rect.height + 45
                elif self.stats.dia == 17:
                    self.heights = self.texts.dia191_rect.height + self.texts.dia192_rect.height + self.texts.dia193_rect.height + 45
                elif self.stats.dia == 18:
                    self.heights = self.texts.dia201_rect.height + self.texts.dia202_rect.height + 45
                elif self.stats.dia == 19:
                    self.heights = self.texts.dia201_rect.height + self.texts.dia202_rect.height + 45
                elif self.stats.dia == 20:
                    self.heights = self.texts.dia211_rect.height + self.texts.dia212_rect.height + 45
                elif self.stats.dia == 21:
                    self.heights = self.texts.dia221_rect.height + self.texts.dia222_rect.height + 45
                elif self.stats.dia == 22:
                    self.heights = self.texts.dia231_rect.height + self.texts.dia232_rect.height + 45
                elif self.stats.dia == 23:
                    self.heights = self.texts.dia231_rect.height + self.texts.dia232_rect.height + 45
                elif self.stats.dia == 24:
                    self.heights = self.texts.dia241_rect.height + self.texts.dia242_rect.height + 45
                elif self.stats.dia == 25:
                    self.heights = self.texts.dia251_rect.height + self.texts.dia252_rect.height + 45
                elif self.stats.dia == 26:
                    self.heights = self.texts.dia261_rect.height + self.texts.dia262_rect.height + 45
                elif self.stats.dia == 27:
                    self.heights = self.texts.dia261_rect.height + self.texts.dia262_rect.height + 45
                elif self.stats.dia == 28:
                    self.heights = self.texts.dia271_rect.height + self.texts.dia272_rect.height + 45
                elif self.stats.dia == 29:
                    self.heights = self.texts.dia281_rect.height + self.texts.dia282_rect.height + self.texts.dia283_rect.height + 45
                elif self.stats.dia == 30:
                    self.heights = self.texts.dia281_rect.height + self.texts.dia282_rect.height + self.texts.dia283_rect.height + 45
                elif self.stats.dia == 31:
                    self.heights = self.texts.dia291_rect.height + self.texts.dia292_rect.height + 45
                elif self.stats.dia == 32:
                    self.heights = self.texts.dia301_rect.height + self.texts.dia302_rect.height + 45
                elif self.stats.dia == 33:
                    self.heights = self.texts.dia311_rect.height + self.texts.dia312_rect.height + 45
                elif self.stats.dia == 34:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 35:
                    self.heights = self.texts.dia321_rect.height + self.texts.dia322_rect.height + 45
                elif self.stats.dia == 37:
                    self.heights = self.texts.dia331_rect.height + self.texts.dia332_rect.height + 45
                elif self.stats.dia == 38:
                    self.heights = self.texts.dia341_rect.height + self.texts.dia342_rect.height + 45
                elif self.stats.dia == 39:
                    self.heights = self.texts.dia351_rect.height + self.texts.dia352_rect.height + 45
                elif self.stats.dia == 40:
                    self.heights = self.texts.dia351_rect.height + self.texts.dia352_rect.height + 45
                elif self.stats.dia == 41:
                    self.heights = self.texts.dia361_rect.height + self.texts.dia362_rect.height + 45
                elif self.stats.dia == 42:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 43:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 44:
                    self.heights = self.texts.dia371_rect.height + self.texts.dia372_rect.height + 45
                elif self.stats.dia == 45:
                    self.heights = self.texts.dia371_rect.height + self.texts.dia372_rect.height + 45
                elif self.stats.dia == 46:
                    self.heights = self.texts.dia371_rect.height + self.texts.dia372_rect.height + 45
                elif self.stats.dia == 47:
                    self.heights = self.texts.dia381_rect.height + self.texts.dia382_rect.height + 45
                elif self.stats.dia == 48:
                    self.heights = self.texts.dia391_rect.height + self.texts.dia392_rect.height + 45
                elif self.stats.dia == 49:
                    self.heights = self.texts.dia401_rect.height + self.texts.dia402_rect.height + 45
                elif self.stats.dia == 50:
                    self.heights = self.texts.dia391_rect.height + self.texts.dia412_rect.height + 45
                elif self.stats.dia == 51:
                    self.heights = self.texts.dia411_rect.height + self.texts.dia432_rect.height + 45
                elif self.stats.dia == 52:
                    self.heights = self.texts.dia421_rect.height + self.texts.dia412_rect.height + 45
                elif self.stats.dia == 53:
                    self.heights = self.texts.dia431_rect.height + self.texts.dia432_rect.height + 45
                elif self.stats.dia == 55:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 57:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 59:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 61:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 63:
                    self.heights = self.texts.dia441_rect.height + self.texts.dia442_rect.height + 45
                elif self.stats.dia == 65:
                    self.heights = self.texts.dia451_rect.height + self.texts.dia452_rect.height + 45
                elif self.stats.dia == 67:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 69:
                    self.heights = self.texts.dia461_rect.height + self.texts.dia462_rect.height + 45
                elif self.stats.dia == 70:
                    self.heights = self.texts.dia471_rect.height + self.texts.dia472_rect.height + 45
                elif self.stats.dia == 72:
                    self.heights = self.texts.dia481_rect.height + self.texts.dia482_rect.height + 45
                elif self.stats.dia == 73:
                    self.heights = self.texts.dia491_rect.height + self.texts.dia492_rect.height + 45
                elif self.stats.dia == 74:
                    self.heights = self.texts.dia501_rect.height + self.texts.dia502_rect.height + 45
            else:
                if self.stats.kill_dia == 4:
                    self.heights = self.texts.dia71_rect.height + self.texts.dia72_rect.height + 45
                elif self.stats.kill_dia == 5:
                    self.heights = self.texts.dia81_rect.height + self.texts.dia82_rect.height + self.texts.dia83_rect.height + 45
                elif self.stats.kill_dia == 6 or self.stats.kill_dia == 8:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 40
                elif self.stats.kill_dia == 7:
                    self.heights = self.texts.dia101_rect.height + self.texts.dia102_rect.height + 45
                elif self.stats.kill_dia == 9:
                    self.heights = self.texts.dia111_rect.height + self.texts.dia112_rect.height + 45
                elif self.stats.kill_dia == 10:
                    self.heights = self.texts.dia121_rect.height + self.texts.dia122_rect.height + 45
        elif self.data[0] == 'never_beat_the_first_attack':
            if self.stats.sans_health == 1:
                if self.stats.dia == 1:
                    self.heights = self.texts.dia11_rect.height + self.texts.dia12_rect.height + 45
                elif self.stats.dia == 2:
                    self.heights = self.texts.dia21_rect.height + self.texts.dia22_rect.height + 45
                elif self.stats.dia == 3:
                    self.heights = self.texts.dia31_rect.height + self.texts.dia32_rect.height + 45
                elif self.stats.dia == 4:
                    self.heights = self.texts.dia41_rect.height + self.texts.dia42_rect.height + 45
                elif self.stats.dia == 5:
                    self.heights = self.texts.dia51_rect.height + self.texts.dia52_rect.height + 45
                elif self.stats.dia == 6:
                    self.heights = self.texts.dia61_rect.height + self.texts.dia62_rect.height + 45
                elif self.stats.dia == 9:
                    self.heights = self.texts.dia131_rect.height + self.texts.dia132_rect.height + 45
                elif self.stats.dia == 10:
                    self.heights = self.texts.dia141_rect.height + self.texts.dia142_rect.height + self.texts.dia143_rect.height + 45
                elif self.stats.dia == 12:
                    self.heights = self.texts.dia151_rect.height + self.texts.dia152_rect.height + 45
                elif self.stats.dia == 13:
                    self.heights = self.texts.dia161_rect.height + self.texts.dia162_rect.height + 45
                elif self.stats.dia == 14:
                    self.heights = self.texts.dia171_rect.height + self.texts.dia172_rect.height + 45
                elif self.stats.dia == 15:
                    self.heights = self.texts.dia181_rect.height + self.texts.dia182_rect.height + 45
                elif self.stats.dia == 16:
                    self.heights = self.texts.dia181_rect.height + self.texts.dia182_rect.height + 45
                elif self.stats.dia == 17:
                    self.heights = self.texts.dia191_rect.height + self.texts.dia192_rect.height + self.texts.dia193_rect.height + 45
                elif self.stats.dia == 18:
                    self.heights = self.texts.dia201_rect.height + self.texts.dia202_rect.height + 45
                elif self.stats.dia == 19:
                    self.heights = self.texts.dia201_rect.height + self.texts.dia202_rect.height + 45
                elif self.stats.dia == 20:
                    self.heights = self.texts.dia211_rect.height + self.texts.dia212_rect.height + 45
                elif self.stats.dia == 21:
                    self.heights = self.texts.dia221_rect.height + self.texts.dia222_rect.height + 45
                elif self.stats.dia == 22:
                    self.heights = self.texts.dia231_rect.height + self.texts.dia232_rect.height + 45
                elif self.stats.dia == 23:
                    self.heights = self.texts.dia231_rect.height + self.texts.dia232_rect.height + 45
                elif self.stats.dia == 24:
                    self.heights = self.texts.dia241_rect.height + self.texts.dia242_rect.height + 45
                elif self.stats.dia == 25:
                    self.heights = self.texts.dia251_rect.height + self.texts.dia252_rect.height + 45
                elif self.stats.dia == 26:
                    self.heights = self.texts.dia261_rect.height + self.texts.dia262_rect.height + 45
                elif self.stats.dia == 27:
                    self.heights = self.texts.dia261_rect.height + self.texts.dia262_rect.height + 45
                elif self.stats.dia == 28:
                    self.heights = self.texts.dia271_rect.height + self.texts.dia272_rect.height + 45
                elif self.stats.dia == 29:
                    self.heights = self.texts.dia281_rect.height + self.texts.dia282_rect.height + self.texts.dia283_rect.height + 45
                elif self.stats.dia == 30:
                    self.heights = self.texts.dia281_rect.height + self.texts.dia282_rect.height + self.texts.dia283_rect.height + 45
                elif self.stats.dia == 31:
                    self.heights = self.texts.dia291_rect.height + self.texts.dia292_rect.height + 45
                elif self.stats.dia == 32:
                    self.heights = self.texts.dia301_rect.height + self.texts.dia302_rect.height + 45
                elif self.stats.dia == 33:
                    self.heights = self.texts.dia311_rect.height + self.texts.dia312_rect.height + 45
                elif self.stats.dia == 34:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 35:
                    self.heights = self.texts.dia321_rect.height + self.texts.dia322_rect.height + 45
                elif self.stats.dia == 37:
                    self.heights = self.texts.dia331_rect.height + self.texts.dia332_rect.height + 45
                elif self.stats.dia == 38:
                    self.heights = self.texts.dia341_rect.height + self.texts.dia342_rect.height + 45
                elif self.stats.dia == 39:
                    self.heights = self.texts.dia351_rect.height + self.texts.dia352_rect.height + 45
                elif self.stats.dia == 40:
                    self.heights = self.texts.dia351_rect.height + self.texts.dia352_rect.height + 45
                elif self.stats.dia == 41:
                    self.heights = self.texts.dia361_rect.height + self.texts.dia362_rect.height + 45
                elif self.stats.dia == 42:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 43:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 44:
                    self.heights = self.texts.dia371_rect.height + self.texts.dia372_rect.height + 45
                elif self.stats.dia == 45:
                    self.heights = self.texts.dia371_rect.height + self.texts.dia372_rect.height + 45
                elif self.stats.dia == 46:
                    self.heights = self.texts.dia371_rect.height + self.texts.dia372_rect.height + 45
                elif self.stats.dia == 47:
                    self.heights = self.texts.dia381_rect.height + self.texts.dia382_rect.height + 45
                elif self.stats.dia == 48:
                    self.heights = self.texts.dia391_rect.height + self.texts.dia392_rect.height + 45
                elif self.stats.dia == 49:
                    self.heights = self.texts.dia401_rect.height + self.texts.dia402_rect.height + 45
                elif self.stats.dia == 50:
                    self.heights = self.texts.dia391_rect.height + self.texts.dia412_rect.height + 45
                elif self.stats.dia == 51:
                    self.heights = self.texts.dia411_rect.height + self.texts.dia432_rect.height + 45
                elif self.stats.dia == 52:
                    self.heights = self.texts.dia421_rect.height + self.texts.dia412_rect.height + 45
                elif self.stats.dia == 53:
                    self.heights = self.texts.dia431_rect.height + self.texts.dia432_rect.height + 45
                elif self.stats.dia == 55:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 57:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 59:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 61:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 63:
                    self.heights = self.texts.dia441_rect.height + self.texts.dia442_rect.height + 45
                elif self.stats.dia == 65:
                    self.heights = self.texts.dia451_rect.height + self.texts.dia452_rect.height + 45
                elif self.stats.dia == 67:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 45
                elif self.stats.dia == 69:
                    self.heights = self.texts.dia461_rect.height + self.texts.dia462_rect.height + 45
                elif self.stats.dia == 70:
                    self.heights = self.texts.dia471_rect.height + self.texts.dia472_rect.height + 45
                elif self.stats.dia == 72:
                    self.heights = self.texts.dia481_rect.height + self.texts.dia482_rect.height + 45
                elif self.stats.dia == 73:
                    self.heights = self.texts.dia491_rect.height + self.texts.dia492_rect.height + 45
                elif self.stats.dia == 74:
                    self.heights = self.texts.dia501_rect.height + self.texts.dia502_rect.height + 45
            else:
                if self.stats.kill_dia == 4:
                    self.heights = self.texts.dia71_rect.height + self.texts.dia72_rect.height + 45
                elif self.stats.kill_dia == 5:
                    self.heights = self.texts.dia81_rect.height + self.texts.dia82_rect.height + self.texts.dia83_rect.height + 45
                elif self.stats.kill_dia == 6 or self.stats.kill_dia == 8:
                    self.heights = self.texts.dia91_rect.height + self.texts.dia92_rect.height + 40
                elif self.stats.kill_dia == 7:
                    self.heights = self.texts.dia101_rect.height + self.texts.dia102_rect.height + 45
                elif self.stats.kill_dia == 9:
                    self.heights = self.texts.dia111_rect.height + self.texts.dia112_rect.height + 45
                elif self.stats.kill_dia == 10:
                    self.heights = self.texts.dia121_rect.height + self.texts.dia122_rect.height + 45

    def update_bubble_width(self):
        if self.data[0] == 'beat_the_first_attack':
            if self.stats.sans_health == 1:
                if self.stats.dia == 1:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 5:
                    self.widths = self.texts.diaAF1_rect.width + 35
                elif self.stats.dia == 6:
                    self.widths = self.texts.dia61_rect.width + 35
                elif self.stats.dia == 9:
                    self.widths = self.texts.dia131_rect.width + 35
                elif self.stats.dia == 10:
                    self.widths = self.texts.dia141_rect.width + 35
                elif self.stats.dia == 12:
                    self.widths = self.texts.dia151_rect.width + 35
                elif self.stats.dia == 13:
                    self.widths = self.texts.dia162_rect.width + 35
                elif self.stats.dia == 14:
                    self.widths = self.texts.dia171_rect.width + 35
                elif self.stats.dia == 15:
                    self.widths = self.texts.dia181_rect.width + 35
                elif self.stats.dia == 16:
                    self.widths = self.texts.dia181_rect.width + 35
                elif self.stats.dia == 17:
                    self.widths = self.texts.dia191_rect.width + 35
                elif self.stats.dia == 18:
                    self.widths = self.texts.dia201_rect.width + 35
                elif self.stats.dia == 19:
                    self.widths = self.texts.dia201_rect.width + 35
                elif self.stats.dia == 20:
                    self.widths = self.texts.dia211_rect.width + 35
                elif self.stats.dia == 21:
                    self.widths = self.texts.dia221_rect.width + 35
                elif self.stats.dia == 22:
                    self.widths = self.texts.dia231_rect.width + 35
                elif self.stats.dia == 23:
                    self.widths = self.texts.dia231_rect.width + 35
                elif self.stats.dia == 24:
                    self.widths = self.texts.dia241_rect.width + 35
                elif self.stats.dia == 25:
                    self.widths = self.texts.dia251_rect.width + 35
                elif self.stats.dia == 26:
                    self.widths = self.texts.dia262_rect.width + 35
                elif self.stats.dia == 27:
                    self.widths = self.texts.dia262_rect.width + 35
                elif self.stats.dia == 28:
                    self.widths = self.texts.dia271_rect.width + 35
                elif self.stats.dia == 29:
                    self.widths = self.texts.dia281_rect.width + 35
                elif self.stats.dia == 30:
                    self.widths = self.texts.dia281_rect.width + 35
                elif self.stats.dia == 31:
                    self.widths = self.texts.dia291_rect.width + 35
                elif self.stats.dia == 32:
                    self.widths = self.texts.dia301_rect.width + 35
                elif self.stats.dia == 33:
                    self.widths = self.texts.dia311_rect.width + 35
                elif self.stats.dia == 34:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 35:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 36:
                    self.widths = self.texts.dia321_rect.width + 35
                elif self.stats.dia == 37:
                    self.widths = self.texts.dia331_rect.width + 35
                elif self.stats.dia == 38:
                    self.widths = self.texts.dia342_rect.width + 35
                elif self.stats.dia == 39:
                    self.widths = self.texts.dia351_rect.width + 35
                elif self.stats.dia == 40:
                    self.widths = self.texts.dia351_rect.width + 35
                elif self.stats.dia == 41:
                    self.widths = self.texts.dia361_rect.width + 35
                elif self.stats.dia == 42:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 43:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 44:
                    self.widths = self.texts.dia371_rect.width + 35
                elif self.stats.dia == 45:
                    self.widths = self.texts.dia371_rect.width + 35
                elif self.stats.dia == 46:
                    self.widths = self.texts.dia371_rect.width + 35
                elif self.stats.dia == 47:
                    self.widths = self.texts.dia381_rect.width + 35
                elif self.stats.dia == 48:
                    self.widths = self.texts.dia391_rect.width + 35
                elif self.stats.dia == 49:
                    self.widths = self.texts.dia401_rect.width + 35
                elif self.stats.dia == 50:
                    self.widths = self.texts.dia391_rect.width + 35
                elif self.stats.dia == 51:
                    self.widths = self.texts.dia411_rect.width + 35
                elif self.stats.dia == 52:
                    self.widths = self.texts.dia421_rect.width + 35
                elif self.stats.dia == 53:
                    self.widths = self.texts.dia431_rect.width + 35
                elif self.stats.dia == 55:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 57:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 59:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 61:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 63:
                    self.widths = self.texts.dia441_rect.width + 35
                elif self.stats.dia == 65:
                    self.widths = self.texts.dia451_rect.width + 35
                elif self.stats.dia == 67:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 69:
                    self.widths = self.texts.dia461_rect.width + 35
                elif self.stats.dia == 70:
                    self.widths = self.texts.dia471_rect.width + 35
                elif self.stats.dia == 72:
                    self.widths = self.texts.dia481_rect.width + 35
                elif self.stats.dia == 73:
                    self.widths = self.texts.dia491_rect.width + 35
                elif self.stats.dia == 74:
                    self.widths = self.texts.dia501_rect.width + 35
            else:
                if self.stats.kill_dia == 4:
                    self.widths = self.texts.dia72_rect.width + 35
                elif self.stats.kill_dia == 5:
                    self.widths = self.texts.dia81_rect.width + 35
                elif self.stats.kill_dia == 6 or self.stats.kill_dia == 8:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.kill_dia == 7:
                    self.widths = self.texts.dia101_rect.width + 35
                elif self.stats.kill_dia == 9:
                    self.widths = self.texts.dia111_rect.width + 35
                elif self.stats.kill_dia == 10:
                    self.widths = self.texts.dia122_rect.width + 35
        elif self.data[0] == 'never_beat_the_first_attack':
            if self.stats.sans_health == 1:
                if self.stats.dia == 1:
                    self.widths = self.texts.dia11_rect.width + 35
                elif self.stats.dia == 2:
                    self.widths = self.texts.dia21_rect.width + 35
                elif self.stats.dia == 3:
                    self.widths = self.texts.dia31_rect.width + 35
                elif self.stats.dia == 4:
                    self.widths = self.texts.dia41_rect.width + 35
                elif self.stats.dia == 5:
                    self.widths = self.texts.dia51_rect.width + 35
                elif self.stats.dia == 6:
                    self.widths = self.texts.dia61_rect.width + 35
                elif self.stats.dia == 9:
                    self.widths = self.texts.dia131_rect.width + 35
                elif self.stats.dia == 10:
                    self.widths = self.texts.dia141_rect.width + 35
                elif self.stats.dia == 12:
                    self.widths = self.texts.dia151_rect.width + 35
                elif self.stats.dia == 13:
                    self.widths = self.texts.dia162_rect.width + 35
                elif self.stats.dia == 14:
                    self.widths = self.texts.dia171_rect.width + 35
                elif self.stats.dia == 15:
                    self.widths = self.texts.dia181_rect.width + 35
                elif self.stats.dia == 16:
                    self.widths = self.texts.dia181_rect.width + 35
                elif self.stats.dia == 17:
                    self.widths = self.texts.dia191_rect.width + 35
                elif self.stats.dia == 18:
                    self.widths = self.texts.dia201_rect.width + 35
                elif self.stats.dia == 19:
                    self.widths = self.texts.dia201_rect.width + 35
                elif self.stats.dia == 20:
                    self.widths = self.texts.dia211_rect.width + 35
                elif self.stats.dia == 21:
                    self.widths = self.texts.dia221_rect.width + 35
                elif self.stats.dia == 22:
                    self.widths = self.texts.dia231_rect.width + 35
                elif self.stats.dia == 23:
                    self.widths = self.texts.dia231_rect.width + 35
                elif self.stats.dia == 24:
                    self.widths = self.texts.dia241_rect.width + 35
                elif self.stats.dia == 25:
                    self.widths = self.texts.dia251_rect.width + 35
                elif self.stats.dia == 26:
                    self.widths = self.texts.dia262_rect.width + 35
                elif self.stats.dia == 27:
                    self.widths = self.texts.dia262_rect.width + 35
                elif self.stats.dia == 28:
                    self.widths = self.texts.dia271_rect.width + 35
                elif self.stats.dia == 29:
                    self.widths = self.texts.dia281_rect.width + 35
                elif self.stats.dia == 30:
                    self.widths = self.texts.dia281_rect.width + 35
                elif self.stats.dia == 31:
                    self.widths = self.texts.dia291_rect.width + 35
                elif self.stats.dia == 32:
                    self.widths = self.texts.dia301_rect.width + 35
                elif self.stats.dia == 33:
                    self.widths = self.texts.dia311_rect.width + 35
                elif self.stats.dia == 34:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 35:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 36:
                    self.widths = self.texts.dia321_rect.width + 35
                elif self.stats.dia == 37:
                    self.widths = self.texts.dia331_rect.width + 35
                elif self.stats.dia == 38:
                    self.widths = self.texts.dia342_rect.width + 35
                elif self.stats.dia == 39:
                    self.widths = self.texts.dia351_rect.width + 35
                elif self.stats.dia == 40:
                    self.widths = self.texts.dia351_rect.width + 35
                elif self.stats.dia == 41:
                    self.widths = self.texts.dia361_rect.width + 35
                elif self.stats.dia == 42:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 43:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 44:
                    self.widths = self.texts.dia371_rect.width + 35
                elif self.stats.dia == 45:
                    self.widths = self.texts.dia371_rect.width + 35
                elif self.stats.dia == 46:
                    self.widths = self.texts.dia371_rect.width + 35
                elif self.stats.dia == 47:
                    self.widths = self.texts.dia381_rect.width + 35
                elif self.stats.dia == 48:
                    self.widths = self.texts.dia391_rect.width + 35
                elif self.stats.dia == 49:
                    self.widths = self.texts.dia401_rect.width + 35
                elif self.stats.dia == 50:
                    self.widths = self.texts.dia391_rect.width + 35
                elif self.stats.dia == 51:
                    self.widths = self.texts.dia411_rect.width + 35
                elif self.stats.dia == 52:
                    self.widths = self.texts.dia421_rect.width + 35
                elif self.stats.dia == 53:
                    self.widths = self.texts.dia431_rect.width + 35
                elif self.stats.dia == 55:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 57:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 59:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 61:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 63:
                    self.widths = self.texts.dia441_rect.width + 35
                elif self.stats.dia == 65:
                    self.widths = self.texts.dia451_rect.width + 35
                elif self.stats.dia == 67:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.dia == 69:
                    self.widths = self.texts.dia461_rect.width + 35
                elif self.stats.dia == 70:
                    self.widths = self.texts.dia471_rect.width + 35
                elif self.stats.dia == 72:
                    self.widths = self.texts.dia481_rect.width + 35
                elif self.stats.dia == 73:
                    self.widths = self.texts.dia491_rect.width + 35
                elif self.stats.dia == 74:
                    self.widths = self.texts.dia501_rect.width + 35
            else:
                if self.stats.kill_dia == 4:
                    self.widths = self.texts.dia72_rect.width + 35
                elif self.stats.kill_dia == 5:
                    self.widths = self.texts.dia81_rect.width + 35
                elif self.stats.kill_dia == 6 or self.stats.kill_dia == 8:
                    self.widths = self.texts.dia91_rect.width + 35
                elif self.stats.kill_dia == 7:
                    self.widths = self.texts.dia101_rect.width + 35
                elif self.stats.kill_dia == 9:
                    self.widths = self.texts.dia111_rect.width + 35
                elif self.stats.kill_dia == 10:
                    self.widths = self.texts.dia122_rect.width + 35

    def speech_bubble(self):
        self.bubble_stem()
        self.update_bubble_height()
        self.update_bubble_width()

        self.speech = pygame.image.load('images/speech_bubble.png').convert_alpha()
        self.speech = pygame.transform.scale(self.speech, (self.widths, self.heights)).convert_alpha()

        self.speech_rect = self.speech.get_rect()
        self.speech_rect.left = self.stem_rect.right
        self.speech_rect.y += 35

    def bubble_stem(self):
        self.stem = pygame.image.load('images/speech_bubble_stem.png').convert_alpha()

        self.stem_rect = self.stem.get_rect()
        self.stem_rect.left = self.sans_rect.right
        self.stem_rect.y += 85
        self.stem_rect.x -= 45

    def show_speech(self):
        self.screen.blit(self.speech, self.speech_rect)

    def show_stem(self):
        self.screen.blit(self.stem, self.stem_rect)