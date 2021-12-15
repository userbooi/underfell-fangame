import pygame

class BigHand:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.battle = UF_game.battle

        self.make_big_hand()

    def make_big_hand(self):
        self.bighand = pygame.image.load('images/gaster_big_hand.png').convert_alpha()
        self.bighand = pygame.transform.scale(self.bighand, (378, 84)).convert_alpha()
        self.bighand_rect = self.bighand.get_rect()

        self.bighand_rect.bottom = self.battle.rect.top - 20
        self.bighand_rect.left = self.battle.rect.left - 70

        self.y = float(self.bighand_rect.y)

    def move_big_hand_down(self):
        self.y += 0.5

        self.bighand_rect.y = self.y

    def show_big_hand(self):
        self.screen.blit(self.bighand, self.bighand_rect)
