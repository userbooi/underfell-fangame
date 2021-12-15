class GameStats:

    def __init__(self, UF_game):
        self.reset_stats(UF_game)
        # self.active = True
        # self.active = False
        self.active = 'instruction'

    def reset_stats(self, UF_game):
        self.heart_color = 'red'
        self.platform_color = 'red'
        self.health = 20
        self.sans_health = 1
        self.kill_dia = 1
        self.phase = 1
        self.sans_amount = 1
        self.turn = 'speech turn'
        self.dia = 1
        # self.phase = 2
        # self.turn = 'speech turn'
        # UF_game.mercyed = True
        # self.dia = 55
        # self.sans_amount = 89

    def change_dia(self):
        self.dia += 1

    def change_kill_dia(self):
        self.kill_dia += 1
