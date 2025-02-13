import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE)), texture='grass_3'):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.texture = texture
        self.original_image = surface
        self.reset_time = None
        self.reset_duration = 5000
        self.is_collectable = True

        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=pos)
        else:
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -25)

    def set_texture(self, texture):
        self.texture = texture

    def reset(self):
        self.image = self.original_image
        self.texture = self.sprite_type
        self.is_collectable = True
        self.reset_time = None

    def update(self):
        if self.reset_time:
            current_time = pygame.time.get_ticks()
            if current_time - self.reset_time >= self.reset_duration:
                self.reset()
