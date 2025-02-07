import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=pos)
        else:
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -100)


class Newgr(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=pos)
        else:
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -100)
# class Tile(pygame.sprite.Sprite):
#     def __init__(self, pos, groups):
#         super().__init__(groups)
#         self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
#         self.rect = self.image.get_rect(topleft=pos)
#
#
# class Trava(pygame.sprite.Sprite):
#     def __init__(self, pos, groups):
#         super().__init__(groups)
#         self.image = pygame.image.load('../graphics/grass/grass_3.png').convert_alpha()
#         self.rect = self.image.get_rect(topleft=pos)
#         print(self.rect)
