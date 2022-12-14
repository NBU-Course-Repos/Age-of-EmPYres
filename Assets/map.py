from pygame.math import Vector2 as Vector2
from Assets.settings import MAP_SETTINGS, SCREEN_HEIGHT, SCREEN_WIDTH
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
        self.__MAP_SIZE = Vector2((MAP_SETTINGS["Tiles"]["Count"]["x"],
                                   MAP_SETTINGS["Tiles"]["Count"]["y"]))
        
        self.__TILE_SIZE = Vector2((MAP_SETTINGS["Tiles"]["Size"]["x"],
                                    MAP_SETTINGS["Tiles"]["Size"]["y"]))
        self.__generate_terrain(camera)
        # self.__generate_resources(group)
        # camera.town_center = TownCenter([camera,camera.buildings_group])
        # starter_building = Building(camera, "starting_building", pos=Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), ct=0, to=2.5)
        # camera.town_center.set_size(Vector2(250, 150))
        # camera.town_center.construct()
        # camera.town_center.state = BuildingState.BUILT

    def __generate_terrain(self, group):
        total_map_size = self.__MAP_SIZE.elementwise()*self.__TILE_SIZE
        counter: int = 0
        for row in range(-int(total_map_size.y/2), int(total_map_size.y/2), 64):
            for col in range(-int(total_map_size.x/2), int(total_map_size.x/2), 64):
                tile = Tile((col, row), group, "grass")
                if randint(0, 9) % 4 == 0 and self.tree_count <= 3000:
                    i = randint(1, 9)
                    self.__generate_resources((col, row), group, ResourceType.WOOD, i, tile)
                elif randint(0, 13) % 7 == 0 and self.stone_count <= 300:
                    self.__generate_resources((col, row), group, ResourceType.STONE, 1, tile)

    def __generate_resources(self, pos: Vector2, camera, resource: ResourceType, image_enum: int, tile):
        obj = Resource(pos, camera, resource, image_enum, tile=tile)
        obj.add(camera.resources)
        if resource == ResourceType.WOOD:
            self.tree_count += 1
        if resource == ResourceType.STONE:
            self.stone_count += 1
                    
