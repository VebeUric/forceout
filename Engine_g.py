import Pygame


class Player:
    def __init__(self, mass, size, x_pose=0, y_pose=0, v=120, fps=60):
        self.pressed_shift = None
        self.mass = mass
        self.size = size
        self.x_pose = x_pose
        self.y_pose = y_pose
        self.fps = fps
        self.v = 120

    def respawn(self, x_pose, y_pose):
        self.x_pose = x_pose
        self.y_pose = y_pose

    def move_right(self):
        self.y_pose += self.v / self.fps

    def move_back(self):
        self.y_pose -= self.v / self.fps

    def move_left(self):
        self.x_pose -= self.v / self.fps

    def move_stright(self):
        self.x_pose += self.v / self.fps


    def press_shift(self):
        self.pressed_shift = True

    def not_press_shift(self):
        self.pressed_shift = False