import pygame


class Building:
    def __init__(self):
        self._workers: int
        self._completion_time: int
        self._required_materials: dict
        self._is_built = False
        self._tiles_occupied: int
        self._image: pygame.image
        self._remaining_build_time: int # To be used when the building process is paused
        self._health_points: int

    def build(self):
        if self._is_built:
            return
        else:
            return
            # Do something

    def destroy(self):
        if self._is_built:
            # Do something
            return
        else:
            return

