from Assets.Units.unit import Unit
import pygame
from pygame.math import Vector2


class Villager(Unit):
    def __init__(self, group, pos=Vector2(0, 0), image="villager", hp=100, size=Vector2(30, 30)):
        super().__init__(group, pos, image, hp, size)

    def select_unit(self, image="villager_selected"):
        self.image = pygame.image.load(f"Assets/Textures/Units/{image}.png")
        self.image = pygame.transform.scale(self.image, self.size)