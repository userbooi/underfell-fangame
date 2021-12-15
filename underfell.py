import sys, pygame
from time import time, sleep
from pygame import mixer
import random

from settings import Settings
from UFsans import SANNESS
from player_box import BattleBox
from player_heart import Player_heart
from game_stats import GameStats
from Game_title import Title
from begin_buttons import Begin
from background_sans import BgSans
from begin_heart import Bg_heart
from show_health_bar_y import HealthBar
from show_health_bar_r import HealthBar2
from show_health import health_number
from fight import Fight
from act import Act
from itams import Item
from mercy import Mercy
from speech_bubble import Bubble
from text import Text
from attacks import Attacks
from slam import Slam
from swirl_bone import SwirlBone
from gasterblaster import FellBlaster
from blastingblaster import FellBlasted
from blastbeam import BlastBeam
from battletext import BattleText
from instruction import Instructions
from menu_heart import MenuHeart
from inside_text import InsideText
from fightbar import FightBar
from fight_marker import FightMarker
from slash import Slash
from full_bone import FullBone, BlueBoneStem, OrangeBoneStem
from bone_tip import BoneTip, BlueBoneTip, OrangeBoneTip
from warning_arrow import Arrow
from warning import Warning
from platforms import PlatformRed, PlatformYellow
from flying_bones import FlyingBones, FlyingBonesTop, FlyingBonesLeft, FlyingBonesBottom
from gaster_hand_blast import HandBlast
from gaster_big_hand import BigHand
from credit import Credit

