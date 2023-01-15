from pygame.math import Vector2
from Assets.Resources.types import ResourceType
from Assets.Buildings.town_center import TownCenter
from Assets.Units.villager import Villager
from Assets.UserInterface.text import Text, Colors


class Player:

    def __init__(self, team: int, camera):
        self.camera = camera
        self.team = team
        self.resources: dict = {
            ResourceType.STONE: 200,
            ResourceType.WOOD: 200,
            ResourceType.BRONZE: 0,
            ResourceType.IRON: 0,
            ResourceType.FOOD: 200,
            ResourceType.GOLD: 120
        }
        self.units_max = 5
        self.units_cur = 4
        self._player_setup()
        self.ui = []

    # Init player Town center and starting units
    def _player_setup(self):
        self.HQ = TownCenter(self.camera, self.team)
        self.HQ.instantly_build()
        pos = Vector2(self.HQ.rect.left)
        for count in range(0, self.units_cur):
            Villager(self.camera, player=self, pos=pos)
            pos += Vector2(0, 50)

    def _generate_ui(self):
        ui = []
        pos = Vector2(0, 10)
        for resource in self.resources:
            element = Text(pos=pos, text=f"{resource.value.upper()}: {self.resources[resource]}",
                           font_size=20, color=Colors.WHITE.value)
            ui.append(element)
            pos = Vector2(element.rect.midright) + (10, 0)
        ui.append(Text(pos=pos, text=f"UNITS: {self.units_cur}/{self.units_max} ",
                       font_size=20, color=Colors.WHITE.value))
        return ui

    def _update_ui(self):
        self.camera.ui_group.remove(self.ui)
        self.ui = self._generate_ui()
        self.camera.ui_group.add(self.ui)

    def custom_update(self):
        self._update_ui()
