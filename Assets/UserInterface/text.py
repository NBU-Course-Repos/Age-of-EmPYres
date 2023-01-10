import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.sprite import AbstractGroup
from Assets.UserInterface.colors import Colors


class Text(Sprite):

    def __init__(self, group=AbstractGroup(), pos=Vector2(0, 0), text="", color=Colors.BLACK.value, font_size=20):
        super().__init__(group)
        self.color = color
        self.pos = pos
        self.font = pygame.font.SysFont(name="Trajan Bold", size=font_size)
        self.image = self.font.render(text, True, color, None).convert_alpha()  # Keep Antialias to True
        self.rect = self.image.get_rect()
        self.rect.midleft = pos

    def change_text(self, text, color=Colors.BLACK.value):
        self.image = self.font.render(text, True, self.color, None)
