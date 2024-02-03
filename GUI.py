from PIL import Image
import pygame
import os
import sys


def load_alpha_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    image = image.convert()
    rect = image.get_rect()
    image.set_colorkey((255, 255, 255))
    alpha_channel = pygame.Surface(rect.size, pygame.SRCALPHA)
    alpha_channel.fill((0, 0, 0, 0))
    alpha_channel.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    image_with_transparent_background = pygame.Surface(rect.size, pygame.SRCALPHA)
    image_with_transparent_background.blit(alpha_channel, (0, 0))
    return image


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def prepear_frames(sprite_width, sprite_height, player_sprite_sheet, space, frame_count):
    frames = []
    for i in range(0, frame_count):
        frame_rect = pygame.Rect(i * space + sprite_width * i, 0, sprite_width, sprite_height)
        frames.append(player_sprite_sheet.subsurface(frame_rect))
    return frames


def prepear_trans_frames(sprite_width, sprite_height, player_sprite_sheet, space, frame_count):
    frames = []
    for i in range(0, frame_count):
        frame_rect = pygame.Rect(i * space + sprite_width * i, 0, sprite_width, sprite_height)
        frames.append(pygame.transform.flip(player_sprite_sheet.subsurface(frame_rect), True, False))
    return frames


def crop_to_first_non_empty_pixels(input_path, output_path):
    # Открытие изображения
    img = Image.open(input_path)
    _, _ = img.size
    left_bound, top_bound, right_bound, bottom_bound = find_non_empty_bounds(img)

    cropped_img = img.crop((left_bound, top_bound, right_bound, bottom_bound))
    cropped_img.save(output_path)


def split_image(input_image_path, output_folder, rows, cols):
    original_image = Image.open(input_image_path)

    width, height = original_image.size

    tile_width = width // cols
    tile_height = height // rows

    os.makedirs(output_folder, exist_ok=True)
    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = left + tile_width
            lower = upper + tile_height

            tile = original_image.crop((left, upper, right, lower))

            tile.save(os.path.join(output_folder, f"frame_{row}_{col}.png"))


def find_non_empty_bounds(image):
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


class Animation:
    def __init__(self):
        pass

    def split_image(self, input_image_path, output_folder, rows, cols):
        original_image = Image.open(input_image_path)

        width, height = original_image.size

        tile_width = width // cols
        tile_height = height // rows

        os.makedirs(output_folder, exist_ok=True)

        for row in range(rows):
            for col in range(cols):
                left = col * tile_width
                upper = row * tile_height
                right = left + tile_width
                lower = upper + tile_height
                tile = original_image.crop((left, upper, right, lower))

                tile.save(os.path.join(output_folder, f"frame_{row}_{col}.png"))

    def load_alpha_image(self, name):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            sys.exit()
        image = pygame.image.load(fullname)
        image = image.convert()
        rect = image.get_rect()
        image.set_colorkey((255, 255, 255))
        alpha_channel = pygame.Surface(rect.size, pygame.SRCALPHA)
        alpha_channel.fill((0, 0, 0, 0))
        alpha_channel.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        image_with_transparent_background = pygame.Surface(rect.size, pygame.SRCALPHA)
        image_with_transparent_background.blit(alpha_channel, (0, 0))
        return image


    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):

            sys.exit()
        image = pygame.image.load(fullname)
        return image


    def crop_to_first_non_empty_pixels(self, input_path, output_path):
        img = Image.open(input_path)
        width, height = img.size
        left_bound, top_bound, right_bound, bottom_bound = find_non_empty_bounds(img)
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
    def __init__(self, anim, screen, surr_path, zoom_kof=4, is_scrol=True):
        self.rect = None
        self.anim = anim
        self.screen = screen
        self.v = 15
        self.x = 0
        self.is_scroll = is_scrol
        self.y = 0
        self.current_scroll = None
        self.image = pygame.transform.scale(self.anim.load_image(surr_path), (1280 * zoom_kof, 720 * zoom_kof))

    def draw(self):
        print(self.x, self.y, 111111111111111)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.screen.blit(self.image, self.rect)

    def move_down(self):
        self.current_scroll = 'up'
        self.y -= self.v

    # def set_spawn_point(self, x, y):
    #     self.x -= x
    #     self.y += y

    def move_up(self):
        if self.is_scroll:
            self.current_scroll = 'down'
            self.y += self.v

    def move_left(self):
        if self.is_scroll:
            self.current_scroll = 'right'
            self.x += self.v

    def move_right(self):
        if self.is_scroll:
            self.current_scroll = 'left'
            self.x -= self.v

    def set_spawn(self):
        pass
