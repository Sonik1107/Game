import pygame
from settings import *
from tile import Tile

class Grass(Tile):
    def __init__(self, pos, groups):
        surface = pygame.image.load('../graphics/grass/grass_3.png').convert_alpha() # Загружаем изображение здесь
        super().__init__(pos, groups, 'grass', surface, texture='grass_3')