from GUI import Surrounded, Animation
from Engine_g import Player, GameObject

anim = Animation()

class Hub:
    def __init__(self, screen, game_controller):
        self.screen = screen
        self.game_controller = game_controller
        self.anim = Animation()
        self.player = Player(80, 'data/Sprites/main_character_sprite/hesh', 'Sprites/main_character_sprite/Fire_player_sprite.png', 'Sprites/main_character_sprite/hesh/frame_0_0.png')
        self.hub_sur = Surrounded(anim, screen, 'Surrounded/hub.png')
        # self.wall_one = GameObject(0, 286, 600, 200, self.screen)
        self.home = GameObject(0, 0, 316, 280, self.screen,self.hub_sur, 'Surrounded/home.png' )
        # self.player.respawn(3000, 1800)
        self.player.respawn(100, 100)


    def update(self, event, keys):
        print(self.player.rect.x, self.player.rect.y)
        # self.wall_one.check_colision(self.player)
        self.home.check_colision(self.player)
        if not self.screen.get_rect().contains(self.player.scroll_box):
            self.player.scroll_screen(self.screen, self.hub_sur)
        self.player.update(self.screen, keys)


    def draw(self):
        self.hub_sur.draw()
        self.player.draw(self.screen)
        # self.wall_one.draw()
        self.home.draw()


    def chech_shop_orange(self):
        pass

    def blacksmith(self):
        pass

    def choice_level(self):
        pass

