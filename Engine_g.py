from game_state_manager import Settings
import pygame
import sys
import os
from GUI import Animation
from random import randint

player_animation = {
    'walk':('Sprites/main_character_sprite/hesh/frame_2_0.png', 32, 113, 45, 7),
    'run':('Sprites/main_character_sprite/hesh/frame_1_0.png', ),
    'idle':('Sprites/main_character_sprite/hesh/frame_0_0.png', 27, 117, 45, 7),
    'up_corner_attack':('Sprites/main_character_sprite/hesh/frame_9_0.png', ),
    'up_down_attack':('Sprites/main_character_sprite/hesh/frame_11_0.png', ),
    'low_attack':('Sprites/main_character_sprite/hesh/frame_16_0.png', )

}
close_type_animation = {
'idle':('Sprites/CloseTypeEnemy/hesh/frame_0_0.png', 35, 45, 29, 8),
    'walk':('Sprites/CloseTypeEnemy/hesh/frame_1_0.png',36, 43, 27, 5),
    'attack':('Sprites/CloseTypeEnemy/frame_0_0.png', ),
    'damadge':('Sprites/CloseTypeEnemy/frame_0_0.png', ),
    'death':('Sprites/CloseTypeEnemy/frame_0_0.png', )

}


anim= Animation()
class Player(pygame.sprite.Sprite):
    def __init__(self, mass, size,  character_folder_path, x_pose=0, y_pose=0, v=120, fps=60, health=100, armore=100):
        super().__init__()
        self.armore = armore
        self.health = health
        self.is_pressed_shift = None
        self.mass = mass
        self.size = size
        self.x_pose = x_pose
        self.y_pose = y_pose
        self.fps = fps
        self.v = 520
        self.move_again = None
        self.frames = None
        self.scroll_box = pygame.Rect(83, 65, 100, 100)
        self.sprite_width = 27 # Ширина каждого кадра
        self.sprite_height = 70 # Высота каждого кадра
        self.animation_speed = 10  # Скорость смены кадров
        self.animation_index = 0

        self.player_rect = anim.load_image('Sprites/main_character_sprite/hesh/frame_0_0.png').get_rect()
        self.respawn(100, 100)
        if not (os.path.exists(character_folder_path) and os.path.isdir(character_folder_path)):
            anim.split_image('data/Sprites/main_character_sprite/Fire_player_sprite.png', character_folder_path, 25, 1)
        self.idle()

    def idle(self):
        self.clear_frames()
        idle = player_animation['idle']
        player_sprite_sheet = anim.load_image(idle[0])
        self.frames = anim.prepear_frames(self.sprite_width, self.sprite_height, player_sprite_sheet, idle[2], idle[4])


    def draw(self, screen):
        screen.blit(self.image, self.player_rect.topleft)

    def update(self, screen):
        self.scroll_box.center = self.player_rect.center
        if self.frames:
            self.animation_index += 1
            if self.animation_index >= len(self.frames):
                self.animation_index = 0
            if not self.move_again:
                self.image = self.frames[int(self.animation_index)]
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image = pygame.transform.flip(self.frames[int(self.animation_index)], -1, False)
                self.mask = pygame.mask.from_surface(self.image)



    def scroll_screen(self):


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
        self.player_rect.x = x_pose
        self.player_rect.y = y_pose

    def move_right(self):
        walk = player_animation['walk']
        player_sprite_sheet = anim.load_image(walk[0])
        self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
        self.player_rect.y -= self.v / self.fps



    def move_back(self):
        walk = player_animation['walk']
        player_sprite_sheet = anim.load_image(walk[0])
        self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
        self.player_rect.y += self.v / self.fps


    def move_left(self):
        self.move_again = True
        walk = player_animation['walk']
        player_sprite_sheet = anim.load_image(walk[0])
        self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
        self.player_rect.x -= self.v / self.fps

    def move_stright(self):
        self.move_again = None
        walk = player_animation['walk']
        player_sprite_sheet = anim.load_image(walk[0])
        self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
        self.player_rect.x += self.v / self.fps


    def press_shift(self):
        self.is_pressed_shift = True

    def not_press_shift(self):
        self.is_pressed_shift = False

    def speed_up(self):
        if self.v != 600:
            self.v += 10

    def speed_down(self):
        if self.v != 560:
            self.v -= 10

