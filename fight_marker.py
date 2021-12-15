import pygame

class FightMarker:

    def __init__(self, UF_game):
        self.settings = UF_game.settings
        self.fightbar = UF_game.fightbar
        self.screen = UF_game.screen

        self.color = self.settings.fight_marker_color

        self.make_fight_marker()

    def make_fight_marker(self):
        self.fight_marker = pygame.Rect(0, 0, 15, self.fightbar.fightbar_rect.height)

        self.fight_marker.right = self.fightbar.fightbar_rect.right
        self.fight_marker.top = self.fightbar.fightbar_rect.top

    def show_fight_marker(self):
        pygame.draw.rect(self.screen, self.color, self.fight_marker)