class GameStateManager:
    def __init__(self):
        self.game_states = {}
        self.current_state = None

    def add_game_state(self, text, state):
        self.game_states[text] = state

    def set_current_game_state(self, text):
        self.current_state = text

    def check_current_game_state(self):
        return self.current_state

class Settings:
    def __init__(self):
        self.screen_size = (1080, 1920)

    def change_screen_size(self,  new_width, new_hieght):
        self.screen_size  = (new_width, new_hieght)