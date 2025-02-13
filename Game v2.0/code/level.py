from settings import *
from tile import Tile
from weapon import Weapon
from player import Player


class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        with open('scr.txt', 'w') as fl:
            fl.write('0')

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == ' ':
                    surf = pygame.image.load(r'..\textures\water.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'x':
                    surf = pygame.image.load('../textures/rock_new.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites,
                                         self.create_attack,
                                         self.destroy_attack)
                if col == 'l':
                    surf = pygame.image.load('../textures/water_left.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'd':
                    surf = pygame.image.load('../textures/water_down.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'd1':
                    surf = pygame.image.load('../textures/water_d_l.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'd2':
                    surf = pygame.image.load(r'..\textures\water_d_r.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'u':
                    surf = pygame.image.load(r'..\textures\water_up.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'u1':
                    surf = pygame.image.load(r'..\textures\water_u_l.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'u2':
                    surf = pygame.image.load(r'..\textures\water_u_r.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'r':
                    surf = pygame.image.load('../textures/water_right.png')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                if col == 'e':
                    surf = pygame.image.load('../textures/grass.png')
                    Tile((x, y), [self.visible_sprites], 'plant', surf)
                if col == '@':
                    surf = pygame.image.load('../textures/ogeriz.png')
                    Tile((x, y), [self.visible_sprites, self.attackable_sprites], 'oger', surf)
                if col == '!':
                    surf = pygame.image.load('../textures/wheel.png')
                    Tile((x, y), [self.visible_sprites, self.attackable_sprites], 'wheel', surf)
                if col == 'q':
                    surf = pygame.image.load('../textures/pomidor.jpg')
                    Tile((x, y), [self.visible_sprites, self.attackable_sprites], 'pomid', surf)
                if col == '-':
                    surf = pygame.image.load('../textures/morkov.png')
                    Tile((x, y), [self.visible_sprites, self.attackable_sprites], 'pint', surf)
                if col == ']':
                    surf = pygame.image.load('../textures/grass.png')
                    Tile((x, y), [self.visible_sprites], 'zamok', surf)
                if col == ']':
                    surf = pygame.image.load('../textures/zamok1.jpg')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], 'zamok1', surf)

                if col == '[':
                    surf = pygame.image.load('../textures/grass.png')
                    Tile((x, y), [self.visible_sprites], 'zamok', surf)
                if col == '[':
                    surf = pygame.image.load('../textures/zamok2.jpg')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], 'zamok2', surf)

                if col == 'n':
                    surf = pygame.image.load('../textures/grass.png')
                    Tile((x, y), [self.visible_sprites], 'zamok', surf)
                if col == 'n':
                    surf = pygame.image.load('../textures/zamok3.jpg')
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], 'zamok3', surf)

                if col == 's':
                    surf = pygame.image.load('../textures/magaz.png')
                    Tile((x, y), [self.visible_sprites], 'magaz', surf)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def display_score(self):
        with open('scr.txt', 'r') as fl:
            s = fl.readlines()
            self.score = int(''.join(s))
        score_surf = self.font.render(f'Score: {self.score}', True, 'White')
        score_rect = score_surf.get_rect(topleft=(10, 10))
        pygame.draw.rect(self.screen, 'Black', score_rect)  # Опционально: рисуем фон для текста
        self.screen.blit(score_surf, score_rect)

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:

                        if target_sprite.is_collectable:
                            if target_sprite.sprite_type == 'pint':
                                target_sprite.image = pygame.image.load('../textures/dirt.png').convert_alpha()
                                target_sprite.set_texture('grass_1')
                                target_sprite.reset_time = pygame.time.get_ticks()
                                target_sprite.is_collectable = False
                                self.score += 1
                                with open('scr.txt', 'w') as r:
                                    r.write(str(self.score))
                            elif target_sprite.sprite_type == 'wheel':
                                target_sprite.image = pygame.image.load('../textures/dirt.png').convert_alpha()
                                target_sprite.set_texture('grass_1')
                                target_sprite.reset_time = pygame.time.get_ticks() + 5000
                                target_sprite.is_collectable = False
                                self.score += 2
                                with open('scr.txt', 'w') as r:
                                    r.write(str(self.score))
                            elif target_sprite.sprite_type == 'pomid':
                                target_sprite.image = pygame.image.load('../textures/dirt.png').convert_alpha()
                                target_sprite.set_texture('plant_1')
                                target_sprite.reset_time = pygame.time.get_ticks() + 10000
                                target_sprite.is_collectable = False
                                self.score += 3
                                with open('scr.txt', 'w') as r:
                                    r.write(str(self.score))
                            elif target_sprite.sprite_type == 'oger':
                                target_sprite.image = pygame.image.load('../textures/dirt.png').convert_alpha()
                                target_sprite.set_texture('plant_1')
                                target_sprite.reset_time = pygame.time.get_ticks() + 15000
                                target_sprite.is_collectable = False
                                self.score += 4
                                with open('scr.txt', 'w') as r:
                                    r.write(str(self.score))
                            if target_sprite.sprite_type == 'zamok1' and self.score >= 10:
                                self.score -= 10
                                with open('scr.txt', 'w') as r:
                                    r.write(str(self.score))
                                target_sprite.kill()
                            if target_sprite.sprite_type == 'zamok2' and self.score >= 20:
                                self.score -= 20
                                with open('scr.txt', 'w') as r:
                                    r.write(str(self.score))
                                target_sprite.kill()
                            if target_sprite.sprite_type == 'zamok3' and self.score >= 30:
                                self.score -= 30
                                with open('scr.txt', 'w') as r:
                                    r.write(str(self.score))
                                target_sprite.kill()

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.player_attack_logic()
        self.visible_sprites.update()
        self.display_score()
