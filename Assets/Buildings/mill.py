from Assets.Buildings.building import Building
from Assets.Buildings.states import BuildingState


class Mill(Building):
    def __init__(self, group):
        super().__init__(group, texture="mill", ct=5)  # remove ct 5 after fixing building creation
        self._set_image("mill")
        print("Initializing new Mill")
        print(self._remaining_build_time)

    def custom_update(self):
        if self.state == BuildingState.PLACING:
            self._placing()
        elif self.state == BuildingState.BUILT:
            self.groups()[0].has_mill = True # Camera group
            return
        elif self.state == BuildingState.CONSTRUCTING or self.state == BuildingState.PAUSE_CONSTRUCTION:
            self._construct()