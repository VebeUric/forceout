from GUI import Surrounded, Animation
from Engine_g import Player, GameObject
import pygame
from manager_Tools import Text
from DataBaseController import DataBaseController

anim = Animation()


class Hub:
    def __init__(self, screen, game_controller):
        self.text_count_of_money = None
        self.screen = screen
        self.account = DataBaseController('data/Db.db')

        self.game_controller = game_controller
        self.anim = Animation()
        self.level_menu_is_active = False
        self.player = Player(80, 'data/Sprites/main_character_sprite/hesh',
                             'Sprites/main_character_sprite/Fire_player_sprite.png',
                             'Sprites/main_character_sprite/hesh/frame_0_0.png')
        self.hub_sur = Surrounded(anim, screen, 'Surrounded/hub.png', 1, False)
        # self.wall_one = GameObject(0, 286, 600, 200, self.screen)
        self.home = GameObject(0, 0, 250, 280, self.screen, self.hub_sur, 'Surrounded/home.png')
        self.trade = GameObject(350, 150, 100, 100, self.screen, self.hub_sur, 'Surrounded/trade.png')
        self.kuzn = GameObject(600, 0, 250, 150, self.screen, self.hub_sur, 'Surrounded/kuzn.png')
        self.obj_list = [self.kuzn, self.home]

        self.count_of_money = self.account.get_account(1)
        self.money_icon = GameObject(0, 0, 50, 50, self.screen, self.hub_sur, 'buttons/money.png')

        self.player.respawn(400, 400)

    def update(self, event, keys):
        self.count_of_money = self.account.get_account(1)
        self.text_count_of_money = Text(str(self.count_of_money), 25, (255, 255, 255), 90, 40)

        if self.player.rect.x <= 0:
            self.player.m_l_d = False
        elif self.player.rect.x >= 1280 - 27:
            self.player.m_s_d = False
        if self.player.rect.y <= 0:
            self.player.m_r_d = False
        elif self.player.rect.y >= 1280 - 660:
            self.player.m_b_d = False
        # self.wall_one.check_colision(self.player)
        self.home.check_colision(self.player)
        self.trade.check_colision(self.player)
        self.kuzn.check_colision(self.player)
        # self.home.update()
        self.player.update(self.screen, keys, event)

    def draw(self, keys, event):
        self.hub_sur.draw()
        self.home.draw()
        self.kuzn.draw()
        self.trade.draw()
        self.player.draw(self.screen)

        self.text_count_of_money.draw(self.screen)
        self.money_icon.draw()

        for obj in self.obj_list:
            if obj.is_colide:
                obj.get_image()
                if keys[pygame.K_e]:
                    if obj == self.home:
                        self.game_controller.levels_menu(event)
                    elif obj == self.kuzn:
                        self.game_controller.trade()

    def chech_shop_orange(self):
        pass

    def blacksmith(self):
        pass

    def choice_level(self):
        pass
