from level_logic import Level
from Windows import StartWindow
from Hub import Hub
import pygame
from GUI import Animation
from manager_Tools import Button

anim = Animation()
class GameStateManager:
    def __init__(self, screen):
        self.game_states = {
    'start_menu':'',
    'hub':'',
    'level_1':''

        }
        self.levels_list = [('Первый уровень', 'level_one')]
        self.levels_menu_is_active = False
        self.do_exit = False
        self.screen = screen
        self.start_window = StartWindow(self.screen, self)
        self.hub = Hub(self.screen, self)
        self.level = Level(screen)
        self.current_state = 'start_menu'

    def update(self, event, keys):
        if self.current_state == 'start_menu':
            self.level.clear_level()
            self.start_window.update(event)
            self.start_window.draw()
        elif self.current_state == 'hub':
            self.level.clear_level()
            self.hub.update(event, keys)
            self.hub.draw(keys, event)
        elif self.current_state == 'level_one':
            self.level.update()
            self.level.draw(keys, event)
            if self.level.mode:
                self.set_current_game_state(self.level.mode)
        elif self.current_state == 'exit':
             self.do_exit = True

    def exit(self):
        return True


    def add_game_state(self, text, state):
        self.game_states[text] = state

    def set_current_game_state(self, text):
        self.current_state = text

    def check_current_game_state(self):
        return self.current_state


    def levels_menu(self, event):
        self.menu_background = anim.load_image('buttons/menu_background.png')
        self.screen.blit(self.menu_background, (200, 10))
        for i in range(len(self.levels_list)):
            play_level_button = Button(self.levels_list[i][0], lambda: self.set_current_game_state('level_one'), 'data/buttons/not_pressed_two.png',
                                      'buttons/pressed.png')
            play_level_button.replace((205, 15 + i * 5))
            play_level_button.resize((500, 100))
            play_level_button.update(event)
            play_level_button.render(self.screen)


    def activate_pause(self):
        pass

    def inactivate_pause(self):
        pass

    def wait_for_e_press(self):
        pass


    def trade(self):
       pass

class Settings:
    def __init__(self):
        self.screen_size = (1080, 1920)

    def change_screen_size(self,  new_width, new_hieght):
        self.screen_size  = (new_width, new_hieght)