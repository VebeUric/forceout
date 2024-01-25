import time
from game_state_manager import GameStateManager
from Engine_g import Player, EnemyCloseType
import pygame
from random import randint
from GUI import Animation, Surrounded


settings_width, settings_height = 1280, 720
size = width, height = settings_width, settings_height
screen = pygame.display.set_mode(size)
pygame.init()
player = None
nim = Animation()
game_controller = GameStateManager(screen)

running = True
fps = 60
is_pressed_shift = None
clock = pygame.time.Clock()

IDLE_TIME_THRESHOLD = 10
pygame.time.set_timer(pygame.USEREVENT, IDLE_TIME_THRESHOLD)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if player:
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            player.is_pressed_shift = True
        else:
            player.is_pressed_shift = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move_left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move_stright()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move_right()
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move_back()
        if not (keys[pygame.K_s] or keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_a]):
            player.idle()


        if player.is_pressed_shift:
            player.speed_up()
        else:
            player.speed_down()
    screen.fill((0, 0, 0))


    game_controller.update(event)
    pygame.display.flip()
    clock.tick(10)
pygame.quit()




