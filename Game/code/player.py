# import pygame
# from settings import *
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self, pos, groups, obstacle_sprites, create_attack):
#         super().__init__(groups)
#         self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
#         self.rect = self.image.get_rect(topleft=pos)
#
#         self.direction = pygame.math.Vector2()
#         self.speed = 5
#         self.status = 'down'
#
#         self.create_attack = create_attack
#         self.attacking = False
#         self.attack_cooldown = 400
#         self.attack_time = None
#         self.obstacle_sprites = obstacle_sprites
#
#     def input(self):
#         keys = pygame.key.get_pressed()
#
#         if keys[pygame.K_UP]:
#             self.direction.y = -1
#             self.status = 'up'
#         elif keys[pygame.K_DOWN]:
#             self.direction.y = 1
#             self.status = 'down'
#         else:
#             self.direction.y = 0
#
#         if keys[pygame.K_RIGHT]:
#             self.direction.x = 1
#             self.status = 'right'
#         elif keys[pygame.K_LEFT]:
#             self.direction.x = -1
#             self.status = 'left'
#         else:
#             self.direction.x = 0
#
#             # attack input
#         if keys[pygame.K_SPACE]:
#             self.attacking = True
#             self.attack_time = pygame.time.get_ticks()
#             self.create_attack()
#
#     def move(self, speed):
#         if self.direction.magnitude() != 0:
#             self.direction = self.direction.normalize()
#
#         self.rect.x += self.direction.x * speed
#         self.collision('horizontal')
#         self.rect.y += self.direction.y * speed
#         self.collision('vertical')
#
#     # self.rect.center += self.direction * speed
#
#     def collision(self, direction):
#         if direction == 'horizontal':
#             for sprite in self.obstacle_sprites:
#                 if sprite.rect.colliderect(self.rect):
#                     if self.direction.x > 0:  # moving right
#                         self.rect.right = sprite.rect.left
#                     if self.direction.x < 0:  # moving left
#                         self.rect.left = sprite.rect.right
#
#         if direction == 'vertical':
#             for sprite in self.obstacle_sprites:
#                 if sprite.rect.colliderect(self.rect):
#                     if self.direction.y > 0:  # moving down
#                         self.rect.bottom = sprite.rect.top
#                     if self.direction.y < 0:  # moving up
#                         self.rect.top = sprite.rect.bottom
#
#     def update(self):
#         self.input()
#         self.move(self.speed)
import pygame
from settings import *
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.direction = pygame.math.Vector2()

        # graphics setup
        self.import_player_assets()
        self.status = 'down'

        # movement
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites

        # weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        self.speed = 5

        # damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500

    def import_player_assets(self):
        character_path = '../graphics/player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()

            # movement input
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            # attack input
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()

    def move(self, speed):

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            self.rect.x += self.direction.x * speed
            self.collision('horizontal')
            self.rect.y += self.direction.y * speed
            self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # moving up
                        self.rect.top = sprite.rect.bottom

    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
                self.attacking = False
                self.destroy_attack()

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.move(self.speed)
