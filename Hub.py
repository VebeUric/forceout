from manager_Tools import Button
from GUI import Animation
import pygame



anim = Animation()
class StartWindow:
    def __init__(self, screen):
        self.frames = []
        self.screen = screen
        self.current_frame = 0
        self.play_button = Button('Играть', self.go_to_hub(), 'data/buttons/not_pressed.png', 'buttons/pressed.png')
        self.play_button.replace((200, 200))
        self.play_button.resize((200, 200))
        self.exit_button = Button('Выход', self.exit(), 'data/buttons/not_pressed.png', 'data/buttons/pressed.png')
        self.learning_button = Button('Обучение', self.start_learning(), 'data/buttons/not_pressed.png', 'data/buttons/pressed.png')
        self.rect = anim.load_image('start_background/1.png').get_rect()
        for i in range(1, 251):
            self.frames.append(anim.load_image(f'start_background/{i}.png'))

    def update(self, event):
        self.current_frame += 1
        zoom_kof= 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.play_button.update(event)
        self.image = pygame.transform.scale(self.image, (1280 * zoom_kof, 720 * zoom_kof))


    def draw(self):
        self.play_button.render(self.screen)
        self.screen.blit(self.image, self.rect.topleft)

    def go_to_hub(self):
        pass

    def exit(self):
        pass

    def start_learning(self):
        pass


class Hub:
    def __init__(self):
        pass