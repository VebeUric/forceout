import pygame
from pygame.sprite import Sprite
from pygame import Surface
from pygame import Rect
from GUI import Animation

anim = Animation()
class Button(Sprite):
    def __init__(self, text=None, issue=lambda: None, picture_path=None, alternative_picture_path=None):
        super().__init__()
        self.issue = issue
        print(issue)
        self.text = text
        self.text_size = 50
        self.is_active = None
        self.color = (0, 0, 0)
        self.picture_path = picture_path
        self.alternative_picture_path = alternative_picture_path
        self.rect = Rect(0, 0, 100, 100)
        self.image = Surface(self.rect.size)
        self.add_buttton_picture(self.picture_path)
        self.render(self.image)

    def resize_text(self, new_size):
        self.text_size = new_size


    def resize(self, size):
        self.rect.width, self.rect.height = size

    def replace(self, pos):
        self.rect.x, self.rect.y = pos

    def make_new_text_color(self, new_color):
        self.color = new_color

    def on_click(self):
        if self.issue:
            self.issue()
    def connect_issue(self, foo):
        self.issue = foo

    def add_buttton_picture(self, path):
        if path:
            self.picture_path = pygame.image.load(path)

    def add_alternative_picture(self, path):
        if path:
            self.alternative_picture_path = pygame.image.load(path)

    def update(self, *args):
        if not args:
            return

        if args[0].type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(args[0].pos):
                 if not self.is_active:
                      self.is_active = True
                      self.render(self.image)

            else:
                if self.is_active:
                    self.is_active = False
                    self.render(self.image)
        elif args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.on_click()

    def render(self, screen):
        self.button_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        if self.picture_path:
            if self.alternative_picture_path:
                if self.is_active:
                    if not type(self.alternative_picture_path) is Surface:
                        self.alternative_picture_path = anim.load_image(self.alternative_picture_path)
                    self.alternative_picture_path = pygame.transform.scale(self.alternative_picture_path, (self.rect.width, self.rect.height))
                    screen.blit(self.alternative_picture_path, (self.rect.x, self.rect.y))
                else:
                    self.picture_path = pygame.transform.scale(self.picture_path, (self.rect.width, self.rect.height))
                    screen.blit(self.picture_path, (self.rect.x, self.rect.y))
            else:
                self.picture_path = pygame.transform.scale(self.picture_path, (self.rect.width, self.rect.height))
                screen.blit(self.picture_path, (self.rect.x, self.rect.y))
        else:
            if self.is_active:
                color = (200, 100, 100)
            else:
                color = (100, 200, 100)
            pygame.draw.rect(screen, color, (self.rect.width, self.rect.height // 2), self.rect.size // 2)
        font = pygame.font.Font(None, self.text_size)                                        # Сделать обособленную фуекцию чтобы можно было скрывать текст
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect.center)






class RaangeSlider(Sprite):
    def __init__(self, text, min=0, max=100, issue = lambda: None):
        super().__init__()
        self.text = text()

    def init_button(self):
        pass

    def resize(self, hiegth, width):
        pass

    def replace(self, x, y):
        pass

    def on_click(self):
        pass

