import pygame
import sys
import os
import math
from GUI import Animation
from random import randint

player_animation = {
    'walk': ('Sprites/main_character_sprite/hesh/frame_2_0.png', 32, 113, 45, 7),
    'run': ('Sprites/main_character_sprite/hesh/frame_1_0.png',),
    'idle': ('Sprites/main_character_sprite/hesh/frame_0_0.png', 27, 117, 45, 7),
    'up_corner_attack': ('Sprites/main_character_sprite/hesh/frame_9_0.png',),
    'up_down_attack': ('Sprites/main_character_sprite/hesh/frame_11_0.png',),
    'low_attack': ('Sprites/main_character_sprite/hesh/frame_16_0.png', 75, 65, 30, 5),
    'death': ('Sprites/main_character_sprite/hesh/frame_24_0.png', 44, 96, 46, 11)

}
close_type_animation = {
    'idle': ('Sprites/CloseTypeEnemy/hesh/frame_0_0.png', 35, 45, 29, 8),
    'walk': ('Sprites/CloseTypeEnemy/hesh/frame_1_0.png', 36, 43, 27, 5),
    'attack': ('Sprites/CloseTypeEnemy/hesh/frame_2_0.png', 45, 35, 50, 12),
    'damadge': ('Sprites/CloseTypeEnemy/hesh/frame_3_0.png', 32, 45, 32, 5),
    'death': ('Sprites/CloseTypeEnemy/frame_0_0.png',)

}

health_bar = {
    'full': 'health_indicators/full.png',
    'step_one': 'health_indicators/step_one.png',
    'step_two': 'health_indicators/step_two.png',
    'step_three': 'health_indicators/step_three.png',
    'step_four': 'health_indicators/step_four.png',
    'null': 'health_indicators/null.png'

}

anim = Animation()


