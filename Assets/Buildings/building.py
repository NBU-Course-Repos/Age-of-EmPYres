import pygame
from pygame.sprite import Group
from Assets.Buildings.states import BuildingState
from pygame.math import Vector2
from Assets.settings import MAP_SETTINGS


class Building(pygame.sprite.Sprite):
    tile_x = MAP_SETTINGS["Tiles"]["Size"]["x"]
    tile_y = MAP_SETTINGS["Tiles"]["Size"]["y"]

    def __init__(self, group, texture, team=1, hp=1000, ct=20, to=2, pos=Vector2(0, 0)):
        super().__init__(group)
        self.texture = texture      # Image to use for the building
        self.state = BuildingState.PLACING   # Initial building state
        self._workers = Group()     # Sprite.Group to store the worker assigned to the building
        self._completion_time = ct  # Total time that it should take to construct a building
        # self._required_materials: dict
        self._tiles_occupied = to     # Used to determine the number of tiles used in every coordinate
        self._remaining_build_time = self._completion_time  # To be used when the building process is paused
        self._health_points = hp     # HP for the building
        self.pos: Vector2 = pos      # Building Position
        self._start_ticks = 0  # Used as time to denote the construction start
        self._size = Vector2(self._tiles_occupied * self.tile_x, self._tiles_occupied * self.tile_y)  # Image dimensions
        self.team = team

    def set_size(self, size: Vector2):
        self._size = size

    def get_workers(self):
        return self._workers.sprites()

    def add_worker(self, worker):
        if self._workers.has(worker):
            return
        else:
            self._workers.add(worker)

    def remove_worker(self, worker):
        if self._workers.has(worker):
            self._workers.remove(worker)

    def _set_image(self, image, alpha=255):
        self.image = pygame.image.load(f"Assets//Textures//Buildings//{image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, self._size)
        # self.image.set_alpha(alpha)
        self.rect = self.image.get_rect(center=self.pos)
        self.mask = pygame.mask.from_surface(self.image, threshold=127)
        print(self.mask.count())
        # print("Image size")
        # print(self.image.get_size())
        # print("Mask size")
        # print(self.mask.get_size())
        # print("Ret size")
        # print(self.rect.size)

    def construct(self):
        if self._remaining_build_time == 0:  # Complete construction
            self._set_image(self.texture)
            self.state = BuildingState.BUILT
            return
        if self._workers.sprites() and self.state != BuildingState.BUILT:  # Start Constructing the building
            if self._start_ticks == 0:
                self._start_ticks = pygame.time.get_ticks()
            self.state = BuildingState.CONSTRUCTING
            workers_cnt = len(self._workers.sprites())
            self._remaining_build_time = self._completion_time - int((pygame.time.get_ticks()-self._start_ticks)/1000)*workers_cnt
            print("ticks: " + str(pygame.time.get_ticks()/1000))
            print("remaining time " + str(self._remaining_build_time))
        else:  # Pause Construction
            self.state = BuildingState.PAUSE_CONSTRUCTION
            self._start_ticks = 0  # If the construction is paused reset the start time
            self._set_image("foundation", 255)

    def get_position(self):
        return Vector2(self.pos)

    def placing(self):
        self.pos = Vector2(pygame.mouse.get_pos())
        self._set_image(self.texture)

    def highlight_foundation(self):
        if self.state != BuildingState.BUILT:
            self._set_image("foundation-selection")

    def is_colliding(self):
        for sprite in self.groups()[0].resources.sprites():
            print(self.mask.overlap_area(sprite.mask, (0, 0)))
            if self.mask.overlap_area(sprite.mask, (0, 0)) > 0:
                return True
        return False

    def custom_update(self):
        if self.state == BuildingState.PLACING:
            self.placing()
        elif self.state == BuildingState.BUILT:
            return
        elif self.state == BuildingState.CONSTRUCTING or self.state == BuildingState.PAUSE_CONSTRUCTION:
            self.construct()
