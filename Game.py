

from Engine_g import Player
import pygame




pygame.init()
settings_width, settings_height = 900, 800
player = Player(80, (30, 50))

size = width, height = settings_width, settings_height
screen = pygame.display.set_mode(size)

running = True
x_pose, y_pose = start_pose_x, start_pose_y
fps = player.fps
is_pressed_shift = None
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        is_pressed_shift = True
    else:
        is_pressed_shift = False

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x_pose -= V / fps
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x_pose += V / fps
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y_pose -= V / fps
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y_pose += V / fps

    if is_pressed_shift:
        if V != 160:
            V += 10
    else:
        if V != 120:
            V -= 10

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (x_pose, y_pose, 30, 50))

    clock.tick(fps)
    pygame.display.flip()
pygame.quit()


