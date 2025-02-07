import pygame
from settings import *
from tile import Tile

class Pol(Tile):
    def __init__(self, pos, groups):
        surface = pygame.image.load('../graphics/textures/stone.png').convert_alpha() # Загружаем изображение здесь
        super().__init__(pos, groups, 'plant', surface, texture='plant_2')