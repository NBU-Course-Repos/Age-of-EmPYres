from pygame.sprite import Group
from Assets.UserInterface.ui import UI
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.math import Vector2 as Vector2


class UIGroup(Group):
    def __init__(self):
        super().__init__(self)
        self.isPaused = False
        self.pause_menu = UI(pos=Vector2(335, 100), dimensions=Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT-150))
        self.bottom_bar = UI(group=self, image="bottom_bar",
                             pos=Vector2(235, 603))

    def set_pause(self):
        if self.isPaused:
            self.pause_menu.remove(self)
            self.isPaused = False
        else:
            self.pause_menu.add(self)
            self.isPaused = True
