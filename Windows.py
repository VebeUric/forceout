from manager_Tools import Button
from GUI import Animation
import pygame



anim = Animation()
class StartWindow:
    def __init__(self, screen, game_controller):
        self.frames = []
        self.screen = screen
        self.game_controller = game_controller
        self.current_frame = 0

        self.play_button = Button('Играть', lambda: self.go_to_hub(), 'data/buttons/not_pressed_two.png', 'buttons/pressed.png')
        self.play_button.make_new_text_color((0, 0, 0))

        self.play_button.replace((150, 400))
        self.play_button.resize((200, 90))

        self.learning_button = Button('Обучение', lambda: self.start_learning(), 'data/buttons/not_pressed_two.png', 'buttons/pressed.png')
        self.learning_button.make_new_text_color((0, 0, 0))
        self.learning_button.replace((150, 500))
        self.learning_button.resize((200, 90))

        self.exit_button = Button('Выход', lambda: self.exit(), 'data/buttons/not_pressed_two.png', 'buttons/pressed.png')
        self.exit_button.make_new_text_color((0, 0, 0))
        self.exit_button.replace((150, 600))
        self.exit_button.resize((200, 90))

        self.rect = anim.load_image('start_background/1.png').get_rect()
        for i in range(1, 251):
            self.frames.append(anim.load_image(f'start_background/{i}.png'))

    def update(self, event):
        self.current_frame += 1
        zoom_kof= 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.image = pygame.transform.scale(self.image, (1280 * zoom_kof, 720 * zoom_kof))
        self.play_button.update(event)
        self.learning_button.update(event)
        self.exit_button.update(event)


    def draw(self):
        print(self.play_button.rect.size)
        self.screen.blit(self.image, self.rect.topleft)
        self.play_button.render(self.screen)
        self.learning_button.render(self.screen)
        self.exit_button.render(self.screen)

    def go_to_hub(self):
        self.game_controller.set_current_game_state('hub')

    def exit(self):
        self.game_controller.set_current_game_state('exit')
    def start_learning(self):
        pass


class Hub:
    def __init__(self):
        pass