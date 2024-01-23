from PIL import Image
import pygame
import os
import sys


class Animation:
    def __init__(self):
        pass
    def split_image(self, input_image_path, output_folder, rows, cols):
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


    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):

            sys.exit()
        image = pygame.image.load(fullname)
        return image


    def crop_to_first_non_empty_pixels(self, input_path, output_path):
        # Открытие изображения
        img = Image.open(input_path)

        # Получение размеров изображения
        width, height = img.size

        # Находим координаты первого непустого пикселя
        left_bound, top_bound, right_bound, bottom_bound = find_non_empty_bounds(img)

        # Обрезка изображения и сохранение
        cropped_img = img.crop((left_bound, top_bound, right_bound, bottom_bound))
        cropped_img.save(output_path)

    def find_non_empty_bounds(self,  image):
        width, height = image.size
        left_bound = width
        top_bound = height
        right_bound = 0
        bottom_bound = 0

        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                if pixel[3] != 0 and pixel[:3] != (255, 255, 255):  # Не прозрачный и не белый пиксель
                    left_bound = min(left_bound, x)
                    top_bound = min(top_bound, y)
                    right_bound = max(right_bound, x)
                    bottom_bound = max(bottom_bound, y)

        return left_bound, top_bound, right_bound, bottom_bound

    def prepear_frames(self, sprite_width, sprite_height,  player_sprite_sheet, space, frame_count):
        frames = []
        for i in range(0, frame_count):
            frame_rect = pygame.Rect(i * space + sprite_width * i, 0, sprite_width, sprite_height)
            frames.append(player_sprite_sheet.subsurface(frame_rect))
        return frames


    def prepear_trans_frames(self, sprite_width, sprite_height,  player_sprite_sheet, space, frame_count):
        frames = []
        for i in range(0, frame_count):
            frame_rect = pygame.Rect(i * space + sprite_width * i, 0, sprite_width, sprite_height)
            frames.append(pygame.transform.flip(player_sprite_sheet.subsurface(frame_rect), True, False))
        return frames


class Surrounded:
    def __init__(self, anim, screen):
        self.anim = anim
        self.screen = screen
        self.v = 5
        self.i = 0
        self.image = pygame.transform.scale(self.anim.load_image('Surrounded/surbub.png'), (1280 * 2, 720 * 2))

    def move_surrounded(self):
        self.i -= self.v
        self.rect = self.image.get_rect(topleft=(self.i, self.i))
        self.screen.blit(self.image, self.rect)




