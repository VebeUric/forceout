import pygame


class Player:
    def __init__(self, mass, size, x_pose=0, y_pose=0, v=120, fps=60, health=100, armore=100):
        self.armore = armore
        self.health = health
        self.is_pressed_shift = None
        self.mass = mass
        self.size = size
        self.x_pose = x_pose
        self.y_pose = y_pose
        self.fps = fps
        self.v = 120

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def respawn(self, x_pose, y_pose):
        self.x_pose = x_pose
        self.y_pose = y_pose

    def move_right(self):
        self.y_pose -= self.v / self.fps

    def move_back(self):
        self.y_pose += self.v / self.fps

    def move_left(self):
        self.x_pose -= self.v / self.fps

    def move_stright(self):
        self.x_pose += self.v / self.fps


    def press_shift(self):
        self.is_pressed_shift = True

    def not_press_shift(self):
        self.is_pressed_shift = False

    def speed_up(self):
        if self.v != 160:
            self.v += 10

    def speed_down(self):
        if self.v != 120:
            self.v -= 10

class EnemyCloseType:
    pass

class EnemyFurtherType:
    pass