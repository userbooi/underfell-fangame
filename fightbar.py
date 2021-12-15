import pygame

class FightBar:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.battle = UF_game.battle
        self.width = 10

        self.make_fight_bar()

    def make_fight_bar(self):
        self.fightbar_image = pygame.image.load('images/fightbar.png').convert_alpha()
        self.fightbar_image = pygame.transform.scale(self.fightbar_image, (self.width, 244)).convert_alpha()
        self.fightbar_rect = self.fightbar_image.get_rect()

        self.fightbar_rect.center = self.battle.rect.center

    def expand_fight_bar(self):
        if self.fightbar_rect.width <= 760:
            self.width += 15

            self.make_fight_bar()

    def reset_fight_bar(self):
        self.width = 10

        self.make_fight_bar()

    def show_fight_bar(self):
        self.screen.blit(self.fightbar_image, self.fightbar_rect)
