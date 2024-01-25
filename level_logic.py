


enemycloseSquad = pygame.sprite.Group()
player = Player(80, 'data/Sprites/main_character_sprite/hesh', 'Sprites/main_character_sprite/Fire_player_sprite.png', 'Sprites/main_character_sprite/hesh/frame_0_0.png')
flag = True
def prepeare_enemy_squad():
    global flag
    player_coords = (player.rect.x, player.rect.y)
    for i in range(1):
        some_x_y = (randint(player_coords[0] - 500, player_coords[0] + 500), randint(player_coords[1] - 500, player_coords[1] + 500))
        print(some_x_y)
        enemyclose = EnemyCloseType(80, (30, 50), 'data/Sprites/CloseTypeEnemy/hesh')
        enemyclose.respawn(100, 100)
        enemycloseSquad.add_internal(enemyclose)
        enemycloseSquad.add(enemyclose)
    flag = False
player = Player(80, 'data/Sprites/main_character_sprite/hesh', 'Sprites/main_character_sprite/Fire_player_sprite.png', 'Sprites/main_character_sprite/hesh/frame_0_0.png')
sur = Surrounded(nim, screen, 'Surrounded/surbub.png')
def level_update():
    if flag:
        prepeare_enemy_squad()
    if not screen.get_rect().contains(player.scroll_box):
            player.scroll_screen(screen, sur)

    for sprit in enemycloseSquad:
        if pygame.sprite.spritecollideany(player, enemycloseSquad):
            sprit.attack(player)
    sur.draw()
    player.update(screen)
    player.controller_hp()
    player.draw(screen)
    for i in enemycloseSquad:
        i.strive_to_player(player.rect.x, player.rect.y, enemycloseSquad)
        i.update(screen, player.rect.x, player.rect.y)
        i.draw(screen)
