import pygame

class HandBlast:

    def __init__(self, UF_game):
        self.screen = UF_game.screen
        self.battle = UF_game.battle
        self.setting = UF_game.settings

        self.blue = self.setting.blue_color
        self.orange = self.setting.orange_color
        self.location = 1000

        self.blast_hand()
        self.blast_color()
        self.blast_beam()

    def blast_hand(self):
        self.hand = pygame.image.load('images/hand_blast.png').convert_alpha()
        self.hand = pygame.transform.scale(self.hand, (114, 168)).convert_alpha()
        self.hand_rect = self.hand.get_rect()

        self.hand_rect.right = self.battle.rect.left - 10
        self.hand_rect.centery = self.battle.rect.centery - 35

    def blast_color(self):
        self.color = pygame.Rect(0, 0, 45, 45)
        self.color.centery = self.hand_rect.centery + 32
        self.color.centerx = self.hand_rect.centerx + 11

    def blast_beam(self):
        self.beam1 = pygame.Rect(0, 0, 15, 45)
        self.beam1.bottom = self.hand_rect.centery + self.location
        self.beam1.left = self.hand_rect.centerx + 20

        self.beam2 = pygame.Rect(0, 0, 30, 75)
        self.beam2.centery = self.beam1.centery
        self.beam2.left = self.beam1.right

        self.beam3 = pygame.Rect(0, 0, 850, 110)
        self.beam3.centery = self.beam2.centery
        self.beam3.left = self.beam2.right

    def show_blue_blast_hand(self):
        pygame.draw.rect(self.screen, self.blue, self.color)
        self.screen.blit(self.hand, self.hand_rect)

    def show_blue_blasted_hand(self):
        pygame.draw.rect(self.screen, self.blue, self.color)
        self.screen.blit(self.hand, self.hand_rect)
        pygame.draw.rect(self.screen, self.blue, self.beam1)
        pygame.draw.rect(self.screen, self.blue, self.beam2)
        pygame.draw.rect(self.screen, self.blue, self.beam3)

    def show_orange_blast_hand(self):
        pygame.draw.rect(self.screen, self.orange, self.color)
        self.screen.blit(self.hand, self.hand_rect)

    def show_orange_blasted_hand(self):
        pygame.draw.rect(self.screen, self.orange, self.color)
        self.screen.blit(self.hand, self.hand_rect)
        pygame.draw.rect(self.screen, self.orange, self.beam1)
        pygame.draw.rect(self.screen, self.orange, self.beam2)
        pygame.draw.rect(self.screen, self.orange, self.beam3)
