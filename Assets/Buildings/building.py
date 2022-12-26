import pygame
from pygame.sprite import Group
from Assets.Buildings.states import BuildingState
from pygame.math import Vector2
from Assets.settings import MAP_SETTINGS


class Building(pygame.sprite.Sprite):
    tile_x = MAP_SETTINGS["Tiles"]["Size"]["x"]
    tile_y = MAP_SETTINGS["Tiles"]["Size"]["y"]

    def __init__(self, group, texture, hp=1000, ct=20):
        super().__init__(group)
        self.texture = texture
        self.building_state = BuildingState.PLACING
        self._workers = Group()
        self._completion_time = ct
        # self._required_materials: dict
        self._tiles_occupied = 1
        self._remaining_build_time = self._completion_time  # To be used when the building process is paused
        self._health_points = hp
        self._position = Vector2(0, 0)
        self._size = Vector2(self._tiles_occupied * self.tile_x, self._tiles_occupied * self.tile_y)

    def add_worker(self, worker):
        if self._workers.has(worker):
            return
        else:
            self._workers.add(worker)

    def remove_worker(self, worker):
        if self._workers.has(worker):
            self._workers.remove(worker)

    def _set_image(self, image, alpha=255):
        self.image = pygame.image.load(f"Assets//Textures//Buildings//{image}.png")
        self.image = pygame.transform.scale(self.image, self._size)
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect(center=self._position)

    def construct(self):
        if self._completion_time == 0:
            self.building_state = BuildingState.BUILT
            return
        if self._workers.sprites():
            print(self._remaining_build_time)
            self.building_state = BuildingState.CONSTRUCTING
            _remaining_build_time = pygame.time.get_ticks()
            if self._remaining_build_time <= 0:
                self._set_image(self.texture)
                self.building_state == BuildingState.BUILT
            workers_cnt = len(self._workers.sprites())
            self._remaining_build_time = self._completion_time - int(pygame.time.get_ticks()/1000)*workers_cnt
        else:
            self.building_state = BuildingState.PAUSE_CONSTRUCTION
            self._set_image("foundation", 255)
            # Do something

    def get_position(self):
        return Vector2(self._position)

    def placing(self):
        self._position = pygame.mouse.get_pos()
        self._set_image(self.texture, alpha=255)

    def custom_update(self):
        if self.building_state == BuildingState.PLACING:
            self.placing()
        elif self.building_state == BuildingState.BUILT:
            return
        elif self.building_state == BuildingState.CONSTRUCTING or self.building_state == BuildingState.PAUSE_CONSTRUCTION:
            self.construct()
