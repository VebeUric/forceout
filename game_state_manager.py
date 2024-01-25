# from level_logic import Hub, Level
from Windows import StartWindow
from Hub import Hub


class GameStateManager:
    def __init__(self, screen):
        self.game_states = {
    'start_menu':'',
    'hub':'',
    'level_1':''

        }
        self.do_exit = False
        self.screen = screen
        self.start_window = StartWindow(self.screen, self)
        self.hub = Hub(self.screen, self)
        # self.level = Level_logic()
        self.current_state = 'start_menu'

    def update(self, event, keys):
        if self.current_state == 'start_menu':
            self.start_window.update(event)
            self.start_window.draw()
        elif self.current_state == 'hub':
            self.hub.update(event, keys)
            self.hub.draw()
        elif self.current_state == 'level_one':
            self.level.update()
            self.level.draw()
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

    def activate_pause(self):
        pass

    def inactivate_pause(self):
        pass

class Settings:
    def __init__(self):
        self.screen_size = (1080, 1920)

    def change_screen_size(self,  new_width, new_hieght):
        self.screen_size  = (new_width, new_hieght)