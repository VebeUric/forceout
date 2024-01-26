import pygame
from Engine_g import Player, EnemyCloseType
from GUI import Surrounded, Animation
from random import randint
from manager_Tools import Button, Text
from DataBaseController import DataBaseController

nim = Animation()


class Level:
    def __init__(self, screen):
        self.text_count_of_money = None
        self.text_count_of_money = None
        self.menu_background = None
        self.mode = None
        self.game = True
        self.get_money_flag = True
        self.account = DataBaseController('data/Db.db')
        self.enemycloseSquad = pygame.sprite.Group()
        self.player = Player(80, 'data/Sprites/main_character_sprite/hesh',
                             'Sprites/main_character_sprite/Fire_player_sprite.png',
                             'Sprites/main_character_sprite/hesh/frame_0_0.png')
        self.sur = Surrounded(nim, screen, 'Surrounded/surbub.png')
        self.sur.x, self.sur.y = -100, -1390
        self.player.rect.x, self.player.rect.y = 100, 250
        self.screen = screen
        self.flag = True

    def game_controller(self, mode):
        self.mode = mode

    def prepeare_enemy_squad(self):
        player_coords = (self.player.rect.x, self.player.rect.y)
        for i in range(10):
            some_x_y = (randint(player_coords[0] - 900, player_coords[0] + 900),
                        randint(player_coords[1] - 900, player_coords[1] + 900))
            enemyclose = EnemyCloseType(80, (30, 50), 'data/Sprites/CloseTypeEnemy/hesh')
            enemyclose.respawn(some_x_y[0], some_x_y[1])
            self.enemycloseSquad.add_internal(enemyclose)
            self.enemycloseSquad.add(enemyclose)
            self.flag = False

    def clear_level(self):
        self.mode = None
        print('cleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeem')
        self.player.health = 100
        self.player.is_alive = True
        self.sur.x, self.sur.y = -100, -1390
        self.player.rect.x, self.player.rect.y = 100, 250
        player_coords = (self.player.rect.x, self.player.rect.y)
        for i in self.enemycloseSquad:
            i.is_alive = True
            i.rect.x, i.rect.y = (randint(player_coords[0] - 900, player_coords[0] + 900),
                                  randint(player_coords[1] - 900, player_coords[1] + 900))
            i.health = 100

    def update(self):
        if self.flag:
            self.prepeare_enemy_squad()
        if not self.screen.get_rect().contains(self.player.scroll_box):
            self.player.scroll_screen(self.screen, self.sur, self.enemycloseSquad)

        for i in self.enemycloseSquad:
            if pygame.sprite.collide_rect(self.player, i):
                if self.player.attac:
                    print(self.player.attac)
                    i.get_damage(20)
                self.player.attac = False
                i.attack(self.player)

    def draw(self, keys, event):
        global return_to_hub_button
        self.sur.draw()
        self.player.update(self.screen, keys, event)
        self.player.controller_hp()
        print(self.player.health)
        self.player.draw(self.screen)
        self.player.check_death()
        if not self.player.is_alive:
            self.menu_background = nim.load_image('buttons/death_background.png')
            self.screen.blit(self.menu_background, (500, 10))
            return_to_hub_button = Button('Вернуться в hub', lambda: self.game_controller('hub'),
                                          'data/buttons/not_pressed_two.png',
                                          'buttons/pressed.png')
            return_to_hub_button.replace((505, 110))
            return_to_hub_button.resize((500, 100))

            return_to_main_menu = Button('Вернуться в главное меню', lambda: self.game_controller('start_menu'),
                                         'data/buttons/not_pressed_two.png',
                                         'buttons/pressed.png')
            return_to_main_menu.replace((505, 240))
            return_to_main_menu.resize((500, 100))
            self.game = False
        for i in self.enemycloseSquad:
            i.check_death()
            if not i.is_alive:
                i.get_damage(0)
                i.death()
            i.strive_to_player(self.player.rect.x, self.player.rect.y, self.enemycloseSquad, self.player)
            i.update(self.screen, self.player.rect.x, self.player.rect.y)
            i.draw(self.screen)
        tmp = []
        for i in self.enemycloseSquad:
            if i.is_alive:
                tmp.append(1)

        if len(tmp) == 0:
            if self.get_money_flag:
                b_money = self.account.get_account(1)
                money = 100 + b_money
                self.account.add_money(1, money)
                self.get_money_flag = False
            self.menu_background = nim.load_image('buttons/win_background.png')
            self.screen.blit(self.menu_background, (500, 10))
            return_to_hub_button = Button('Вернуться в hub', lambda: self.game_controller('hub'),
                                          'data/buttons/not_pressed_two.png',
                                          'buttons/pressed.png')
            return_to_hub_button.replace((605, 310))
            return_to_hub_button.resize((500, 100))
            self.text_count_of_money = Text('Вы получили 100 монет', 25, (255, 255, 255), 605, 150)
            return_to_main_menu = Button('Вернуться в главное меню', lambda: self.game_controller('start_menu'),
                                         'data/buttons/not_pressed_two.png',
                                         'buttons/pressed.png')
            return_to_main_menu.replace((605, 440))
            return_to_main_menu.resize((500, 100))

        if not tmp:
            return_to_main_menu.update(event)
            return_to_hub_button.update(event)
            return_to_hub_button.render(self.screen)
            return_to_main_menu.render(self.screen)
            self.text_count_of_money.draw(self.screen)

        if not self.player.is_alive:
            return_to_main_menu.update(event)
            return_to_hub_button.update(event)
            return_to_hub_button.render(self.screen)
            return_to_main_menu.render(self.screen)
