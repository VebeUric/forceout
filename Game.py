import time
from game_state_manager import GameStateManager
from Engine_g import Player, EnemyCloseType
import pygame
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
is_pause = False
IDLE_TIME_THRESHOLD = 10
pygame.time.set_timer(pygame.USEREVENT, IDLE_TIME_THRESHOLD)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:

        if is_pause is False:
            is_pause = True
        else:
            is_pause = False

    if not is_pause:
        game_controller.activate_pause()
        screen.fill((0, 0, 0))
        game_controller.update(event, keys)
        if game_controller.do_exit:
            running = False
    else:
        game_controller.inactivate_pause()

    pygame.display.flip()
    clock.tick(15)
pygame.quit()
