from pygame.sprite import Group
from Assets.UserInterface.ui import UI
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.math import Vector2 as Vector2


class UIGroup(Group):
    civilian_buttons = []
    isPaused = False
    PAUSE_MENU = UI()
    villager_buttons_display = False

    def __init__(self):
        super().__init__(self)
        self.civilian_building = None
        self.bottom_bar = UI(group=self, image="bottom_bar",
                             pos=Vector2(235, 603))
        self.bottom_left_bar = UI(group=self, image="dirt",
                                  pos=Vector2(0, 603), dimensions=(235, 603))
        self.pause_menu = UI(pos=Vector2(335, 100), dimensions=Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 150))
        self.PAUSE_MENU = self.pause_menu

    def set_pause(self):
        if self.isPaused:
            self.PAUSE_MENU.remove(self)
            self.isPaused = False
        else:
            self.PAUSE_MENU.add(self)
            self.isPaused = True

    def set_villager_buttons(self):
        if len(self.civilian_buttons) > 0:
            return
        starting_pos = self.bottom_left_bar.pos + Vector2(20, 20)
        self.civilian_building = UI(starting_pos, dimensions=Vector2(40, 40),
                                    group=self, image="Icons//civil_building")
