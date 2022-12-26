import pygame.display
from pygame.sprite import Group
from pygame.math import Vector2 as Vector2
from Assets.UserInterface.ui import UI
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.UserInterface.Buttons.buildings_button import BuildingsButton


class UIGroup(Group):
    isPaused = False
    PAUSE_MENU = UI(pos=Vector2(335, 100), dimensions=Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 150))
    villager_buttons_display = False
    rendered_buttons = []
    buttons = Group()

    def __init__(self):
        super().__init__(self)
        self.civilian_building = None
        self.bottom_bar = UI(group=self, image="bottom_bar",
                             pos=Vector2(235, 603))
        self.bottom_left_bar = UI(group=self, image="dirt",
                                  pos=Vector2(0, 603), dimensions=(235, 603))

    def set_pause(self):
        if self.isPaused:
            self.PAUSE_MENU.remove(self)
            self.isPaused = False
        else:
            self.PAUSE_MENU.add(self)
            self.isPaused = True

    def render_villager_buttons(self):
        if UIGroup.buttons.sprites():
            UIGroup.clear_buttons()
        button = BuildingsButton(group=UIGroup.buttons, pos=self.bottom_left_bar.pos+Vector2(20, 20))
        button.add(self)

    @staticmethod
    def clear_buttons():
        print("Clearing buttons")
        for button in UIGroup.buttons.sprites():
            button.kill()
        UIGroup.buttons.empty

    def custom_update(self):
        self.update()
        self.draw(pygame.display.get_surface())
        UIGroup.buttons.update()
        UIGroup.buttons.draw(pygame.display.get_surface())