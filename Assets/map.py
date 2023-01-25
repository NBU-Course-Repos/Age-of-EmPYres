from pygame.math import Vector2 as Vector2
from Assets.settings import MAP_SIZE, TILE_SIZE
from Assets.tile import Tile
from random import randint
from Assets.Buildings.town_center import TownCenter
from Assets.Buildings.building import Building
from Assets.Buildings.states import BuildingState
from Assets.Resources.resource import Resource
from Assets.Resources.types import ResourceType


class Map:

    def __init__(self, camera):
        self.resources = []
        self.tree_count = 0
        self.stone_count = 0
        self.__generate_terrain(camera)

    def __generate_terrain(self, group):
        total_map_size = MAP_SIZE.elementwise()*TILE_SIZE
        for row in range(-int(total_map_size.y/2), int(total_map_size.y/2), 64):
            for col in range(-int(total_map_size.x/2), int(total_map_size.x/2), 64):
                tile = Tile((col, row), group, "grass")
                if randint(0, 9) % 4 == 0 and self.tree_count <= 2000:
                    i = randint(1, 9)
                    self.__generate_resources((col, row), group, ResourceType.WOOD, i, tile)
                elif randint(0, 13) % 7 == 0 and self.stone_count <= 300:
                    self.__generate_resources((col, row), group, ResourceType.STONE, 1, tile)

    def __generate_resources(self, pos: Vector2, camera, resource: ResourceType, image_enum: int, tile):
        obj = Resource(pos, camera, resource, image_enum, tile=tile)
        obj.add(camera.resource_group)
        if resource == ResourceType.WOOD:
            self.tree_count += 1
        if resource == ResourceType.STONE:
            self.stone_count += 1
                    
