from game_state_manager import Settings
import pygame
import sys
from PIL import Image
import os
from random import randint


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
        self.v = 120
        self.frames = None
        self.sprite_width = 50  # Ширина каждого кадра
        self.sprite_height = 79  # Высота каждого кадра
        self.animation_speed = 10  # Скорость смены кадров
        self.animation_index = 0
        if not (os.path.exists(character_folder_path) and os.path.isdir(character_folder_path)):
            split_image('data/Sprites/main_character_sprite/Fire_player_sprite.png', character_folder_path, 25, 1)
        player_sprite_sheet = load_image("Sprites/main_character_sprite/hesh/frame_0_0.png")
        self.frames = prepear_frames(self.sprite_width, self.sprite_height, player_sprite_sheet)


    def draw(self, screen):
        self.player_rect = self.image.get_rect()
        self.player_rect.x = 100
        self.player_rect.y = 100
        screen.blit(self.image, self.player_rect.topleft)

    def update(self, screen):
        if self.frames:
            self.animation_index += 1
            if self.animation_index >= len(self.frames):
                self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def respawn(self, x_pose, y_pose):
        self.x_pose = x_pose
        self.y_pose = y_pose

    def move_right(self):
        self.rect.y-= self.v / self.fps

    def move_back(self):
        self.rect.y += self.v / self.fps

    def move_left(self):
        self.rect.x -= self.v / self.fps

    def move_stright(self):
        self.rect.x += self.v / self.fps


    def press_shift(self):
        self.is_pressed_shift = True

    def not_press_shift(self):
        self.is_pressed_shift = False

    def speed_up(self):
        if self.v != 160:
            self.v += 10

    def speed_down(self):
        if self.v != 120:
            self.v -= 10

class EnemyCloseType:
    def __init__(self, attack_distance, size, screen_size):
        self.close_enemy_sprit_group = pygame.sprite.Group()
        self.attack_distance = attack_distance
        self.size = size

    def enemy_spawn(self):
        pass




class EnemyFurtherType:
    pass


def prepear_frames(sprite_width, sprite_height,  player_sprite_sheet):
    frames = []
    for i in range(player_sprite_sheet.get_width() // sprite_width):
        frame_rect = pygame.Rect(i * sprite_width, 0, sprite_width, sprite_height)
        frames.append(player_sprite_sheet.subsurface(frame_rect))
    return frames





def split_image(input_image_path, output_folder, rows, cols):
    # Открытие изображения
    original_image = Image.open(input_image_path)

    # Получение размеров изображения
    width, height = original_image.size

    # Размеры каждого фрагмента
    tile_width = width // cols
    tile_height = height // rows

    # Создание папки для сохранения фрагментов
    os.makedirs(output_folder, exist_ok=True)

    # Разрезание изображения
    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = left + tile_width
            lower = upper + tile_height

            # Вырезаем фрагмент
            tile = original_image.crop((left, upper, right, lower))

            # Сохраняем фрагмент в отдельном файле
            tile.save(os.path.join(output_folder, f"frame_{row}_{col}.png"))
            print('ok')

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image