class EnemyCloseType:
    def __init__(self, mass, size,  character_folder_path, x_pose=0, y_pose=0, v=120, fps=60, health=100, armore=100):
        super().__init__()
        self.armore = armore
        self.health = health
        self.is_pressed_shift = None
        self.mass = mass
        self.size = size
        self.x_pose = x_pose
        self.y_pose = y_pose
        self.fps = fps
        self.move_again = None
        self.v = 90
        self.frames = None
        self.sprite_width = 27 # Ширина каждого кадра
        self.sprite_height = 70 # Высота каждого кадра
        self.animation_speed = 10  # Скорость смены кадров
        self.animation_index = 0
        self.player_rect = anim.load_image('Sprites/CloseTypeEnemy/NightBorne.png').get_rect()
        self.respawn(50, 50)
        if not (os.path.exists(character_folder_path) and os.path.isdir(character_folder_path)):
            anim.split_image('data/Sprites/CloseTypeEnemy/NightBorne.png', character_folder_path, 5, 1)
        self.idle()


    def respawn(self, x_pose, y_pose):
        self.player_rect.x = x_pose
        self.player_rect.y = y_pose

    def draw(self, screen):
        screen.blit(self.image, self.player_rect.topleft)


    def attack(self):
        pass

    def idle(self):
        self.clear_frames()
        idle = close_type_animation['idle']
        player_sprite_sheet = anim.load_image(idle[0])
        self.frames = anim.prepear_frames(idle[1], idle[3], player_sprite_sheet, idle[2], idle[4])
        self.transverse_frames = anim.prepear_trans_frames(idle[1], idle[3], player_sprite_sheet, idle[2], idle[4])


    def draw(self, screen):
        screen.blit(self.image, self.player_rect.topleft)

    def update(self, screen, player_rect_x, player_rect_y):
        self.strive_to_player(player_rect_x, player_rect_y)
        if self.frames:
            self.animation_index += 1
            if self.animation_index >= len(self.frames):
                self.animation_index = 0
            if not self.move_again:
                self.image = self.transverse_frames[int(self.animation_index)]
            else:
                self.image = pygame.transform.flip(self.frames[int(self.animation_index)], -1, False)


    def clear_frames(self):
        self.image = None
        self.animation_index = 0

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def respawn(self, x_pose, y_pose):
        self.player_rect.x = x_pose
        self.player_rect.y = y_pose

    def move_right(self):
        walk = close_type_animation['walk']
        player_sprite_sheet = anim.load_image(walk[0])
        self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
        self.player_rect.y -= self.v / self.fps



    def move_back(self):
        walk = close_type_animation['walk']
        player_sprite_sheet = anim.load_image(walk[0])
        self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
        self.player_rect.y += self.v / self.fps



    def move_left(self):
        self.move_again = True
        walk = close_type_animation['walk']
        player_sprite_sheet = anim.load_image(walk[0])
        self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
        self.player_rect.x -= self.v / self.fps

    def move_stright(self):
        self.move_again = None
        walk = close_type_animation['walk']
        player_sprite_sheet = anim.load_image(walk[0])
        self.frames = anim.prepear_frames(walk[1], walk[3], player_sprite_sheet, walk[2], walk[4])
        self.player_rect.x += self.v / self.fps

    def check_intersection(self, player_pose_x, player_pose_y):
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0, 128), (25, 25), 25)
        self.rect = self.image.get_rect(center=(self.player_rect.x, self.player_rect.y))
        self.transparent_circle_rect = self.image.get_rect(center=(self.player_rect.x, self.player_rect.y))
        return False

    def strive_to_player(self, player_pose_x, player_pose_y):
        if not self.check_intersection(player_pose_x, player_pose_y):
            if self.player_rect.x + 10 > player_pose_x:
                self.move_left()
            elif self.player_rect.x + 10 < player_pose_x:
                self.move_stright()

            if self.player_rect.y + 10 < player_pose_y:
                self.move_back()
            elif self.player_rect.y + 10 > player_pose_y:
                self.move_right()




    def enemy_spawn(self):
        pass




class EnemyFurtherType:
    pass








