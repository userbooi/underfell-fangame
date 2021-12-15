import pygame.font
import pygame

class Text:

    def __init__(self, UF_game):

        self.screen = UF_game.screen
        self.stats = UF_game.stats
        self.setting = UF_game.settings
        self.heart = UF_game.heart
        self.fight = UF_game.fighted
        self.ufgame = UF_game

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('comicsansms', 17)

        with open('data/data.txt', 'r') as d:
            self.data = d.read()
            self.data = self.data.split(' ')

        self.D1()
        self.D2()
        self.D3()
        self.D4()
        self.D5()
        self.D6()
        self.D7()
        self.D8()
        self.D9()
        self.D10()
        self.D11()
        self.D12()
        self.D13()
        self.D14()
        self.D15()
        self.D16()
        self.D17()
        self.D18()
        self.D19()
        self.D20()
        self.D21()
        self.D22()
        self.D23()
        self.D24()
        self.D25()
        self.D26()
        self.D27()
        self.D28()
        self.D29()
        self.D30()
        self.D31()
        self.D32()
        self.D33()
        self.D34()
        self.D35()
        self.D36()
        self.D37()
        self.D38()
        self.D39()
        self.D40()
        self.D41()
        self.D42()
        self.D43()
        self.D44()
        self.KD1()
        self.KD2()
        self.KD3()
        self.KD4()
        self.KD5()
        self.KD6()
        self.AFD()

    def D1(self):
        dialogue = 'Its a terrible day'
        dialogue2 = 'outside'
        self.dia11 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia11_rect = self.dia11.get_rect()
        self.dia11_rect.x = 583
        self.dia11_rect.y = 50

        self.dia12 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia12_rect = self.dia12.get_rect()
        self.dia12_rect.top = self.dia11_rect.bottom
        self.dia12_rect.left = self.dia11_rect.left

    def D2(self):
        dialogue = "birds aren't flying..."
        dialogue2 = ''
        self.dia21 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia21_rect = self.dia21.get_rect()
        self.dia21_rect.x = 583
        self.dia21_rect.y = 50

        self.dia22 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia22_rect = self.dia22.get_rect()
        self.dia22_rect.top = self.dia21_rect.bottom
        self.dia22_rect.left = self.dia21_rect.left

    def D3(self):
        dialogue = 'flowers are dying...'
        dialogue2 = ''
        self.dia31 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia31_rect = self.dia31.get_rect()
        self.dia31_rect.x = 583
        self.dia31_rect.y = 50

        self.dia32 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia32_rect = self.dia32.get_rect()
        self.dia32_rect.top = self.dia31_rect.bottom
        self.dia32_rect.left = self.dia31_rect.left

    def D4(self):
        dialogue = 'and if you spare'
        dialogue2 = 'me, well'
        self.dia41 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia41_rect = self.dia41.get_rect()
        self.dia41_rect.x = 583
        self.dia41_rect.y = 50

        self.dia42 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia42_rect = self.dia42.get_rect()
        self.dia42_rect.top = self.dia41_rect.bottom
        self.dia42_rect.left = self.dia41_rect.left

    def D5(self):
        dialogue = 'I WILL HAVE A'
        dialogue2 = 'GREAT TIME!'
        self.dia51 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia51_rect = self.dia51.get_rect()
        self.dia51_rect.x = 583
        self.dia51_rect.y = 50

        self.dia52 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia52_rect = self.dia52.get_rect()
        self.dia52_rect.top = self.dia51_rect.bottom
        self.dia52_rect.left = self.dia51_rect.left

    def D6(self):
        dialogue = "let's start"
        dialogue2 = ''
        self.dia61 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia61_rect = self.dia61.get_rect()
        self.dia61_rect.x = 583
        self.dia61_rect.y = 50

        self.dia62 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia62_rect = self.dia62.get_rect()
        self.dia62_rect.left = self.dia61_rect.left
        self.dia62_rect.top = self.dia61_rect.bottom

    def D7(self):
        dialogue = "as always, you"
        dialogue2 = "won't fight."
        self.dia131 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia131_rect = self.dia131.get_rect()
        self.dia131_rect.x = 583
        self.dia131_rect.y = 50

        self.dia132 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia132_rect = self.dia132.get_rect()
        self.dia132_rect.left = self.dia131_rect.left
        self.dia132_rect.top = self.dia131_rect.bottom

    def D8(self):
        dialogue = "But, I got news"
        dialogue2 = "for you, this"
        dialogue3 = "won't work"
        self.dia141 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia141_rect = self.dia141.get_rect()
        self.dia141_rect.x = 583
        self.dia141_rect.y = 50

        self.dia142 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia142_rect = self.dia142.get_rect()
        self.dia142_rect.left = self.dia141_rect.left
        self.dia142_rect.top = self.dia141_rect.bottom

        self.dia143 = self.font.render(dialogue3, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia143_rect = self.dia143.get_rect()
        self.dia143_rect.left = self.dia142_rect.left
        self.dia143_rect.top = self.dia142_rect.bottom

    def D9(self):
        dialogue = "you spared every"
        dialogue2 = "one."
        self.dia151 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia151_rect = self.dia151.get_rect()
        self.dia151_rect.x = 583
        self.dia151_rect.y = 50

        self.dia152 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia152_rect = self.dia152.get_rect()
        self.dia152_rect.left = self.dia151_rect.left
        self.dia152_rect.top = self.dia151_rect.bottom

    def D10(self):
        dialogue = "even when they"
        dialogue2 = "tried to kill you."
        self.dia161 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia161_rect = self.dia161.get_rect()
        self.dia161_rect.x = 583
        self.dia161_rect.y = 50

        self.dia162 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia162_rect = self.dia162.get_rect()
        self.dia162_rect.left = self.dia161_rect.left
        self.dia162_rect.top = self.dia161_rect.bottom

    def D11(self):
        dialogue = "I just want to"
        dialogue2 = "know why?"
        self.dia171 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia171_rect = self.dia171.get_rect()
        self.dia171_rect.x = 583
        self.dia171_rect.y = 50

        self.dia172 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia172_rect = self.dia172.get_rect()
        self.dia172_rect.left = self.dia171_rect.left
        self.dia172_rect.top = self.dia171_rect.bottom

    def D12(self):
        dialogue = "you have been nice"
        dialogue2 = "from the start"
        self.dia181 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia181_rect = self.dia181.get_rect()
        self.dia181_rect.x = 583
        self.dia181_rect.y = 50

        self.dia182 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia182_rect = self.dia182.get_rect()
        self.dia182_rect.left = self.dia181_rect.left
        self.dia182_rect.top = self.dia181_rect.bottom

    def D13(self):
        dialogue = "where you just"
        dialogue2 = "trying to change"
        dialogue3 = "our ways?"
        self.dia191 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia191_rect = self.dia191.get_rect()
        self.dia191_rect.x = 583
        self.dia191_rect.y = 50

        self.dia192 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia192_rect = self.dia192.get_rect()
        self.dia192_rect.left = self.dia191_rect.left
        self.dia192_rect.top = self.dia191_rect.bottom

        self.dia193 = self.font.render(dialogue3, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia193_rect = self.dia193.get_rect()
        self.dia193_rect.left = self.dia192_rect.left
        self.dia193_rect.top = self.dia192_rect.bottom

    def D14(self):
        dialogue = "c'mon kid, just"
        dialogue2 = "hit me"
        self.dia201 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia201_rect = self.dia201.get_rect()
        self.dia201_rect.x = 583
        self.dia201_rect.y = 50

        self.dia202 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia202_rect = self.dia202.get_rect()
        self.dia202_rect.left = self.dia201_rect.left
        self.dia202_rect.top = self.dia201_rect.bottom

    def D15(self):
        dialogue = "i promise..."
        dialogue2 = ""
        self.dia211 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia211_rect = self.dia211.get_rect()
        self.dia211_rect.x = 583
        self.dia211_rect.y = 50

        self.dia212 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia212_rect = self.dia212.get_rect()
        self.dia212_rect.left = self.dia211_rect.left
        self.dia212_rect.top = self.dia211_rect.bottom

    def D16(self):
        dialogue = "i won't dodge"
        dialogue2 = ""
        self.dia221 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia221_rect = self.dia221.get_rect()
        self.dia221_rect.x = 583
        self.dia221_rect.y = 50

        self.dia222 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia222_rect = self.dia222.get_rect()
        self.dia222_rect.left = self.dia221_rect.left
        self.dia222_rect.top = self.dia221_rect.bottom

    def D17(self):
        dialogue = "even knowing that you"
        dialogue2 = "are persistent"
        self.dia231 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia231_rect = self.dia231.get_rect()
        self.dia231_rect.x = 583
        self.dia231_rect.y = 50

        self.dia232 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia232_rect = self.dia232.get_rect()
        self.dia232_rect.left = self.dia231_rect.left
        self.dia232_rect.top = self.dia231_rect.bottom

    def D18(self):
        dialogue = "seeing you got through"
        dialogue2 = "to undyne"
        self.dia241 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia241_rect = self.dia241.get_rect()
        self.dia241_rect.x = 583
        self.dia241_rect.y = 50

        self.dia242 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia242_rect = self.dia242.get_rect()
        self.dia242_rect.left = self.dia241_rect.left
        self.dia242_rect.top = self.dia241_rect.bottom

    def D19(self):
        dialogue = "I thought you would"
        dialogue2 = "have given up by now"
        self.dia251 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia251_rect = self.dia251.get_rect()
        self.dia251_rect.x = 583
        self.dia251_rect.y = 50

        self.dia252 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia252_rect = self.dia252.get_rect()
        self.dia252_rect.left = self.dia251_rect.left
        self.dia252_rect.top = self.dia251_rect.bottom

    def D20(self):
        dialogue = "Please, just kill"
        dialogue2 = "me and take my LV"
        self.dia261 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia261_rect = self.dia261.get_rect()
        self.dia261_rect.x = 583
        self.dia261_rect.y = 50

        self.dia262 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia262_rect = self.dia262.get_rect()
        self.dia262_rect.left = self.dia261_rect.left
        self.dia262_rect.top = self.dia261_rect.bottom

    def D21(self):
        dialogue = "kill the king, free"
        dialogue2 = "the underground"
        self.dia271 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia271_rect = self.dia271.get_rect()
        self.dia271_rect.x = 583
        self.dia271_rect.y = 50

        self.dia272 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia272_rect = self.dia272.get_rect()
        self.dia272_rect.left = self.dia271_rect.left
        self.dia272_rect.top = self.dia271_rect.bottom

    def D22(self):
        dialogue = "even if you were"
        dialogue2 = "trying to do"
        dialogue3 = "'GOOD'"
        self.dia281 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia281_rect = self.dia281.get_rect()
        self.dia281_rect.x = 583
        self.dia281_rect.y = 50

        self.dia282 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia282_rect = self.dia282.get_rect()
        self.dia282_rect.left = self.dia281_rect.left
        self.dia282_rect.top = self.dia281_rect.bottom

        self.dia283 = self.font.render(dialogue3, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia283_rect = self.dia283.get_rect()
        self.dia283_rect.left = self.dia271_rect.left
        self.dia283_rect.top = self.dia282_rect.bottom

    def D23(self):
        dialogue = "time lines were still"
        dialogue2 = "starting and stopping"
        self.dia291 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia291_rect = self.dia291.get_rect()
        self.dia291_rect.x = 583
        self.dia291_rect.y = 50

        self.dia292 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia292_rect = self.dia292.get_rect()
        self.dia292_rect.left = self.dia291_rect.left
        self.dia292_rect.top = self.dia291_rect.bottom

    def D24(self):
        dialogue = "he he he..."
        dialogue2 = ''
        self.dia301 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia301_rect = self.dia301.get_rect()
        self.dia301_rect.x = 583
        self.dia301_rect.y = 50

        self.dia302 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia302_rect = self.dia302.get_rect()
        self.dia302_rect.left = self.dia301_rect.left
        self.dia302_rect.top = self.dia301_rect.bottom

    def D25(self):
        dialogue = "looks like they still"
        dialogue2 = "gave you a hard time"
        self.dia311 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia311_rect = self.dia311.get_rect()
        self.dia311_rect.x = 583
        self.dia311_rect.y = 50

        self.dia312 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia312_rect = self.dia312.get_rect()
        self.dia312_rect.left = self.dia311_rect.left
        self.dia312_rect.top = self.dia311_rect.bottom

    def D26(self):
        dialogue = "well, you see... "
        dialogue2 = ""
        self.dia321 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia321_rect = self.dia321.get_rect()
        self.dia321_rect.x = 583
        self.dia321_rect.y = 50

        self.dia322 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia322_rect = self.dia322.get_rect()
        self.dia322_rect.left = self.dia321_rect.left
        self.dia322_rect.top = self.dia321_rect.bottom

    def D27(self):
        dialogue = "I'm getting a bit"
        dialogue2 = "tired"
        self.dia331 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia331_rect = self.dia331.get_rect()
        self.dia331_rect.x = 583
        self.dia331_rect.y = 50

        self.dia332 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia332_rect = self.dia332.get_rect()
        self.dia332_rect.left = self.dia331_rect.left
        self.dia332_rect.top = self.dia331_rect.bottom

    def D28(self):
        dialogue = "so please, end me"
        dialogue2 = "while I'm weekended"
        self.dia341 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia341_rect = self.dia341.get_rect()
        self.dia341_rect.x = 583
        self.dia341_rect.y = 50

        self.dia342 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia342_rect = self.dia342.get_rect()
        self.dia342_rect.left = self.dia341_rect.left
        self.dia342_rect.top = self.dia341_rect.bottom

    def D29(self):
        dialogue = "please..."
        dialogue2 = ""
        self.dia351 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia351_rect = self.dia351.get_rect()
        self.dia351_rect.x = 583
        self.dia351_rect.y = 50

        self.dia352 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia352_rect = self.dia352.get_rect()
        self.dia352_rect.left = self.dia351_rect.left
        self.dia352_rect.top = self.dia351_rect.bottom

    def D30(self):
        dialogue = "just do it"
        dialogue2 = ""
        self.dia361 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia361_rect = self.dia361.get_rect()
        self.dia361_rect.x = 583
        self.dia361_rect.y = 50

        self.dia362 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia362_rect = self.dia362.get_rect()
        self.dia362_rect.left = self.dia361_rect.left
        self.dia362_rect.top = self.dia361_rect.bottom

    def D31(self):
        dialogue = "you didn't fight?"
        dialogue2 = ""
        self.dia371 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia371_rect = self.dia371.get_rect()
        self.dia371_rect.x = 583
        self.dia371_rect.y = 50

        self.dia372 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia372_rect = self.dia372.get_rect()
        self.dia372_rect.left = self.dia371_rect.left
        self.dia372_rect.top = self.dia371_rect.bottom

    def D32(self):
        dialogue = "even when I was"
        dialogue2 = "left wide open"
        self.dia381 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia381_rect = self.dia381.get_rect()
        self.dia381_rect.x = 583
        self.dia381_rect.y = 50

        self.dia382 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia382_rect = self.dia382.get_rect()
        self.dia382_rect.left = self.dia381_rect.left
        self.dia382_rect.top = self.dia381_rect.bottom

    def D33(self):
        dialogue = "he he he..."
        dialogue2 = ""
        self.dia391 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia391_rect = self.dia391.get_rect()
        self.dia391_rect.x = 583
        self.dia391_rect.y = 50

        self.dia392 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia392_rect = self.dia392.get_rect()
        self.dia392_rect.left = self.dia391_rect.left
        self.dia392_rect.top = self.dia391_rect.bottom

    def D34(self):
        dialogue = "I'm done with this"
        dialogue2 = ""
        self.dia401 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia401_rect = self.dia401.get_rect()
        self.dia401_rect.x = 583
        self.dia401_rect.y = 50

        self.dia402 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia402_rect = self.dia402.get_rect()
        self.dia402_rect.left = self.dia401_rect.left
        self.dia402_rect.top = self.dia401_rect.bottom

    def D35(self):
        dialogue = "ha ha ha ha"
        dialogue2 = ""
        self.dia411 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia411_rect = self.dia411.get_rect()
        self.dia411_rect.x = 583
        self.dia411_rect.y = 50

        self.dia412 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia412_rect = self.dia412.get_rect()
        self.dia412_rect.left = self.dia411_rect.left
        self.dia412_rect.top = self.dia411_rect.bottom

    def D36(self):
        dialogue = "HA HA HA HA"
        dialogue2 = "HA HA HA HA"
        self.dia421 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia421_rect = self.dia421.get_rect()
        self.dia421_rect.x = 583
        self.dia421_rect.y = 50

        self.dia422 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia422_rect = self.dia422.get_rect()
        self.dia422_rect.left = self.dia421_rect.left
        self.dia422_rect.top = self.dia421_rect.bottom

    def D37(self):
        dialogue = "YOU WILL NOW"
        dialogue2 = "DIE!!!"
        self.dia431 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia431_rect = self.dia431.get_rect()
        self.dia431_rect.x = 583
        self.dia431_rect.y = 50

        self.dia432 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia432_rect = self.dia432.get_rect()
        self.dia432_rect.left = self.dia431_rect.left
        self.dia432_rect.top = self.dia431_rect.bottom

    def D38(self):
        dialogue = "a knife should be"
        dialogue2 = "inside my back..."
        self.dia441 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia441_rect = self.dia441.get_rect()
        self.dia441_rect.x = 583
        self.dia441_rect.y = 50

        self.dia442 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia442_rect = self.dia442.get_rect()
        self.dia442_rect.left = self.dia441_rect.left
        self.dia442_rect.top = self.dia441_rect.bottom

    def D39(self):
        dialogue = "why do you insist"
        dialogue2 = "on sparing?"
        self.dia451 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia451_rect = self.dia451.get_rect()
        self.dia451_rect.x = 583
        self.dia451_rect.y = 50

        self.dia452 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia452_rect = self.dia452.get_rect()
        self.dia452_rect.left = self.dia451_rect.left
        self.dia452_rect.top = self.dia451_rect.bottom

    def D40(self):
        dialogue = "maybe, I should give"
        dialogue2 = "kindness a chance"
        self.dia461 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia461_rect = self.dia461.get_rect()
        self.dia461_rect.x = 583
        self.dia461_rect.y = 50

        self.dia462 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia462_rect = self.dia462.get_rect()
        self.dia462_rect.left = self.dia461_rect.left
        self.dia462_rect.top = self.dia461_rect.bottom

    def D41(self):
        dialogue = "I... really have"
        dialogue2 = "nothin to lose"
        self.dia471 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia471_rect = self.dia471.get_rect()
        self.dia471_rect.x = 583
        self.dia471_rect.y = 50

        self.dia472 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia472_rect = self.dia472.get_rect()
        self.dia472_rect.left = self.dia471_rect.left
        self.dia472_rect.top = self.dia471_rect.bottom

    def D42(self):
        dialogue = "papyrus and I might"
        dialogue2 = "have normal chats"
        self.dia481 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia481_rect = self.dia481.get_rect()
        self.dia481_rect.x = 583
        self.dia481_rect.y = 50

        self.dia482 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia482_rect = self.dia482.get_rect()
        self.dia482_rect.left = self.dia481_rect.left
        self.dia482_rect.top = self.dia481_rect.bottom

    def D43(self):
        dialogue = "I might even make"
        dialogue2 = "friends"
        self.dia491 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia491_rect = self.dia491.get_rect()
        self.dia491_rect.x = 583
        self.dia491_rect.y = 50

        self.dia492 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia492_rect = self.dia492.get_rect()
        self.dia492_rect.left = self.dia491_rect.left
        self.dia492_rect.top = self.dia491_rect.bottom

    def D44(self):
        dialogue = "thanks"
        dialogue2 = ""
        self.dia501 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia501_rect = self.dia501.get_rect()
        self.dia501_rect.x = 583
        self.dia501_rect.y = 50

        self.dia502 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia502_rect = self.dia502.get_rect()
        self.dia502_rect.left = self.dia501_rect.left
        self.dia502_rect.top = self.dia501_rect.bottom

    def KD1(self):
        dialogue = 'so, you finally'
        dialogue2 = 'decided to fight'
        self.dia71 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia71_rect = self.dia71.get_rect()
        self.dia71_rect.x = 583
        self.dia71_rect.y = 50

        self.dia72 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia72_rect = self.dia72.get_rect()
        self.dia72_rect.left = self.dia71_rect.left
        self.dia72_rect.top = self.dia71_rect.bottom

    def KD2(self):
        dialogue = 'You should have done'
        dialogue2 = 'this from the'
        dialogue3 = 'beginning'
        self.dia81 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia81_rect = self.dia81.get_rect()
        self.dia81_rect.x = 583
        self.dia81_rect.y = 50

        self.dia82 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia82_rect = self.dia82.get_rect()
        self.dia82_rect.left = self.dia81_rect.left
        self.dia82_rect.top = self.dia81_rect.bottom

        self.dia83 = self.font.render(dialogue3, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia83_rect = self.dia83.get_rect()
        self.dia83_rect.left = self.dia82_rect.left
        self.dia83_rect.top = self.dia82_rect.bottom

    def KD3(self):
        dialogue = '...            '
        dialogue2 = ''
        self.dia91 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia91_rect = self.dia91.get_rect()
        self.dia91_rect.x = 583
        self.dia91_rect.y = 50

        self.dia92 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia92_rect = self.dia92.get_rect()
        self.dia92_rect.left = self.dia91_rect.left
        self.dia92_rect.top = self.dia91_rect.bottom

    def KD4(self):
        dialogue = 'it woulda been...'
        dialogue2 = 'more easier...'
        self.dia101 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia101_rect = self.dia101.get_rect()
        self.dia101_rect.x = 583
        self.dia101_rect.y = 50

        self.dia102 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia102_rect = self.dia102.get_rect()
        self.dia102_rect.left = self.dia101_rect.left
        self.dia102_rect.top = self.dia101_rect.bottom

    def KD5(self):
        dialogue = 'take my LV and...'
        dialogue2 = 'finish the king'
        self.dia111 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia111_rect = self.dia111.get_rect()
        self.dia111_rect.x = 583
        self.dia111_rect.y = 50

        self.dia112 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia112_rect = self.dia112.get_rect()
        self.dia112_rect.left = self.dia111_rect.left
        self.dia112_rect.top = self.dia111_rect.bottom

    def KD6(self):
        dialogue = 'free... the...'
        dialogue2 = 'underground.....'
        self.dia121 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia121_rect = self.dia121.get_rect()
        self.dia121_rect.x = 583
        self.dia121_rect.y = 50

        self.dia122 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.dia122_rect = self.dia122.get_rect()
        self.dia122_rect.left = self.dia121_rect.left
        self.dia122_rect.top = self.dia121_rect.bottom

    def AFD(self):
        dialogue = "let's just get"
        dialogue2 = 'to the point'
        self.diaAF1 = self.font.render(dialogue, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.diaAF1_rect = self.diaAF1.get_rect()
        self.diaAF1_rect.x = 583
        self.diaAF1_rect.y = 50

        self.diaAF2 = self.font.render(dialogue2, True, self.text_color, self.setting.text_bg).convert_alpha()

        self.diaAF2_rect = self.diaAF2.get_rect()
        self.diaAF2_rect.left = self.diaAF1_rect.left
        self.diaAF2_rect.top = self.diaAF1_rect.bottom

    def show_D(self):
        if self.data[0] == 'never_beat_the_first_attack':
            if self.stats.dia == 1 and self.stats.sans_health == 1:
                self.screen.blit(self.dia11, self.dia11_rect)
                self.screen.blit(self.dia12, self.dia12_rect)

            elif self.stats.dia == 2 and self.stats.sans_health == 1:
                self.screen.blit(self.dia21, self.dia21_rect)
                self.screen.blit(self.dia22, self.dia22_rect)

            elif self.stats.dia == 3 and self.stats.sans_health == 1:
                self.screen.blit(self.dia31, self.dia31_rect)
                self.screen.blit(self.dia32, self.dia32_rect)

            elif self.stats.dia == 4 and self.stats.sans_health == 1:
                self.screen.blit(self.dia41, self.dia41_rect)
                self.screen.blit(self.dia42, self.dia42_rect)

            elif self.stats.dia == 5 and self.stats.sans_health == 1:
                self.screen.blit(self.dia51, self.dia51_rect)
                self.screen.blit(self.dia52, self.dia52_rect)

            elif self.stats.dia == 6 and self.stats.sans_health == 1:
                self.stats.heart_color = 'red'
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 7 and self.stats.sans_health == 1:
                self.screen.blit(self.dia61, self.dia61_rect)
                self.screen.blit(self.dia62, self.dia62_rect)

            elif self.stats.dia == 8 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'
                self.fight = True
                self.ufgame.fighted = self.fight

            elif self.stats.dia == 9 and self.stats.sans_health == 1:
                self.screen.blit(self.dia131, self.dia131_rect)
                self.screen.blit(self.dia132, self.dia132_rect)

            elif self.stats.dia == 10 and self.stats.sans_health == 1:
                self.screen.blit(self.dia141, self.dia141_rect)
                self.screen.blit(self.dia142, self.dia142_rect)
                self.screen.blit(self.dia143, self.dia143_rect)

            elif self.stats.dia == 11 and self.stats.sans_health == 1:
                self.stats.turn = 'sans turn'
                self.stats.sans_amount += 1
                self.heart.reset_pos()

            elif self.stats.dia == 12 and self.stats.sans_health == 1:
                self.screen.blit(self.dia151, self.dia151_rect)
                self.screen.blit(self.dia152, self.dia152_rect)

            elif self.stats.dia == 13 and self.stats.sans_health == 1:
                self.screen.blit(self.dia161, self.dia161_rect)
                self.screen.blit(self.dia162, self.dia162_rect)

            elif self.stats.dia == 14 and self.stats.sans_health == 1:
                self.screen.blit(self.dia171, self.dia171_rect)
                self.screen.blit(self.dia172, self.dia172_rect)

            elif self.stats.dia == 15 and self.stats.sans_health == 1:
                self.stats.turn = 'sans turn'
                self.stats.sans_amount += 1
                self.heart.reset_pos()

            elif self.stats.dia == 16 and self.stats.sans_health == 1:
                self.screen.blit(self.dia181, self.dia181_rect)
                self.screen.blit(self.dia182, self.dia182_rect)

            elif self.stats.dia == 17 and self.stats.sans_health == 1:
                self.screen.blit(self.dia191, self.dia191_rect)
                self.screen.blit(self.dia192, self.dia192_rect)
                self.screen.blit(self.dia193, self.dia193_rect)

            elif self.stats.dia == 18 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 19 and self.stats.sans_health == 1:
                self.screen.blit(self.dia201, self.dia201_rect)
                self.screen.blit(self.dia202, self.dia202_rect)

            elif self.stats.dia == 20 and self.stats.sans_health == 1:
                self.screen.blit(self.dia211, self.dia211_rect)
                self.screen.blit(self.dia212, self.dia212_rect)

            elif self.stats.dia == 21 and self.stats.sans_health == 1:
                self.screen.blit(self.dia221, self.dia221_rect)
                self.screen.blit(self.dia222, self.dia222_rect)

            elif self.stats.dia == 22 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 23 and self.stats.sans_health == 1:
                self.screen.blit(self.dia231, self.dia231_rect)
                self.screen.blit(self.dia232, self.dia232_rect)

            elif self.stats.dia == 24 and self.stats.sans_health == 1:
                self.screen.blit(self.dia241, self.dia241_rect)
                self.screen.blit(self.dia242, self.dia242_rect)

            elif self.stats.dia == 25 and self.stats.sans_health == 1:
                self.screen.blit(self.dia251, self.dia251_rect)
                self.screen.blit(self.dia252, self.dia252_rect)

            elif self.stats.dia == 26 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 27 and self.stats.sans_health == 1:
                self.screen.blit(self.dia261, self.dia261_rect)
                self.screen.blit(self.dia262, self.dia262_rect)

            elif self.stats.dia == 28 and self.stats.sans_health == 1:
                self.screen.blit(self.dia271, self.dia271_rect)
                self.screen.blit(self.dia272, self.dia272_rect)

            elif self.stats.dia == 29 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 30 and self.stats.sans_health == 1:
                self.screen.blit(self.dia281, self.dia281_rect)
                self.screen.blit(self.dia282, self.dia282_rect)
                self.screen.blit(self.dia283, self.dia283_rect)

            elif self.stats.dia == 31 and self.stats.sans_health == 1:
                self.screen.blit(self.dia291, self.dia291_rect)
                self.screen.blit(self.dia292, self.dia292_rect)

            elif self.stats.dia == 32 and self.stats.sans_health == 1:
                self.screen.blit(self.dia301, self.dia301_rect)
                self.screen.blit(self.dia302, self.dia302_rect)

            elif self.stats.dia == 33 and self.stats.sans_health == 1:
                self.screen.blit(self.dia311, self.dia311_rect)
                self.screen.blit(self.dia312, self.dia312_rect)

            elif self.stats.dia == 34 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 35 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 36 and self.stats.sans_health == 1:
                self.screen.blit(self.dia321, self.dia321_rect)
                self.screen.blit(self.dia322, self.dia322_rect)

            elif self.stats.dia == 37 and self.stats.sans_health == 1:
                self.screen.blit(self.dia331, self.dia331_rect)
                self.screen.blit(self.dia332, self.dia332_rect)

            elif self.stats.dia == 38 and self.stats.sans_health == 1:
                self.screen.blit(self.dia341, self.dia341_rect)
                self.screen.blit(self.dia342, self.dia342_rect)

            elif self.stats.dia == 39 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 40 and self.stats.sans_health == 1:
                self.screen.blit(self.dia351, self.dia351_rect)
                self.screen.blit(self.dia352, self.dia352_rect)

            elif self.stats.dia == 41 and self.stats.sans_health == 1:
                self.screen.blit(self.dia361, self.dia361_rect)
                self.screen.blit(self.dia362, self.dia362_rect)

            elif self.stats.dia == 42 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 43 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 44 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 46 and self.stats.sans_health == 1:
                self.screen.blit(self.dia371, self.dia371_rect)
                self.screen.blit(self.dia372, self.dia372_rect)

            elif self.stats.dia == 47 and self.stats.sans_health == 1:
                self.screen.blit(self.dia381, self.dia381_rect)
                self.screen.blit(self.dia382, self.dia382_rect)

            elif self.stats.dia == 48 and self.stats.sans_health == 1:
                self.screen.blit(self.dia391, self.dia391_rect)
                self.screen.blit(self.dia392, self.dia392_rect)

            elif self.stats.dia == 49 and self.stats.sans_health == 1:
                self.screen.blit(self.dia401, self.dia401_rect)
                self.screen.blit(self.dia402, self.dia402_rect)

            elif self.stats.dia == 50 and self.stats.sans_health == 1:
                self.screen.blit(self.dia391, self.dia391_rect)
                self.screen.blit(self.dia392, self.dia392_rect)

            elif self.stats.dia == 51 and self.stats.sans_health == 1:
                self.screen.blit(self.dia411, self.dia411_rect)
                self.screen.blit(self.dia412, self.dia412_rect)

            elif self.stats.dia == 52 and self.stats.sans_health == 1:
                self.screen.blit(self.dia421, self.dia421_rect)
                self.screen.blit(self.dia422, self.dia422_rect)

            elif self.stats.dia == 53 and self.stats.sans_health == 1:
                self.screen.blit(self.dia431, self.dia431_rect)
                self.screen.blit(self.dia432, self.dia432_rect)

            elif self.stats.dia == 54 and self.stats.sans_health == 1:
                self.stats.turn = 'black_out'
                self.heart.reset_pos()

            elif self.stats.dia == 55 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 56 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'
                self.stats.sans_amount += 1

            elif self.stats.dia == 57 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 58 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 59 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 60 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 61 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 62 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 63 and self.stats.sans_health == 1:
                self.screen.blit(self.dia441, self.dia441_rect)
                self.screen.blit(self.dia442, self.dia442_rect)

            elif self.stats.dia == 64 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 65 and self.stats.sans_health == 1:
                self.screen.blit(self.dia451, self.dia451_rect)
                self.screen.blit(self.dia452, self.dia452_rect)

            elif self.stats.dia == 66 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 67 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 68 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 69 and self.stats.sans_health == 1:
                self.screen.blit(self.dia461, self.dia461_rect)
                self.screen.blit(self.dia462, self.dia462_rect)

            elif self.stats.dia == 70 and self.stats.sans_health == 1:
                self.screen.blit(self.dia471, self.dia471_rect)
                self.screen.blit(self.dia472, self.dia472_rect)

            elif self.stats.dia == 71 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 72 and self.stats.sans_health == 1:
                self.screen.blit(self.dia481, self.dia481_rect)
                self.screen.blit(self.dia482, self.dia482_rect)

            elif self.stats.dia == 73 and self.stats.sans_health == 1:
                self.screen.blit(self.dia491, self.dia491_rect)
                self.screen.blit(self.dia492, self.dia492_rect)

            elif self.stats.dia == 74 and self.stats.sans_health == 1:
                self.screen.blit(self.dia501, self.dia501_rect)
                self.screen.blit(self.dia502, self.dia502_rect)

            elif self.stats.dia == 75 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.kill_dia == 4 and self.stats.sans_health == 0:
                self.screen.blit(self.dia71, self.dia71_rect)
                self.screen.blit(self.dia72, self.dia72_rect)

            elif self.stats.kill_dia == 5 and self.stats.sans_health == 0:
                self.screen.blit(self.dia81, self.dia81_rect)
                self.screen.blit(self.dia82, self.dia82_rect)
                self.screen.blit(self.dia83, self.dia83_rect)

            elif self.stats.kill_dia == 6 or self.stats.kill_dia == 8 and self.stats.sans_health == 0:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.kill_dia == 7 and self.stats.sans_health == 0:
                self.screen.blit(self.dia101, self.dia101_rect)
                self.screen.blit(self.dia102, self.dia102_rect)

            elif self.stats.kill_dia == 9 and self.stats.sans_health == 0:
                self.screen.blit(self.dia111, self.dia111_rect)
                self.screen.blit(self.dia112, self.dia112_rect)

            elif self.stats.kill_dia == 10 and self.stats.sans_health == 0:
                self.screen.blit(self.dia121, self.dia121_rect)
                self.screen.blit(self.dia122, self.dia122_rect)

            elif self.stats.kill_dia == 11 and self.stats.sans_health == 0:
                self.stats.turn = 'end game'

        elif self.data[0] == 'beat_the_first_attack':
            if self.stats.dia == 1 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 5 and self.stats.sans_health == 1:
                self.screen.blit(self.diaAF1, self.diaAF1_rect)
                self.screen.blit(self.diaAF2, self.diaAF2_rect)

            elif self.stats.dia == 6 and self.stats.sans_health == 1:
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 7 and self.stats.sans_health == 1:
                self.screen.blit(self.dia61, self.dia61_rect)
                self.screen.blit(self.dia62, self.dia62_rect)

            elif self.stats.dia == 8 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'
                self.fight = True
                self.ufgame.fighted = self.fight

            elif self.stats.dia == 9 and self.stats.sans_health == 1:
                self.screen.blit(self.dia131, self.dia131_rect)
                self.screen.blit(self.dia132, self.dia132_rect)

            elif self.stats.dia == 10 and self.stats.sans_health == 1:
                self.screen.blit(self.dia141, self.dia141_rect)
                self.screen.blit(self.dia142, self.dia142_rect)
                self.screen.blit(self.dia143, self.dia143_rect)

            elif self.stats.dia == 11 and self.stats.sans_health == 1:
                self.stats.turn = 'sans turn'
                self.stats.sans_amount += 1
                self.heart.reset_pos()

            elif self.stats.dia == 12 and self.stats.sans_health == 1:
                self.screen.blit(self.dia151, self.dia151_rect)
                self.screen.blit(self.dia152, self.dia152_rect)

            elif self.stats.dia == 13 and self.stats.sans_health == 1:
                self.screen.blit(self.dia161, self.dia161_rect)
                self.screen.blit(self.dia162, self.dia162_rect)

            elif self.stats.dia == 14 and self.stats.sans_health == 1:
                self.screen.blit(self.dia171, self.dia171_rect)
                self.screen.blit(self.dia172, self.dia172_rect)

            elif self.stats.dia == 15 and self.stats.sans_health == 1:
                self.stats.turn = 'sans turn'
                self.stats.sans_amount += 1
                self.heart.reset_pos()

            elif self.stats.dia == 16 and self.stats.sans_health == 1:
                self.screen.blit(self.dia181, self.dia181_rect)
                self.screen.blit(self.dia182, self.dia182_rect)

            elif self.stats.dia == 17 and self.stats.sans_health == 1:
                self.screen.blit(self.dia191, self.dia191_rect)
                self.screen.blit(self.dia192, self.dia192_rect)
                self.screen.blit(self.dia193, self.dia193_rect)

            elif self.stats.dia == 18 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 19 and self.stats.sans_health == 1:
                self.screen.blit(self.dia201, self.dia201_rect)
                self.screen.blit(self.dia202, self.dia202_rect)

            elif self.stats.dia == 20 and self.stats.sans_health == 1:
                self.screen.blit(self.dia211, self.dia211_rect)
                self.screen.blit(self.dia212, self.dia212_rect)

            elif self.stats.dia == 21 and self.stats.sans_health == 1:
                self.screen.blit(self.dia221, self.dia221_rect)
                self.screen.blit(self.dia222, self.dia222_rect)

            elif self.stats.dia == 22 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 23 and self.stats.sans_health == 1:
                self.screen.blit(self.dia231, self.dia231_rect)
                self.screen.blit(self.dia232, self.dia232_rect)

            elif self.stats.dia == 24 and self.stats.sans_health == 1:
                self.screen.blit(self.dia241, self.dia241_rect)
                self.screen.blit(self.dia242, self.dia242_rect)

            elif self.stats.dia == 25 and self.stats.sans_health == 1:
                self.screen.blit(self.dia251, self.dia251_rect)
                self.screen.blit(self.dia252, self.dia252_rect)

            elif self.stats.dia == 26 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 27 and self.stats.sans_health == 1:
                self.screen.blit(self.dia261, self.dia261_rect)
                self.screen.blit(self.dia262, self.dia262_rect)

            elif self.stats.dia == 28 and self.stats.sans_health == 1:
                self.screen.blit(self.dia271, self.dia271_rect)
                self.screen.blit(self.dia272, self.dia272_rect)

            elif self.stats.dia == 29 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 30 and self.stats.sans_health == 1:
                self.screen.blit(self.dia281, self.dia281_rect)
                self.screen.blit(self.dia282, self.dia282_rect)
                self.screen.blit(self.dia283, self.dia283_rect)

            elif self.stats.dia == 31 and self.stats.sans_health == 1:
                self.screen.blit(self.dia291, self.dia291_rect)
                self.screen.blit(self.dia292, self.dia292_rect)

            elif self.stats.dia == 32 and self.stats.sans_health == 1:
                self.screen.blit(self.dia301, self.dia301_rect)
                self.screen.blit(self.dia302, self.dia302_rect)

            elif self.stats.dia == 33 and self.stats.sans_health == 1:
                self.screen.blit(self.dia311, self.dia311_rect)
                self.screen.blit(self.dia312, self.dia312_rect)

            elif self.stats.dia == 34 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 35 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 36 and self.stats.sans_health == 1:
                self.screen.blit(self.dia321, self.dia321_rect)
                self.screen.blit(self.dia322, self.dia322_rect)

            elif self.stats.dia == 37 and self.stats.sans_health == 1:
                self.screen.blit(self.dia331, self.dia331_rect)
                self.screen.blit(self.dia332, self.dia332_rect)

            elif self.stats.dia == 38 and self.stats.sans_health == 1:
                self.screen.blit(self.dia341, self.dia341_rect)
                self.screen.blit(self.dia342, self.dia342_rect)

            elif self.stats.dia == 39 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 40 and self.stats.sans_health == 1:
                self.screen.blit(self.dia351, self.dia351_rect)
                self.screen.blit(self.dia352, self.dia352_rect)

            elif self.stats.dia == 41 and self.stats.sans_health == 1:
                self.screen.blit(self.dia361, self.dia361_rect)
                self.screen.blit(self.dia362, self.dia362_rect)

            elif self.stats.dia == 42 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 43 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 44 and self.stats.sans_health == 1:
                self.stats.sans_amount += 1
                self.stats.turn = 'sans turn'
                self.heart.reset_pos()

            elif self.stats.dia == 46 and self.stats.sans_health == 1:
                self.screen.blit(self.dia371, self.dia371_rect)
                self.screen.blit(self.dia372, self.dia372_rect)

            elif self.stats.dia == 47 and self.stats.sans_health == 1:
                self.screen.blit(self.dia381, self.dia381_rect)
                self.screen.blit(self.dia382, self.dia382_rect)

            elif self.stats.dia == 48 and self.stats.sans_health == 1:
                self.screen.blit(self.dia391, self.dia391_rect)
                self.screen.blit(self.dia392, self.dia392_rect)

            elif self.stats.dia == 49 and self.stats.sans_health == 1:
                self.screen.blit(self.dia401, self.dia401_rect)
                self.screen.blit(self.dia402, self.dia402_rect)

            elif self.stats.dia == 50 and self.stats.sans_health == 1:
                self.screen.blit(self.dia391, self.dia391_rect)
                self.screen.blit(self.dia392, self.dia392_rect)

            elif self.stats.dia == 51 and self.stats.sans_health == 1:
                self.screen.blit(self.dia411, self.dia411_rect)
                self.screen.blit(self.dia412, self.dia412_rect)

            elif self.stats.dia == 52 and self.stats.sans_health == 1:
                self.screen.blit(self.dia421, self.dia421_rect)
                self.screen.blit(self.dia422, self.dia422_rect)

            elif self.stats.dia == 53 and self.stats.sans_health == 1:
                self.screen.blit(self.dia431, self.dia431_rect)
                self.screen.blit(self.dia432, self.dia432_rect)

            elif self.stats.dia == 54 and self.stats.sans_health == 1:
                self.stats.turn = 'black_out'
                self.heart.reset_pos()

            elif self.stats.dia == 55 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 56 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'
                self.stats.sans_amount += 1

            elif self.stats.dia == 57 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 58 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 59 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 60 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 61 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 62 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 63 and self.stats.sans_health == 1:
                self.screen.blit(self.dia441, self.dia441_rect)
                self.screen.blit(self.dia442, self.dia442_rect)

            elif self.stats.dia == 64 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 65 and self.stats.sans_health == 1:
                self.screen.blit(self.dia451, self.dia451_rect)
                self.screen.blit(self.dia452, self.dia452_rect)

            elif self.stats.dia == 66 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 67 and self.stats.sans_health == 1:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.dia == 68 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 69 and self.stats.sans_health == 1:
                self.screen.blit(self.dia461, self.dia461_rect)
                self.screen.blit(self.dia462, self.dia462_rect)

            elif self.stats.dia == 70 and self.stats.sans_health == 1:
                self.screen.blit(self.dia471, self.dia471_rect)
                self.screen.blit(self.dia472, self.dia472_rect)

            elif self.stats.dia == 71 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.dia == 72 and self.stats.sans_health == 1:
                self.screen.blit(self.dia481, self.dia481_rect)
                self.screen.blit(self.dia482, self.dia482_rect)

            elif self.stats.dia == 73 and self.stats.sans_health == 1:
                self.screen.blit(self.dia491, self.dia491_rect)
                self.screen.blit(self.dia492, self.dia492_rect)

            elif self.stats.dia == 74 and self.stats.sans_health == 1:
                self.screen.blit(self.dia501, self.dia501_rect)
                self.screen.blit(self.dia502, self.dia502_rect)

            elif self.stats.dia == 75 and self.stats.sans_health == 1:
                self.stats.turn = 'my turn'

            elif self.stats.kill_dia == 4 and self.stats.sans_health == 0:
                self.screen.blit(self.dia71, self.dia71_rect)
                self.screen.blit(self.dia72, self.dia72_rect)

            elif self.stats.kill_dia == 5 and self.stats.sans_health == 0:
                self.screen.blit(self.dia81, self.dia81_rect)
                self.screen.blit(self.dia82, self.dia82_rect)
                self.screen.blit(self.dia83, self.dia83_rect)

            elif self.stats.kill_dia == 6 or self.stats.kill_dia == 8 and self.stats.sans_health == 0:
                self.screen.blit(self.dia91, self.dia91_rect)
                self.screen.blit(self.dia92, self.dia92_rect)

            elif self.stats.kill_dia == 7 and self.stats.sans_health == 0:
                self.screen.blit(self.dia101, self.dia101_rect)
                self.screen.blit(self.dia102, self.dia102_rect)

            elif self.stats.kill_dia == 9 and self.stats.sans_health == 0:
                self.screen.blit(self.dia111, self.dia111_rect)
                self.screen.blit(self.dia112, self.dia112_rect)

            elif self.stats.kill_dia == 10 and self.stats.sans_health == 0:
                self.screen.blit(self.dia121, self.dia121_rect)
                self.screen.blit(self.dia122, self.dia122_rect)

            elif self.stats.kill_dia == 11 and self.stats.sans_health == 0:
                self.stats.turn = 'end game'
