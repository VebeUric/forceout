from Engine_g import Player, EnemyCloseType
import pygame
from GUI import Animation, Surrounded


pygame.init()
nim = Animation()

settings_width, settings_height = 1280, 720

size = width, height = settings_width, settings_height
screen = pygame.display.set_mode(size)

player = Player(80, 'data/Sprites/main_character_sprite/hesh', 'Sprites/main_character_sprite/Fire_player_sprite.png', 'Sprites/main_character_sprite/hesh/frame_0_0.png')
enemyclose = EnemyCloseType(80, (30, 50), 'data/Sprites/CloseTypeEnemy/hesh')


def update():
    if not screen.get_rect().contains(player.scroll_box):
            player.scroll_screen(screen, sur)

    sur.draw()
    player.update(screen)
    player.controller_hp()
    player.draw(screen)

    enemyclose.strive_to_player(player.player_rect.x, player.player_rect.y)
    enemyclose.update(screen, player.player_rect.x, player.player_rect.y)
    enemyclose.draw(screen)



sur = Surrounded(nim, screen)

running = True
fps = player.fps
is_pressed_shift = None
clock = pygame.time.Clock()

IDLE_TIME_THRESHOLD = 10
pygame.time.set_timer(pygame.USEREVENT, IDLE_TIME_THRESHOLD)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        player.is_pressed_shift = True
    else:
        player.is_pressed_shift = False

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move_left()
        print('LEFT')
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


    update()
    pygame.display.flip()
    clock.tick(10)
pygame.quit()