class UnderFell:

    def __init__(self):
        pygame.init()

        self.icon = pygame.image.load('images/underfell_icon1.png')

        self.settings = Settings()
        self.screen = pygame.display.set_mode((1000, 750))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('UnderFell Sans Fight')
        pygame.display.set_icon(self.icon)

        self.initialize_every()

    def initialize_every(self):

        mixer.music.stop()

        with open('data/data.txt', 'r') as f:
            self.data = f.read()
            self.data = self.data.split(' ')

        self.begin = False
        self.loop_interval = None
        self.fighted = False
        self.acted = False
        self.itemed = False
        self.mercyed = False
        self.sound_played = False
        self.stop_blaster = False
        self.stop_blaster2 = False
        self.stop_blaster3 = False
        self.stop_blaster4 = False
        self.stop_blaster5 = False
        self.stop_blaster6 = False
        self.created_bone = False
        self.blaster_created = False
        self.blaster_created2 = False
        self.blaster_blasted = False
        self.blaster_blasted2 = False
        self.center = False
        self.last_time = None
        self.last_time2 = None
        self.last_time3 = None
        self.last_time4 = None
        self.last_time5 = None
        self.last_time6 = None
        self.last_time7 = None
        self.last_time8 = None
        self.last_time9 = None
        self.last_time10 = None
        self.last_time11 = None
        self.last_time12 = None
        self.last_time13 = None
        self.repeat_interval = None
        self.hit_sans_delay = None
        self.invincibility = None
        self.selected = None
        self.arrow_type = None
        self.arrow_randomed = False
        self.switch_sans = None
        self.bone_color = None
        self.color_randomed = False
        self.platform_created = False
        self.platform_moved_left_once1 = False
        self.platform_moved_left_once2 = False
        self.platform_moved_left_once3 = False
        self.platform_moved_left_once4 = False
        self.changed_once = False
        self.gaster_hand_color = None
        self.gaster_hand_color_randomed = False
        self.reset_var = False
        self.set_volume = False
        self.wrote = False
        self.shrunk_battle_box = 0
        self.between_bones_height = 'high'
        self.gaster_number = 0
        self.selected_page = 1
        self.items_ate = []
        self.repeat = 0
        self.bone_number_between_left = 1
        self.bone_number_between_right = 1
        self.right_bone_number = 1
        self.top_bone_number = 1
        self.left_bone_number = 1
        self.bottom_bone_number = 1
        self.flyingbone_right_spin_degree = 0
        self.flyingbone_top_spin_degree = 0
        self.volume = 5

        self.slam = Slam()
        self.stats = GameStats(self)
        self.battle = BattleBox(self)
        self.platformrs = pygame.sprite.Group()
        self.platformys = pygame.sprite.Group()
        self.heart = Player_heart(self)
        self.platformr = PlatformRed(self)
        self.platformy = PlatformYellow(self)
        self.title = Title(self)
        self.start = Begin(self)
        self.bgsans = BgSans(self)
        self.bgheart = Bg_heart(self)
        self.hb2 = HealthBar2(self)
        self.hb = HealthBar(self)
        self.hn = health_number(self)
        self.fight = Fight(self)
        self.act = Act(self)
        self.item = Item(self)
        self.mercy = Mercy(self)
        self.text = Text(self)
        self.bones = pygame.sprite.Group()
        self.swirl = SwirlBone(self)
        self.att = Attacks(self)
        self.Sanness = SANNESS(self)
        self.SB = Bubble(self)
        self.blaster = FellBlaster(self)
        self.gasterblaster = pygame.sprite.Group()
        self.blockblaster = pygame.sprite.Group()
        self.blockblast = pygame.sprite.Group()
        self.blasted = FellBlasted(self)
        self.blast = pygame.sprite.Group()
        self.beam = BlastBeam(self)
        self.bt = BattleText(self)
        self.instruc = Instructions(self)
        self.mh = MenuHeart(self)
        self.inside = InsideText(self)
        self.used = pygame.sprite.Group()
        self.fightbar = FightBar(self)
        self.fightmarker = FightMarker(self)
        self.slash = Slash(self)
        self.fullbone = FullBone(self)
        self.bone_tip = BoneTip(self)
        self.right_bone = pygame.sprite.Group()
        self.top_bone = pygame.sprite.Group()
        self.left_bone = pygame.sprite.Group()
        self.bottom_bone = pygame.sprite.Group()
        self.wa = Arrow(self)
        self.blue_bone_stem = BlueBoneStem(self)
        self.blue_bone_tip = BlueBoneTip(self)
        self.orange_bone_stem = OrangeBoneStem(self)
        self.orange_bone_tip = OrangeBoneTip(self)
        self.blue_bones = pygame.sprite.Group()
        self.orange_bones = pygame.sprite.Group()
        self.w = Warning(self)
        self.platformrs = pygame.sprite.Group()
        self.platformys = pygame.sprite.Group()
        self.between_bones_right = pygame.sprite.Group()
        self.between_bones_left = pygame.sprite.Group()
        self.swirls = pygame.sprite.Group()
        self.flyingbonestop = pygame.sprite.Group()
        self.flyingbonesright = pygame.sprite.Group()
        self.flyingbonesbottom = pygame.sprite.Group()
        self.flyingbonesleft = pygame.sprite.Group()
        self.flyingboneright = FlyingBones(self)
        self.flyingbonetop = FlyingBonesTop(self)
        self.flyingboneleft = FlyingBonesLeft(self)
        self.flyingbonebottom = FlyingBonesBottom(self)
        self.hand_blast = HandBlast(self)
        self.big_hand = BigHand(self)
        self.credit = Credit(self)

        self.add_used_items()

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.active and self.stats.turn == 'sans turn':
                if self.stats.heart_color == 'red':
                    self.heart.update_red()
                if self.stats.heart_color == 'blue':
                    self.heart.update_blue()
                    self.heart.gravity()
                    if self.heart.blue_rect.bottom == self.battle.rect.bottom and self.heart.heart_direction == 'up' or pygame.sprite.spritecollideany(self.heart, self.platformrs):
                        self.heart.jump = False
                    elif self.heart.blue_rect.left == self.battle.rect.left and self.heart.heart_direction == 'left':
                        self.heart.jump = False
                    elif self.heart.blue_rect.right == self.battle.rect.right and self.heart.heart_direction == 'right':
                        self.heart.jump = False
                    elif self.heart.blue_rect.top == self.battle.rect.top and self.heart.heart_direction == 'down':
                        self.heart.jump = False
                self.hit_heart()
            if self.stats.sans_amount != 90:
                self.play_sound()
            self._update_screen()
            self.check_health()

    def check_health(self):
        if self.stats.health >= 1:
            pass
        else:
            self.initialize_every()
            self.stats.active = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_ESCAPE:
            if self.stats.active:
                self.initialize_every()
                self.stats.active = False
            elif self.stats.active == False:
                sys.exit()

        elif self.stats.turn == 'sans turn':
            if event.key == pygame.K_RIGHT:
                self.heart.moving_right = True
            if event.key == pygame.K_LEFT:
                self.heart.moving_left = True
            if event.key == pygame.K_UP:
                self.heart.moving_up = True
            if event.key == pygame.K_DOWN:
                self.heart.moving_down = True

        elif event.key == pygame.K_z:
            if self.stats.active == 'credits':
                self.initialize_every()
                self.stats.active = False
            elif self.bgheart.bg_heart_rect.x == 387 and self.bgheart.bg_heart_rect.y == 350 and self.bgheart.visability == True and self.bgsans.visability == True \
                    and self.stats.active == False and self.begin == True:
                self.stats.reset_stats(self)
                self.settings.health_bar_width = 100
                self.hb.make_bar()
                self.heart.reset_pos()
                self.initialize_every()
                self.stats.active = True
            elif self.stats.active == 'instruction':
                self.initialize_every()
                self.stats.active = False
            elif self.stats.turn == 'speech turn' and self.stats.active == True:
                if self.data[0] == 'beat_the_first_attack' and self.stats.dia == 1:
                    self.stats.dia = 5
                elif self.stats.dia != 45:
                    self.stats.change_dia()
            elif self.stats.turn == 'killed speech turn' and self.stats.active == True:
                self.stats.change_kill_dia()
            elif self.stats.turn == 'my turn' and self.fighted == True and self.acted == False and self.itemed == False and self.mercyed == False:
                self.stats.turn = 'fightb'
            elif self.stats.turn == 'my turn' and self.fighted == False and self.acted == True and self.itemed == False and self.mercyed == False:
                self.stats.turn = 'actb'
            elif self.stats.turn == 'my turn' and self.fighted == False and self.acted == False and self.itemed == True and self.mercyed == False:
                self.stats.turn = 'itemb'
                self.selected = 'Pie'
                self.selected_page = 1
            elif self.stats.turn == 'my turn' and self.fighted == False and self.acted == False and self.itemed == False and self.mercyed == True:
                self.stats.turn = 'mercyb'
            elif self.stats.turn == 'actb':
                self.selected = 'check'
                self.stats.turn = 'acti'
            elif self.stats.turn == 'fightb':
                self.stats.turn = 'fightis'
            elif self.stats.turn == 'fightis' and self.fightmarker.fight_marker.left >= self.fightbar.fightbar_rect.left and self.fightbar.fightbar_rect.width >= 760:
                self.stats.turn = 'fightie'
            elif self.stats.turn == 'acti':
                if self.selected == 'check':
                    self.stats.turn = 'checked'
                elif self.selected == 'reason':
                    self.stats.turn = 'reasoned'
            elif self.stats.turn == 'itemb':
                if self.selected == 'Pie' and 'Pie' not in self.items_ate:
                    self.items_ate.append('Pie')
                    self.add_health()
                    self.stats.turn = 'ate pie'
                elif self.selected == 'Noodles1' and 'Noodles1' not in self.items_ate:
                    self.items_ate.append('Noodles1')
                    self.add_health()
                    self.stats.turn = 'ate noodles'
                elif self.selected == 'Noodles2' and 'Noodles2' not in self.items_ate:
                    self.items_ate.append('Noodles2')
                    self.stats.turn = 'ate noodles'
                    self.add_health()
                elif self.selected == 'Fsteak' and 'Fsteak' not in self.items_ate:
                    self.items_ate.append('Fsteak')
                    self.add_health()
                    self.stats.turn = 'ate steak'
                elif self.selected == 'Lhero1' and 'Lhero1' not in self.items_ate:
                    self.items_ate.append('Lhero1')
                    self.add_health()
                    self.stats.turn = 'ate lhero'
                elif self.selected == 'Lhero2' and 'Lhero2' not in self.items_ate:
                    self.items_ate.append('Lhero2')
                    self.add_health()
                    self.stats.turn = 'ate lhero'
                elif self.selected == 'Lhero3' and 'Lhero3' not in self.items_ate:
                    self.items_ate.append('Lhero3')
                    self.add_health()
                    self.stats.turn = 'ate lhero'
                elif self.selected == 'Lhero4' and 'Lhero4' not in self.items_ate:
                    self.items_ate.append('Lhero4')
                    self.add_health()
                    self.stats.turn = 'ate lhero'
            elif self.stats.turn == 'mercyb':
                if self.stats.dia != 75:
                    self.stats.change_dia()
                    self.stats.turn = 'speech turn'
                    self.heart.reset_pos()
                else:
                    self.stats.change_dia()
                    self.stats.turn = 'spared turn'
            elif self.stats.turn == 'checked' or self.stats.turn == 'reasoned' or self.stats.turn == 'ate pie' or self.stats.turn == 'ate noodles' or self.stats.turn == 'ate steak' \
                    or self.stats.turn == 'ate lhero':
                if self.stats.dia != 75:
                    self.stats.change_dia()
                    self.stats.turn = 'speech turn'
                    self.heart.reset_pos()
                else:
                    self.stats.change_dia()
                    self.stats.turn = 'spared turn'

        elif event.key == pygame.K_RIGHT:
            if self.stats.turn == 'my turn':
                if self.fighted == True and self.acted == False and self.itemed == False and self.mercyed == False:
                    self.acted = True
                    self.itemed = False
                    self.mercyed = False
                    self.fighted = False
                elif self.fighted == False and self.acted == True and self.itemed == False and self.mercyed == False:
                    self.fighted = False
                    self.itemed = True
                    self.mercyed = False
                    self.acted = False
                elif self.fighted == False and self.acted == False and self.itemed == True and self.mercyed == False:
                    self.fighted = False
                    self.acted = False
                    self.mercyed = True
                    self.itemed = False
                elif self.fighted == False and self.acted == False and self.itemed == False and self.mercyed == True:
                    self.fighted = True
                    self.acted = False
                    self.itemed = False
                    self.mercyed = False
            elif self.stats.turn == 'acti':
                if self.selected == 'check':
                    self.selected = 'reason'
                elif self.selected == 'reason':
                    self.selected = 'check'
            elif self.stats.turn == 'itemb':
                if self.selected_page == 1:
                    if self.selected == 'Pie':
                        self.selected = 'Noodles1'
                    elif self.selected == 'Noodles2':
                        self.selected = 'Fsteak'
                    elif self.selected == 'Noodles1':
                        self.selected = 'Lhero1'
                        self.selected_page = 2
                    elif self.selected == 'Fsteak':
                        self.selected = 'Lhero3'
                        self.selected_page = 2
                elif self.selected_page == 2:
                    if self.selected == 'Lhero2':
                        self.selected = 'Pie'
                        self.selected_page = 1
                    elif self.selected == 'Lhero4':
                        self.selected = 'Noodles2'
                        self.selected_page = 1
                    elif self.selected == 'Lhero1':
                        self.selected = 'Lhero2'
                    elif self.selected == 'Lhero3':
                        self.selected = 'Lhero4'

        if event.key == pygame.K_LEFT:
            if self.stats.turn == 'my turn':
                if self.fighted == True and self.acted == False and self.itemed == False and self.mercyed == False:
                    self.acted = False
                    self.itemed = False
                    self.mercyed = True
                    self.fighted = False
                elif self.fighted == False and self.acted == False and self.itemed == False and self.mercyed == True:
                    self.fighted = False
                    self.itemed = True
                    self.mercyed = False
                    self.acted = False
                elif self.fighted == False and self.acted == False and self.itemed == True and self.mercyed == False:
                    self.fighted = False
                    self.acted = True
                    self.mercyed = False
                    self.itemed = False
                elif self.fighted == False and self.acted == True and self.itemed == False and self.mercyed == False:
                    self.fighted = True
                    self.acted = False
                    self.itemed = False
                    self.mercyed = False
            elif self.stats.turn == 'acti':
                if self.selected == 'reason':
                    self.selected = 'check'
                elif self.selected == 'check':
                    self.selected = 'reason'
            elif self.stats.turn == 'itemb':
                if self.selected_page == 1:
                    if self.selected == 'Noodles1':
                        self.selected = 'Pie'
                    elif self.selected == 'Fsteak':
                        self.selected = 'Noodles2'
                    elif self.selected == 'Pie':
                        self.selected = 'Lhero2'
                        self.selected_page = 2
                    elif self.selected == 'Noodles2':
                        self.selected = 'Lhero4'
                        self.selected_page = 2
                elif self.selected_page == 2:
                    if self.selected == 'Lhero1':
                        self.selected = 'Noodles1'
                        self.selected_page = 1
                    elif self.selected == 'Lhero3':
                        self.selected = 'Fsteak'
                        self.selected_page = 1
                    elif self.selected == 'Lhero2':
                        self.selected = 'Lhero1'
                    elif self.selected == 'Lhero4':
                        self.selected = 'Lhero3'

        elif event.key == pygame.K_DOWN:
            if self.stats.turn == 'itemb':
                if self.selected_page == 1:
                    if self.selected == 'Pie':
                        self.selected = 'Noodles2'
                    elif self.selected == 'Noodles1':
                        self.selected = 'Fsteak'
                elif self.selected_page == 2:
                    if self.selected == 'Lhero1':
                        self.selected = 'Lhero3'
                    elif self.selected == 'Lhero2':
                        self.selected = 'Lhero4'

        elif event.key == pygame.K_UP:
            if self.selected_page == 1:
                if self.selected == 'Noodles2':
                    self.selected = 'Pie'
                elif self.selected == 'Fsteak':
                    self.selected = 'Noodles1'
            elif self.selected_page == 2:
                if self.selected == 'Lhero3':
                    self.selected = 'Lhero1'
                elif self.selected == 'Lhero4':
                    self.selected = 'Lhero2'

        elif event.key == pygame.K_x:
            if self.stats.turn == 'fightb':
                self.stats.turn = 'my turn'
                self.fighted = True
                self.acted = False
                self.itemed = False
                self.mercyed = False
                self.selected = False
            elif self.stats.turn == 'actb':
                self.stats.turn = 'my turn'
                self.fighted = False
                self.acted = True
                self.itemed = False
                self.mercyed = False
                self.selected = False
            elif self.stats.turn == 'itemb':
                self.stats.turn = 'my turn'
                self.fighted = False
                self.acted = False
                self.itemed = True
                self.mercyed = False
                self.selected = False
            elif self.stats.turn == 'mercyb':
                self.stats.turn = 'my turn'
                self.fighted = False
                self.acted = False
                self.itemed = False
                self.mercyed = True
                self.selected = False
            elif self.stats.turn == 'acti':
                top = self.battle.rect.top + 35
                left = self.battle.rect.left + 28
                self.mh.menu_heart_rect.top = top
                self.mh.menu_heart_rect.left = left
                self.stats.turn = 'actb'
                self.selected = False

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.heart.moving_right = False
            if self.heart.heart_direction == 'left':
                self.heart.jump = True
        if event.key == pygame.K_LEFT:
            self.heart.moving_left = False
            if self.heart.heart_direction == 'right':
                self.heart.jump = True
        if event.key == pygame.K_UP:
            self.heart.moving_up = False
            if self.heart.heart_direction == 'up':
                self.heart.jump = True
        if event.key == pygame.K_DOWN:
            self.heart.moving_down = False
            if self.heart.heart_direction == 'down':
                self.heart.jump = True

    def add_used_items(self):
        for row in range(1, 3):
            for number in range(1, 3):
                used = InsideText(self)
                used.rect.y = 218 + 91 * row
                used.rect.x = -238 + 400 * number

                self.used.add(used)

    def add_platform(self):
        platformr = PlatformRed(self)
        platformy = PlatformYellow(self)

        self.platformrs.add(platformr)
        self.platformys.add(platformy)
        self.heart.platformrs.add(platformr)
        self.heart.platformys.add(platformy)

    def make_platform_left(self):
        for platformr in self.platformrs.sprites():
            platformr.locate_battle_rect_left()
        for platformy in self.platformys.sprites():
            platformy.locate_battle_rect_left()
        for hplatformr in self.heart.platformrs.sprites():
            hplatformr.locate_battle_rect_left()
        for hplatformy in self.heart.platformys.sprites():
            hplatformy.locate_battle_rect_left()

        self.platformrs.update()
        self.platformys.update()
        self.heart.platformrs.update()
        self.heart.platformys.update()

    def move_platform_to_center(self):
        for platformr in self.platformrs.sprites():
            platformr.move_plat_to_battle_center1()
        for hplatformr in self.heart.platformrs.sprites():
            hplatformr.move_plat_to_battle_center2()
        for platformy in self.platformys.sprites():
            platformy.move_plat_to_battle_center1()
        for hplatformy in self.heart.platformys.sprites():
            hplatformy.move_plat_to_battle_center2()

        self.platformrs.update()
        self.platformys.update()
        self.heart.platformrs.update()
        self.heart.platformys.update()

    def test_move_platforms(self):
        for platformr in self.platformrs.sprites():
            platformr.test_move1()
        for hplatformr in self.heart.platformrs.sprites():
            hplatformr.test_move2()
        for platformy in self.platformys.sprites():
            platformy.test_move1()
        for hplatformy in self.heart.platformys.sprites():
            hplatformy.test_move2()

        self.platformrs.update()
        self.platformys.update()
        self.heart.platformrs.update()
        self.heart.platformys.update()

    def move_platforms_left_right(self):
        for platformr in self.platformrs.sprites():
            if self.platform_moved_left_once1 is False:
                platformr.move_platform_left1()
            else:
                platformr.move_platform_left_right1()
            if platformr.rect.centerx == self.battle.rect.centerx - 125:
                self.platform_moved_left_once1 = True
        for hplatformr in self.heart.platformrs.sprites():
            if self.platform_moved_left_once2 is False:
                hplatformr.move_platform_left2()
            else:
                hplatformr.move_platform_left_right2()
            if hplatformr.rect.centerx == self.battle.rect.centerx - 125:
                self.platform_moved_left_once2 = True
        for platformy in self.platformys.sprites():
            if self.platform_moved_left_once1 is False:
                platformy.move_platform_left1()
            else:
                platformy.move_platform_left_right1()
            if platformy.rect.centerx == self.battle.rect.centerx - 125:
                self.platform_moved_left_once3 = True
        for hplatformy in self.heart.platformys.sprites():
            if self.platform_moved_left_once2 is False:
                hplatformy.move_platform_left2()
            else:
                hplatformy.move_platform_left_right2()
            if hplatformy.rect.centerx == self.battle.rect.centerx - 125:
                self.platform_moved_left_once4 = True

        self.platformrs.update()
        self.platformys.update()
        self.heart.platformrs.update()
        self.heart.platformys.update()

    def create_flying_bone(self):
        locations = ['right', 'top', 'bottom', 'left']

        for location in locations:
            self.add_flying_bone(location)

    def add_flying_bone(self, location):
        if location == 'right':
            flyingboneright = FlyingBones(self)
            flyingboneright.rect.y = self.heart.rect.y
            flyingboneright.rect.left = self.battle.rect.right + 15

            self.flyingbonesright.add(flyingboneright)

        if location == 'left':
            flyingboneleft = FlyingBonesLeft(self)
            flyingboneleft.rect.y = self.heart.rect.y
            flyingboneleft.rect.right = self.battle.rect.left - 15

            self.flyingbonesleft.add(flyingboneleft)

        if location == 'top':
            flyingbonetop = FlyingBonesTop(self)
            flyingbonetop.image = pygame.transform.rotozoom(flyingbonetop.image, 90, 1)
            flyingbonetop.rect = flyingbonetop.image.get_rect()
            flyingbonetop.rect.x = self.heart.rect.x
            flyingbonetop.rect.bottom = self.battle.rect.top - 15

            self.flyingbonestop.add(flyingbonetop)

        if location == 'bottom':
            flyingbonebottom = FlyingBonesBottom(self)
            flyingbonebottom.image = pygame.transform.rotozoom(flyingbonebottom.image, 90, 1)
            flyingbonebottom.rect = flyingbonebottom.image.get_rect()
            flyingbonebottom.rect.x = self.heart.rect.x
            flyingbonebottom.rect.top = self.battle.rect.bottom + 15

            self.flyingbonesbottom.add(flyingbonebottom)

    def create_going_left_up_bones(self):
        types_ = ['stem', 'tip']

        for type_ in types_:
            self.add_going_left_up_bones(type_)

    def add_going_left_up_bones(self, type):
        if type == 'stem':
            stem = FullBone(self)
            stem.image = pygame.transform.scale(stem.image, (16, 50))
            stem.rect = stem.image.get_rect()
            stem.rect.top = self.battle.rect.top
            stem.rect.right = self.battle.rect.right

            self.bones.add(stem)
        elif type == 'tip':
            tip = BoneTip(self)
            width = tip.rect.width
            height = tip.rect.height

            tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10))
            tip.image = pygame.transform.rotozoom(tip.image, 180, 1)
            tip.rect = tip.image.get_rect()
            tip.rect.top = self.battle.rect.top + 48
            tip.rect.right = self.battle.rect.right + 8

            self.bones.add(tip)

    def create_bones(self):
        bone = Attacks(self)
        bone_width = bone.rect.width
        available_space_x = self.battle.rect.width
        number_bone_x = available_space_x // bone_width

        for bone_number in range(number_bone_x):
            self.add_bones(bone_number)

    def add_bones(self, bone_number):
        bone = Attacks(self)
        bone_width = bone.rect.width
        bone.x = bone_width * bone_number + (self.battle.rect.left + 7)
        bone.rect.x = bone.x
        self.bones.add(bone)

    def create_between_bones(self):
        types = ['stemup', 'up', 'stemdown', 'down']
        sides = ['right', 'left']

        for side in sides:
            for type in types:
                self.add_between_bone(side, type)

    def add_between_bone(self, side, type):
        if self.between_bones_height == 'high':
            if side == 'right':
                stem = FullBone(self)
                tip = BoneTip(self)

                if type == 'stemdown' or type == 'stemup':
                    if type == 'stemdown':
                        stem.image = pygame.transform.scale(stem.image, (16, 125)).convert_alpha()
                        stem.rect = stem.image.get_rect()
                        stem.rect.right = self.battle.rect.right
                        stem.rect.bottom = self.battle.rect.bottom

                        self.between_bones_right.add(stem)
                    elif type == 'stemup':
                        stem.image = pygame.transform.scale(stem.image, (16, 30)).convert_alpha()
                        stem.rect = stem.image.get_rect()
                        stem.rect.right = self.battle.rect.right
                        stem.rect.top = self.battle.rect.top

                        self.between_bones_right.add(stem)
                elif type == 'up' or type == 'down':
                    width = tip.rect.width
                    height = tip.rect.height

                    if type == 'up':
                        tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                        tip.rect = tip.image.get_rect()
                        tip.rect.right = self.battle.rect.right + 7
                        tip.rect.bottom = 435

                        self.between_bones_right.add(tip)
                    elif type == 'down':
                        tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                        tip.image = pygame.transform.rotozoom(tip.image, 180, 1).convert_alpha()
                        tip.rect = tip.image.get_rect()
                        tip.rect.right = self.battle.rect.right + 8
                        tip.rect.top = 310

                        self.between_bones_right.add(tip)
            if side == 'left':
                stem = FullBone(self)
                tip = BoneTip(self)

                if type == 'stemdown' or type == 'stemup':
                    if type == 'stemdown':
                        stem.image = pygame.transform.scale(stem.image, (16, 125)).convert_alpha()
                        stem.rect = stem.image.get_rect()
                        stem.rect.left = self.battle.rect.left
                        stem.rect.bottom = self.battle.rect.bottom

                        self.between_bones_left.add(stem)
                    elif type == 'stemup':
                        stem.image = pygame.transform.scale(stem.image, (16, 30)).convert_alpha()
                        stem.rect = stem.image.get_rect()
                        stem.rect.left = self.battle.rect.left
                        stem.rect.top = self.battle.rect.top

                        self.between_bones_left.add(stem)
                elif type == 'up' or type == 'down':
                    width = tip.rect.width
                    height = tip.rect.height

                    if type == 'up':
                        tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                        tip.rect = tip.image.get_rect()
                        tip.rect.left = self.battle.rect.left - 7
                        tip.rect.bottom = 435

                        self.between_bones_left.add(tip)
                    elif type == 'down':
                        tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                        tip.image = pygame.transform.rotozoom(tip.image, 180, 1).convert_alpha()
                        tip.rect = tip.image.get_rect()
                        tip.rect.left = self.battle.rect.left - 8
                        tip.rect.top = 310

                        self.between_bones_left.add(tip)

        if self.between_bones_height == 'low':
            if side == 'right':
                stem = FullBone(self)
                tip = BoneTip(self)

                if type == 'stemdown' or type == 'stemup':
                    if type == 'stemdown':
                        stem.image = pygame.transform.scale(stem.image, (16, 30)).convert_alpha()
                        stem.rect = stem.image.get_rect()
                        stem.rect.right = self.battle.rect.right
                        stem.rect.bottom = self.battle.rect.bottom

                        self.between_bones_right.add(stem)
                    elif type == 'stemup':
                        stem.image = pygame.transform.scale(stem.image, (16, 125)).convert_alpha()
                        stem.rect = stem.image.get_rect()
                        stem.rect.right = self.battle.rect.right
                        stem.rect.top = self.battle.rect.top

                        self.between_bones_right.add(stem)
                elif type == 'up' or type == 'down':
                    width = tip.rect.width
                    height = tip.rect.height

                    if type == 'up':
                        tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                        tip.rect = tip.image.get_rect()
                        tip.rect.right = self.battle.rect.right + 7
                        tip.rect.bottom = 530

                        self.between_bones_right.add(tip)
                    elif type == 'down':
                        tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                        tip.image = pygame.transform.rotozoom(tip.image, 180, 1).convert_alpha()
                        tip.rect = tip.image.get_rect()
                        tip.rect.right = self.battle.rect.right + 8
                        tip.rect.top = 405

                        self.between_bones_right.add(tip)
            if side == 'left':
                stem = FullBone(self)
                tip = BoneTip(self)

                if type == 'stemdown' or type == 'stemup':
                    if type == 'stemdown':
                        stem.image = pygame.transform.scale(stem.image, (16, 30)).convert_alpha()
                        stem.rect = stem.image.get_rect()
                        stem.rect.left = self.battle.rect.left
                        stem.rect.bottom = self.battle.rect.bottom

                        self.between_bones_left.add(stem)
                    elif type == 'stemup':
                        stem.image = pygame.transform.scale(stem.image, (16, 125)).convert_alpha()
                        stem.rect = stem.image.get_rect()
                        stem.rect.left = self.battle.rect.left
                        stem.rect.top = self.battle.rect.top

                        self.between_bones_left.add(stem)
                elif type == 'up' or type == 'down':
                    width = tip.rect.width
                    height = tip.rect.height

                    if type == 'up':
                        tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                        tip.rect = tip.image.get_rect()
                        tip.rect.left = self.battle.rect.left - 7
                        tip.rect.bottom = 530

                        self.between_bones_left.add(tip)
                    elif type == 'down':
                        tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                        tip.image = pygame.transform.rotozoom(tip.image, 180, 1).convert_alpha()
                        tip.rect = tip.image.get_rect()
                        tip.rect.left = self.battle.rect.left - 8
                        tip.rect.top = 405

                        self.between_bones_left.add(tip)

    def create_bones_going_left_and_right_up_down(self):
        types = ['stemup', 'up', 'stemdown', 'down']

        for type in types:
            self.add_going_left_right_up_down_bone(type)

    def add_going_left_right_up_down_bone(self, type):
        stem = FullBone(self)
        tip = BoneTip(self)

        if type == 'stemdown' or type == 'stemup':
            if type == 'stemdown':
                stem.image = pygame.transform.scale(stem.image, (16, 35)).convert_alpha()
                stem.rect = stem.image.get_rect()
                stem.rect.left = self.battle.rect.left
                stem.rect.bottom = self.battle.rect.bottom

                self.between_bones_left.add(stem)
            elif type == 'stemup':
                stem.image = pygame.transform.scale(stem.image, (16, 175)).convert_alpha()
                stem.rect = stem.image.get_rect()
                stem.rect.right = self.battle.rect.right
                stem.rect.top = self.battle.rect.top

                self.between_bones_right.add(stem)
        elif type == 'up' or type == 'down':
            width = tip.rect.width
            height = tip.rect.height

            if type == 'up':
                tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                tip.rect = tip.image.get_rect()
                tip.rect.left = self.battle.rect.left - 7
                tip.rect.bottom = 525

                self.between_bones_left.add(tip)
            elif type == 'down':
                tip.image = pygame.transform.scale(tip.image, (width + 10, height + 10)).convert_alpha()
                tip.image = pygame.transform.rotozoom(tip.image, 180, 1).convert_alpha()
                tip.rect = tip.image.get_rect()
                tip.rect.right = self.battle.rect.right + 8
                tip.rect.top = 455

                self.between_bones_right.add(tip)

    def create_40_bones(self):
        directions = ['up', 'down']

        bonetip = BlueBoneTip(self)
        available_space = self.battle.rect.width * 1 // 3

        number_tip = available_space // (bonetip.rect.width + 10)

        for direction in directions:
            for tip in range(number_tip):
                self.add_40_bone(tip, direction)

        for tip in range(number_tip):
            self.add_40_bone(tip)

    def add_40_bone(self, tip, direction=None):
        if self.bone_color is None:
            bonetip = BoneTip(self)
            bonestem = FullBone(self)

            if direction == 'up':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.top = self.battle.rect.top + 10
                bonetip.rect.x = 413 - tip * bonetip.rect.width

                self.bones.add(bonetip)
            elif direction == 'down':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.image = pygame.transform.rotozoom(bonetip.image, 180, 1).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.bottom = self.battle.rect.bottom - 10
                bonetip.rect.x = 413 - tip * (bonetip.rect.width - 2)

                self.bones.add(bonetip)

            elif direction is None:
                bonestem.image = pygame.transform.scale(bonestem.image, (16, self.battle.rect.height - 2 * (bonetip.rect.height + 16))).convert_alpha()
                bonestem.rect = bonestem.image.get_rect()
                bonestem.rect.bottom = self.battle.rect.bottom - (bonetip.rect.height + 15)
                bonestem.rect.x = 421 - tip * (bonetip.rect.width + 10)

                self.bones.add(bonestem)

        elif self.bone_color == 'orange':
            bonetip = OrangeBoneTip(self)
            bonestem = OrangeBoneStem(self)

            if direction == 'up':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.top = self.battle.rect.top + 10
                bonetip.rect.x = 390 - tip * bonetip.rect.width

                self.orange_bones.add(bonetip)
            elif direction == 'down':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.image = pygame.transform.rotozoom(bonetip.image, 180, 1).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.bottom = self.battle.rect.bottom - 10
                bonetip.rect.x = 390 - tip * (bonetip.rect.width - 2)

                self.orange_bones.add(bonetip)

            elif direction is None:
                bonestem.image = pygame.transform.scale(bonestem.image, (16, self.battle.rect.height - 2 * (bonetip.rect.height + 16))).convert_alpha()
                bonestem.rect = bonestem.image.get_rect()
                bonestem.rect.bottom = self.battle.rect.bottom - (bonetip.rect.height + 15)
                bonestem.rect.x = 398 - tip * (bonetip.rect.width + 10)

                self.orange_bones.add(bonestem)

        elif self.bone_color == 'blue':
            bonetip = BlueBoneTip(self)
            bonestem = BlueBoneStem(self)

            if direction == 'up':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.top = self.battle.rect.top + 10
                bonetip.rect.x = 390 - tip * bonetip.rect.width

                self.blue_bones.add(bonetip)
            elif direction == 'down':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.image = pygame.transform.rotozoom(bonetip.image, 180, 1).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.bottom = self.battle.rect.bottom - 10
                bonetip.rect.x = 390 - tip * (bonetip.rect.width - 2)

                self.blue_bones.add(bonetip)

            elif direction is None:
                bonestem.image = pygame.transform.scale(bonestem.image, (16, self.battle.rect.height - 2 * (bonetip.rect.height + 16))).convert_alpha()
                bonestem.rect = bonestem.image.get_rect()
                bonestem.rect.bottom = self.battle.rect.bottom - (bonetip.rect.height + 15)
                bonestem.rect.x = 398 - tip * (bonetip.rect.width + 10)

                self.blue_bones.add(bonestem)

    def create_60_bones(self):
        directions = ['up', 'down']

        bonetip = BoneTip(self)
        available_space = self.battle.rect.width * 2 // 3

        number_tip = available_space // (bonetip.rect.width + 10)

        for direction in directions:
            for tip in range(number_tip):
                self.add_60_bone(tip, direction)

        for tip in range(number_tip):
            self.add_60_bone(tip)

    def add_60_bone(self, tip, direction=None):
        if self.bone_color is None:
            bonetip = BoneTip(self)
            bonestem = FullBone(self)

            if direction == 'up':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.top = self.battle.rect.top + 10
                bonetip.rect.x = 710 - tip * bonetip.rect.width

                self.bones.add(bonetip)
            elif direction == 'down':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.image = pygame.transform.rotozoom(bonetip.image, 180, 1).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.bottom = self.battle.rect.bottom - 10
                bonetip.rect.x = 710 - tip * (bonetip.rect.width - 2)

                self.bones.add(bonetip)

            elif direction is None:
                bonestem.image = pygame.transform.scale(bonestem.image, (16, self.battle.rect.height - 2 * (bonetip.rect.height + 16))).convert_alpha()
                bonestem.rect = bonestem.image.get_rect()
                bonestem.rect.bottom = self.battle.rect.bottom - (bonetip.rect.height + 15)
                bonestem.rect.x = 718 - tip * (bonetip.rect.width + 10)

                self.bones.add(bonestem)

        elif self.bone_color == 'orange':
            bonetip = OrangeBoneTip(self)
            bonestem = OrangeBoneStem(self)

            if direction == 'up':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.top = self.battle.rect.top + 10
                bonetip.rect.x = 710 - tip * bonetip.rect.width

                self.orange_bones.add(bonetip)
            elif direction == 'down':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.image = pygame.transform.rotozoom(bonetip.image, 180, 1).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.bottom = self.battle.rect.bottom - 10
                bonetip.rect.x = 710 - tip * (bonetip.rect.width - 2)

                self.orange_bones.add(bonetip)

            elif direction is None:
                bonestem.image = pygame.transform.scale(bonestem.image, (16, self.battle.rect.height - 2 * (bonetip.rect.height + 16))).convert_alpha()
                bonestem.rect = bonestem.image.get_rect()
                bonestem.rect.bottom = self.battle.rect.bottom - (bonetip.rect.height + 15)
                bonestem.rect.x = 718 - tip * (bonetip.rect.width + 10)

                self.orange_bones.add(bonestem)

        elif self.bone_color == 'blue':
            bonetip = BlueBoneTip(self)
            bonestem = BlueBoneStem(self)

            if direction == 'up':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.top = self.battle.rect.top + 10
                bonetip.rect.x = 710 - tip * bonetip.rect.width

                self.blue_bones.add(bonetip)
            elif direction == 'down':
                width = bonetip.rect.width
                height = bonetip.rect.height

                bonetip.image = pygame.transform.scale(bonetip.image, (width + 10, height + 10)).convert_alpha()
                bonetip.image = pygame.transform.rotozoom(bonetip.image, 180, 1).convert_alpha()
                bonetip.rect = bonetip.image.get_rect()
                bonetip.rect.bottom = self.battle.rect.bottom - 10
                bonetip.rect.x = 710 - tip * (bonetip.rect.width - 2)

                self.blue_bones.add(bonetip)

            elif direction is None:
                bonestem.image = pygame.transform.scale(bonestem.image, (16, self.battle.rect.height - 2 * (bonetip.rect.height + 16))).convert_alpha()
                bonestem.rect = bonestem.image.get_rect()
                bonestem.rect.bottom = self.battle.rect.bottom - (bonetip.rect.height + 15)
                bonestem.rect.x = 718 - tip * (bonetip.rect.width + 10)

                self.blue_bones.add(bonestem)

    def make_60_warning(self):
        self.heart.warnings()

        self.heart.warning = pygame.transform.scale(self.heart.warning, (self.battle.rect.height, self.battle.rect.width * 2 // 3))
        self.heart.warning = pygame.transform.rotozoom(self.heart.warning, 90, 1)
        self.heart.warning_rect = self.heart.warning.get_rect()
        self.heart.warning_rect.top = self.battle.rect.top
        self.heart.warning_rect.right = self.battle.rect.right

    def make_full_warning(self):
        self.heart.warnings()
        height = self.heart.warning_rect.height

        self.heart.warning = pygame.transform.scale(self.heart.warning, (self.battle.rect.width, height))
        self.heart.warning_rect = self.heart.warning.get_rect()
        self.heart.warning_rect.bottom = self.battle.rect.bottom
        self.heart.warning_rect.right = self.battle.rect.right

    def create_center_blasters_o(self):
        direction = 'center'
        type_ = 'opened'

        for number in range(1, 5):
            self.add_blasters(direction, number, type_)

    def create_center_blasters_c(self):
        direction = 'center'
        type_ = 'closed'

        for number in range(1, 5):
            self.add_blasters(direction, number, type_)

    def create_diagonal_blasters_o(self):
        direction = 'diagonal'
        type_ = 'opened'

        for number in range(1, 5):
            self.add_blasters(direction, number, type_)

    def create_diagonal_blasters_c(self):
        direction = 'diagonal'
        type_ = 'closed'

        for number in range(1, 5):
            self.add_blasters(direction, number, type_)

    def create_up_down_blasters_c(self):
        direction = 'up down'
        type_ = 'closed'

        for number in range(1, 5):
            self.add_blasters(direction, number, type_)

    def create_up_down_blasters_o(self):
        direction = 'up down'
        type_ = 'opened'

        for number in range(1, 5):
            self.add_blasters(direction, number, type_)

    def create_trap_bone_bl_gasterblaster_c(self):
        direction = 'bottom left'
        type_ = 'closed'

        for number in range(1, 3):
            self.add_blasters(direction, number, type_)

    def create_trap_bone_bl_gasterblaster_o_up(self):
        direction = 'bottom left (up)'
        type_ = 'opened'

        for number in range(1, 3):
            self.add_blasters(direction, number, type_)

    def create_trap_bone_bl_gasterblaster_o_down(self):
        direction = 'bottom left (down)'
        type_ = 'opened'

        for number in range(1, 3):
            self.add_blasters(direction, number, type_)

    def create_block_gasterblaster_c(self):
        direction = 'trap bone bl'
        type_ = 'close'

        self.add_blasters(direction, 1, type_)

    def create_block_gasterblaster_o(self):
        direction = 'trap bone bl'
        type_ = 'opened'

        self.add_blasters(direction, 1, type_)

    def create_just_bottom_gasterblaster_c(self):
        direction = 'just bottom'
        type_ = 'closed'

        self.add_blasters(direction, 1, type_)

    def create_just_top_gasterblaster_c(self):
        direction = 'just top'
        type_ = 'closed'

        self.add_blasters(direction, 1, type_)

    def create_just_bottom_gasterblaster_o(self):
        direction = 'just bottom'
        type_ = 'opened'

        self.add_blasters(direction, 1, type_)

    def create_just_top_gasterblaster_o(self):
        direction = 'just top'
        type_ = 'opened'

        self.add_blasters(direction, 1, type_)

    def create_just_left_gasterblaster_c(self):
        direction = 'just left'
        type_ = 'closed'

        self.add_blasters(direction, 1, type_)

    def create_just_left_gasterblaster_o(self):
        direction = 'just left'
        type_ = 'opened'

        self.add_blasters(direction, 1, type_)

    def create_just_right_gasterblaster_c(self):
        direction = 'just right'
        type_ = 'closed'

        self.add_blasters(direction, 1, type_)

    def create_just_right_gasterblaster_o(self):
        direction = 'just right'
        type_ = 'opened'

        self.add_blasters(direction, 1, type_)

    def create_full_bottom_and_half_side_gaster_blaster_c(self):
        direction = 'full bottom half side'
        type_ = 'closed'

        for number in range(1, 3):
            self.add_blasters(direction, number, type_)

    def create_full_bottom_and_half_side_gaster_blaster_o(self):
        direction = 'full bottom half side'
        type_ = 'opened'

        for number in range(1, 3):
            self.add_blasters(direction, number, type_)

    def created_just_bottom_right_diagonal_c(self):
        direction = 'just bottom left diagonal'
        type_ = 'closed'

        self.add_blasters(direction, 1, type_)

    def created_just_bottom_right_diagonal_o(self):
        direction = 'just bottom left diagonal'
        type_ = 'opened'

        self.add_blasters(direction, 1, type_)

    def created_blaster_above_just_bottom_c(self):
        direction = 'blaster above just bottom'
        type_ = 'closed'

        self.add_blasters(direction, 1, type_)

    def created_blaster_above_just_bottom_o(self):
        direction = 'blaster above just bottom'
        type_ = 'opened'

        self.add_blasters(direction, 1, type_)

    def create_tracking_blaster_top_c(self):
        direction = 'tracking blaster top'
        type_ = 'closed'

        self.add_blasters(direction, 1, type_)

    def create_center_of_battlebox_c(self):
        direction = 'center of battlebox'
        type_ = 'closed'

        self.add_blasters(direction, 1, type_)

    def add_blasters(self, direction, number, type):
        if direction == 'center of battlebox' and type == 'closed':
            blaster = FellBlaster(self)

            width = self.blaster.rect.width
            height = self.blaster.rect.height

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.top - 10
            blaster.rect.centerx = self.battle.rect.centerx

            self.gasterblaster.add(blaster)
        if direction == 'tracking blaster top' and type == 'closed':
            blaster = FellBlaster(self)

            width = self.blaster.rect.width
            height = self.blaster.rect.height

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.top - 10
            blaster.rect.centerx = self.heart.rect.centerx

            self.gasterblaster.add(blaster)

        if direction == 'blaster above just bottom' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            height = self.blaster.rect.height
            width = self.blaster.rect.width

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.bottom - 40
            blaster.rect.left = self.battle.rect.right + 15
            blastbeam.image = pygame.transform.scale(blastbeam.image, (75, 900)).convert_alpha()
            blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -90, 1).convert_alpha()
            blastbeam.rect = blastbeam.image.get_rect()
            blastbeam.rect.right = blaster.rect.left + 90
            blastbeam.rect.bottom = blaster.rect.bottom - 30

            self.gasterblaster.add(blaster)
            self.blast.add(blastbeam)

        if direction == 'blaster above just bottom' and type == 'closed':
            blaster = FellBlaster(self)

            width = self.blaster.rect.width
            height = self.blaster.rect.height

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.bottom - 40
            blaster.rect.left = self.battle.rect.right + 15

            self.gasterblaster.add(blaster)

        if direction == 'just bottom left diagonal' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            x = blaster.rect.x
            y = blaster.rect.y
            x2 = blastbeam.rect.x
            y2 = blastbeam.rect.y

            blaster.image = pygame.transform.rotate(blaster.image, -135).convert_alpha()
            blaster.rect.x = x + 10
            blaster.rect.y = y + 435
            blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -135, 1).convert_alpha()
            blastbeam.rect = blastbeam.image.get_rect()
            blastbeam.rect.x = x2 - 175
            blastbeam.rect.y = y2 + 110

            self.gasterblaster.add(blaster)
            self.blast.add(blastbeam)

        if direction == 'just bottom left diagonal' and type == 'closed':
            blaster = FellBlaster(self)

            x = blaster.rect.x
            y = blaster.rect.y

            blaster.image = pygame.transform.rotozoom(blaster.image, -135, 1).convert_alpha()
            blaster.rect.x = x + 10
            blaster.rect.y = y + 435

            self.gasterblaster.add(blaster)

        if direction == 'full bottom half side' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)
            width = blaster.rect.width
            height = blaster.rect.height

            if number == 1:
                blaster.image = pygame.transform.scale(blaster.image, (width + 45, height + 20))
                blaster.image = pygame.transform.rotozoom(blaster.image, -75, 1)
                blaster.rect = blaster.image.get_rect()
                blaster.rect.left = self.battle.rect.right + 35
                blaster.rect.bottom = self.battle.rect.bottom + 5
                blastbeam.image = pygame.transform.scale(blastbeam.image, (100, 900))
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -75, 1)
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.left = self.battle.rect.right - 735
                blastbeam.rect.top = self.battle.rect.bottom - 165
            if number == 2:
                blaster.image = pygame.transform.scale(blaster.image, (width + 45, height + 20))
                blaster.image = pygame.transform.rotozoom(blaster.image, -75, 1)
                blaster.image = pygame.transform.flip(blaster.image, True, False)
                blaster.rect = blaster.image.get_rect()
                blaster.rect.right = self.battle.rect.left - 35
                blaster.rect.bottom = self.battle.rect.bottom + 5
                blastbeam.image = pygame.transform.scale(blastbeam.image, (100, 900))
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -75, 1)
                blastbeam.image = pygame.transform.flip(blastbeam.image, True, False)
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.right = self.battle.rect.left + 735
                blastbeam.rect.top = self.battle.rect.bottom - 165

            self.gasterblaster.add(blaster)
            self.blast.add(blastbeam)

        if direction == 'full bottom half side' and type == 'closed':
            blaster = FellBlaster(self)
            width = blaster.rect.width
            height = blaster.rect.height

            if number == 1:
                blaster.image = pygame.transform.scale(blaster.image, (width + 45, height + 20))
                blaster.image = pygame.transform.rotozoom(blaster.image, -75, 1)
                blaster.rect = blaster.image.get_rect()
                blaster.rect.left = self.battle.rect.right + 35
                blaster.rect.bottom = self.battle.rect.bottom + 5
            if number == 2:
                blaster.image = pygame.transform.scale(blaster.image, (width + 45, height + 20))
                blaster.image = pygame.transform.rotozoom(blaster.image, -75, 1)
                blaster.image = pygame.transform.flip(blaster.image, True, False)
                blaster.rect = blaster.image.get_rect()
                blaster.rect.right = self.battle.rect.left - 35
                blaster.rect.bottom = self.battle.rect.bottom + 5

            self.gasterblaster.add(blaster)

        if direction == 'just right' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            width = self.blaster.rect.width
            height = self.blaster.rect.height

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.top - 10
            blaster.rect.right = self.battle.rect.right + 35
            blastbeam.image = pygame.transform.scale(blastbeam.image, (75, 600)).convert_alpha()
            blastbeam.rect = blastbeam.image.get_rect()
            blastbeam.rect.right = self.battle.rect.right
            blastbeam.rect.top = blaster.rect.top + 50

            self.gasterblaster.add(blaster)
            self.blast.add(blastbeam)

        if direction == 'just right' and type == 'closed':
            blaster = FellBlaster(self)

            width = self.blaster.rect.width
            height = self.blaster.rect.height

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.top - 10
            blaster.rect.right = self.battle.rect.right + 35

            self.gasterblaster.add(blaster)

        if direction == 'just left' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            width = self.blaster.rect.width
            height = self.blaster.rect.height

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.top - 10
            blaster.rect.left = self.battle.rect.left - 35
            blastbeam.image = pygame.transform.scale(blastbeam.image, (75, 600)).convert_alpha()
            blastbeam.rect = blastbeam.image.get_rect()
            blastbeam.rect.left = self.battle.rect.left
            blastbeam.rect.top = blaster.rect.top + 50

            self.gasterblaster.add(blaster)
            self.blast.add(blastbeam)

        if direction == 'just left' and type == 'closed':
            blaster = FellBlaster(self)

            width = self.blaster.rect.width
            height = self.blaster.rect.height

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.top - 10
            blaster.rect.left = self.battle.rect.left - 35

            self.gasterblaster.add(blaster)

        if direction == 'just top' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            height = self.blaster.rect.height
            width = self.blaster.rect.width

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.top = self.battle.rect.top - 30
            blaster.rect.left = self.battle.rect.right + 15
            blastbeam.image = pygame.transform.scale(blastbeam.image, (75, 900)).convert_alpha()
            blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -90, 1).convert_alpha()
            blastbeam.rect = blastbeam.image.get_rect()
            blastbeam.rect.right = blaster.rect.left + 90
            blastbeam.rect.top = blaster.rect.top + 35

            self.gasterblaster.add(blaster)
            self.blast.add(blastbeam)

        if direction == 'just bottom' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            height = self.blaster.rect.height
            width = self.blaster.rect.width

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.bottom + 30
            blaster.rect.left = self.battle.rect.right + 15
            blastbeam.image = pygame.transform.scale(blastbeam.image, (75, 900)).convert_alpha()
            blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -90, 1).convert_alpha()
            blastbeam.rect = blastbeam.image.get_rect()
            blastbeam.rect.right = blaster.rect.left + 90
            blastbeam.rect.bottom = blaster.rect.bottom - 30

            self.gasterblaster.add(blaster)
            self.blast.add(blastbeam)

        if direction == 'just top' and type == 'closed':
            blaster = FellBlaster(self)

            width = self.blaster.rect.width
            height = self.blaster.rect.height

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.top = self.battle.rect.top - 30
            blaster.rect.left = self.battle.rect.right + 15

            self.gasterblaster.add(blaster)

        if direction == 'just bottom' and type == 'closed':
            blaster = FellBlaster(self)

            width = self.blaster.rect.width
            height = self.blaster.rect.height

            blaster.image = pygame.transform.scale(blaster.image, (width - 25, height)).convert_alpha()
            blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.bottom = self.battle.rect.bottom + 30
            blaster.rect.left = self.battle.rect.right + 15

            self.gasterblaster.add(blaster)

        if direction == 'trap bone bl' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            height = self.blaster.rect.height
            width = self.blaster.rect.width

            blaster.image = pygame.transform.scale(blaster.image, (width + 60, height)).convert_alpha()
            blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.top = self.battle.rect.top - 40
            blaster.rect.left = self.battle.rect.right + 15
            blastbeam.image = pygame.transform.scale(blastbeam.image, (125, 900)).convert_alpha()
            blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -90, 1).convert_alpha()
            blastbeam.rect = blastbeam.image.get_rect()
            blastbeam.rect.right = blaster.rect.left + 90
            blastbeam.rect.top = blaster.rect.top + 55

            self.blockblast.add(blastbeam)
            self.blockblaster.add(blaster)

        if direction == 'trap bone bl' and type == 'close':
            blaster = FellBlaster(self)

            height = self.blaster.rect.height
            width = self.blaster.rect.width

            blaster.image = pygame.transform.scale(blaster.image, (width + 60, height)).convert_alpha()
            blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
            blaster.rect = blaster.image.get_rect()
            blaster.rect.top = self.battle.rect.top - 40
            blaster.rect.left = self.battle.rect.right + 15

            self.blockblaster.add(blaster)

        if direction == 'bottom left (down)' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            height = self.blaster.rect.height

            if number == 1:
                blaster.image = pygame.transform.scale(blaster.image, (75, height - 20)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom - 45
                blaster.rect.left = self.battle.rect.right + 15
            if number == 2:
                blaster.image = pygame.transform.scale(blaster.image, (75,  height - 20)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom - 5
                blaster.rect.left = self.battle.rect.right + 15
                blastbeam.image = pygame.transform.scale(blastbeam.image, (45, 900)).convert_alpha()
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -90, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.right = self.battle.rect.right + 100
                blastbeam.rect.bottom = self.battle.rect.bottom - 21

                self.blast.add(blastbeam)

            self.gasterblaster.add(blaster)

        if direction == 'bottom left (up)' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            height = self.blaster.rect.height

            if number == 1:
                blaster.image = pygame.transform.scale(blaster.image, (75, height - 20)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom - 45
                blaster.rect.left = self.battle.rect.right + 15
                blastbeam.image = pygame.transform.scale(blastbeam.image, (45, 900)).convert_alpha()
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -90, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.right = self.battle.rect.right + 100
                blastbeam.rect.bottom = self.battle.rect.bottom - 58

                self.blast.add(blastbeam)
            if number == 2:
                blaster.image = pygame.transform.scale(blaster.image, (75,  height - 20)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom - 5
                blaster.rect.left = self.battle.rect.right + 15

            self.gasterblaster.add(blaster)

        if direction == 'bottom left' and type == 'closed':
            blaster = FellBlaster(self)

            height = self.blaster.rect.height

            if number == 1:
                blaster.image = pygame.transform.scale(blaster.image, (75, height - 20)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom - 45
                blaster.rect.left = self.battle.rect.right + 15
            if number == 2:
                blaster.image = pygame.transform.scale(blaster.image, (75,  height - 20)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom - 5
                blaster.rect.left = self.battle.rect.right + 15

            self.gasterblaster.add(blaster)

        if direction == 'up down' and type == 'closed':
            blaster = FellBlaster(self)

            height = self.blaster.rect.height

            if number == 1:
                blaster.image = pygame.transform.scale(blaster.image, (146, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom + 30
                blaster.rect.left = self.battle.rect.right + 25
            if number == 2:
                blaster.image = pygame.transform.scale(blaster.image, (146, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, 90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom + 30
                blaster.rect.right = self.battle.rect.left - 25
            if number == 3:
                blaster.image = pygame.transform.scale(blaster.image, (146, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.top = self.battle.rect.top - 30
                blaster.rect.left = self.battle.rect.right + 25
            if number == 4:
                blaster.image = pygame.transform.scale(blaster.image, (146, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, 90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.top = self.battle.rect.top - 30
                blaster.rect.right = self.battle.rect.left - 25

            self.gasterblaster.add(blaster)

        if direction == 'up down' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            height = self.blaster.rect.height

            if number == 1:
                blaster.image = pygame.transform.scale(blaster.image, (146, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom + 30
                blaster.rect.left = self.battle.rect.right + 25
                blastbeam.image = pygame.transform.scale(blastbeam.image, (75, 870)).convert_alpha()
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -90, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.centerx = self.battle.rect.centerx
                blastbeam.rect.bottom = self.battle.rect.bottom - 7

                self.blast.add(blastbeam)

            if number == 2:
                blaster.image = pygame.transform.scale(blaster.image, (146, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, 90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.bottom = self.battle.rect.bottom + 30
                blaster.rect.right = self.battle.rect.left - 25
            if number == 3:
                blaster.image = pygame.transform.scale(blaster.image, (146, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.top = self.battle.rect.top - 30
                blaster.rect.left = self.battle.rect.right + 25
                blastbeam.image = pygame.transform.scale(blastbeam.image, (75, 870)).convert_alpha()
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -90, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.centerx = self.battle.rect.centerx
                blastbeam.rect.top = self.battle.rect.top + 7

                self.blast.add(blastbeam)

            if number == 4:
                blaster.image = pygame.transform.scale(blaster.image, (146, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, 90, 1).convert_alpha()
                blaster.rect = blaster.image.get_rect()
                blaster.rect.top = self.battle.rect.top - 30
                blaster.rect.right = self.battle.rect.left - 25

            self.gasterblaster.add(blaster)

        if direction == 'center' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            x = self.blaster.rect.x
            y = self.blaster.rect.y
            x2 = self.beam.rect.x
            y2 = self.beam.rect.y
            width = self.blaster.rect.width
            height = self.blaster.rect.height
            width2 = self.beam.rect.width
            height2 = self.beam.rect.height

            if number == 1:
                blaster.image = pygame.transform.scale(blaster.image, (width + 75, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -55, 1).convert_alpha()
                blaster.rect.y = y + 175
                blastbeam.image = pygame.transform.scale(blastbeam.image, (width2 + 50, height2 + 70)).convert_alpha()
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -55, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.x = x2 - 310
                blastbeam.rect.y = y2 + 270

            if number == 2:
                blaster.image = pygame.transform.scale(blaster.image, (width + 75, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -310, 1).convert_alpha()
                blaster.rect.x = x - 475
                blaster.rect.y = y + 175
                blastbeam.image = pygame.transform.scale(blastbeam.image, (width2 + 50, height2 - 5)).convert_alpha()
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -310, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.x = x2 - 220
                blastbeam.rect.y = y2 + 270

            if number == 3:
                blaster.image = pygame.transform.scale(blaster.image, (width + 75, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -125, 1).convert_alpha()
                blaster.rect.x = x + 5
                blaster.rect.y = y + 190
                blastbeam.image = pygame.transform.scale(blastbeam.image, (width2 + 50, height2 + 190)).convert_alpha()
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -125, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.x = x2 - 405
                blastbeam.rect.y = y2 - 185

            if number == 4:
                blaster.image = pygame.transform.scale(blaster.image, (width + 75, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -240, 1).convert_alpha()
                blaster.rect.x = x - 460
                blaster.rect.y = y + 198
                blastbeam.image = pygame.transform.scale(blastbeam.image, (width2 + 50, height2 + 230)).convert_alpha()
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -240, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.x = x2 - 200
                blastbeam.rect.y = y2 - 150

            self.blast.add(blastbeam)
            self.gasterblaster.add(blaster)

        if direction == 'center' and type == 'closed':
            blaster = FellBlaster(self)

            x = self.blaster.rect.x
            y = self.blaster.rect.y
            width = self.blaster.rect.width
            height = self.blaster.rect.height

            if number == 1:
                blaster.image = pygame.transform.scale(blaster.image, (width + 75, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -55, 1).convert_alpha()
                blaster.rect.y = y + 175
            if number == 2:
                blaster.image = pygame.transform.scale(blaster.image, (width + 75, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -310, 1).convert_alpha()
                blaster.rect.x = x - 475
                blaster.rect.y = y + 175
            if number == 3:
                blaster.image = pygame.transform.scale(blaster.image, (width + 75, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -125, 1).convert_alpha()
                blaster.rect.x = x + 5
                blaster.rect.y = y + 190
            if number == 4:
                blaster.image = pygame.transform.scale(blaster.image, (width + 75, height)).convert_alpha()
                blaster.image = pygame.transform.rotozoom(blaster.image, -240, 1).convert_alpha()
                blaster.rect.x = x - 460
                blaster.rect.y = y + 198

            self.gasterblaster.add(blaster)

        if direction == 'diagonal' and type == 'opened':
            blaster = FellBlasted(self)
            blastbeam = BlastBeam(self)

            x = self.blasted.rect.x
            y = self.blasted.rect.y
            x2 = self.beam.rect.x
            y2 = self.beam.rect.y

            if number == 1:
                blaster.image = pygame.transform.rotate(blaster.image, -45).convert_alpha()
                blaster.rect.x = x
                blaster.rect.y = y
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -45, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.x = x2 - 200
                blastbeam.rect.y = y2 + 100

                self.blast.add(blastbeam)

            if number == 2:
                blaster.image = pygame.transform.rotate(blaster.image, -135).convert_alpha()
                blaster.rect.x = x + 10
                blaster.rect.y = y + 435
                blastbeam.image = pygame.transform.rotozoom(blastbeam.image, -135, 1).convert_alpha()
                blastbeam.rect = blastbeam.image.get_rect()
                blastbeam.rect.x = x2 - 175
                blastbeam.rect.y = y2 + 110

                self.blast.add(blastbeam)

            if number == 3:
                blaster.image = pygame.transform.rotate(blaster.image, -225).convert_alpha()
                blaster.rect.x = x - 425
                blaster.rect.y = y + 445
            if number == 4:
                blaster.image = pygame.transform.rotate(blaster.image, -315).convert_alpha()
                blaster.rect.x = x - 430
                blaster.rect.y = y + 10

            self.gasterblaster.add(blaster)

        if direction == 'diagonal' and type == 'closed':
            blaster = FellBlaster(self)
            x = self.blaster.rect.x
            y = self.blaster.rect.y

            if number == 1:
                blaster.image = pygame.transform.rotozoom(blaster.image, -45, 1).convert_alpha()
                blaster.rect.x = x
                blaster.rect.y = y
            if number == 2:
                blaster.image = pygame.transform.rotozoom(blaster.image, -135, 1).convert_alpha()
                blaster.rect.x = x + 10
                blaster.rect.y = y + 435
            if number == 3:
                blaster.image = pygame.transform.rotozoom(blaster.image, -225, 1).convert_alpha()
                blaster.rect.x = x - 425
                blaster.rect.y = y + 445
            if number == 4:
                blaster.image = pygame.transform.rotozoom(blaster.image, -315, 1).convert_alpha()
                blaster.rect.x = x - 430
                blaster.rect.y = y + 10

            self.gasterblaster.add(blaster)

    def create_trap_bone_bl(self):
        stem_amount = 2
        end_spot = 'bottom left corner'

        self.add_trap_bone(stem_amount, end_spot)

    def create_single_bone_horizontal(self):
        stem_amount = 1
        end_spot = 'horizontal thin'

        self.add_trap_bone(stem_amount, end_spot)

    def add_trap_bone(self, amount, end_spot):
        for index in range(amount):
            if amount == 2 and end_spot == 'bottom left corner':
                fullbone = FullBone(self)

                if index == 0:
                    fullbone.image = pygame.transform.scale(fullbone.image, (20, self.battle.rect.height + 20)).convert_alpha()
                    fullbone.rect = fullbone.image.get_rect()
                    fullbone.rect.bottom = self.battle.rect.bottom
                    fullbone.rect.centery = self.battle.rect.centery
                    fullbone.rect.left = self.battle.rect.right + 25
                    for number in range(1, 3):
                        bonetip = BoneTip(self)

                        width = bonetip.rect.width
                        height = bonetip.rect.height

                        if number == 1:
                            bonetip.image = pygame.transform.scale(bonetip.image, (width * 2, height * 2)).convert_alpha()
                            bonetip.rect = bonetip.image.get_rect()
                            bonetip.rect.bottom = fullbone.rect.top
                            bonetip.rect.centerx = fullbone.rect.centerx

                        elif number == 2:
                            bonetip.image = pygame.transform.scale(bonetip.image, (width * 2, height * 2)).convert_alpha()
                            bonetip.image = pygame.transform.rotozoom(bonetip.image, 180, 1).convert_alpha()
                            bonetip.rect = bonetip.image.get_rect()
                            bonetip.rect.top = fullbone.rect.bottom - 5
                            bonetip.rect.centerx = fullbone.rect.centerx

                        self.right_bone.add(bonetip)

                    self.right_bone.add(fullbone)

                elif index == 1:
                    fullbone.image = pygame.transform.scale(fullbone.image, (20, self.battle.rect.width + 20)).convert_alpha()
                    fullbone.image = pygame.transform.rotozoom(fullbone.image, 90, 1).convert_alpha()
                    fullbone.rect = fullbone.image.get_rect()
                    fullbone.rect.bottom = self.battle.rect.top - 25
                    fullbone.rect.centerx = self.battle.rect.centerx
                    for number in range(1, 3):
                        bonetip = BoneTip(self)

                        width = bonetip.rect.width
                        height = bonetip.rect.height

                        if number == 1:
                            bonetip.image = pygame.transform.scale(bonetip.image, (width * 2, height * 2)).convert_alpha()
                            bonetip.image = pygame.transform.rotozoom(bonetip.image, 90, 1).convert_alpha()
                            bonetip.rect = bonetip.image.get_rect()
                            bonetip.rect.right = fullbone.rect.left + 3
                            bonetip.rect.centery = fullbone.rect.centery

                        elif number == 2:
                            bonetip.image = pygame.transform.scale(bonetip.image, (width * 2, height * 2)).convert_alpha()
                            bonetip.image = pygame.transform.rotozoom(bonetip.image, -90, 1).convert_alpha()
                            bonetip.rect = bonetip.image.get_rect()
                            bonetip.rect.left = fullbone.rect.right - 5
                            bonetip.rect.centery = fullbone.rect.centery

                        self.top_bone.add(bonetip)

                    self.top_bone.add(fullbone)

            if amount == 1 and end_spot == 'horizontal thin':
                fullbone = FullBone(self)

                fullbone.image = pygame.transform.scale(fullbone.image, (20, self.battle.rect.width - 5)).convert_alpha()
                fullbone.image = pygame.transform.rotozoom(fullbone.image, 90, 1).convert_alpha()
                fullbone.rect = fullbone.image.get_rect()
                fullbone.rect.bottom = self.battle.rect.bottom - 6
                fullbone.rect.left = self.battle.rect.right + 38
                for number in range(1, 3):
                    bonetip = BoneTip(self)

                    width = bonetip.rect.width
                    height = bonetip.rect.height

                    if number == 1:
                        bonetip.image = pygame.transform.scale(bonetip.image, (width * 2, height * 2)).convert_alpha()
                        bonetip.image = pygame.transform.rotozoom(bonetip.image, 90, 1).convert_alpha()
                        bonetip.rect = bonetip.image.get_rect()
                        bonetip.rect.right = fullbone.rect.left + 3
                        bonetip.rect.centery = fullbone.rect.centery

                    elif number == 2:
                        bonetip.image = pygame.transform.scale(bonetip.image, (width * 2, height * 2)).convert_alpha()
                        bonetip.image = pygame.transform.rotozoom(bonetip.image, -90, 1).convert_alpha()
                        bonetip.rect = bonetip.image.get_rect()
                        bonetip.rect.left = fullbone.rect.right - 5
                        bonetip.rect.centery = fullbone.rect.centery

                    self.bottom_bone.add(bonetip)

                self.bottom_bone.add(fullbone)

    def change_right_bone_number(self):
        if self.right_bone_number == 1:
            self.right_bone_number = 2
        elif self.right_bone_number == 2:
            self.right_bone_number = 3
        elif self.right_bone_number == 3:
            self.right_bone_number = 1

    def change_top_bone_number(self):
        if self.top_bone_number == 1:
            self.top_bone_number = 2
        elif self.top_bone_number == 2:
            self.top_bone_number = 3
        elif self.top_bone_number == 3:
            self.top_bone_number = 1

    def move_right_trap_bone_bl(self):
        self.right_bone.update()

        for bone in self.right_bone.sprites():
            self.change_right_bone_number()

            if bone.rect.x >= 325 and self.right_bone_number == 2:
                bone.update_right_bone_bl()
            elif bone.rect.x >= 325 and self.right_bone_number == 3:
                bone.update_right_bone_bl()
            elif bone.rect.x >= 338 and self.right_bone_number == 1:
                bone.update_right_bone_bl()

    def move_top_trap_bone_bl(self):
        self.top_bone.update()

        for bone in self.top_bone.sprites():
            self.change_top_bone_number()

            if bone.rect.y <= 415 and self.top_bone_number == 2:
                bone.update_top_bone_bl()
            elif bone.rect.y <= 415 and self.top_bone_number == 3:
                bone.update_top_bone_bl()
            elif bone.rect.y <= 426 and self.top_bone_number == 1:
                bone.update_top_bone_bl()

    def animate_title(self):
        self.title.animate_title()
        self.title.draw_title()

    def animate_title2(self):
        self.title.draw_title2()
        self.title.animate_title2()

    def add_health(self):
        self.stats.health += 20 - self.stats.health
        self.settings.health_bar_width = 100
        self.hb.make_bar()
        self.hn.health1()
        self.show_healths()

    def subtract_health(self):
        if self.invincibility == None:
            self.invincibility = time()
        if time() - self.invincibility >= 0.04:
            self.settings.health_bar_width -= 5
            self.stats.health -= 1
            self.hb.make_bar()
            self.hn.health1()
            self.invincibility = None

    def hit_heart(self):
        # pass
        if pygame.sprite.spritecollideany(self.heart, self.blast) or self.swirl.rect1.colliderect(self.heart) \
                or self.swirl.rect2.colliderect(self.heart) or self.swirl.rect3.colliderect(self.heart) \
                or self.swirl.rect4.colliderect(self.heart) or self.swirl.rect5.colliderect(self.heart) \
                or self.swirl.rect6.colliderect(self.heart) or self.swirl.rect7.colliderect(self.heart) \
                or self.swirl.rect8.colliderect(self.heart) or self.swirl.rect9.colliderect(self.heart) \
                or self.swirl.rect10.colliderect(self.heart) or self.swirl.rect11.colliderect(self.heart) \
                or self.swirl.rect12.colliderect(self.heart) or self.swirl.rectb1.colliderect(self.heart) \
                or self.swirl.rectb2.colliderect(self.heart) or self.swirl.rectb3.colliderect(self.heart) \
                or self.swirl.rectb3.colliderect(self.heart) or self.swirl.rectb4.colliderect(self.heart) \
                or self.swirl.rectb5.colliderect(self.heart) or self.swirl.rectb6.colliderect(self.heart) \
                or self.swirl.rectb7.colliderect(self.heart) or self.swirl.rectb8.colliderect(self.heart) \
                or self.swirl.rectb9.colliderect(self.heart) or self.swirl.rectb10.colliderect(self.heart) \
                or self.swirl.rectb11.colliderect(self.heart) or self.swirl.rectb12.colliderect(self.heart) \
                or pygame.sprite.spritecollideany(self.heart, self.bones) or pygame.sprite.spritecollideany(self.heart, self.right_bone) \
                or pygame.sprite.spritecollideany(self.heart, self.top_bone) or pygame.sprite.spritecollideany(self.heart, self.left_bone) \
                or pygame.sprite.spritecollideany(self.heart, self.bottom_bone) or pygame.sprite.spritecollideany(self.heart, self.blue_bones) \
                and (self.heart.moving_down is True or self.heart.moving_up is True or self.heart.moving_left is True or self.heart.moving_right is True)\
                or pygame.sprite.spritecollideany(self.heart, self.orange_bones) and self.heart.moving_down is False \
                and self.heart.moving_up is False and self.heart.moving_left is False and self.heart.moving_right is False or pygame.sprite.spritecollideany(self.heart, self.between_bones_right) \
                or pygame.sprite.spritecollideany(self.heart, self.between_bones_left) or pygame.sprite.spritecollideany(self.heart, self.flyingbonestop) \
                or pygame.sprite.spritecollideany(self.heart, self.flyingbonesright) or pygame.sprite.spritecollideany(self.heart, self.flyingbonesleft) \
                or pygame.sprite.spritecollideany(self.heart, self.flyingbonesbottom) or self.hand_blast.beam3.colliderect(self.heart) and self.gaster_hand_color == 'blue' \
                and (self.heart.moving_up is True or self.heart.moving_down is True or self.heart.moving_left is True or self.heart.moving_right is True) \
                or self.hand_blast.beam3.colliderect(self.heart) and self.gaster_hand_color == 'orange' and self.heart.moving_up is False and self.heart.moving_down is False \
                and self.heart.moving_left is False and self.heart.moving_right is False or self.big_hand.bighand_rect.colliderect(self.heart):

            if self.stats.sans_amount == 4:
                if 446 <= self.heart.rect.x <= 520 and 493 <= self.heart.rect.y <= 528 or 563 <= self.heart.rect.x <= 603 and 373 <= self.heart.rect.y <= 453 \
                        or 365 <= self.heart.rect.x <= 407 and 371 <= self.heart.rect.y <= 452 or 444 <= self.heart.rect.x <= 529 and 290 <= self.heart.rect.y <= 338:
                    pass

                else:
                    self.subtract_health()

            elif self.stats.sans_amount == 5 or self.stats.sans_amount == 26:
                if 502 <= self.heart.rect.x <= 520 and 353 <= self.heart.rect.y <= 361 or 490 <= self.heart.rect.x <= 531 and \
                        361 <= self.heart.rect.y <= 367 or 477 <= self.heart.rect.x <= 536 and 367 <= self.heart.rect.y <= 373 or 470 <= self.heart.rect.x <= 545 and \
                        373 <= self.heart.rect.y <= 383 or 454 <= self.heart.rect.x <= 559 and 383 <= self.heart.rect.y <= 411 or 559 <= self.heart.rect.x <= 572 and \
                        391 <= self.heart.rect.y <= 406 or 432 <= self.heart.rect.x <= 454 and 396 <= self.heart.rect.y <= 411 or 423 <= self.heart.rect.x <= 432 and \
                        400 <= self.heart.rect.y <= 411 or 407 <= self.heart.rect.x <= 423 and 409 <= self.heart.rect.y <= 411 or 404 <= self.heart.rect.x <= 407 and \
                        self.heart.rect.y == 411 or 411 <= self.heart.rect.x <= 552 and 411 <= self.heart.rect.y <= 427 or 432 <= self.heart.rect.x <= 531 and \
                        427 <= self.heart.rect.y <= 445 or 442 <= self.heart.rect.x <= 511 and 445 <= self.heart.rect.y <= 456 or 456 <= self.heart.rect.x <= 491 and \
                        456 <= self.heart.rect.y <= 466 or 460 <= self.heart.rect.x <= 484 and 466 <= self.heart.rect.y <= 472 or 467 <= self.heart.rect.x <= 479 and \
                        472 <= self.heart.rect.x <= 476:
                    pass

                else:
                    self.subtract_health()

            elif self.stats.sans_amount == 62 or self.stats.sans_amount == 63 and not pygame.sprite.spritecollideany(self.heart, self.bones):
                if 468 <= self.heart.rect.x <= 488 and self.heart.rect.x == 461 or 414 <= self.heart.rect.x <= 554 and 447 <= self.heart.rect.y <= 461 or 373 <= self.heart.rect.x <= 592 and 435 <= self.heart.rect.y <= 447 \
                        or 319 <= self.heart.rect.x <= 648 and 420 <= self.heart.rect.y <= 435 or 255 <= self.heart.rect.x <= 713 and 403 <= self.heart.rect.y <= 420 \
                        or 255 <= self.heart.rect.x <= 713 and 290 <= self.heart.rect.y <= 403:
                    pass

                else:
                    self.subtract_health()

            elif self.stats.sans_amount == 67:
                if 365 <= self.heart.rect.x <= 447 and 444 <= self.heart.rect.y <= 453 or 365 <= self.heart.rect.x <= 427 and 428 <= self.heart.rect.y <= 444 or 365 <= self.heart.rect.x <= 419 and 417 <= self.heart.rect.y <= 428 \
                        or 365 <= self.heart.rect.x <= 406 and 405 <= self.heart.rect.y <= 417 or 365 <= self.heart.rect.x <= 394 and 394 <= self.heart.rect.y <= 405 \
                        or 365 <= self.heart.rect.x <= 383 and 383 <= self.heart.rect.y <= 394 or 365 <= self.heart.rect.x <= 372 and 372 <= self.heart.rect.y <= 383 or 365 <= self.heart.rect.x <= 366 and 364 <= self.heart.rect.y <= 383 \
                        or 453 <= self.heart.rect.x <= 603 and 290 <= self.heart.rect.y <= 310 or 469 <= self.heart.rect.x <= 603 and 310 <= self.heart.rect.y <= 324 \
                        or 487 <= self.heart.rect.x <= 603 and 324 <= self.heart.rect.y <= 341 or 504 <= self.heart.rect.x <= 603 and 341 <= self.heart.rect.y <= 358 \
                        or 523 <= self.heart.rect.x <= 603 and 358 <= self.heart.rect.y <= 378 or 539 <= self.heart.rect.x <= 603 and 378 <= self.heart.rect.y <= 395 \
                        or 558 <= self.heart.rect.x <= 603 and 395 <= self.heart.rect.y <= 413 or 575 <= self.heart.rect.x <= 603 and 413 <= self.heart.rect.y <= 430 \
                        or 586 <= self.heart.rect.x <= 603 and 430 <= self.heart.rect.y <= 441 or 597 <= self.heart.rect.x <= 603 and 441 <= self.heart.rect.y <= 451:
                    pass

                else:
                    self.subtract_health()

            elif self.stats.sans_amount == 68:
                if 453 <= self.heart.rect.x <= 603 and 290 <= self.heart.rect.y <= 310 or 469 <= self.heart.rect.x <= 603 and 310 <= self.heart.rect.y <= 324 \
                        or 487 <= self.heart.rect.x <= 603 and 324 <= self.heart.rect.y <= 341 or 504 <= self.heart.rect.x <= 603 and 341 <= self.heart.rect.y <= 358 \
                        or 523 <= self.heart.rect.x <= 603 and 358 <= self.heart.rect.y <= 378 or 539 <= self.heart.rect.x <= 603 and 378 <= self.heart.rect.y <= 395 \
                        or 558 <= self.heart.rect.x <= 603 and 395 <= self.heart.rect.y <= 413 or 575 <= self.heart.rect.x <= 603 and 413 <= self.heart.rect.y <= 430 \
                        or 586 <= self.heart.rect.x <= 603 and 430 <= self.heart.rect.y <= 441 or 597 <= self.heart.rect.x <= 603 and 441 <= self.heart.rect.y <= 451:
                    pass

                else:
                    self.subtract_health()

            else:
                self.subtract_health()

    def blast_gaster_diagonal(self):
        if self.last_time == None:
            self.last_time = time()
        if time() - self.last_time >= 0.3:
            if self.blaster_created == False and self.last_time2 == None:
                self.create_diagonal_blasters_c()
                self.blaster_created = True
            if self.stop_blaster == False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 == None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.8:
                if self.blaster_blasted == False:
                    self.gasterblaster.empty()
                    self.create_diagonal_blasters_o()
                    self.stop_blaster = True
                    self.blaster_blasted = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 == None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 1:
                    self.stats.sans_amount += 1
                    self.gasterblaster.empty()
                    self.stop_blaster = False
                    self.blast.empty()
                    self.blaster_created = False
                    self.blaster_blasted = False
                    self.center = False
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None

    def blast_gaster_center(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.35:
            if self.blaster_created == False:
                self.create_center_blasters_c()
                self.blaster_created = True
            if self.stop_blaster == False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.8:
                if self.blaster_blasted == False:
                    self.gasterblaster.empty()
                    self.create_center_blasters_o()
                    self.stop_blaster = True
                    self.blaster_blasted = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 1:
                    self.stats.sans_amount += 1
                    self.gasterblaster.empty()
                    self.stop_blaster = False
                    self.blast.empty()
                    self.blaster_created = False
                    self.blaster_blasted = False
                    self.center = False
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None

    def blast_gaster_up_down(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.8:
            if self.blaster_created == False:
                self.create_up_down_blasters_c()
                self.blaster_created = True
            if self.stop_blaster == False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.5:
                if self.blaster_blasted == False:
                    self.gasterblaster.empty()
                    self.create_up_down_blasters_o()
                    self.blaster_blasted = True
                    self.stop_blaster = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.6:
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.stop_blaster = False
                    self.blaster_created = False
                    self.blaster_blasted = False
                    self.repeat += 1

    def blast_gaster_bottom_left_up(self):
        if self.last_time is None:
            self.last_time = time()
            self.gasterblaster.empty()
        if time() - self.last_time >= 2:
            if self.blaster_created is False:
                self.create_trap_bone_bl_gasterblaster_c()
                self.blaster_created = True
                self.arrow_type = None
            if self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 1.2:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.create_trap_bone_bl_gasterblaster_o_up()
                    self.blaster_blasted = True
                    self.stop_blaster = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.5:
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.blaster_created = False
                    self.stop_blaster = False
                    self.blaster_blasted = False
                    self.arrow_randomed = False
                    self.wa.arrow_direction = None
                    self.repeat += 1

    def blast_gaster_bottom_left_down(self):
        if self.last_time is None:
            self.last_time = time()
            self.gasterblaster.empty()
        if time() - self.last_time >= 2:
            if self.blaster_created is False:
                self.create_trap_bone_bl_gasterblaster_c()
                self.blaster_created = True
                self.arrow_type = None
            if self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 1.2:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.create_trap_bone_bl_gasterblaster_o_down()
                    self.blaster_blasted = True
                    self.stop_blaster = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.5:
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.blaster_created = False
                    self.stop_blaster = False
                    self.blaster_blasted = False
                    self.arrow_randomed = False
                    self.wa.arrow_direction = None
                    self.repeat += 1

    def blast_gaster_up_down_delayed(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.6:
            if self.blaster_created is False:
                self.create_just_bottom_gasterblaster_c()
                self.blaster_created = True
            if self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.45:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.create_just_bottom_gasterblaster_o()
                    self.blaster_blasted = True
                    self.stop_blaster = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.09:
                    if self.blaster_created2 is False:
                        self.create_just_top_gasterblaster_c()
                        self.blaster_created2 = True
                    if self.last_time4 is None:
                        self.last_time4 = time()
                    if time() - self.last_time4 >= 0.165:
                        if self.blaster_blasted2 is False:
                            self.gasterblaster.empty()
                            self.blast.empty()
                            self.create_just_top_gasterblaster_o()
                            self.blaster_blasted2 = True
                        if self.last_time5 is None:
                            self.last_time5 = time()
                        if time() - self.last_time5 >= 0.4:
                            self.stats.sans_amount += 1
                            self.last_time = None
                            self.last_time2 = None
                            self.last_time3 = None
                            self.last_time4 = None
                            self.last_time5 = None
                            self.blaster_created = False
                            self.blaster_created2 = False
                            self.blaster_blasted = False
                            self.blaster_blasted2 = False

    def blast_gaster_just_left(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.8:
            if self.blaster_created is False:
                self.create_just_left_gasterblaster_c()
                self.blaster_created = True
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.275:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.create_just_top_gasterblaster_o()
                    self.create_just_left_gasterblaster_o()
                    self.blaster_blasted = True
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.35:
                    self.stats.sans_amount += 1
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.last_time12 = None
                    self.blaster_created = False
                    self.blaster_blasted = False

    def blast_gaster_just_left_phase_2(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.8:
            if self.blaster_created is False:
                self.create_just_left_gasterblaster_c()
                self.blaster_created = True
            if self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.275:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.stop_blaster = True
                    self.create_just_left_gasterblaster_o()
                    self.blaster_blasted = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.35:
                    self.stats.sans_amount += 1
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.last_time12 = None
                    self.last_time8 = None
                    self.stop_blaster = False
                    self.blaster_created = False
                    self.blaster_blasted = False

    def blast_gaster_bottom_right(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.8:
            if self.blaster_created is False:
                self.create_just_bottom_gasterblaster_c()
                self.create_just_right_gasterblaster_c()
                self.blaster_created = True
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.275:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.create_just_top_gasterblaster_o()
                    self.create_just_left_gasterblaster_o()
                    self.create_just_bottom_gasterblaster_o()
                    self.create_just_right_gasterblaster_o()
                    self.blaster_blasted = True
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.45:
                    self.stats.sans_amount += 1
                    self.stats.heart_color = 'red'
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.blaster_created = False
                    self.blaster_blasted = False

    def blast_gaster_top_right_left(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.8:
            if self.blaster_created is False:
                self.create_just_top_gasterblaster_c()
                self.create_just_right_gasterblaster_c()
                self.create_just_left_gasterblaster_c()
                self.blaster_created = True
            elif self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.275:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.create_just_top_gasterblaster_o()
                    self.create_just_right_gasterblaster_o()
                    self.create_just_left_gasterblaster_o()
                    self.stop_blaster = True
                    self.blaster_blasted = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.45:
                    self.stats.sans_amount += 1
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.stop_blaster = False
                    self.blaster_created = False
                    self.blaster_blasted = False

    def blast_gaster_just_bottom(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.8:
            if self.blaster_created is False:
                self.create_just_bottom_gasterblaster_c()
                self.blaster_created = True
            elif self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.3:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.create_just_bottom_gasterblaster_o()
                    self.stop_blaster = True
                    self.blaster_blasted = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.65:
                    self.stats.sans_amount += 1
                    self.stats.turn = 'my turn'
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.stop_blaster = False
                    self.blaster_created = False
                    self.blaster_blasted = False

    def blast_gaster_just_bottom_phase_2(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.8:
            if self.blaster_created is False:
                self.create_just_bottom_gasterblaster_c()
                self.blaster_created = True
            elif self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.3:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.create_just_bottom_gasterblaster_o()
                    self.stop_blaster = True
                    self.blaster_blasted = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.65:
                    self.stats.sans_amount += 1
                    self.gasterblaster.empty()
                    self.blast.empty()
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.stop_blaster = False
                    self.blaster_created = False
                    self.blaster_blasted = False

    def move_going_left_up_bones(self):
        if self.created_bone is False:
            self.create_going_left_up_bones()
            self.created_bone = True
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.75:
            self.create_going_left_up_bones()
            self.repeat += 1
            self.last_time = None
        for bone in self.bones.sprites():
            bone.update_up_bones_going_left()
            if bone.rect.left == self.battle.rect.left:
                self.bones.remove(bone)

    def bone_up(self):
        if self.last_time == None:
            self.last_time = time()
        if time() - self.last_time > 1:
            if self.created_bone == False:
                self.create_bones()
                self.created_bone = True
            self.bones.draw(self.screen)
            self.att.bone_down_visibility = 'mid_true'
            self.slam.reset_slam()
            if self.last_time2 == None:
                self.last_time2 = time()
            if time() - self.last_time2 > 0.7:
                self.bones.empty()
                self.stats.sans_amount += 1
                self.stats.heart_color = 'red'
                self.created_bone = False
                self.last_time = None
                self.last_time2 = None
                self.att.bone_down_visibility = False

    def show_trap_bone_bl(self):
        if self.last_time is None:
            self.last_time = time()
            self.create_block_gasterblaster_c()
        if time() - self.last_time >= 0.6:
            if self.created_bone is False:
                self.create_trap_bone_bl()
                self.created_bone = True
            self.blockblaster.draw(self.screen)
            self.right_bone.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time >= 0.8:
                self.move_right_trap_bone_bl()
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 1.2:
                    self.top_bone.draw(self.screen)
                    if self.last_time4 is None:
                        self.last_time4 = time()
                    if time() - self.last_time4 >= 0.4:
                        self.move_top_trap_bone_bl()
                        if self.last_time5 is None:
                            self.last_time5 = time()
                        if time() - self.last_time5 >= 2:
                            self.stats.sans_amount += 1
                            self.last_time = None
                            self.last_time2 = None
                            self.last_time3 = None
                            self.last_time4 = None
                            self.last_time5 = None
                            self.created_bone = False
                            self.right_bone_number = 1
                            self.top_bone_number = 1
                            self.blockblaster.empty()
                            self.create_block_gasterblaster_o()

    def show_60_bones(self):
        if self.last_time is None:
            self.last_time = time()
            self.bone_color = None
            self.make_60_warning()
            self.Sanness.sd_warning()
        if time() - self.last_time <= 1:
            self.Sanness.sd_warning()
        else:
            if self.last_time2 is None:
                self.last_time2 = time()
                if self.created_bone is False:
                    self.create_60_bones()
                    self.created_bone = True
                self.bones.draw(self.screen)
            if time() - self.last_time2 <= 1.5:
                self.bones.draw(self.screen)
            else:
                self.bones.draw(self.screen)
                self.stats.sans_amount += 1
                self.last_time = None
                self.last_time2 = None
                self.created_bone = False

    def show_40_bones(self):
        if self.bone_color == 'orange':
            if self.last_time is None:
                self.w.make_warnings_40()
                self.last_time = time()
                self.w.show_orange_warning()
            if time() - self.last_time <= 1.5:
                self.w.show_orange_warning()
            else:
                if self.last_time2 is None:
                    self.last_time2 = time()
                    if self.created_bone is False:
                        self.create_40_bones()
                        self.created_bone = True
                    self.orange_bones.draw(self.screen)
                if time() - self.last_time2 <= 1:
                    self.orange_bones.draw(self.screen)
                else:
                    self.orange_bones.empty()
                    self.repeat += 1
                    self.last_time = None
                    self.last_time2 = None
                    self.created_bone = False
                    self.color_randomed = False
        elif self.bone_color == 'blue':
            if self.last_time is None:
                self.w.make_warnings_40()
                self.last_time = time()
                self.w.show_blue_warning()
            if time() - self.last_time <= 1.5:
                self.w.show_blue_warning()
            else:
                if self.last_time2 is None:
                    self.last_time2 = time()
                    if self.created_bone is False:
                        self.create_40_bones()
                        self.created_bone = True
                    self.blue_bones.draw(self.screen)
                if time() - self.last_time2 <= 1:
                    self.blue_bones.draw(self.screen)
                else:
                    self.blue_bones.empty()
                    self.repeat += 1
                    self.last_time = None
                    self.last_time2 = None
                    self.created_bone = False
                    self.color_randomed = False

    def create_gasterblaster_to_left(self):
        blaster = FellBlaster(self)
        width = 1750
        available_space_x = width * 2 // 3
        gaster_number = available_space_x // blaster.rect.width

        for number in range(gaster_number):
            self.add_gasterblaster_to_left(number)

    def add_gasterblaster_to_left(self, number):
        blaster = FellBlaster(self)
        blaster.image = pygame.transform.scale(blaster.image, (blaster.rect.width, blaster.rect.height))
        blaster.rect = blaster.image.get_rect()
        blaster.rect.bottom = self.battle.rect.top - 20
        blaster.rect.right = 930 - number * (blaster.rect.width - 75)
        self.gasterblaster.add(blaster)

    def create_gasterblasted_to_left(self):
        blaster = FellBlasted(self)
        width = 1750
        available_space_x = width * 2 // 3
        gaster_number = available_space_x // blaster.rect.width

        for number in range(gaster_number):
            self.add_gasterblasted_to_left(number)

    def add_gasterblasted_to_left(self, number):
        blaster = FellBlasted(self)
        blastbeam = BlastBeam(self)

        blaster.image = pygame.transform.scale(blaster.image, (blaster.rect.width, blaster.rect.height))
        blaster.rect = blaster.image.get_rect()
        blaster.rect.bottom = self.battle.rect.top - 20
        blaster.rect.right = 930 - number * (blaster.rect.width - 75)

        blastbeam.image = pygame.transform.scale(blastbeam.image, (90, 575))
        blastbeam.rect = blastbeam.image.get_rect()
        blastbeam.rect.top = blaster.rect.bottom - 80
        blastbeam.rect.right = blaster.rect.right - 35

        self.blast.add(blastbeam)
        self.gasterblaster.add(blaster)

    def blast_gaster_to_left(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.8:
            if self.blaster_created is False:
                self.create_gasterblaster_to_left()
                self.blaster_created = True
            if self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 1.5:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.create_gasterblasted_to_left()
                    self.stop_blaster = True
                    self.blaster_blasted = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
            if self.last_time3 is None:
                self.last_time3 = time()
            if time() - self.last_time3 >= 2:
                self.last_time = None
                self.last_time2 = None
                self.last_time3 = None
                self.stop_blaster = False
                self.blaster_created = False
                self.blaster_blasted = False
                self.gasterblaster.empty()
                self.blast.empty()
                self.stats.sans_amount += 1

    def create_gasterblaster_to_right(self):
        blaster = FellBlaster(self)
        width = 1750
        available_space_x = width * 2 // 3
        gaster_number = available_space_x // blaster.rect.width

        for number in range(gaster_number):
            self.add_gasterblaster_to_right(number)

    def add_gasterblaster_to_right(self, number):
        blaster = FellBlaster(self)
        blaster.image = pygame.transform.scale(blaster.image, (blaster.rect.width, blaster.rect.height))
        blaster.rect = blaster.image.get_rect()
        blaster.rect.bottom = self.battle.rect.top - 20
        blaster.rect.left = 55 + number * (blaster.rect.width - 75)
        self.gasterblaster.add(blaster)

    def create_gasterblasted_to_right(self):
        blaster = FellBlasted(self)
        width = 1750
        available_space_x = width * 2 // 3
        gaster_number = available_space_x // blaster.rect.width

        for number in range(gaster_number):
            self.add_gasterblasted_to_right(number)

    def add_gasterblasted_to_right(self, number):
        blaster = FellBlasted(self)
        blastbeam = BlastBeam(self)

        blaster.image = pygame.transform.scale(blaster.image, (blaster.rect.width, blaster.rect.height))
        blaster.rect = blaster.image.get_rect()
        blaster.rect.bottom = self.battle.rect.top - 20
        blaster.rect.left = 55 + number * (blaster.rect.width - 75)

        blastbeam.image = pygame.transform.scale(blastbeam.image, (90, 575))
        blastbeam.rect = blastbeam.image.get_rect()
        blastbeam.rect.top = blaster.rect.bottom - 80
        blastbeam.rect.left = blaster.rect.left + 35

        self.blast.add(blastbeam)
        self.gasterblaster.add(blaster)

    def blast_gaster_to_right(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.8:
            if self.blaster_created is False:
                self.create_gasterblaster_to_right()
                self.blaster_created = True
            if self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 1.5:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.create_gasterblasted_to_right()
                    self.stop_blaster = True
                    self.blaster_blasted = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
            if self.last_time3 is None:
                self.last_time3 = time()
            if time() - self.last_time3 >= 2:
                self.last_time = None
                self.last_time2 = None
                self.last_time3 = None
                self.stop_blaster = False
                self.blaster_created = False
                self.blaster_blasted = False
                self.gasterblaster.empty()
                self.blast.empty()
                self.stats.sans_amount += 1

    def blast_gaster_full_bottom_half_side(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.45:
            if self.blaster_created is False:
                self.create_full_bottom_and_half_side_gaster_blaster_c()
                self.blaster_created = True
            if self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.45:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.create_full_bottom_and_half_side_gaster_blaster_o()
                    self.blaster_blasted = True
                    self.stop_blaster = True
                self.blast.draw(self.screen)
                self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.4:
                    self.stats.sans_amount += 1
                    self.blaster_created = False
                    self.stop_blaster = False
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.blaster_blasted = False

    def bone_up_general(self):
        if self.last_time is None:
            self.last_time = time()
            self.make_full_warning()
            self.Sanness.sd_warning()
        if time() - self.last_time <= 1:
            self.Sanness.sd_warning()
        else:
            if self.last_time2 is None:
                self.last_time2 = time()
                self.create_bones()
                self.bones.draw(self.screen)
            if time() - self.last_time2 <= 0.1:
                self.bones.draw(self.screen)
            else:
                self.stats.sans_amount += 1
                self.last_time = None
                self.last_time2 = None

    def move_plat_center_battle(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.03:
            if self.platform_created is False:
                self.add_platform()
                self.make_platform_left()
                self.platform_created = True
            if self.stats.platform_color == 'red':
                self.platformrs.draw(self.screen)
            elif self.stats.platform_color == 'yellow':
                self.platformys.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.02:
                self.move_platform_to_center()

    def move_between_bones_inward(self):
        if self.created_bone is False:
            self.create_between_bones()
            self.created_bone = True
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 2:
            self.create_between_bones()
            self.repeat += 1
            self.last_time = None
        for bone in self.between_bones_right.sprites():
            bone.update_right_bone_in()
            if bone.rect.left == self.battle.rect.left:
                self.between_bones_right.remove(bone)
        for bone in self.between_bones_left.sprites():
            bone.update_left_bone_in()
            if bone.rect.right == self.battle.rect.right:
                self.between_bones_left.remove(bone)

        self.between_bones_left.update()
        self.between_bones_right.update()

    def move_going_right_and_left_up_down_bones(self):
        if self.created_bone is False:
            self.create_bones_going_left_and_right_up_down()
            self.created_bone = True
        if self.last_time10 is None:
            self.last_time10 = time()
        if time() - self.last_time10 >= 0.75:
            self.create_bones_going_left_and_right_up_down()
            self.last_time10 = None
            self.repeat += 1
        for bone in self.between_bones_right.sprites():
            bone.update_right_bone_in2()
            if bone.rect.left == self.battle.rect.left:
                self.between_bones_right.remove(bone)
        for bone in self.between_bones_left.sprites():
            bone.update_left_bone_in2()
            if bone.rect.right == self.battle.rect.right:
                self.between_bones_left.remove(bone)

        self.between_bones_right.update()
        self.between_bones_left.update()

    def move_flying_bone(self):
        if self.created_bone is False:
            self.create_flying_bone()
            self.created_bone = True
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.6:
            self.create_flying_bone()
            self.last_time = None
        for flyingbone in self.flyingbonesright:
            if flyingbone.flyingbone_right_spin_degree <= 360:
                flyingbone.turn_flyingbone_right()
            else:
                flyingbone.rect.x -= 1
            if flyingbone.rect.right <= self.screen_rect.left:
                self.flyingbonesright.remove(flyingbone)
        for flyingbone in self.flyingbonestop:
            if flyingbone.flyingbone_top_spin_degree <= 360:
                flyingbone.turn_flyingbone_top()
            else:
                flyingbone.rect.y += 1
            if flyingbone.rect.top >= self.screen_rect.bottom:
                self.flyingbonestop.remove(flyingbone)
        for flyingbone in self.flyingbonesleft:
            if flyingbone.flyingbone_left_spin_degree <= 360:
                flyingbone.turn_flyingbone_left()
            else:
                flyingbone.rect.x += 1
            if flyingbone.rect.left >= self.screen_rect.right:
                self.flyingbonesleft.remove(flyingbone)
        for flyingbone in self.flyingbonesbottom:
            if flyingbone.flyingbone_bottom_spin_degree <= 360:
                flyingbone.turn_flyingbone_bottom()
            else:
                flyingbone.rect.y -= 1
            if flyingbone.rect.bottom <= self.screen_rect.top:
                self.flyingbonesbottom.remove(flyingbone)

        self.flyingbonesright.update()
        self.flyingbonestop.update()
        self.flyingbonesleft.update()
        self.flyingbonesbottom.update()

    def blast_gaster_hand(self):
        if self.gaster_hand_color == 'blue':
            if self.last_time is None:
                self.last_time = time()
            if time() - self.last_time >= 1:
                self.hand_blast.show_blue_blast_hand()
                if self.last_time2 is None:
                    self.last_time2 = time()
                if time() - self.last_time2 >= 1:
                    self.hand_blast.location = 58
                    self.hand_blast.blast_hand()
                    self.hand_blast.blast_color()
                    self.hand_blast.blast_beam()
                    self.hand_blast.show_blue_blasted_hand()
                    if self.last_time3 is None:
                        self.last_time3 = time()
                    if time() - self.last_time3 >= 1.25:
                        self.repeat += 1
                        self.last_time = None
                        self.last_time2 = None
                        self.last_time3 = None
                        self.gaster_hand_color_randomed = False
        if self.gaster_hand_color == 'orange':
            if self.last_time is None:
                self.last_time = time()
            if time() - self.last_time >= 1:
                self.hand_blast.show_orange_blast_hand()
                if self.last_time2 is None:
                    self.last_time2 = time()
                if time() - self.last_time2 >= 1:
                    self.hand_blast.location = 58
                    self.hand_blast.blast_hand()
                    self.hand_blast.blast_color()
                    self.hand_blast.blast_beam()
                    self.hand_blast.show_orange_blasted_hand()
                    if self.last_time3 is None:
                        self.last_time3 = time()
                    if time() - self.last_time3 >= 1.25:
                        self.repeat += 1
                        self.last_time = None
                        self.last_time2 = None
                        self.last_time3 = None
                        self.gaster_hand_color_randomed = False

    def random_gaster_hand_color(self):
        self.hand_blast.location = 1000
        self.hand_blast.blast_hand()
        self.hand_blast.blast_color()
        self.hand_blast.blast_beam()
        if self.gaster_hand_color_randomed is False:
            self.gaster_hand_color = random.randint(1, 2)
            self.gaster_hand_color_randomed = True
        if self.gaster_hand_color == 1:
            self.gaster_hand_color = 'blue'
        elif self.gaster_hand_color == 2:
            self.gaster_hand_color = 'orange'

    def trap_player_by_blaster1(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 1:
            if self.blaster_created is False:
                self.create_just_bottom_gasterblaster_c()
                self.blaster_created = True
            if self.stop_blaster is False:
                self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 1:
                if self.blaster_blasted is False:
                    self.gasterblaster.empty()
                    self.created_just_bottom_right_diagonal_c()
                    self.create_just_bottom_gasterblaster_o()
                    self.blaster_blasted = True
                    self.stop_blaster = True
                if self.stop_blaster2 is False:
                    self.blast.draw(self.screen)
                    self.gasterblaster.draw(self.screen)
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 1:
                    if self.blaster_created2 is False:
                        self.gasterblaster.empty()
                        self.blast.empty()
                        self.created_just_bottom_right_diagonal_o()
                        self.create_just_bottom_gasterblaster_o()
                        self.create_just_left_gasterblaster_c()
                        self.created_blaster_above_just_bottom_c()
                        self.blaster_created2 = True
                        self.stop_blaster2 = True
                    if self.stop_blaster3 is False:
                        self.blast.draw(self.screen)
                        self.gasterblaster.draw(self.screen)
                    if self.last_time4 is None:
                        self.last_time4 = time()
                    if time() - self.last_time4 >= 1:
                        self.stats.sans_amount += 1
                        self.stop_blaster = False
                        self.stop_blaster2 = False
                        self.stop_blaster3 = False
                        self.stop_blaster4 = False
                        self.stop_blaster5 = False
                        self.stop_blaster6 = False
                        self.created_bone = False
                        self.blaster_created = False
                        self.blaster_created2 = False
                        self.blaster_blasted = False
                        self.blaster_blasted2 = False
                        self.last_time = None
                        self.last_time2 = None
                        self.last_time3 = None
                        self.last_time4 = None
                        self.last_time5 = None
                        self.last_time6 = None
                        self.last_time7 = None
                        self.last_time8 = None
                        self.last_time9 = None
                        self.last_time10 = None
                        self.last_time11 = None
                        self.last_time12 = None
                        self.last_time13 = None
                        self.changed_once = False
                        self.gaster_hand_color = None
                        self.gaster_hand_color_randomed = False

    def trap_player_by_blaster2(self):
        if self.blaster_blasted is False:
            self.gasterblaster.empty()
            self.blast.empty()
            self.created_just_bottom_right_diagonal_o()
            self.create_just_bottom_gasterblaster_o()
            self.create_just_left_gasterblaster_o()
            self.created_blaster_above_just_bottom_o()
            self.blaster_blasted = True
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 1.2:
            self.stats.sans_amount += 1
            self.blaster_blasted = False
            self.last_time = None
            self.gasterblaster.empty()
            self.blast.empty()

    def track_player_with_gaster(self):
        global xs, ys, widths, heights, times_removed, times_blasted

        if self.reset_var is False:
            xs, ys, widths, heights = [], [], [], []
            times_removed = 0
            times_blasted = 0
            self.reset_var = True

        if self.blaster_created is False:
            self.create_tracking_blaster_top_c()
            self.blaster_created = True
        if self.last_time2 is None:
            self.last_time2 = time()
        if time() - self.last_time2 >= 0.35:
            self.create_tracking_blaster_top_c()
            self.last_time2 = None
        if self.last_time3 is None:
            self.last_time3 = time()
        if time() - self.last_time3 >= 2.1:
            self.last_time2 = None
            for blaster in self.gasterblaster.sprites():
                if times_removed <= 6:

                    widths.append(blaster.rect.width)
                    heights.append(blaster.rect.height)
                    xs.append(blaster.rect.x)
                    ys.append(blaster.rect.y)

                    self.gasterblaster.remove(blaster)
                    times_removed += 1

            if len(xs) == 6:
                if times_blasted <= 6:
                    for index in range(0, 6):
                        blasted = FellBlasted(self)
                        blastbeam = BlastBeam(self)

                        width = widths[index]
                        height = heights[index]
                        x = xs[index]
                        y = ys[index]

                        blasted.image = pygame.transform.scale(blasted.image, (width, height)).convert_alpha()
                        blasted.rect = blasted.image.get_rect()
                        blasted.rect.x = x
                        blasted.rect.y = y
                        blastbeam.image = pygame.transform.scale(blastbeam.image, (75, 900)).convert_alpha()
                        blastbeam.rect = blastbeam.image.get_rect()
                        blastbeam.rect.centerx = blasted.rect.centerx
                        blastbeam.rect.top = blasted.rect.centery

                        self.gasterblaster.add(blasted)
                        self.blast.add(blastbeam)
                        times_blasted += 1
        if self.last_time4 is None:
            self.last_time4 = time()
        if time() - self.last_time4 >= 3.1:
            self.stats.sans_amount += 1
            self.blaster_created = False
            self.blaster_blasted = False
            self.last_time = None
            self.last_time2 = None
            self.last_time3 = None
            self.last_time4 = None
            self.last_time5 = None
            self.last_time6 = None
            self.last_time7 = None
            self.last_time8 = None
            self.last_time9 = None
            self.last_time10 = None
            self.last_time11 = None
            self.last_time12 = None
            self.last_time13 = None
            self.reset_var = False
            self.gasterblaster.empty()
            self.blast.empty()

    def change_bone_number(self):
        if self.bottom_bone_number == 1:
            self.bottom_bone_number = 2
        elif self.bottom_bone_number == 2:
            self.bottom_bone_number = 3
        elif self.bottom_bone_number == 3:
            self.bottom_bone_number = 1

    def poke_player_with_bone(self):
        if self.created_bone is False:
            self.create_single_bone_horizontal()
            self.created_bone = True
        for sprite in self.bottom_bone.sprites():
            sprite.update_right_bone_bl()

            if self.bottom_bone_number == 3:
                if sprite.rect.x == self.battle.rect.left + 190:
                    self.stats.sans_amount += 1
                    self.bottom_bone_number = 1
                    self.last_time = None

            self.change_bone_number()

            self.bottom_bone.update()

    def make_blaster_stretch_sike(self):
        global width

        if self.reset_var is False:
            width = 0
            self.reset_var = True
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.4:
            if self.blaster_created is False:
                self.create_center_of_battlebox_c()
                self.blaster_created = True
            self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.2:
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 >= 0.0001:
                    if width <= 370:
                        for sprite in self.gasterblaster.sprites():
                            blaster = FellBlaster(self)

                            width = sprite.rect.width
                            height = sprite.rect.height
                            y = sprite.rect.y

                            blaster.image = pygame.transform.scale(blaster.image, (width + 2, height))
                            blaster.rect = blaster.image.get_rect()
                            blaster.rect.y = y
                            blaster.rect.centerx = self.battle.rect.centerx

                            self.gasterblaster.empty()
                            self.gasterblaster.add(blaster)

                            self.last_time3 = None
                    else:
                        if self.last_time4 is None:
                            self.last_time4 = time()
                        if time() - self.last_time4 >= 0.35:
                            self.blaster_created = False
                            self.blaster_blasted = False
                            self.last_time = None
                            self.last_time2 = None
                            self.last_time3 = None
                            self.last_time4 = None
                            self.last_time5 = None
                            self.last_time6 = None
                            self.last_time7 = None
                            self.last_time8 = None
                            self.last_time9 = None
                            self.last_time10 = None
                            self.last_time11 = None
                            self.last_time12 = None
                            self.last_time13 = None
                            self.reset_var = False
                            self.stop_blaster = False
                            self.gasterblaster.empty()
                            self.bottom_bone.empty()
                            self.big_hand.bighand_rect.y = 2000
                            self.stats.heart_color = 'blue'
                            self.stats.turn = 'black_out'

    def blast_gaster_top_right_left_down(self):
        if self.stop_blaster is False:
            self.gasterblaster.draw(self.screen)
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 1.254:
            if self.blaster_blasted is False:
                self.gasterblaster.empty()
                self.create_just_left_gasterblaster_o()
                self.create_just_top_gasterblaster_o()
                self.create_just_bottom_gasterblaster_o()
                self.create_just_right_gasterblaster_o()
                self.blaster_blasted = True
                self.stop_blaster = False
            self.blast.draw(self.screen)
            self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.3:
                self.blaster_created = False
                self.blaster_blasted = False
                self.last_time = None
                self.last_time2 = None
                self.last_time3 = None
                self.last_time4 = None
                self.last_time5 = None
                self.last_time6 = None
                self.last_time7 = None
                self.last_time8 = None
                self.last_time9 = None
                self.last_time10 = None
                self.last_time11 = None
                self.last_time12 = None
                self.last_time13 = None
                self.reset_var = False
                self.stop_blaster = False
                self.gasterblaster.empty()
                self.blast.empty()
                self.stats.turn = 'black_out'

    def blast_gaster_up_down2(self):
        if self.stop_blaster == False:
            self.gasterblaster.draw(self.screen)
        if self.last_time2 is None:
            self.last_time2 = time()
        if time() - self.last_time2 >= 0.5:
            if self.blaster_blasted == False:
                self.gasterblaster.empty()
                self.create_up_down_blasters_o()
                self.blaster_blasted = True
                self.stop_blaster = True
            self.blast.draw(self.screen)
            self.gasterblaster.draw(self.screen)
            if self.last_time3 is None:
                self.last_time3 = time()
            if time() - self.last_time3 >= 0.6:
                self.gasterblaster.empty()
                self.blast.empty()
                self.last_time = None
                self.last_time2 = None
                self.last_time3 = None
                self.stop_blaster = False
                self.blaster_created = False
                self.blaster_blasted = False
                self.stats.turn = 'black_out'

    def blast_gaster_up_down_left(self):
        if self.stop_blaster == False:
            self.gasterblaster.draw(self.screen)
        if self.last_time2 is None:
            self.last_time2 = time()
        if time() - self.last_time2 >= 0.5:
            if self.blaster_blasted == False:
                self.gasterblaster.empty()
                self.create_just_bottom_gasterblaster_o()
                self.create_just_top_gasterblaster_o()
                self.create_just_left_gasterblaster_o()
                self.blaster_blasted = True
                self.stop_blaster = True
            self.blast.draw(self.screen)
            self.gasterblaster.draw(self.screen)
            if self.last_time3 is None:
                self.last_time3 = time()
            if time() - self.last_time3 >= 0.6:
                self.gasterblaster.empty()
                self.blast.empty()
                self.last_time = None
                self.last_time2 = None
                self.last_time3 = None
                self.stop_blaster = False
                self.blaster_created = False
                self.blaster_blasted = False
                self.stats.turn = 'black_out'

    def blast_gaster_just_top(self):
        if self.stop_blaster is False:
            self.gasterblaster.draw(self.screen)
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 0.5:
            if self.blaster_blasted is False:
                self.gasterblaster.empty()
                self.create_just_top_gasterblaster_o()
                self.blaster_blasted = True
                self.stop_blaster = True
            self.blast.draw(self.screen)
            self.gasterblaster.draw(self.screen)
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 >= 0.6:
                self.gasterblaster.empty()
                self.blast.empty()
                self.last_time = None
                self.last_time2 = None
                self.last_time3 = None
                self.stop_blaster = False
                self.blaster_created = False
                self.blaster_blasted = False
                self.stats.turn = 'black_out'

    def move_swirl(self):
        self.swirl.first_swirl_top += 1.5
        self.swirl.swirly_bones_top()
        self.swirl.swirly_bones_bottom()

    def swirl_bone(self):
        if self.last_time == None:
            self.last_time = time()
        if time() - self.last_time > 1.3:
            self.swirl.show_swirl()
            self.move_swirl()

    def show_red_menu(self):
        self.fight.show_fightr()
        self.act.show_actr()
        self.item.show_itemr()
        self.mercy.show_mercyr()

    def show_fight_y_red_menu(self):
        self.fight.show_fighty()
        self.act.show_actr()
        self.item.show_itemr()
        self.mercy.show_mercyr()

    def show_act_y_red_menu(self):
        self.fight.show_fightr()
        self.act.show_acty()
        self.item.show_itemr()
        self.mercy.show_mercyr()

    def show_item_y_red_menu(self):
        self.fight.show_fightr()
        self.act.show_actr()
        self.item.show_itemy()
        self.mercy.show_mercyr()

    def show_mercy_y_red_menu(self):
        self.fight.show_fightr()
        self.act.show_actr()
        self.item.show_itemr()
        self.mercy.show_mercyy()

    def show_orange_menu(self):
        self.fight.show_fighto()
        self.act.show_acto()
        self.item.show_itemo()
        self.mercy.show_mercyo()

    def show_healths(self):
        self.hb2.draw_bar()
        self.hb.draw_bar()
        self.hn.show_health1()
        self.hn.show_other_health()

    def sans_shrug_delay(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 1.25:
            self.stats.dia += 1
            self.stats.sans_amount += 1
            self.stats.turn = 'speech turn'
            self.last_time = None

    def show_all_speech(self):
        self.SB.bubble_stem()
        self.SB.speech_bubble()
        self.SB.show_stem()
        self.SB.show_speech()
        self.text.show_D()

    def show_first_page_items(self):
        self.inside.show_page_number_1()
        if 'Pie' not in self.items_ate:
            self.inside.show_item_1()
        if 'Noodles1' not in self.items_ate:
            self.inside.show_item_2()
        if 'Noodles2' not in self.items_ate:
            self.inside.show_item_3()
        if 'Fsteak' not in self.items_ate:
            self.inside.show_item_4()

    def show_second_page_items(self):
        self.inside.show_page_number_2()
        if 'Lhero1' not in self.items_ate:
            self.inside.show_item_5()
        if 'Lhero2' not in self.items_ate:
            self.inside.show_item_6()
        if 'Lhero3' not in self.items_ate:
            self.inside.show_item_7()
        if 'Lhero4' not in self.items_ate:
            self.inside.show_item_8()

    def sans_hit_delay(self):
        if self.hit_sans_delay is None:
            self.hit_sans_delay = time()
            mixer.music.stop()
        if time() - self.hit_sans_delay <= 0.5:
            self.fightbar.show_fight_bar()
            self.fightmarker.show_fight_marker()
        else:
            self.stats.turn = 'hit sans'
            self.hit_sans_delay = None

    def slash_mark(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time <= 0.09:
            self.slash.show_slash1()
        else:
            if self.last_time2 is None:
                self.last_time2 = time()
            if time() - self.last_time2 <= 0.09:
                self.slash.show_slash2()
            else:
                if self.last_time3 is None:
                    self.last_time3 = time()
                if time() - self.last_time3 <= 0.09:
                    self.slash.show_slash3()
                else:
                    if self.last_time4 is None:
                        self.last_time4 = time()
                    if time() - self.last_time4 <= 0.09:
                        self.slash.show_slash4()
                    else:
                        if self.last_time5 is None:
                            self.last_time5 = time()
                        if time() - self.last_time5 <= 0.27:
                            self.slash.show_slash5()
                        else:
                            self.stats.turn = 'sans down'
                            self.last_time = None
                            self.last_time2 = None
                            self.last_time3 = None
                            self.last_time4 = None
                            self.last_time5 = None
                            self.stats.sans_health = 0

    def delay_sans_smile(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 2.5:
            self.stats.kill_dia += 1
            self.last_time = None

    def delay_kill_speech(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 1.2:
            self.stats.kill_dia += 1
            self.stats.turn = 'killed speech turn'
            self.last_time = None

    def delay_win_screen(self):
        if self.last_time is None:
            self.last_time = time()
        if time() - self.last_time >= 3:
            self.stats.active = 'credits'
            self.last_time = None

    def move_swirl_off_screen(self):
        self.swirl.first_swirl_top = 2000
        self.swirl.swirly_bones_top()
        self.swirl.swirly_bones_bottom()

    def move_fight_marker(self):
        if self.fightmarker.fight_marker.left >= self.fightbar.fightbar_rect.left:
            self.fightmarker.fight_marker.x -= 1

    def show_normal_fight_sans(self):
        if self.stats.dia >= 1 and self.stats.dia <= 4:
            self.Sanness.show_closed()
        elif self.stats.dia == 5:
            self.Sanness.show_craze_no_glow()
        elif self.stats.dia == 6:
            if self.stats.sans_amount == 1 or self.stats.sans_amount == 2:
                self.Sanness.show_craze_glow_slamdown()
            elif self.stats.sans_amount == 3:
                self.Sanness.show_craze_glow()
            elif self.stats.sans_amount == 4:
                self.Sanness.show_craze_no_glow()
            elif self.stats.sans_amount == 5:
                self.Sanness.show_craze_no_glow_drop1()
            elif self.stats.sans_amount == 6:
                self.Sanness.show_craze_no_glow_drop2()
        elif self.stats.dia == 7:
            self.Sanness.show_craze_no_glow_shrug()
        elif self.stats.dia == 8 or self.stats.dia == 9:
            self.Sanness.show_normal_sans()
        elif self.stats.dia == 10:
            self.Sanness.show_normal_eyes_closed_sans()
        elif self.stats.dia == 11:
            self.Sanness.show_normal_sans()
        elif self.stats.dia == 12 or self.stats.dia == 13:
            self.Sanness.show_normal_sans()
        elif self.stats.dia == 14:
            self.Sanness.show_normal_confused_sans()
        elif self.stats.dia == 15:
            self.Sanness.show_normal_sans()
        elif self.stats.dia == 16 or self.stats.dia == 17:
            self.Sanness.show_normal_confused_sans()
        elif self.stats.dia == 18:
            if self.stats.sans_amount == 13:
                self.Sanness.show_normal_sans_slamdown()
            elif self.stats.sans_amount == 14:
                if self.switch_sans is None:
                    self.switch_sans = time()
                    self.Sanness.show_normal_sans_slamdown()
                if time() - self.switch_sans >= 0.55:
                    self.Sanness.show_normal_sans()
                else:
                    self.Sanness.show_normal_sans_slamdown()
            elif self.stats.sans_amount == 15:
                self.switch_sans = None
                self.Sanness.show_normal_sans_slamleft()
            elif self.stats.sans_amount == 16 or self.stats.sans_amount == 17:
                self.Sanness.show_normal_sans()
            elif self.stats.sans_amount == 18:
                self.Sanness.show_normal_sans_slamright()
            elif self.stats.sans_amount == 19:
                if self.switch_sans is None:
                    self.switch_sans = time()
                    self.Sanness.show_normal_sans_slamright()
                if time() - self.switch_sans >= 0.55:
                    self.Sanness.show_normal_sans()
                else:
                    self.Sanness.show_normal_sans_slamright()
            elif self.stats.sans_amount == 20 or self.stats.sans_amount == 21:
                self.Sanness.show_normal_sans()
        elif self.stats.dia == 19 or self.stats.dia == 20:
            self.Sanness.show_normal_eyes_closed_sans()
        elif self.stats.dia == 21:
            self.Sanness.show_normal_sans_glow()
        elif self.stats.dia == 22:
            self.Sanness.show_normal_sans()
        elif self.stats.dia == 23 or self.stats.dia == 25:
            self.Sanness.show_normal_sans()
        elif self.stats.dia == 24:
            self.Sanness.show_normal_sans_look_right()
        elif self.stats.dia == 26:
            self.Sanness.show_normal_sans()
        elif self.stats.dia == 27 or self.stats.dia == 28:
            self.Sanness.show_normal_confused_sans()
        elif self.stats.dia == 29:
            self.Sanness.show_normal_sans()
        elif self.stats.dia == 30:
            self.Sanness.show_normal_sans_look_right()
        elif self.stats.dia == 31:
            self.Sanness.show_normal_sans()
        elif self.stats.dia == 32:
            self.Sanness.show_normal_eyes_closed_sans()
        elif self.stats.dia == 33:
            self.Sanness.show_normal_sans_no_glow()
        elif self.stats.dia == 34:
            if 39 <= self.stats.sans_amount <= 41:
                self.Sanness.show_normal_sans()
            elif self.stats.sans_amount == 42:
                self.Sanness.show_normal_sans_a_bit_tired()
        elif self.stats.dia == 35:
            self.Sanness.show_confused_sans_a_bit_tired()
        elif self.stats.dia == 36:
            self.Sanness.show_normal_sans_a_bit_tired()
        elif self.stats.dia == 37:
            self.Sanness.show_normal_sans_tired_shrug()
        elif 38 <= self.stats.dia <= 41:
            if 42 <= self.stats.sans_amount <= 44:
                self.Sanness.show_normal_sans_a_bit_tired()
            elif self.stats.sans_amount == 45:
                self.Sanness.show_normal_sans_quite_tired()
        elif self.stats.dia == 42:
            if 44 <= self.stats.sans_amount <= 47:
                self.Sanness.show_normal_sans_quite_tired()
            elif self.stats.sans_amount == 48:
                self.Sanness.show_normal_sans_very_tired()
        elif self.stats.dia == 43:
            self.Sanness.show_normal_sans_very_tired()
        elif self.stats.dia == 44:
            if 49 <= self.stats.sans_amount <= 50:
                self.Sanness.show_normal_sans_very_tired()
            elif self.stats.sans_amount == 51:
                mixer.music.stop()
                self.Sanness.show_normal_sans_sleeping()
        elif self.stats.dia == 45:
            mixer.music.stop()
            self.Sanness.sans_waking_up()
        elif self.stats.dia == 46:
            mixer.music.stop()
            self.Sanness.show_normal_sans_a_bit_tired2()
        elif self.stats.dia == 47:
            mixer.music.stop()
            self.Sanness.show_confused_sans_a_bit_tired()
        elif self.stats.dia == 48:
            mixer.music.stop()
            self.Sanness.show_normal_sans_a_bit_tired_eyes_closed()
        elif self.stats.dia == 49:
            mixer.music.stop()
            self.Sanness.show_normal_sans_a_bit_tired()
        elif self.stats.dia == 50:
            self.stats.phase = 2
            mixer.music.set_volume(5)
            if self.changed_once is False:
                self.sound_played = False
                self.loop_interval = None
                self.changed_once = True
            self.Sanness.show_angry_sans_eyes_closed()
        elif self.stats.dia == 51:
            self.Sanness.show_angry_crazy_sans_no_glow()
        elif 52 <= self.stats.dia <= 53:
             self.Sanness.show_angry_crazy_sans_glow()
        elif self.stats.dia >= 54:
            if 52 <= self.stats.sans_amount <= 53:
                self.Sanness.last_time = None
                self.Sanness.last_time2 = None
                self.Sanness.show_angry_crazy_sans_glow_with_gaster()
            elif self.stats.sans_amount == 54:
                self.Sanness.show_angry_crazy_sans_glow_with_gaster_slamup()
            elif self.stats.sans_amount == 55:
                if self.last_time8 is None:
                    self.last_time8 = time()
                if time() - self.last_time8 <= 1.25:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster_slamup()
                else:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster()
            elif self.stats.sans_amount == 56:
                self.Sanness.show_angry_crazy_sans_glow_with_gaster_slamdown()
            elif self.stats.sans_amount == 57:
                if self.last_time8 is None:
                    self.last_time8 = time()
                if time() - self.last_time8 <= 1.25:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster_slamdown()
                else:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster()
            elif self.stats.sans_amount == 58:
                self.Sanness.show_angry_crazy_sans_glow_with_gaster_slamleft()
            elif self.stats.sans_amount == 59:
                self.Sanness.show_angry_crazy_sans_glow_with_gaster()
            elif self.stats.sans_amount == 60:
                if self.last_time8 is None:
                    self.last_time8 = time()
                if time() - self.last_time8 <= 1.25:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster_slamup()
                else:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster()
                    self.last_time8 = None
            elif self.stats.sans_amount == 61:
                if self.last_time8 is None:
                    self.last_time8 = time()
                if time() - self.last_time8 <= 1.25:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster_slamdown()
                else:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster()
                    self.last_time8 = None
            elif self.stats.sans_amount == 62:
                self.Sanness.show_angry_crazy_sans_glow_with_gaster()
                self.last_time8 = None
            elif self.stats.sans_amount == 63:
                if self.last_time8 is None:
                    self.last_time8 = time()
                if time() - self.last_time8 <= 1:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster_slamup()
                else:
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster()
            elif self.stats.sans_amount == 64:
                self.Sanness.show_angry_crazy_sans_glow_with_gaster()
            elif 65 <= self.stats.sans_amount <= 68:
                self.Sanness.show_angry_crazy_sans_glow_with_gaster()
            elif self.stats.sans_amount == 69:
                if self.last_time13 is None:
                    self.last_time13 = time()
                if time() - self.last_time13 <= 1.25:
                    self.stats.heart_color = 'blue'
                    self.Sanness.show_angry_crazy_sans_glow_with_gaster_slamdown()
                else:
                    self.Sanness.show_difficult_angry_crazy_sans_with_gaster_slamdown()
                    self.Sanness.last_time = None
                    self.Sanness.last_time2 = None
            elif self.stats.sans_amount == 70:
                self.Sanness.show_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamleft()
            elif self.stats.sans_amount == 71:
                self.Sanness.show_a_bit_tired_angry_crazy_sans_glow_with_gaster()
            elif self.stats.sans_amount == 72:
                if self.last_time13 is None:
                    self.last_time13 = time()
                if time() - self.last_time13 <= 0.1:
                    self.Sanness.show_a_bit_tired_angry_crazy_sans_glow_with_gaster()
                else:
                    self.Sanness.show_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamdown()
            elif self.stats.sans_amount == 73:
                self.Sanness.show_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamup()
            elif self.stats.sans_amount == 74:
                self.Sanness.show_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamright()
            elif self.stats.sans_amount == 75:
                self.Sanness.show_a_bit_tired_angry_crazy_sans_glow_with_gaster_slamleft()
            elif 76 <= self.stats.sans_amount <= 81:
                self.Sanness.show_a_bit_tired_angry_crazy_sans_glow_with_gaster()
            elif self.stats.sans_amount == 82:
                self.Sanness.show_tired_angry_crazy_sans_glow_with_gaster()
            elif self.stats.sans_amount == 83:
                self.Sanness.show_quite_tired_angry_crazy_sans_glow_with_gaster()
            elif 84 <= self.stats.sans_amount < 89:
                self.Sanness.show_really_tired_angry_crazy_sans_glow_with_gaster()
            elif 89 <= self.stats.sans_amount < 91:
                if 54 <= self.stats.dia <= 68:
                    self.Sanness.show_really_tired_normal_sans()
                    mixer.music.set_volume(0)
                elif self.stats.dia == 69:
                    self.Sanness.show_really_tired_normal_sans_smile()
                elif self.stats.dia == 70:
                    self.Sanness.show_normal_sans_a_bit_tired()
                elif 71 <= self.stats.dia < 74:
                    self.Sanness.show_normal_sans_a_bit_tired()
                elif self.stats.dia == 74:
                    self.Sanness.show_normal_sans()
                elif self.stats.dia == 75:
                    self.Sanness.show_happy_sans_red()
                elif self.stats.dia == 76:
                    self.Sanness.show_happy_sans_white()
                    if self.last_time is None:
                        self.last_time = time()
                    if time() - self.last_time >= 0.65:
                        self.stats.sans_amount += 1
                        self.last_time = None
            elif self.stats.sans_amount == 91:
                self.Sanness.show_happy_sans_white()

    def up_down_blast_random(self):
        self.arrow_type = random.randint(1, 2)
        self.arrow_randomed = True

    def orange_blue_bones_random(self):
        self.bone_color = random.randint(1, 2)
        if self.bone_color == 1:
            self.bone_color = 'blue'
        elif self.bone_color == 2:
            self.bone_color = 'orange'
        self.color_randomed = True

    def play_sound(self):
        # pass
        if self.stats.sans_amount != 0 and self.stats.dia >= 8 and self.stats.active == True:
            if self.stats.phase == 1:
                if self.loop_interval is None:
                    self.loop_interval = time()
                    mixer.music.load("soundtracks/M.E.G.A.L.O.V.A.N.I.A.mp3")
                    mixer.music.set_volume(2)
                    mixer.music.play(-1)
                if time() - self.loop_interval >= 183:
                    self.loop_interval = None
                    self.sound_played = False
            elif self.stats.phase == 2:
                if self.loop_interval is None:
                    self.loop_interval = time()
                    mixer.music.load("soundtracks/the_last_slacker_continues.mp3")
                    mixer.music.set_volume(5)
                    mixer.music.play(-1)
                if time() - self.loop_interval >= 178:
                    self.loop_interval = None
                    self.sound_played = False
        elif self.bgsans.visability == True and self.stats.active == False:
            if self.loop_interval is None:
                self.loop_interval = time()
                mixer.music.load('soundtracks/Intro_music.mp3')
                mixer.music.set_volume(0.3)
                mixer.music.play(-1)
            if time() - self.loop_interval >= 170:
                self.loop_interval = None
                self.sound_played = False
        elif self.stats.active == 'instruction':
            if self.loop_interval is None:
                self.loop_interval = time()
                mixer.music.load('soundtracks/instruc_music.mp3')
                mixer.music.set_volume(0.4)
                mixer.music.play(-1)
            if time() - self.loop_interval >= 31:
                self.loop_interval = None
                self.sound_played = False
        elif self.stats.active == 'credits':
            if self.loop_interval is None:
                self.loop_interval = time()
                mixer.music.load('soundtracks/credit_music.mp3')
                mixer.music.set_volume(2)
                mixer.music.play(-1)
            if time() - self.loop_interval >= 111:
                self.loop_interval = None
                self.sound_played = False
        else:
            self.loop_interval = None
            self.sound_played = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        if self.stats.active == True:
            if self.stats.turn != 'black_out' and self.stats.turn != 'black_out2' and self.stats.turn != 'black_out3' and self.stats.turn != 'black_out4' \
                    and self.stats.turn != 'black_out5' and self.stats.turn != 'black_out6' and self.stats.turn != 'black_out7' and self.stats.turn != 'black_out8' \
                    and self.stats.turn != 'black_out9' and self.stats.turn != 'black_out10' and self.stats.turn != 'black_out11':
                # if self.stats.sans_amount == 67:
                #     print(f'x: {self.heart.rect.x}      y: {self.heart.rect.y}')
                if self.slam.slam == 'down' and self.att.bone_down_visibility == False and self.stats.dia == 6:
                    self.Sanness.sd_warning()
                self.battle.blitme()
                if self.stats.turn != 'hit sans' and self.stats.turn != 'sans down' and self.stats.turn != 'killed speech turn' and self.stats.turn != 'sans dead' and self.stats.sans_health == 1:
                    self.show_normal_fight_sans()
                elif self.stats.turn == 'hit sans' and self.stats.sans_health == 1:
                    self.Sanness.show_shocked_sans()
                    self.slash_mark()
                elif self.stats.turn == 'sans down' and self.stats.sans_health == 0:
                    if self.stats.kill_dia == 1 or self.stats.kill_dia == 2:
                        self.Sanness.show_downed_sans()
                        if self.stats.kill_dia == 1:
                            self.Sanness.shake_sans()
                        elif self.stats.kill_dia == 2:
                            self.delay_sans_smile()
                    elif self.stats.kill_dia == 3:
                        self.Sanness.show_pleased_sans()
                        self.delay_kill_speech()
                elif self.stats.turn == 'killed speech turn' and self.stats.sans_health == 0:
                    if self.stats.kill_dia == 4 or self.stats.kill_dia == 5:
                        self.Sanness.show_pleased_sans()
                    elif self.stats.kill_dia == 6 or self.stats.kill_dia == 7:
                        self.Sanness.show_killed_tired_sans()
                    elif self.stats.kill_dia == 8 or self.stats.kill_dia == 9:
                        self.Sanness.show_almost_dead_sans()
                    elif self.stats.kill_dia == 10:
                        self.Sanness.show_dead_sans()
                elif self.stats.turn == 'end game' and self.stats.sans_health == 0:
                    if self.stats.kill_dia == 11:
                        self.Sanness.show_dead_sans()
                        self.Sanness.show_fade()
                        if self.Sanness.fade_value <= 255:
                            self.Sanness.increase_fade()
                        else:
                            self.stats.sans_amount = 0
                self.show_healths()
                if self.stats.turn == 'fightb' or self.stats.turn == 'actb' or self.stats.turn == 'itemb' or self.stats.turn == 'mercyb' or self.stats.turn == 'acti':
                    self.mh.show_menu_heart()
                if self.stats.turn == 'fightb':
                    self.inside.show_fighttext()
                    top = self.battle.rect.top + 35
                    left = self.battle.rect.left + 28
                    self.mh.menu_heart_rect.top = top
                    self.mh.menu_heart_rect.left = left
                elif self.stats.turn == 'fightis':
                    self.fightbar.show_fight_bar()
                    self.fightbar.expand_fight_bar()
                    if 730 <= self.fightbar.fightbar_rect.width < 760:
                        self.fightmarker.make_fight_marker()
                    if self.fightbar.fightbar_rect.width >= 760 and self.fightmarker.fight_marker.left >= self.fightbar.fightbar_rect.left:
                        self.fightmarker.show_fight_marker()
                        self.move_fight_marker()
                    if self.fightmarker.fight_marker.left <= self.fightbar.fightbar_rect.left:
                        self.stats.turn = 'speech turn'
                        self.stats.dia += 1
                        self.heart.reset_pos()
                elif self.stats.turn == 'fightie':
                    self.sans_hit_delay()
                elif self.stats.turn == 'actb':
                    self.inside.show_act_name()
                    top = self.battle.rect.top + 35
                    left = self.battle.rect.left + 28
                    self.mh.menu_heart_rect.top = top
                    self.mh.menu_heart_rect.left = left
                elif self.stats.turn == 'acti':
                    self.inside.show_act_options()
                    if self.selected == 'check':
                        top = self.battle.rect.top + 35
                        left = self.battle.rect.left + 28
                        self.mh.menu_heart_rect.top = top
                        self.mh.menu_heart_rect.left = left
                    elif self.selected == 'reason':
                        top = self.battle.rect.top + 35
                        right = self.inside.act_options_pair[1]['rect'].left - 20
                        self.mh.menu_heart_rect.top = top
                        self.mh.menu_heart_rect.right = right
                elif self.stats.turn == 'itemb':
                    self.used.draw(self.screen)
                    if self.selected_page == 1:
                        self.show_first_page_items()
                    elif self.selected_page == 2:
                        self.show_second_page_items()
                    if self.selected == 'Pie' or self.selected == 'Lhero1':
                        top = self.battle.rect.top + 35
                        left = self.battle.rect.left + 28
                        self.mh.menu_heart_rect.top = top
                        self.mh.menu_heart_rect.left = left
                    elif self.selected == 'Noodles1' or self.selected == 'Lhero2':
                        top = self.battle.rect.top + 35
                        right = self.inside.item_options[1]['rect'].left - 20
                        self.mh.menu_heart_rect.top = top
                        self.mh.menu_heart_rect.right = right
                    elif self.selected == 'Noodles2' or self.selected == 'Lhero3':
                        bottom = self.battle.rect.bottom - 125
                        left = self.battle.rect.left + 28
                        self.mh.menu_heart_rect.bottom = bottom
                        self.mh.menu_heart_rect.left = left
                    elif self.selected == 'Fsteak' or self.selected == 'Lhero4':
                        bottom = self.battle.rect.bottom - 125
                        right = self.inside.item_options[3]['rect'].left - 20
                        self.mh.menu_heart_rect.bottom = bottom
                        self.mh.menu_heart_rect.right = right
                elif self.stats.turn == 'mercyb':
                    self.inside.show_mercy()
                    top = self.battle.rect.top + 35
                    left = self.battle.rect.left + 28
                    self.mh.menu_heart_rect.top = top
                    self.mh.menu_heart_rect.left = left
                if self.stats.turn == 'sans turn' or self.stats.turn == 'speech turn' or self.stats.turn == 'fightb' or self.stats.turn == 'actb' or self.stats.turn == 'itemb' \
                        or self.stats.turn == 'mercyb' or self.stats.turn == 'acti' or self.stats.turn == 'fightis' or self.stats.turn == 'fightie' or self.stats.turn == 'hit sans' \
                        or self.stats.turn == 'sans down' or self.stats.turn == 'killed speech turn' or self.stats.turn == 'end game' or self.stats.turn == 'checked' \
                        or self.stats.turn == 'reasoned' or self.stats.turn == 'ate pie' or self.stats.turn == 'ate noodles' or self.stats.turn == 'ate steak' or self.stats.turn == 'ate lhero':
                    self.show_red_menu()
                if self.stats.turn == 'spared turn':
                    self.show_orange_menu()
                if self.stats.turn == 'my turn' and self.fighted == True and self.acted == False and self.itemed == False and self.mercyed == False:
                    self.show_fight_y_red_menu()
                if self.stats.turn == 'my turn' and self.fighted == False and self.acted == True and self.itemed == False and self.mercyed == False:
                    self.show_act_y_red_menu()
                if self.stats.turn == 'my turn' and self.fighted == False and self.acted == False and self.itemed == True and self.mercyed == False:
                    self.show_item_y_red_menu()
                if self.stats.turn == 'my turn' and self.fighted == False and self.acted == False and self.itemed == False and self.mercyed == True:
                    self.show_mercy_y_red_menu()
                if self.stats.turn == 'speech turn' or self.stats.turn == 'killed speech turn':
                    if self.stats.dia != 45:
                        self.show_all_speech()
                if self.stats.turn == 'spared turn' and self.stats.sans_amount == 91:
                    self.bt.show_TDE2()
                    if self.last_time is None:
                        self.last_time = time()
                    if time() - self.last_time >= 4.25:
                        self.stats.active = 'credits'
                        self.last_time = None
                        self.last_time2 = None
                        self.last_time3 = None
                        mixer.music.stop()
                        self.loop_interval = None
                        self.sound_played = False
                if self.stats.turn == 'my turn' and self.battle.rect.width == 810:
                    if self.stats.sans_amount == 7:
                        self.bt.show_T1()
                    elif self.stats.sans_amount == 9:
                        self.bt.show_T2()
                    elif 12 <= self.stats.sans_amount <= 41:
                        self.bt.show_T3()
                    elif self.stats.sans_amount == 42:
                        self.bt.show_T4()
                    elif self.stats.sans_amount == 45:
                        self.bt.show_T5()
                    elif self.stats.sans_amount == 48:
                        self.bt.show_T6()
                    elif self.stats.sans_amount == 51:
                        self.bt.show_T7()
                    elif 90 <= self.stats.sans_amount:
                        if 55 <= self.stats.dia <= 68:
                            self.bt.show_T8()
                        elif 70 <= self.stats.dia:
                            self.bt.show_T9()
                if self.stats.turn == 'checked' or self.stats.turn == 'reasoned':
                    self.bt.show_AT()
                if self.stats.turn == 'ate pie' or self.stats.turn == 'ate noodles' or self.stats.turn == 'ate steak' or self.stats.turn == 'ate lhero':
                    self.bt.show_IT()
                if self.stats.turn == 'end game':
                    if self.stats.sans_amount == 0:
                        if self.stats.sans_health == 0:
                            self.bt.show_TDE()
                            self.delay_win_screen()
                if self.stats.turn == 'sans turn':
                    if self.fightbar.width != 10 or self.fightmarker.fight_marker.right != self.fightbar.fightbar_rect.right:
                        self.fightbar.reset_fight_bar()
                        self.fightmarker.make_fight_marker()
                    if self.stats.sans_amount == 1:
                        self.battle.shrinks()
                if self.stats.turn != 'speech turn' and self.stats.turn != 'sans turn' and self.stats.turn != 'black_out' and self.stats.turn != 'black_out2' \
                        and self.stats.turn != 'black_out3' and self.stats.turn != 'black_out4' and self.stats.turn != 'black_out5' and self.stats.turn != 'black_out6' \
                        and self.stats.turn != 'black_out7' and self.stats.turn != 'black_out8' and self.stats.turn != 'black_out9' and self.stats.turn != 'black_out10' \
                        and self.stats.turn != 'black_out11':
                    if self.battle.rect.width != 810:
                        self.battle.return_size_width()
                    if self.battle.rect.height != 270:
                        self.battle.return_size_height()
                if self.battle.rect.width == 270 and self.stats.sans_amount == 1:
                    self.stats.heart_color = 'blue'
                if self.battle.rect.width == 270 and self.stats.sans_amount == 3:
                    self.stats.heart_color = 'red'
                if self.stats.sans_amount == 1 and self.stats.heart_color == 'blue' and self.stats.turn == 'sans turn' and self.slam.slam == 'down':
                    self.heart.gravity_instant()
                    if self.heart.rect.bottom == self.battle.rect.bottom:
                        self.stats.sans_amount += 1
                if self.stats.sans_amount == 2 and self.att.bone_down_visibility != True:
                    self.bone_up()
                if self.stats.sans_amount == 3:
                    self.swirl_bone()
                    if self.swirl.rect12.left >= self.battle.rect.right:
                        self.stats.sans_amount += 1
                        self.last_time = None
                        self.last_time2 = None
                if self.stats.sans_amount == 4 and self.stats.turn == 'sans turn':
                    self.blast_gaster_diagonal()
                if self.stats.sans_amount == 5 and self.stats.turn == 'sans turn':
                    self.blast_gaster_center()
                if self.stats.sans_amount == 6 and self.stats.turn == 'sans turn':
                    if self.wrote is False:
                        with open('data/data.txt', 'r') as file:
                            lines = file.read()
                            lines = lines.split(' ')
                            del lines[0]
                            lines.insert(0, 'beat_the_first_attack')
                            second_line = f' {lines[1]}'
                            del lines[1]
                            lines.append(second_line)

                        with open('data/data.txt', 'w') as d:
                            for line in lines:
                                d.write(line)
                        self.wrote = True
                    self.sans_shrug_delay()
                if self.stats.sans_amount == 8 and self.stats.turn == 'sans turn':
                    if self.heart.add != 0 or self.heart.jump != False:
                        self.heart.add = 0
                        self.heart.jump = False
                    self.stats.heart_color = 'blue'
                    if self.swirl.first_swirl_top != 2000:
                        self.move_swirl_off_screen()
                    if self.battle.rect.width != 670:
                        self.battle.shrink_a_bit1()
                    else:
                        self.stats.sans_amount += 1
                if self.stats.sans_amount == 9 and self.stats.turn == 'sans turn':
                    if self.repeat <= 5:
                        self.blast_gaster_up_down()
                    if self.repeat == 6:
                        self.stats.turn = 'my turn'
                        self.repeat = 0
                if self.stats.sans_amount == 10 and self.stats.turn == 'sans turn':
                    self.stats.heart_color = 'red'
                    if self.swirl.first_swirl_top != 2000:
                        self.move_swirl_off_screen()
                    if self.battle.rect.width != 490:
                        self.battle.shrink_a_bit2()
                    else:
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time >= 0.5:
                            self.stats.sans_amount += 1
                            self.last_time = None
                if self.stats.sans_amount == 11 or self.stats.sans_amount == 12 and self.stats.turn == 'sans turn':
                    if self.stats.sans_amount == 11:
                        self.show_trap_bone_bl()
                    elif self.stats.sans_amount == 12:
                        if self.repeat <= 3:
                            self.right_bone.draw(self.screen)
                            self.top_bone.draw(self.screen)
                            self.blockblast.draw(self.screen)
                            self.blockblaster.draw(self.screen)
                            if self.arrow_randomed is False:
                                self.up_down_blast_random()
                            if self.arrow_type == 1:
                                self.wa.show_arrow_up()
                            elif self.arrow_type == 2:
                                self.wa.show_arrow_down()
                            if self.wa.arrow_direction == 'up':
                                self.blast_gaster_bottom_left_up()
                            elif self.wa.arrow_direction == 'down':
                                self.blast_gaster_bottom_left_down()
                        elif self.repeat == 4:
                            self.stats.turn = 'my turn'
                            self.repeat = 0
                            self.right_bone.empty()
                            self.top_bone.empty()
                if self.stats.sans_amount == 13 or self.stats.sans_amount == 14 or self.stats.sans_amount == 15 or self.stats.sans_amount == 16 \
                        or self.stats.sans_amount == 17 or self.stats.sans_amount == 18 or self.stats.sans_amount == 19 or self.stats.sans_amount == 20 and self.stats.turn == 'sans turn':
                    if self.stats.sans_amount == 13:
                        self.stats.heart_color = 'blue'
                        if self.swirl.first_swirl_top != 2000:
                            self.move_swirl_off_screen()
                        if self.heart.rect.bottom != self.battle.rect.bottom or self.battle.rect.width != 270:
                            self.heart.gravity_instant()
                            self.battle.shrinks()
                        else:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 14:
                        self.blast_gaster_up_down_delayed()
                    elif self.stats.sans_amount == 15 or self.stats.sans_amount == 16:
                        self.blast.draw(self.screen)
                        self.gasterblaster.draw(self.screen)
                        if self.stats.sans_amount == 15:
                            pass
                        elif self.stats.sans_amount == 16:
                            self.heart.gravity_instant()
                            if self.heart.rect.left == self.battle.rect.left:
                                self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 17:
                        self.blast.draw(self.screen)
                        self.gasterblaster.draw(self.screen)
                        self.blast_gaster_just_left()
                    elif self.stats.sans_amount == 18:
                        self.blast.draw(self.screen)
                        self.gasterblaster.draw(self.screen)
                        self.heart.gravity_instant()
                        if self.heart.rect.right == self.battle.rect.right:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 19:
                        self.blast.draw(self.screen)
                        self.gasterblaster.draw(self.screen)
                        self.blast_gaster_bottom_right()
                    elif self.stats.sans_amount == 20:
                        self.blast.draw(self.screen)
                        self.gasterblaster.draw(self.screen)
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time >= 1.5:
                            self.stats.sans_amount += 1
                            self.gasterblaster.empty()
                            self.blast.empty()
                            self.last_time = None
                            self.stats.turn = 'my turn'
                if self.stats.sans_amount == 22 or self.stats.sans_amount == 23 or self.stats.sans_amount == 24 or self.stats.sans_amount == 25 \
                        or self.stats.sans_amount == 26 or self.stats.sans_amount == 27 and self.stats.turn == 'sans turn':
                    if self.stats.sans_amount == 22:
                        if self.swirl.first_swirl_top != 2000:
                            self.move_swirl_off_screen()
                        if self.battle.rect.width != 490:
                            self.battle.shrink_a_bit2()
                        else:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 23:
                        self.show_60_bones()
                    elif self.stats.sans_amount == 24:
                        if self.repeat <= 3:
                            self.bones.draw(self.screen)
                            if self.color_randomed is False:
                                self.orange_blue_bones_random()
                            self.show_40_bones()
                        else:
                            self.stats.sans_amount += 1
                            self.repeat = 0
                            self.bones.empty()
                            self.blue_bones.empty()
                            self.orange_bones.empty()
                    elif self.stats.sans_amount == 25:
                        self.battle.shrinks()
                        if self.heart.rect.left < self.battle.rect.left:
                            self.heart.x += 10
                            self.heart.x2 += 10
                            self.heart.x3 += 10
                            self.heart.x4 += 10
                        if self.battle.rect.width == 270:
                            self.stats.sans_amount += 1
                            if self.stop_blaster != False:
                                self.stop_blaster = False
                    elif self.stats.sans_amount == 26:
                        self.blast_gaster_center()
                    elif self.stats.sans_amount == 27:
                        self.stats.sans_amount += 1
                        self.stats.turn = 'my turn'
                if self.stats.sans_amount == 29 or self.stats.sans_amount == 30 or self.stats.sans_amount == 31 or self.stats.sans_amount == 32 or self.stats.sans_amount == 33 \
                        or self.stats.sans_amount == 34 and self.stats.turn == 'sans turn':
                    if self.stats.sans_amount == 29:
                        if self.swirl.first_swirl_top != 2000:
                            self.move_swirl_off_screen()
                        self.heart.heart_direction = 'up'
                        self.stats.heart_color = 'blue'
                        self.battle.shrink_a_bit2()
                        if self.battle.rect.width == 490 and self.heart.blue_rect.bottom == self.battle.rect.bottom:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 30:
                        self.bone_up_general()
                    elif self.stats.sans_amount == 31:
                        self.bones.draw(self.screen)
                        self.move_plat_center_battle()
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time >= 2:
                            self.last_time = None
                            self.last_time2 = None
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 32 or self.stats.sans_amount == 33:
                        self.bones.draw(self.screen)
                        if self.stats.sans_amount == 32:
                            self.platformrs.draw(self.screen)
                            self.stats.platform_color = 'red'
                            self.test_move_platforms()
                        elif self.stats.sans_amount == 33:
                            self.platformys.draw(self.screen)
                            self.stats.platform_color = 'yellow'
                            self.test_move_platforms()
                    elif self.stats.sans_amount == 34:
                        self.stats.platform_color = 'red'
                        self.bones.draw(self.screen)
                        self.platformrs.draw(self.screen)
                        self.move_platforms_left_right()
                        if self.repeat <= 6:
                            self.move_between_bones_inward()
                            self.between_bones_left.draw(self.screen)
                            self.between_bones_right.draw(self.screen)
                        else:
                            self.between_bones_right.empty()
                            self.between_bones_left.empty()
                            self.platformrs.empty()
                            self.platformys.empty()
                            self.heart.platformrs.empty()
                            self.heart.platformys.empty()
                            self.bones.empty()
                            self.stats.turn = 'my turn'
                            self.stats.sans_amount += 1
                            self.repeat = 0
                            self.platform_moved_left_once1 = False
                            self.platform_moved_left_once2 = False
                            self.platform_moved_left_once3 = False
                            self.platform_moved_left_once4 = False
                            self.created_bone = False
                            self.last_time = None
                            self.last_time2 = None
                if self.stats.sans_amount == 36 or self.stats.sans_amount == 37 or self.stats.sans_amount == 38 and self.stats.turn == 'sans turn':
                    if self.stats.sans_amount == 36:
                        if self.swirl.first_swirl_top != 2000:
                            self.move_swirl_off_screen()
                        self.stats.heart_color = 'blue'
                        if self.battle.rect.width != 490:
                            self.battle.shrink_a_bit2()
                        else:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 37:
                        self.between_bones_left.draw(self.screen)
                        self.between_bones_right.draw(self.screen)
                        self.blast_gaster_top_right_left()
                        self.move_going_right_and_left_up_down_bones()
                    elif self.stats.sans_amount == 38:
                        self.between_bones_left.draw(self.screen)
                        self.between_bones_right.draw(self.screen)
                        self.blast.draw(self.screen)
                        self.gasterblaster.draw(self.screen)
                        self.move_going_right_and_left_up_down_bones()
                        if self.repeat == 14:
                            self.between_bones_left.empty()
                            self.between_bones_right.empty()
                            self.gasterblaster.empty()
                            self.blast.empty()
                            self.stats.sans_amount += 1
                            self.stats.turn = 'my turn'
                            self.last_time = None
                            self.last_time2 = None
                            self.last_time3 = None
                            self.last_time10 = None
                            self.blaster_created = False
                            self.blaster_created2 = False
                            self.blaster_blasted = False
                            self.blaster_blasted2 = False
                            self.stop_blaster = False
                            self.created_bone = False
                            self.repeat = 0
                if self.stats.sans_amount == 40 or self.stats.sans_amount == 41 and self.stats.turn == 'sans turn':
                    if self.stats.sans_amount == 40:
                        self.stats.heart_color = 'red'
                        if self.swirl.first_swirl_top != 2000:
                            self.move_swirl_off_screen()
                        if self.battle.rect.width != 490:
                            self.battle.shrink_to_left()
                        else:
                            if self.last_time is None:
                                self.last_time = time()
                            if time() - self.last_time >= 1.25:
                                self.last_time = None
                                self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 41:
                        self.flyingbonestop.draw(self.screen)
                        self.flyingbonesright.draw(self.screen)
                        self.flyingbonesleft.draw(self.screen)
                        self.flyingbonesbottom.draw(self.screen)
                        self.move_flying_bone()
                        if self.last_time2 is None:
                            self.last_time2 = time()
                        if time() - self.last_time2 >= 22:
                            self.stats.sans_amount += 1
                            self.created_bone = False
                            self.stats.turn = 'my turn'
                            self.last_time2 = None
                            self.flyingbonestop.empty()
                            self.flyingbonesright.empty()
                            self.flyingbonesleft.empty()
                            self.flyingbonesbottom.empty()
                elif self.stats.sans_amount == 43 or self.stats.sans_amount == 44 and self.stats.turn == 'sans turn':
                    if self.stats.sans_amount == 43:
                        if self.swirl.first_swirl_top != 2000:
                            self.move_swirl_off_screen()
                        self.between_bones_height = 'low'
                        self.stats.heart_color = 'blue'
                        self.battle.shrink_a_bit2()
                        if self.heart.blue_rect.bottom == self.battle.rect.bottom:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 44:
                        if self.repeat <= 5:
                            self.move_between_bones_inward()
                            self.between_bones_left.draw(self.screen)
                            self.between_bones_right.draw(self.screen)
                        else:
                            self.between_bones_right.empty()
                            self.between_bones_left.empty()
                            self.platformrs.empty()
                            self.platformys.empty()
                            self.heart.platformrs.empty()
                            self.heart.platformys.empty()
                            self.bones.empty()
                            self.stats.turn = 'my turn'
                            self.stats.sans_amount += 1
                            self.repeat = 0
                            self.platform_moved_left_once1 = False
                            self.platform_moved_left_once2 = False
                            self.platform_moved_left_once3 = False
                            self.platform_moved_left_once4 = False
                            self.created_bone = False
                            self.last_time = None
                            self.last_time2 = None
                elif self.stats.sans_amount == 46 or self.stats.sans_amount == 47 and self.stats.turn == 'sans turn':
                    mixer.music.set_volume(0.9)
                    if self.stats.sans_amount == 46:
                        if self.swirl.first_swirl_top != 2000:
                            self.move_swirl_off_screen()
                        self.stats.heart_color = 'blue'
                        self.battle.shrink_a_bit2()
                        if self.heart.blue_rect.bottom == self.battle.rect.bottom:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 47:
                        self.blast_gaster_just_bottom()
                elif self.stats.sans_amount == 49 or self.stats.sans_amount == 50 and self.stats.turn == 'sans turn':
                    if self.swirl.first_swirl_top != 2000:
                        self.move_swirl_off_screen()
                    mixer.music.set_volume(0.4)
                    if self.stats.sans_amount == 49:
                        self.stats.heart_color = 'blue'
                        self.battle.shrinks()
                        if self.heart.blue_rect.bottom == self.battle.rect.bottom:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 50:
                        mixer.music.set_volume(0.15)
                        if self.created_bone is False:
                            bone = Attacks(self)
                            bone.rect.bottom = self.battle.rect.bottom
                            bone.rect.left = self.battle.rect.left
                            self.bones.add(bone)
                            self.created_bone = True
                        self.bones.draw(self.screen)
                        for bone in self.bones.sprites():
                            bone.move_bone_right_slow()
                            if bone.rect.right == self.battle.rect.right:
                                self.bones.empty()
                                self.stats.sans_amount += 1
                                self.stats.turn = 'my turn'
                                self.Sanness.last_time = None
                                self.Sanness.last_time2 = None
                                self.Sanness.last_time3 = None
                                self.Sanness.last_time4 = None
                                self.Sanness.last_time5 = None
                                self.Sanness.last_time6 = None
                                self.last_time13 = None
                                mixer.music.stop()
                if 52 <= self.stats.sans_amount and self.stats.turn == 'sans turn':
                    if self.stats.sans_amount == 52:
                        self.stats.heart_color = 'red'
                        if self.swirl.first_swirl_top != 2000:
                            self.move_swirl_off_screen()
                        self.blast_gaster_to_left()
                    elif self.stats.sans_amount == 53:
                        self.blast_gaster_to_right()
                    elif self.stats.sans_amount == 54:
                        self.stats.heart_color = 'blue'
                        self.battle.shrink_a_bit2()
                        if self.heart.rect.right > self.battle.rect.right:
                            self.heart.x -= 10
                            self.heart.x2 -= 10
                            self.heart.x3 -= 10
                            self.heart.x4 -= 10
                            self.heart.x5 -= 10
                        if self.last_time is None:
                            self.last_time = time()
                            self.heart.gravity_instant()
                        if time() - self.last_time <= 0.45:
                            self.heart.gravity_instant()
                            self.between_bones_height = 'low'
                        else:
                            self.last_time = None
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 55:
                        self.battle.shrink_a_bit2()
                        if self.heart.rect.right > self.battle.rect.right:
                            self.heart.x -= 10
                            self.heart.x2 -= 10
                            self.heart.x3 -= 10
                            self.heart.x4 -= 10
                            self.heart.x5 -= 10
                        if self.last_time7 is None:
                            self.last_time7 = time()
                        if time() - self.last_time7 >= 0.75:
                            if self.repeat <= 6:
                                self.between_bones_left.draw(self.screen)
                                self.between_bones_right.draw(self.screen)
                                self.move_between_bones_inward()
                            else:
                                self.between_bones_left.empty()
                                self.between_bones_right.empty()
                                self.created_bone = False
                                self.repeat = 0
                                self.last_time = None
                                self.last_time2 = None
                                self.Sanness.last_time = None
                                self.Sanness.last_time2 = None
                                self.last_time3 = None
                                self.last_time4 = None
                                self.last_time5 = None
                                self.last_time7 = None
                                self.last_time8 = None
                                self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 56:
                        self.heart.gravity_instant()
                        if self.heart.rect.bottom == self.battle.rect.bottom:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 57:
                        self.blast_gaster_just_bottom_phase_2()
                    elif self.stats.sans_amount == 58:
                        self.last_time8 = None
                    elif self.stats.sans_amount == 59:
                        if self.last_time12 is None:
                            self.last_time12 = time()
                        if time() - self.last_time12 <= 0.15:
                            self.heart.gravity_instant()
                        self.blast_gaster_just_left_phase_2()
                    elif self.stats.sans_amount == 60:
                        if self.last_time12 is None:
                            self.last_time12 = time()
                        if time() - self.last_time12 <= 0.28:
                            self.heart.gravity_instant()
                        else:
                            self.stats.sans_amount += 1
                            self.last_time12 = None
                    elif self.stats.sans_amount == 61:
                        if self.last_time12 is None:
                            self.last_time12 = time()
                        if time() - self.last_time12 <= 0.28:
                            self.heart.gravity_instant()
                        else:
                            self.stats.sans_amount += 1
                            self.last_time12 = None
                    elif self.stats.sans_amount == 62:
                        self.stats.heart_color = 'blue'
                        self.blast_gaster_full_bottom_half_side()
                        self.repeat = 0
                    elif self.stats.sans_amount == 63:
                        self.blast.draw(self.screen)
                        self.gasterblaster.draw(self.screen)
                        if self.last_time13 is None:
                            self.last_time13 = time()
                        if time() - self.last_time13 <= 0.15:
                            self.heart.gravity_instant()
                        if self.last_time12 is None:
                            self.last_time12 = time()
                        if time() - self.last_time12 >= 1:
                            if self.repeat <= 18:
                                self.bones.draw(self.screen)
                                self.move_going_left_up_bones()
                            else:
                                self.stats.sans_amount += 1
                                self.last_time = None
                                self.last_time12 = None
                                self.last_time13 = None
                                self.last_time2 = None
                                self.last_time3 = None
                                self.gasterblaster.empty()
                                self.created_bone = False
                                self.blaster_created = False
                                self.blaster_blasted = False
                                self.blast.empty()
                                self.bones.empty()
                                self.repeat = 0
                    elif self.stats.sans_amount == 64:
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time >= 0.5:
                            self.stats.heart_color = 'red'
                            if self.heart.rect.top < self.battle.rect.top:
                                self.heart.y += 2
                                self.heart.y2 += 2
                                self.heart.y3 += 2
                                self.heart.y4 += 2
                                self.heart.y5 += 2
                            if self.heart.rect.right > self.battle.rect.right:
                                self.heart.x -= 2
                                self.heart.x2 -= 2
                                self.heart.x3 -= 2
                                self.heart.x4 -= 2
                                self.heart.x5 -= 2
                            if self.battle.rect.height != 120 and self.shrunk_battle_box == 0:
                                self.battle.shrink_to_bottom()
                            else:
                                if self.shrunk_battle_box == 0:
                                    self.shrunk_battle_box += 1
                                if self.battle.rect.width != 250 and self.shrunk_battle_box == 1:
                                    self.battle.shrink_to_left_a_bit()
                                else:
                                    self.stats.sans_amount += 1
                                    self.shrunk_battle_box = 0
                    elif self.stats.sans_amount == 65:
                        if self.repeat <= 4:
                            self.random_gaster_hand_color()
                            if self.gaster_hand_color_randomed is True:
                                self.blast_gaster_hand()
                        else:
                            self.repeat = 0
                            self.stats.sans_amount += 1
                            self.last_time = None
                            self.last_time2 = None
                            self.last_time3 = None
                            self.last_time4 = None
                            self.last_time5 = None
                            self.last_time6 = None
                            self.last_time7 = None
                            self.last_time8 = None
                            self.last_time9 = None
                            self.last_time10 = None
                            self.last_time11 = None
                            self.last_time12 = None
                            self.last_time13 = None
                            self.hand_blast.location = 1000
                            self.hand_blast.blast_hand()
                            self.hand_blast.blast_color()
                            self.hand_blast.blast_beam()
                    elif self.stats.sans_amount == 66:
                        if self.heart.rect.left < self.battle.rect.left:
                            self.heart.x += 2
                            self.heart.x2 += 2
                            self.heart.x3 += 2
                            self.heart.x4 += 2
                            self.heart.x5 += 2
                        if self.battle.rect.width != 270:
                            self.battle.return_size_width2()
                        elif self.battle.rect.height != 270:
                            self.battle.return_size_height()
                        else:
                            self.stats.sans_amount += 1
                    elif self.stats.sans_amount == 67:
                        if self.heart.rect.left < self.battle.rect.left:
                            self.heart.x += 2
                            self.heart.x2 += 2
                            self.heart.x3 += 2
                            self.heart.x4 += 2
                            self.heart.x5 += 2
                        self.trap_player_by_blaster1()
                    elif self.stats.sans_amount == 68:
                        self.blast.draw(self.screen)
                        self.gasterblaster.draw(self.screen)
                        self.trap_player_by_blaster2()
                    elif self.stats.sans_amount == 69:
                        self.heart.gravity_instant()
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time >= 0.1:
                            self.blast.draw(self.screen)
                            self.gasterblaster.draw(self.screen)
                            self.track_player_with_gaster()
                    elif self.stats.sans_amount == 70:
                        pass
                    elif self.stats.sans_amount == 71 or self.stats.sans_amount == 72 or self.stats.sans_amount == 73 or self.stats.sans_amount == 74:
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time <= 0.15:
                            self.heart.gravity_instant()
                        else:
                            self.stats.sans_amount += 1
                            self.last_time = None
                    elif self.stats.sans_amount == 72:
                        if self.last_time12 is None:
                            self.last_time12 = time()
                        if time() - self.last_time12 >= 0.11:
                            if self.last_time is None:
                                self.last_time = time()
                            if time() - self.last_time <= 0.15:
                                self.heart.gravity_instant()
                            else:
                                self.stats.sans_amount += 1
                                self.last_time = None
                                self.last_time13 = None
                                self.last_time12 = None
                    elif self.stats.sans_amount == 73:
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time <= 0.15:
                            self.heart.gravity_instant()
                        else:
                            self.stats.sans_amount += 1
                            self.last_time = None
                    elif self.stats.sans_amount == 74:
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time <= 0.15:
                            self.heart.gravity_instant()
                        else:
                            self.stats.sans_amount += 1
                            self.last_time = None
                    elif self.stats.sans_amount == 75:
                        pass
                    elif self.stats.sans_amount == 76:
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time <= 0.15:
                            self.heart.gravity_instant()
                        else:
                            self.stats.turn = 'black_out'
                            self.big_hand.make_big_hand()
                            self.last_time = None
                    elif self.stats.sans_amount == 77 or self.stats.sans_amount == 78 or self.stats.sans_amount == 79:
                        if self.stats.sans_amount == 77:
                            self.big_hand.show_big_hand()
                            if self.last_time is None:
                                self.last_time = time()
                            if time() - self.last_time >= 1:
                                if self.big_hand.bighand_rect.bottom <= self.battle.rect.bottom - 34:
                                    self.big_hand.move_big_hand_down()
                                else:
                                    self.stats.sans_amount += 1
                                    self.fullbone.reset_posed_x = False
                                    self.bone_tip.reset_posed_x = False
                                    self.bottom_bone_number = 1
                        if self.stats.sans_amount == 78 or self.stats.sans_amount == 79:
                            self.big_hand.show_big_hand()
                            self.bottom_bone.draw(self.screen)
                            if self.stats.sans_amount == 78:
                                if self.last_time is None:
                                    self.last_time = time()
                                if time() - self.last_time >= 0.15:
                                    self.poke_player_with_bone()
                            if self.stats.sans_amount == 79:
                                self.stats.heart_color = 'red'
                                self.make_blaster_stretch_sike()
                    elif self.stats.sans_amount == 80:
                        self.blast_gaster_top_right_left_down()
                    elif self.stats.sans_amount == 81:
                        self.blast_gaster_up_down2()
                    elif self.stats.sans_amount == 82:
                        self.blast_gaster_up_down_left()
                    elif self.stats.sans_amount == 83:
                        self.blast_gaster_just_top()
                    elif self.stats.sans_amount == 84:
                        self.gasterblaster.draw(self.screen)
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time >= 1:
                            self.last_time = None
                            self.stats.turn = 'black_out2'
                            self.gasterblaster.empty()
                    elif self.stats.sans_amount == 85:
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time >= 0.95:
                            self.last_time = None
                            self.stats.turn = 'black_out3'
                    elif self.stats.sans_amount == 86:
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time >= 0.75:
                            self.last_time = None
                            self.stats.turn = 'black_out4'
                    elif self.stats.sans_amount == 87:
                        if self.last_time is None:
                            self.last_time = time()
                        if time() - self.last_time >= 0.5:
                            self.last_time = None
                            self.stats.turn = 'black_out5'
                            self.repeat = 0
                    elif self.stats.sans_amount == 88:
                        if self.repeat <= 4:
                            if self.last_time is None:
                                self.last_time = time()
                            if time() - self.last_time >= 0.25:
                                self.last_time = None
                                self.stats.turn = 'black_out6'
                                self.repeat += 1
                        else:
                            mixer.music.set_volume(0)
                            self.stats.turn = 'black_out7'
                if self.stats.turn == 'sans turn':
                    if self.stats.heart_color == 'red':
                        self.heart.blitred()
                    if self.stats.heart_color == 'blue':
                        self.heart.blitblue()

            elif self.stats.turn == 'black_out':
                if self.stats.sans_amount == 76:
                    self.heart.heart_direction = 'right'
                    self.slam.slam = 'right'
                    self.heart.x = self.battle.rect.right
                    self.heart.x2 = self.battle.rect.right
                    self.heart.x3 = self.battle.rect.right
                    self.heart.x4 = self.battle.rect.right
                    self.heart.x5 = self.battle.rect.right
                if self.stats.sans_amount == 79:
                    if self.blaster_created is False:
                        self.create_just_right_gasterblaster_c()
                        self.create_just_top_gasterblaster_c()
                        self.create_just_left_gasterblaster_c()
                        self.create_just_bottom_gasterblaster_c()
                        self.blaster_created = True
                    self.heart.heart_direction = 'down'
                    self.slam.slam = 'up'
                    self.heart.y = self.battle.rect.top
                    self.heart.y2 = self.battle.rect.top
                    self.heart.y3 = self.battle.rect.top
                    self.heart.y4 = self.battle.rect.top
                    self.heart.y5 = self.battle.rect.top
                    self.heart.heart_direction = 'right'
                    self.slam.slam = 'right'
                    self.heart.x = self.battle.rect.right
                    self.heart.x2 = self.battle.rect.right
                    self.heart.x3 = self.battle.rect.right
                    self.heart.x4 = self.battle.rect.right
                    self.heart.x5 = self.battle.rect.right
                if self.stats.sans_amount == 80:
                    if self.blaster_created is False:
                        self.create_up_down_blasters_c()
                        self.blaster_created = True
                    self.heart.heart_direction = 'up'
                    self.slam.slam = 'down'
                    self.heart.y = self.battle.rect.bottom
                    self.heart.y2 = self.battle.rect.bottom
                    self.heart.y3 = self.battle.rect.bottom
                    self.heart.y4 = self.battle.rect.bottom
                    self.heart.y5 = self.battle.rect.bottom
                if self.stats.sans_amount == 81:
                    if self.blaster_created is False:
                        self.create_just_bottom_gasterblaster_c()
                        self.create_just_top_gasterblaster_c()
                        self.create_just_left_gasterblaster_c()
                        self.blaster_created = True
                    self.heart.heart_direction = 'left'
                    self.slam.slam = 'left'
                    self.heart.x = self.battle.rect.left
                    self.heart.x2 = self.battle.rect.left
                    self.heart.x3 = self.battle.rect.left
                    self.heart.x4 = self.battle.rect.left
                    self.heart.x5 = self.battle.rect.left
                    self.heart.y = self.battle.rect.centery
                    self.heart.y2 = self.battle.rect.centery
                    self.heart.y3 = self.battle.rect.centery
                    self.heart.y4 = self.battle.rect.centery
                    self.heart.y5 = self.battle.rect.centery
                if self.stats.sans_amount == 82:
                    if self.blaster_created is False:
                        self.create_just_top_gasterblaster_c()
                        self.blaster_created = True
                    self.heart.heart_direction = 'down'
                    self.slam.slam = 'up'
                    self.heart.y = self.battle.rect.top
                    self.heart.y2 = self.battle.rect.top
                    self.heart.y3 = self.battle.rect.top
                    self.heart.y4 = self.battle.rect.top
                    self.heart.y5 = self.battle.rect.top
                    self.heart.x = self.battle.rect.centerx
                    self.heart.x2 = self.battle.rect.centerx
                    self.heart.x3 = self.battle.rect.centerx
                    self.heart.x4 = self.battle.rect.centerx
                    self.heart.x5 = self.battle.rect.centerx
                if self.stats.sans_amount == 83:
                    if self.blaster_created is False:
                        self.create_just_bottom_gasterblaster_c()
                        self.blaster_created = True
                    self.heart.heart_direction = 'up'
                    self.slam.slam = 'down'
                    self.heart.y = self.battle.rect.bottom
                    self.heart.y2 = self.battle.rect.bottom
                    self.heart.y3 = self.battle.rect.bottom
                    self.heart.y4 = self.battle.rect.bottom
                    self.heart.y5 = self.battle.rect.bottom
                    self.heart.x = self.battle.rect.centerx
                    self.heart.x2 = self.battle.rect.centerx
                    self.heart.x3 = self.battle.rect.centerx
                    self.heart.x4 = self.battle.rect.centerx
                    self.heart.x5 = self.battle.rect.centerx
                if self.last_time13 is None:
                    self.last_time13 = time()
                if time() - self.last_time13 >= 1.5:
                    self.stats.sans_amount += 1
                    self.stats.turn = 'sans turn'
                    self.last_time13 = None

            elif self.stats.turn == 'black_out2':
                self.heart.heart_direction = 'down'
                self.slam.slam = 'up'
                self.heart.y = self.battle.rect.top
                self.heart.y2 = self.battle.rect.top
                self.heart.y3 = self.battle.rect.top
                self.heart.y4 = self.battle.rect.top
                self.heart.y5 = self.battle.rect.top
                self.heart.x = self.battle.rect.centerx
                self.heart.x2 = self.battle.rect.centerx
                self.heart.x3 = self.battle.rect.centerx
                self.heart.x4 = self.battle.rect.centerx
                self.heart.x5 = self.battle.rect.centerx
                if self.last_time13 is None:
                    self.last_time13 = time()
                if time() - self.last_time13 >= 0.9:
                    self.stats.sans_amount += 1
                    self.stats.turn = 'sans turn'
                    self.last_time13 = None

            elif self.stats.turn == 'black_out3':
                self.heart.heart_direction = 'left'
                self.slam.slam = 'left'
                self.heart.x = self.battle.rect.left
                self.heart.x2 = self.battle.rect.left
                self.heart.x3 = self.battle.rect.left
                self.heart.x4 = self.battle.rect.left
                self.heart.x5 = self.battle.rect.left
                self.heart.y = self.battle.rect.centery
                self.heart.y2 = self.battle.rect.centery
                self.heart.y3 = self.battle.rect.centery
                self.heart.y4 = self.battle.rect.centery
                self.heart.y5 = self.battle.rect.centery
                if self.last_time13 is None:
                    mixer.music.set_volume(4)
                    self.last_time13 = time()
                if time() - self.last_time13 >= 0.7:
                    self.stats.sans_amount += 1
                    self.stats.turn = 'sans turn'
                    self.last_time13 = None

            elif self.stats.turn == 'black_out4':
                self.heart.heart_direction = 'right'
                self.slam.slam = 'right'
                self.heart.x = self.battle.rect.right
                self.heart.x2 = self.battle.rect.right
                self.heart.x3 = self.battle.rect.right
                self.heart.x4 = self.battle.rect.right
                self.heart.x5 = self.battle.rect.right
                self.heart.y = self.battle.rect.centery
                self.heart.y2 = self.battle.rect.centery
                self.heart.y3 = self.battle.rect.centery
                self.heart.y4 = self.battle.rect.centery
                self.heart.y5 = self.battle.rect.centery
                if self.last_time13 is None:
                    mixer.music.set_volume(3)
                    self.last_time13 = time()
                if time() - self.last_time13 >= 0.45:
                    self.stats.sans_amount += 1
                    self.stats.turn = 'sans turn'
                    self.last_time13 = None

            elif self.stats.turn == 'black_out5':
                self.heart.heart_direction = 'down'
                self.slam.slam = 'up'
                self.heart.y = self.battle.rect.top
                self.heart.y2 = self.battle.rect.top
                self.heart.y3 = self.battle.rect.top
                self.heart.y4 = self.battle.rect.top
                self.heart.y5 = self.battle.rect.top
                self.heart.x = self.battle.rect.centerx
                self.heart.x2 = self.battle.rect.centerx
                self.heart.x3 = self.battle.rect.centerx
                self.heart.x4 = self.battle.rect.centerx
                self.heart.x5 = self.battle.rect.centerx
                if self.last_time13 is None:
                    mixer.music.set_volume(2)
                    self.last_time13 = time()
                if time() - self.last_time13 >= 0.2:
                    self.stats.sans_amount += 1
                    self.stats.turn = 'sans turn'
                    self.last_time13 = None

            elif self.stats.turn == 'black_out6':
                self.heart.heart_direction = 'up'
                self.slam.slam = 'down'
                self.heart.y = self.battle.rect.bottom
                self.heart.y2 = self.battle.rect.bottom
                self.heart.y3 = self.battle.rect.bottom
                self.heart.y4 = self.battle.rect.bottom
                self.heart.y5 = self.battle.rect.bottom
                self.heart.x = self.battle.rect.centerx
                self.heart.x2 = self.battle.rect.centerx
                self.heart.x3 = self.battle.rect.centerx
                self.heart.x4 = self.battle.rect.centerx
                self.heart.x5 = self.battle.rect.centerx
                if self.last_time13 is None:
                    mixer.music.set_volume(1)
                    self.last_time13 = time()
                if time() - self.last_time13 >= 0.15:
                    self.stats.turn = 'sans turn'
                    self.last_time13 = None

            elif self.stats.turn == 'black_out7':
                if self.last_time13 is None:
                    self.wrote = False
                    mixer.music.set_volume(0)
                    self.last_time13 = time()
                if time() - self.last_time13 >= 2:
                    self.stats.change_dia()
                    self.stats.sans_amount += 1
                    self.heart.reset_pos()
                    self.stats.heart_color = 'red'
                    self.stats.turn = 'speech turn'
                    self.last_time13 = None
                    self.last_time = None
                    self.last_time2 = None
                    self.last_time3 = None
                    self.last_time4 = None
                    self.last_time5 = None
                    self.last_time6 = None
                    self.last_time7 = None
                    self.last_time8 = None
                    mixer.music.stop()
                    self.repeat = 0

        elif self.stats.active == False:
            if self.title.title_image_rect.y <= 60 and self.title.title2_image_rect.y <= self.title.title_image_rect.bottom + 10 and self.start.moved:
                if self.data[1] == 'never_beat_the_game':
                    self.bgsans.draw_him()
                elif self.data[1] == 'beat_the_game':
                    self.bgsans.show_background_sans_saved()
            self.animate_title()
            if self.title.title_image_rect.y <= 60:
                self.animate_title2()
                if self.title.title2_image_rect.y <= self.title.title_image_rect.bottom + 10 and not self.start.visibility:
                    sleep(1)
                    self.start.draw_start_button()
                if self.start.visibility:
                    self.start.draw_start_button()
                    self.start.move_title()
            if self.bgsans.visability:
                self.bgheart.draw_bg_heart()
                self.begin = True

        elif self.stats.active == 'instruction':
            if self.last_time is None:
                self.last_time = time()
            if time() - self.last_time >= 0.75:
                self.instruc.show_instruc1()
                if self.last_time2 is None:
                    self.last_time2 = time()
                if time() - self.last_time2 >= 1.65:
                    self.instruc.show_instruc2()
                    if self.last_time3 is None:
                        self.last_time3 = time()
                    if time() - self.last_time3 >= 1.65:
                        self.instruc.show_instruc3()
                        if self.last_time4 is None:
                            self.last_time4 = time()
                        if time() - self.last_time4 >= 1.65:
                            self.instruc.show_instruc4()
                            if self.last_time5 is None:
                                self.last_time5 = time()
                            if time() - self.last_time5 >= 1.65:
                                self.instruc.show_instruc5()
                                if self.last_time6 is None:
                                    self.last_time6 = time()
                                if time() - self.last_time6 >= 1.65:
                                    self.instruc.show_instruc6()
                                    if self.last_time7 is None:
                                        self.last_time7 = time()
                                    if time() - self.last_time7 >= 1.65:
                                        self.instruc.show_instruc7()
                                        if self.last_time8 is None:
                                            self.last_time8 = time()
                                        if time() - self.last_time8 >= 1.65:
                                            self.instruc.show_instruc8()
                                            if self.last_time9 is None:
                                                self.last_time9 = time()
                                            if time() - self.last_time9 >= 1.65:
                                                self.instruc.show_instruc9()
                                                if self.last_time10 is None:
                                                    self.last_time10 = time()
                                                if time() - self.last_time10 >= 1.65:
                                                    self.instruc.show_instruc10()
                                                    if self.last_time11 is None:
                                                        self.last_time11 = time()
                                                    if time() - self.last_time11 >= 1.65:
                                                        self.instruc.show_instruc11()
                                                        if self.last_time12 is None:
                                                            self.last_time12 = time()
                                                        if time() - self.last_time12 >= 5:
                                                            self.instruc.show_continue_prompt()

        elif self.stats.active == 'credits':
            if self.wrote is False:
                with open('data/data.txt', 'r') as file:
                    lines = file.read()
                    lines = lines.split(' ')
                    del lines[1]
                    lines.insert(1, ' beat_the_game')

                with open('data/data.txt', 'w') as d:
                    for line in lines:
                        d.write(line)
                self.wrote = True
            self.credit.show_all_credit_lines()
            if self.last_time is None:
                self.last_time = time()
            if time() - self.last_time >= 1.25:
                self.title.draw_title()
                if self.last_time2 is None:
                    self.last_time2 = time()
                if time() - self.last_time2 >= 1:
                    if self.title.title_image_rect.bottom >= self.title.title2_image_rect.top - 10 and self.last_time3 is None:
                        if self.stats.sans_amount == 90:
                            self.stats.sans_amount += 1
                        self.title.animate_title()
                    else:
                        self.title.draw_title2()
                        if self.last_time3 is None:
                            self.last_time3 = time()
                        if time() - self.last_time3 >= 1:
                            if self.title.title_image_rect.bottom >= self.title.title2_image_rect.top - 10:
                                self.title.animate_title()
                            if self.title.title2_image_rect.bottom >= self.title.credit_rect.top - 55:
                                self.title.animate_title2()
                            else:
                                self.title.show_credit()
                                if self.last_time4 is None:
                                    self.last_time4 = time()
                                if time() - self.last_time4 >= 1.5:
                                    if self.credit.saved_sans_rect.centery >= self.screen_rect.centery - 90:
                                        self.title.slow_up_titles()
                                        self.credit.move_all_lines_up()

        pygame.display.flip()

UF = UnderFell()
UF.run_game()
