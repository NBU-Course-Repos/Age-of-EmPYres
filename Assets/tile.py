import os

import pygame
from pygame.math import Vector2 as Vector2
from Assets.settings import MAP_SETTINGS


class Tile(pygame.sprite.Sprite):
    TILE_VARIATIONS = ['sand', 'dirt']

    def __init__(self, pos, group=pygame.sprite.AbstractGroup(), tile_type=""):
        super().__init__()
        group.add(self)
        self.pos = pos
        self.group = group
        self.TILE_SIZE = Vector2((MAP_SETTINGS["Tiles"]["Size"]["x"],
                                  MAP_SETTINGS["Tiles"]["Size"]["y"]))
        self.tile_type = tile_type
        self.image = pygame.image.load(f"{os.getcwd()}/Textures/{self.tile_type}.png")
        self.image = pygame.transform.scale(self.image, self.TILE_SIZE)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.border: pygame.Rect = None

    def draw_border(self):
        self.border = pygame.draw.rect(surface=self.image,
                                       color=(255, 255, 255),
                                       rect=[0, 0, self.TILE_SIZE.x, self.TILE_SIZE.y],
                                       width=1)

    def delete_border(self):
        self.image = pygame.image.load(f"{os.getcwd()}/Textures/{self.tile_type}.png")