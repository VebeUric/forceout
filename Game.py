from Engine_g import Player
import pygame


pygame.init()

settings_width, settings_height = 900, 800
player = Player(80, (30, 50), 'data/Sprites/main_character_sprite/hesh')

def update():
    player.update(screen)
    player.draw(screen)


size = width, height = settings_width, settings_height
screen = pygame.display.set_mode(size)

running = True
fps = player.fps
is_pressed_shift = None
clock = pygame.time.Clock()

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
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move_stright()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.move_right()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move_back()

    if player.is_pressed_shift:
        player.speed_up()
    else:
        player.speed_down()
    screen.fill((0, 0, 0))
    update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()