class Player(pygame.sprite.Sprite):
    def __init__(self, mass, size, character_folder_path, x_pose=0, y_pose=0, v=120, fps=60, health=100, armore=100):
        super().__init__()
        self.image = None
        self.health_rect = None
        self.healt_image = None
        self.armore = armore
        self.health = health
        self.start_health = health
        self.is_pressed_shift = None
        self.mass = mass
        self.size = size
        self.x_pose = x_pose
        self.y_pose = y_pose
        self.fps = fps
        self.v = 620
        self.attac = None
        self.m_l_d = True
        self.m_b_d = True
        self.m_r_d = True
        self.m_s_d = True
        self.time_attac = 0
        self.move_again = None
        self.frames = None
        self.scroll_box = pygame.Rect(83, 65, 400, 500)
        self.sprite_width = 27  # Ширина каждого кадра
        self.sprite_height = 60  # Высота каждого кадра
        self.animation_speed = 10
        self.animation_index = 0
        self.controller_hp()
        self.rect = anim.load_image('Sprites/main_character_sprite/hesh/origin.png').get_rect()

        # self.rect = anim.load_image('Sprites/main_character_sprite/hesh/frame_0_0.png').get_rect()
        self.respawn(100, 100)
        if not (os.path.exists(character_folder_path) and os.path.isdir(character_folder_path)):
            anim.split_image('data/Sprites/main_character_sprite/Fire_player_sprite.png', character_folder_path, 25, 1)
        self.idle()

    def get_damage(self, damage):
        self.health -= damage

    def low_attack(self):
        self.attac = True
        if self.time_attac == 90:
            self.time_attac = 0
            self.attac = False
        self.rect.width, self.rect.height = 76, 31
        low_attack = player_animation['low_attack']
        player_sprite_sheet = anim.load_image(low_attack[0])
        self.frames = anim.prepear_frames(70, 30, player_sprite_sheet, low_attack[2], low_attack[4])

    def controller_hp(self):
        zoom_level = 0.4
        if self.start_health * 0.8 <= self.health <= self.start_health:
            health_sprite = health_bar['full']
        elif self.start_health * 0.6 <= self.health <= self.start_health * 0.8:
            health_sprite = health_bar['step_one']
        elif self.start_health * 0.4 <= self.health <= self.start_health * 0.6:
            health_sprite = health_bar['step_two']
        elif self.health >= self.start_health * 0.2 and self.health <= self.start_health * 0.4:
            health_sprite = health_bar['step_three']
        elif self.start_health * 0.1 <= self.health <= self.start_health * 0.2:
            health_sprite = health_bar['step_four']
        else:
            health_sprite = health_bar['null']

        self.health_rect = anim.load_alpha_image(health_sprite)
        self.health_rect = pygame.transform.scale(self.health_rect, (
            int(self.health_rect.get_width() * zoom_level), int(self.health_rect.get_height() * zoom_level)))
        self.healt_image = pygame.Rect(1000, 500, 193.6, 48.4)

    def check_death(self):
        if self.health <= 0:
            self.is_alive = False
        if not self.is_alive:
            death = player_animation['death']
            player_sprite_sheet = anim.load_image(death[0])
            self.frames = anim.prepear_frames(44, 46, player_sprite_sheet, death[2], death[4])

    def idle(self):
        self.clear_frames()
        idle = player_animation['idle']
        player_sprite_sheet = anim.load_image(idle[0])
        self.frames = anim.prepear_frames(self.sprite_width, self.sprite_height, player_sprite_sheet, idle[2], idle[4])

    def draw(self, screen):
        zoom_level = 2
        screen.blit(self.health_rect, self.healt_image.topleft)
        self.image = pygame.transform.scale(self.image, (
            int(self.image.get_width() * zoom_level), int(self.image.get_height() * zoom_level)))
        screen.blit(self.image, self.rect.topleft)

    def update(self, screen, keys, event):
        if self.attac:
            self.time_attac += 1
        else:
            self.time_attac = 0
        if self.is_alive:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.is_pressed_shift = True
            else:
                self.is_pressed_shift = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(3333333333344444444444444444444444)
                self.low_attack()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.move_left()
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.move_stright()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.move_right()
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.move_back()
            if self.is_alive and not (
                    keys[pygame.K_s] or keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_a] or keys[
                pygame.K_LEFT] or event.type == pygame.MOUSEBUTTONDOWN):
                self.idle()

            if self.is_pressed_shift:
                self.speed_up()
            else:
                self.speed_down()

        self.radius = 5
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius)

        self.scroll_box.center = self.rect.center
        if self.frames:
            self.animation_index += 1
            if self.animation_index >= len(self.frames):
                self.animation_index = 0
            if not self.move_again:
                self.image = self.frames[int(self.animation_index)]
            else:
                self.image = pygame.transform.flip(self.frames[int(self.animation_index)], -1, False)

    def scroll_screen(self, screen, sur, enemy_squad):
        if self.scroll_box.left < screen.get_rect().left and sur.x != - 100:
            sur.move_left()
            print('move_left')
            self.m_l_d = True
            self.rect.x += self.v / self.fps
            for i in enemy_squad:
                i.rect.x += self.v / self.fps
        elif self.scroll_box.right > screen.get_rect().right and sur.x != -2140:
            sur.move_right()
            self.m_s_d = True
            self.rect.x -= self.v / self.fps
            for i in enemy_squad:
                i.rect.x -= self.v / self.fps
        elif sur.x == - 100:
            self.m_l_d = False
        elif sur.x == -2140:
            self.m_s_d = False
            self.rect.x -= self.v / self.fps
        if self.scroll_box.top < screen.get_rect().top and sur.y != -910:
            self.m_r_d = True
            sur.move_up()
            self.rect.y += self.v / self.fps
            for i in enemy_squad:
                i.rect.y += self.v / self.fps
        elif self.scroll_box.bottom > screen.get_rect().bottom and sur.y != -1690:
            sur.move_down()
            self.m_b_d = False
            self.rect.y -= self.v / self.fps
            for i in enemy_squad:
                i.rect.y -= self.v / self.fps
        elif sur.y == -910:
            self.m_r_d = False
        elif sur.y == -1690:
            self.m_b_d = False

    def clear_frames(self):
        self.move_again = None
        self.image = None
        self.animation_index = 0

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def respawn(self, x_pose, y_pose):
        self.rect.x = x_pose
        self.rect.y = y_pose

    def move_right(self):
        if self.m_r_d:
            walk = player_animation['walk']
            player_sprite_sheet = anim.load_image(walk[0])
            self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
            self.rect.y -= self.v / self.fps
        self.m_r_d = True

    def move_back(self):
        if self.m_b_d:
            walk = player_animation['walk']
            player_sprite_sheet = anim.load_image(walk[0])
            self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
            self.rect.y += self.v / self.fps
        self.m_b_d = True

    def move_left(self):
        if self.m_l_d:
            self.move_again = True
            walk = player_animation['walk']
            player_sprite_sheet = anim.load_image(walk[0])
            self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
            self.rect.x -= self.v / self.fps
        self.m_l_d = True

    def move_stright(self):
        if self.m_s_d:
            self.move_again = None
            walk = player_animation['walk']
            player_sprite_sheet = anim.load_image(walk[0])
            self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
            self.rect.x += self.v / self.fps
        self.m_s_d = True

    def press_shift(self):
        self.is_pressed_shift = True

    def not_press_shift(self):
        self.is_pressed_shift = False

    def speed_up(self):
        if self.v != 700:
            self.v += 10

    def speed_down(self):
        if self.v != 620:
            self.v -= 10


