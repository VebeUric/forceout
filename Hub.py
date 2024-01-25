from GUI import Surrounded, Animation
from Engine_g import Player, GameObject

anim = Animation()

class Hub:
    def __init__(self, screen, game_controller):
        self.screen = screen
        self.game_controller = game_controller
        self.anim = Animation()
        self.player = Player(80, 'data/Sprites/main_character_sprite/hesh', 'Sprites/main_character_sprite/Fire_player_sprite.png', 'Sprites/main_character_sprite/hesh/frame_0_0.png')
        self.hub_sur = Surrounded(anim, screen, 'Surrounded/hub.png',  1, False)
        # self.wall_one = GameObject(0, 286, 600, 200, self.screen)
        self.home = GameObject(0, 0, 250, 280, self.screen, self.hub_sur, 'Surrounded/home.png' )
        self.trade = GameObject(350, 150, 100, 100, self.screen, self.hub_sur, 'Surrounded/trade.png' )
        self.kuzn = GameObject(600, 0, 250, 150, self.screen, self.hub_sur, 'Surrounded/kuzn.png')
        self.obj_list = [self.kuzn, self.home]
        # self.player.respawn(3000, 1800)
        self.player.respawn(400, 400)


    def update(self, event, keys):
        for obj in self.obj_list:
            if obj.is_colide:
                pass
        print(self.player.rect.x, self.player.rect.y)
        # self.wall_one.check_colision(self.player)
        self.home.check_colision(self.player)
        self.trade.check_colision(self.player)
        self.kuzn.check_colision(self.player)
        # self.home.update()
        self.player.update(self.screen, keys)


    def draw(self):
        self.hub_sur.draw()

        # self.wall_one.draw()
        self.home.draw()
        self.kuzn.draw()
        self.trade.draw()
        self.player.draw(self.screen)

    def chech_shop_orange(self):
        pass

    def blacksmith(self):
        pass

    def choice_level(self):
        pass

