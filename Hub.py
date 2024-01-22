import pygame
import sys
import math
import os

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__()
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
# pygame.init()
#
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# clock = pygame.time.Clock()
#
# # Цвета
# white = (255, 255, 255)
# red = (255, 0, 0)
#
# # Класс для персонажа
# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y, radius):
#         super().__init__()
#         self.image = pygame.Surface((2*radius, 2*radius), pygame.SRCALPHA)
#         pygame.draw.circle(self.image, white, (radius, radius), radius)
#         self.rect = self.image.get_rect(center=(x, y))
#         self.radius = radius
#
#     def update(self):
#         # Движение персонажа
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.rect.x -= 5
#         if keys[pygame.K_RIGHT]:
#             self.rect.x += 5
#         if keys[pygame.K_UP]:
#             self.rect.y -= 5
#         if keys[pygame.K_DOWN]:
#             self.rect.y += 5
#
# # Класс для объектов, с которыми может столкнуться персонаж
# class Obstacle(pygame.sprite.Sprite):
#     def __init__(self, x, y, radius):
#         super().__init__()
#         self.image = pygame.Surface((2*radius, 2*radius), pygame.SRCALPHA)
#         pygame.draw.circle(self.image, red, (radius, radius), radius)
#         self.rect = self.image.get_rect(center=(x, y))
#
# # Создание персонажа и объектов
# player = Player(width // 2, height // 2, 20)
# obstacle1 = Obstacle(200, 200, 30)
# obstacle2 = Obstacle(400, 300, 30)
#
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player, obstacle1, obstacle2)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     all_sprites.update()
#
#     # Проверка коллизий
#     collisions = pygame.sprite.spritecollide(player, all_sprites, False)
#     for sprite in collisions:
#         if isinstance(sprite, Obstacle):
#             # Обработка столкновения с препятствием
#             print("Collision with obstacle!")
#
#     screen.fill((0, 0, 0))
#     all_sprites.draw(screen)
#
#     pygame.display.flip()
#     clock.tick(30)
#
# pygame.quit()
# sys.exit()цв
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image



pygame.init()

settings_width, settings_height = 900, 800


size = width, height = settings_width, settings_height
screen = pygame.display.set_mode(size)

running = True
fps = 60
is_pressed_shift = None
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0, 0, 0))
        dragon = AnimatedSprite(load_image("pygame-8-1 (1).png"), 8, 2, 50, 50)


    clock.tick(fps)
    pygame.display.flip()
pygame.quit()