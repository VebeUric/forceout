
print(3)
import pygame


settings_width, settings_height, start_pose_x, start_pose_y = 900, 800, 30, 50


pygame.init()

size = width, height = settings_width, settings_height
screen = pygame.display.set_mode(size)

running = True
x_pose, y_pose = start_pose_x, start_pose_y
V = 120
fps = 60
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