class EnemyCloseType:
    def __init__(self, mass, size, character_folder_path, x_pose=0, y_pose=0, v=120, fps=60, health=100, armore=100):
        super().__init__()
        self.image = None
        self.v = v
        self.armore = armore
        self.health = health
        self.is_pressed_shift = None
        self.mass = mass
        self.size = size
        self.x_pose = x_pose
        self.y_pose = y_pose
        self.get_damage_fl = False
        self.get_time_damage = 0
        self.fps = fps
        self.move_again = None
        self.v = 90
        self.anim_count = 0
        self.stop = False
        self.nonattack = None
        self.time_after_attack = 60
        self.rect = anim.load_image('Sprites/CloseTypeEnemy/hesh/frame_0_0.png').get_rect()
        self.frames = None
        self.sprite_width = 27  # Ширина каждого кадра
        self.sprite_height = 70  # Высота каждого кадра
        self.animation_speed = 10  # Скорость смены кадров
        self.animation_index = 0
        if not (os.path.exists(character_folder_path) and os.path.isdir(character_folder_path)):
            anim.split_image('data/Sprites/CloseTypeEnemy/NightBorne.png', character_folder_path, 5, 1)
        self.idle()

    def respawn(self, x_pose, y_pose):
        self.rect.x = x_pose
        self.rect.y = y_pose

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def attack(self):
        pass

    def idle(self):
        self.clear_frames()
        idle = close_type_animation['idle']
        player_sprite_sheet = anim.load_image(idle[0])
        self.frames = anim.prepear_frames(idle[1], idle[3], player_sprite_sheet, idle[2], idle[4])
        self.transverse_frames = anim.prepear_trans_frames(idle[1], idle[3], player_sprite_sheet, idle[2], idle[4])

    def draw(self, screen):
        zoom_level = 3.5

        self.image = pygame.transform.scale(self.image, (
            int(self.image.get_width() * zoom_level), int(self.image.get_height() * zoom_level)))
        screen.blit(self.image, self.rect.topleft)

    def update(self, screen, player_rect_x, player_rect_y):
        if self.get_damage_fl:
            self.get_time_damage += 1
        if self.get_time_damage == 5:
            self.get_damage_fl = False
            self.get_time_damage = 0
            self.idle()
        self.time_after_attack += 1
        if self.stop:
            if self.anim_count == 12:
                self.stop = False
                self.anim_count = 0
        if self.frames:
            self.animation_index += 1
            if self.animation_index >= len(self.frames):
                self.animation_index = 0
            if not self.move_again:
                self.image = self.frames[int(self.animation_index)]
            else:
                self.image = pygame.transform.flip(self.frames[int(self.animation_index)], -1, False)
        if self.stop:
            self.anim_count += 1

    def clear_frames(self):
        self.image = None
        self.animation_index = 0

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def respawn(self, x_pose, y_pose):
        self.rect.x = x_pose
        self.rect.y = y_pose

    def move_right(self):
        if not self.stop:
            walk = close_type_animation['walk']
            player_sprite_sheet = anim.load_image(walk[0])
            self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
            self.rect.y -= self.v / self.fps

    def move_back(self):
        if not self.stop:
            walk = close_type_animation['walk']
            player_sprite_sheet = anim.load_image(walk[0])
            self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
            self.rect.y += self.v / self.fps

    def move_left(self):
        if not self.stop:
            self.move_again = True
            walk = close_type_animation['walk']
            player_sprite_sheet = anim.load_image(walk[0])
            self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
            self.rect.x -= self.v / self.fps

    def move_stright(self):
        if not self.stop:
            self.move_again = None
            walk = close_type_animation['walk']
            player_sprite_sheet = anim.load_image(walk[0])
            self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
            self.rect.x += self.v / self.fps

    def check_intersection(self, player_pose_x, player_pose_y):
        # self.image = pygame.Surface((50, 50))
        # pygame.draw.circle(self.image, (255, 0, 0, 128), (25, 25), 25)
        # self.rect = self.image.get_rect(center=(self.player_rect.x, self.player_rect.y))
        # self.transparent_circle_rect = self.image.get_rect(center=(self.player_rect.x, self.player_rect.y))
        # self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        # pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)
        # self.rect = self.image.get_rect(center=(x, y))
        # self.mask = pygame.mask.from_surface(self.image)
        # if pygame.sprite.collide_mask(self.rect, mask):
        #     return True
        # else:
        return False

    def strive_to_player(self, player_pose_x, player_pose_y, all_enemies, player):
        if not self.stop:
            self.avoid_enemies(all_enemies)
            if self.rect.x > player_pose_x:
                self.move_left()
            elif self.rect.x < player_pose_x:
                self.move_stright()

            if self.rect.y < player_pose_y:
                self.move_back()
            elif self.rect.y > player_pose_y:
                self.move_right()
        else:
            self.attack(player)

    def avoid_enemies(self, all_enemies):
        for enemy in all_enemies:
            if enemy != self:
                dx = enemy.rect.x - self.rect.x
                dy = enemy.rect.y - self.rect.y
                distance = math.sqrt(dx ** 2 + dy ** 2)
                if distance < 60:
                    angle = math.atan2(dy, dx)
                    self.rect.x -= math.cos(angle) * 2
                    self.rect.y -= math.sin(angle) * 2

    def get_damage(self, damage):
        self.get_damag_fl = True
        self.health -= damage
        get_damage = close_type_animation['damadge']
        player_sprite_sheet = anim.load_image(get_damage[0])
        self.frames = anim.prepear_frames(get_damage[1], get_damage[3], player_sprite_sheet, get_damage[2],
                                          get_damage[4])

    def check_death(self):
        if self.health <= 0:
            self.is_alive = False
            self.death()

    def death(self):
        self.rect.x = -1000
        self.rect.y = -1000

    def attack(self, player):
        self.stop = True
        print(self.time_after_attack)
        if self.time_after_attack % 120 == 0:
            player.get_damage(10)
            self.time_after_attack = 0
            attack = close_type_animation['attack']
            player_sprite_sheet = anim.load_image(attack[0])
            self.frames = anim.prepear_frames(attack[1], attack[3], player_sprite_sheet, attack[2], attack[4])

    def enemy_spawn(self):
        pass


