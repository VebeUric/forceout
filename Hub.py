import pygame
import sys
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)

# Класс для персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.image = pygame.Surface((2*radius, 2*radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, white, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = radius

    def update(self):
        # Движение персонажа
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Класс для объектов, с которыми может столкнуться персонаж
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.image = pygame.Surface((2*radius, 2*radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, red, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

# Создание персонажа и объектов
player = Player(width // 2, height // 2, 20)
obstacle1 = Obstacle(200, 200, 30)
obstacle2 = Obstacle(400, 300, 30)

all_sprites = pygame.sprite.Group()
all_sprites.add(player, obstacle1, obstacle2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Проверка коллизий
    collisions = pygame.sprite.spritecollide(player, all_sprites, False)
    for sprite in collisions:
        if isinstance(sprite, Obstacle):
            # Обработка столкновения с препятствием
            print("Collision with obstacle!")

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()цв