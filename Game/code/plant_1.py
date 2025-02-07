# import pygame
# from settings import *
#
#
# class Plant1(pygame.sprite.Sprite):
#     def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE)), texture='plant_1Up.jpg'):
#         super().__init__(groups)
#         self.sprite_type = sprite_type
#         self.image = surface
#         self.texture = texture  # Текущая текстура
#         self.original_image = surface  # Сохраняем оригинальное изображение
#         self.reset_time = None  # Время, когда нужно вернуть текстуру обратно
#         self.reset_duration = 5000
#         self.is_collectable = True  # Флаг, указывающий, можно ли взаимодействовать с тайлом
#
#         if sprite_type == 'object':
#             self.rect = self.image.get_rect(topleft=pos)
#         else:
#             self.rect = self.image.get_rect(topleft=pos)
#         self.hitbox = self.rect.inflate(0, -100)
#
#     def set_texture(self, texture):
#         self.texture = texture
#
#     def reset(self):
#         self.image = self.original_image  # Возвращаем оригинальное изображение
#         self.texture = self.sprite_type  # Возвращаем оригинальную текстуру
#         self.is_collectable = True  # Снова делаем тайл "собираемым"
#         self.reset_time = None
#
#     def update(self):
#         if self.reset_time:
#             current_time = pygame.time.get_ticks()
#             if current_time - self.reset_time >= self.reset_duration:
#                 self.reset()


import pygame
from settings import *
from tile import Tile

class Plant1(Tile):
    def __init__(self, pos, groups):
        surface = pygame.image.load('../graphics/textures/wheel.png').convert_alpha() # Загружаем изображение здесь
        super().__init__(pos, groups, 'plant', surface, texture='plant_2')