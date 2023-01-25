from pygame import Vector2
from Assets.Buildings.building import Building
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.Buildings.states import BuildingState


class TownCenter(Building):
    def __init__(self, camera, team):
        super().__init__(camera, "town_center", team, hp=2400, pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), ct=0, to=3)
        self._set_image(self.texture)
        
    def instantly_build(self):
        self.set_size(Vector2(250, 200))
        self._construct()
        self.state = BuildingState.BUILT
        return self
