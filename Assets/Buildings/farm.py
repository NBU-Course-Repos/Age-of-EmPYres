from Assets.Buildings.building import Building
from Assets.Buildings.states import BuildingState


class Farm(Building):
    def __init__(self, group):
        super().__init__(group, texture="farm1", ct=0)  # remove ct 5 after fixing building creation
        self._set_image("farm")
        print("Initializing new Farm")
        print(self._remaining_build_time)
