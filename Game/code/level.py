import pygame
from settings import *
from tile import Tile
from tile import Newgr
from weapon import Weapon
from player import Player
from debug import debug



class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()  # Видно ли текстурку?
        self.obstacle_sprites = pygame.sprite.Group()  # Можно войти в нее?

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()


        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    surf = pygame.image.load('../graphics/test/rock.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.create_attack,
                                         self.destroy_attack)
                if col == '@':
                    surf = pygame.image.load('../graphics/grass/grass_3.png')
                    Tile((x, y), [self.visible_sprites, self.attackable_sprites], 'grass', surf)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            target_sprite.image = pygame.image.load('../graphics/grass/grass_1.png')
                            # surf = pygame.image.load('../graphics/grass/grass_1.png')
                            # x, y = target_sprite.rect.topleft
                            # Newgr((x, y), [self.visible_sprites], 'object', surf)
                            # target_sprite.kill()
                            # print(1234)


    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.player_attack_logic()
        debug(self.player.direction)
