import pygame
from Assets.Buildings.states import BuildingState
from pygame.math import Vector2
from Assets.settings import MAP_SETTINGS


class Building(pygame.sprite.Sprite):
    tile_x = MAP_SETTINGS["Tiles"]["Size"]["x"]
    tile_y = MAP_SETTINGS["Tiles"]["Size"]["y"]

    def __init__(self, group, texture, workers=0, hp=1000, ct=20):
        super().__init__(group)
        self.texture = texture
        self.building_state = BuildingState.PLACING
        self._workers = workers
        self._completion_time = ct
        # self._required_materials: dict
        self._tiles_occupied = 1
        self._remaining_build_time = self._completion_time     # To be used when the building process is paused
        self._health_points = hp
        self._position = Vector2(0, 0)
        self._size = Vector2(self._tiles_occupied*self.tile_x, self._tiles_occupied*self.tile_y)

    def add_worker(self):
        self._workers += 1

    def remove_worker(self):
        self._workers -= 1

    def _set_image(self, image, alpha=0):
        self.image = pygame.image.load(f"Assets//Textures//Buildings//{image}.png")
        self.image = pygame.transform.scale(self.image, self._size)
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect(topleft=self._position)

    def construct(self):
        if self._completion_time == 0:
            self.building_state = BuildingState.BUILT
            return
        if self._workers > 0:
            self.building_state = BuildingState.CONSTRUCTING
        else:
            self.building_state = BuildingState.PAUSE_CONSTRUCTION
            self._set_image("foundation", 255)
            # Do something

    def placing(self):
        self._position = pygame.mouse.get_pos()
        self._set_image(self.texture, alpha=255)

    def custom_update(self):
        print(self.building_state)
        if self.building_state == BuildingState.PLACING:
            self.placing()
        elif self.building_state == BuildingState.BUILT:
            return
        elif self.building_state == BuildingState.CONSTRUCTING:
            self.construct()