class EnemyFurtherType:
    pass


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, hieght, screen, sur, image=None):
        super().__init__()
        self.have_image = None
        self.screen = screen
        self.sur = sur
        self.RED = (0, 0, 0)
        self.is_colide = None
        if image:
            self.rect = anim.load_image(image).get_rect()
            self.curcle = pygame.sprite.Sprite()
            self.rect.width = width
            self.rect.height = hieght
            self.image = anim.load_alpha_image(image)
            self.image = self.image = pygame.transform.scale(self.image,
                                                             (self.rect.width * 1.2, self.rect.height * 1.2))
            self.have_image = True
        else:
            self.image = pygame.Surface((width, hieght), pygame.SRCALPHA)
            self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.hieght = hieght
        self.circle = Circle_spr(self, x, y)

    def get_image(self):
        self.rect_e = anim.load_image('buttons/e.png').get_rect()
        self.rect_e.center = self.rect.center
        self.screen.blit(anim.load_image('buttons/e.png'), self.rect.center)

    def update(self):
        self.circle.update()
        if self.sur.current_scroll == 'up':
            self.rect.y = self.rect.y - 15
            self.sur.current_scroll = None
        elif self.sur.current_scroll == 'down':
            self.rect.y = self.rect.y + 15
            self.sur.current_scroll = None

        if self.sur.current_scroll == 'left':
            self.rect.x = self.rect.x - 15
            self.sur.current_scroll = None
        elif self.sur.current_scroll == 'right':
            self.rect.x = self.rect.x + 15
            self.sur.current_scroll = None

    def check_colision(self, player):
        if pygame.sprite.collide_rect(player, self):
            self.is_colide = True
            if self.rect.y <= player.rect.y:
                player.m_r_d = False
                # player.rect.y += 5
            elif self.rect.y <= player.rect.y:
                player.m_b_d = False
                # player.rect.y -= 5
            if self.rect.x <= player.rect.x:
                player.m_l_d = False
                # player.rect.x += 5
            elif self.rect.x >= player.rect.x:
                player.m_s_d = False
                # player.rect.x -= 5
        else:
            self.is_colide = False

    def draw(self):

        self.circle.draw()
        if not self.have_image:
            pygame.draw.rect(self.image, self.RED, (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


class Circle_spr(pygame.sprite.Sprite):
    def __init__(self, obj, x, y):
        self.radius = 250
        self.color = (0, 0, 0)
        self.x = x
        self.y = y
        self.obj = obj
        self.image_c = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image_c, (0, 0, 0), (self.radius, self.radius), self.radius)
        self.rect = self.image_c.get_rect()

    def draw(self):
        pygame.draw.circle(self.image_c, (0, 0, 0), (self.x, self.y), self.radius)

    def update(self):
        self.rect.center = self.obj.rect.center
