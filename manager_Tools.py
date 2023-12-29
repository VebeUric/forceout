from pygame.sprite import Sprite
from pygame import Surface
from pygame import Rect

class Button(Sprite):
    def __init__(self, text, issue=lambda: None, path=''):
        super().__init__()
        self.text = text
        self.issue = issue
        self.rect = Rect(0, 0, 100, 100)
        self.image = Surface(self.rect.size)

    def resize(self, heigth, width):
        self.rect.width, self.height = heigth, width

    def replace(self, x, y):
        self.rect.x, self.rect.y = x, y

    def on_click(self):
        self.issue

class RaangeSlider(Sprite):
    def __init__(self, text, min=0, max=100):
        super().__init__()

    def init_button(self):
        pass

    def resize(self, hiegth, width):
        pass

    def replace(self, x, y):
        pass

    def on_click(self):
        pass

