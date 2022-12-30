from pygame.math import Vector2 as Vector2
from Assets.settings import MAP_SETTINGS, SCREEN_HEIGHT, SCREEN_WIDTH
from Assets.tile import Tile
from random import randint
from Assets.Buildings.building import Building
from Assets.Buildings.states import BuildingState

class Map:
    def __init__(self, group):
        self.__MAP_SIZE = Vector2((MAP_SETTINGS["Tiles"]["Count"]["x"],
                                   MAP_SETTINGS["Tiles"]["Count"]["y"]))
        
        self.__TILE_SIZE = Vector2((MAP_SETTINGS["Tiles"]["Size"]["x"],
                                    MAP_SETTINGS["Tiles"]["Size"]["y"]))
        self.__generate_terrain(group)
        self.__generate_resources(group)
        starter_building = Building(group, "starting_building", pos=Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), ct=0, to=2.5)
        starter_building.construct()
        starter_building.state = BuildingState.BUILT
        
    def __generate_terrain(self, group) -> list:
        total_map_size = self.__MAP_SIZE.elementwise()*self.__TILE_SIZE
        counter: int = 0
        for row in range(-int(total_map_size.y/2), int(total_map_size.y/2), 64):
            for col in range(-int(total_map_size.x/2), int(total_map_size.x/2), 64):
                Tile((col, row), group, "grass")

    def __generate_resources(self, group):
        sprite_list = []
        for row in range(0, 20):
            for col in range(1, 9):
                # Random Tile Spacing in range
                rand_x = randint(45, 55)
                rand_y = randint(45, 60)
                y = row * rand_y
                x = col * rand_x
                tree = randint(1, 9)
                sprite_list.append(Tile((x, y), tile_type=f"Tree/summer_tree_{tree}"))
                for sprite in sorted(sprite_list, key=lambda sprite: sprite.rect.centery):
                    sprite.add(group)
                    
