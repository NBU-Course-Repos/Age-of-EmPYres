import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.sprite import AbstractGroup


class Text(Sprite):

    def __init__(self, group=AbstractGroup(), pos=Vector2(0, 0), text: str = "this is a sample text", font_size=20):
        super().__init__(group)
        self.pos = Vector2(pos) # Converts it to Vector2 in case a tuple was passed in the constructor
        self.font = pygame.font.SysFont(name="Trajan Bold", size=font_size)
        self.image = self.font.render(text, True, (0, 0, 0), None)  # Keep Antialias to True
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def change_text(self, text: str):
        self.image = self.font.render(text, True, (0, 0, 0), None)
