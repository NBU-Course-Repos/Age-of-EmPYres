import pygame
from pygame.math import Vector2 as Vector2
from Assets.settings import MAP_SETTINGS


class Tile(pygame.sprite.Sprite):
    TILE_VARIATIONS = ['sand', 'dirt']

    def __init__(self, pos, group, tile_type):
        super().__init__(group)
        self.TILE_SIZE = Vector2((MAP_SETTINGS["Tiles"]["Size"]["x"],
                                  MAP_SETTINGS["Tiles"]["Size"]["y"]))
        self.image = pygame.image.load(f"Assets/Textures/{tile_type}.png")
        self.image = pygame.transform.scale(self.image, self.TILE_SIZE)
        self.rect = self.image.get_rect(topleft=pos)
