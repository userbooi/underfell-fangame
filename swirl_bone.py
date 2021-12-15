import pygame
from pygame.sprite import Sprite

class SwirlBone(Sprite):

    def __init__(self, UF_game):
        super().__init__()
        self.screen = UF_game.screen
        self.screen_rect = self.screen.get_rect()
        self.battlebox = UF_game.battle
        self.heart = UF_game.heart

        self.first_swirl_top = 340

        self.swirly_bones_top()
        self.swirly_bones_bottom()

    def swirly_bones_top(self):
        self.image_top1 = pygame.image.load('images/swirl_bones_top1.png').convert_alpha()
        self.image_top1 = pygame.transform.scale(self.image_top1, (20, 103)).convert_alpha()
        self.rect1 = self.image_top1.get_rect()
        self.rect1.top = self.battlebox.rect.top
        self.rect1.x = self.first_swirl_top

        self.image_top2 = pygame.image.load('images/swirl_bones_top2.png').convert_alpha()
        self.image_top2 = pygame.transform.scale(self.image_top2, (20, 96)).convert_alpha()

        self.rect2 = self.image_top2.get_rect()
        self.rect2.right = self.rect1.left
        self.rect2.top = self.battlebox.rect.top

        self.image_top3 = pygame.image.load('images/swirl_bones_top3.png').convert_alpha()
        self.image_top3 = pygame.transform.scale(self.image_top3, (20, 89)).convert_alpha()

        self.rect3 = self.image_top3.get_rect()
        self.rect3.right = self.rect2.left
        self.rect3.top = self.battlebox.rect.top

        self.image_top4 = pygame.image.load('images/swirl_bones_top4.png').convert_alpha()
        self.image_top4 = pygame.transform.scale(self.image_top4, (20, 82)).convert_alpha()

        self.rect4 = self.image_top4.get_rect()
        self.rect4.right = self.rect3.left
        self.rect4.top = self.battlebox.rect.top

        self.image_top5 = pygame.image.load('images/swirl_bones_top5.png').convert_alpha()
        self.image_top5 = pygame.transform.scale(self.image_top5, (20, 82)).convert_alpha()

        self.rect5 = self.image_top5.get_rect()
        self.rect5.right = self.rect4.left
        self.rect5.top = self.battlebox.rect.top

        self.image_top6 = pygame.image.load('images/swirl_bones_top6.png').convert_alpha()
        self.image_top6 = pygame.transform.scale(self.image_top6, (20, 89)).convert_alpha()

        self.rect6 = self.image_top6.get_rect()
        self.rect6.right = self.rect5.left
        self.rect6.top = self.battlebox.rect.top

        self.image_top7 = pygame.image.load('images/swirl_bones_top7.png').convert_alpha()
        self.image_top7 = pygame.transform.scale(self.image_top7, (20, 96)).convert_alpha()

        self.rect7 = self.image_top7.get_rect()
        self.rect7.right = self.rect6.left
        self.rect7.top = self.battlebox.rect.top

        self.image_top8 = pygame.image.load('images/swirl_bones_top8.png').convert_alpha()
        self.image_top8 = pygame.transform.scale(self.image_top8, (20, 103)).convert_alpha()

        self.rect8 = self.image_top8.get_rect()
        self.rect8.right = self.rect7.left
        self.rect8.top = self.battlebox.rect.top

        self.image_top9 = pygame.image.load('images/swirl_bones_top9.png').convert_alpha()
        self.image_top9 = pygame.transform.scale(self.image_top9, (20, 103)).convert_alpha()

        self.rect9 = self.image_top9.get_rect()
        self.rect9.right = self.rect8.left
        self.rect9.top = self.battlebox.rect.top

        self.image_top10 = pygame.image.load('images/swirl_bones_top10.png').convert_alpha()
        self.image_top10 = pygame.transform.scale(self.image_top10, (20, 96)).convert_alpha()

        self.rect10 = self.image_top10.get_rect()
        self.rect10.right = self.rect9.left
        self.rect10.top = self.battlebox.rect.top

        self.image_top11 = pygame.image.load('images/swirl_bones_top11.png').convert_alpha()
        self.image_top11 = pygame.transform.scale(self.image_top11, (20, 89)).convert_alpha()

        self.rect11 = self.image_top11.get_rect()
        self.rect11.right = self.rect10.left
        self.rect11.top = self.battlebox.rect.top

        self.image_top12 = pygame.image.load('images/swirl_bones_top12.png').convert_alpha()
        self.image_top12 = pygame.transform.scale(self.image_top12, (20, 82)).convert_alpha()

        self.rect12 = self.image_top12.get_rect()
        self.rect12.right = self.rect11.left
        self.rect12.top = self.battlebox.rect.top

    def swirly_bones_bottom(self):
        self.image_bottom1 = pygame.image.load('images/swirl_bones_bottom1.png').convert_alpha()
        self.image_bottom1 = pygame.transform.scale(self.image_bottom1, (20, 103)).convert_alpha()

        self.rectb1 = self.image_bottom1.get_rect()
        self.rectb1.bottom = self.battlebox.rect.bottom
        self.rectb1.x = self.first_swirl_top

        self.image_bottom2 = pygame.image.load('images/swirl_bones_bottom2.png').convert_alpha()
        self.image_bottom2 = pygame.transform.scale(self.image_bottom2, (20, 110)).convert_alpha()

        self.rectb2 = self.image_bottom2.get_rect()
        self.rectb2.right = self.rectb1.left
        self.rectb2.bottom = self.battlebox.rect.bottom

        self.image_bottom3 = pygame.image.load('images/swirl_bones_bottom3.png').convert_alpha()
        self.image_bottom3 = pygame.transform.scale(self.image_bottom3, (20, 117)).convert_alpha()

        self.rectb3 = self.image_bottom3.get_rect()
        self.rectb3.right = self.rectb2.left
        self.rectb3.bottom = self.battlebox.rect.bottom

        self.image_bottom4 = pygame.image.load('images/swirl_bones_bottom4.png').convert_alpha()
        self.image_bottom4 = pygame.transform.scale(self.image_bottom4, (20, 124)).convert_alpha()

        self.rectb4 = self.image_bottom4.get_rect()
        self.rectb4.right = self.rectb3.left
        self.rectb4.bottom = self.battlebox.rect.bottom

        self.image_bottom5 = pygame.image.load('images/swirl_bones_bottom5.png').convert_alpha()
        self.image_bottom5 = pygame.transform.scale(self.image_bottom5, (20, 124)).convert_alpha()

        self.rectb5 = self.image_bottom5.get_rect()
        self.rectb5.right = self.rectb4.left
        self.rectb5.bottom = self.battlebox.rect.bottom

        self.image_bottom6 = pygame.image.load('images/swirl_bones_bottom6.png').convert_alpha()
        self.image_bottom6 = pygame.transform.scale(self.image_bottom6, (20, 117)).convert_alpha()

        self.rectb6 = self.image_bottom6.get_rect()
        self.rectb6.right = self.rectb5.left
        self.rectb6.bottom = self.battlebox.rect.bottom

        self.image_bottom7 = pygame.image.load('images/swirl_bones_bottom7.png').convert_alpha()
        self.image_bottom7 = pygame.transform.scale(self.image_bottom7, (20, 110)).convert_alpha()

        self.rectb7 = self.image_bottom7.get_rect()
        self.rectb7.right = self.rectb6.left
        self.rectb7.bottom = self.battlebox.rect.bottom

        self.image_bottom8 = pygame.image.load('images/swirl_bones_bottom8.png').convert_alpha()
        self.image_bottom8 = pygame.transform.scale(self.image_bottom8, (20, 103)).convert_alpha()

        self.rectb8 = self.image_bottom8.get_rect()
        self.rectb8.right = self.rectb7.left
        self.rectb8.bottom = self.battlebox.rect.bottom

        self.image_bottom9 = pygame.image.load('images/swirl_bones_bottom9.png').convert_alpha()
        self.image_bottom9 = pygame.transform.scale(self.image_bottom9, (20, 103)).convert_alpha()

        self.rectb9 = self.image_bottom9.get_rect()
        self.rectb9.right = self.rectb8.left
        self.rectb9.bottom = self.battlebox.rect.bottom

        self.image_bottom10 = pygame.image.load('images/swirl_bones_bottom10.png').convert_alpha()
        self.image_bottom10 = pygame.transform.scale(self.image_bottom10, (20, 110)).convert_alpha()

        self.rectb10 = self.image_bottom10.get_rect()
        self.rectb10.right = self.rectb9.left
        self.rectb10.bottom = self.battlebox.rect.bottom

        self.image_bottom11 = pygame.image.load('images/swirl_bones_bottom11.png').convert_alpha()
        self.image_bottom11 = pygame.transform.scale(self.image_bottom11, (20, 117)).convert_alpha()

        self.rectb11 = self.image_bottom11.get_rect()
        self.rectb11.right = self.rectb10.left
        self.rectb11.bottom = self.battlebox.rect.bottom

        self.image_bottom12 = pygame.image.load('images/swirl_bones_bottom12.png').convert_alpha()
        self.image_bottom12 = pygame.transform.scale(self.image_bottom12, (20, 124)).convert_alpha()

        self.rectb12 = self.image_bottom12.get_rect()
        self.rectb12.right = self.rectb11.left
        self.rectb12.bottom = self.battlebox.rect.bottom

    def show_swirl(self):
        self.screen.blit(self.image_top1, self.rect1)
        self.screen.blit(self.image_top2, self.rect2)
        self.screen.blit(self.image_top3, self.rect3)
        self.screen.blit(self.image_top4, self.rect4)
        self.screen.blit(self.image_top5, self.rect5)
        self.screen.blit(self.image_top6, self.rect6)
        self.screen.blit(self.image_top7, self.rect7)
        self.screen.blit(self.image_top8, self.rect8)
        self.screen.blit(self.image_top9, self.rect9)
        self.screen.blit(self.image_top10, self.rect10)
        self.screen.blit(self.image_top11, self.rect11)
        self.screen.blit(self.image_top12, self.rect12)

        self.screen.blit(self.image_bottom1, self.rectb1)
        self.screen.blit(self.image_bottom2, self.rectb2)
        self.screen.blit(self.image_bottom3, self.rectb3)
        self.screen.blit(self.image_bottom4, self.rectb4)
        self.screen.blit(self.image_bottom5, self.rectb5)
        self.screen.blit(self.image_bottom6, self.rectb6)
        self.screen.blit(self.image_bottom7, self.rectb7)
        self.screen.blit(self.image_bottom8, self.rectb8)
        self.screen.blit(self.image_bottom9, self.rectb9)
        self.screen.blit(self.image_bottom10, self.rectb10)
        self.screen.blit(self.image_bottom11, self.rectb11)
        self.screen.blit(self.image_bottom12, self.rectb12)
