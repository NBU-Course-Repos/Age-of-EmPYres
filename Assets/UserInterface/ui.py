import pygame
from Assets.settings import SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.math import Vector2
import os

DEFAULT_DIMENSIONS = Vector2(SCREEN_WIDTH - SCREEN_WIDTH / 3, SCREEN_HEIGHT / 5)


class UI(pygame.sprite.Sprite):
    def __init__(self, pos=Vector2(0, 0), group=pygame.sprite.AbstractGroup(), dimensions=DEFAULT_DIMENSIONS, image="gray"):
        super().__init__(group)
        self.border_dimensions = dimensions
        self.pos = pos
        self.image = pygame.image.load(f"{os.getcwd()}/Assets/Textures/{image}.png")
        self.image = pygame.transform.scale(self.image, self.border_dimensions)
        self.rect = self.image.get_rect(topleft=self.pos)

