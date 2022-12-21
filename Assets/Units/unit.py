import pygame
from pygame.math import Vector2 as Vector2
from Assets.UserInterface.ui import UI


class Unit(pygame.sprite.Sprite):
    def __init__(self, group, pos=Vector2(0, 0), image="", hp=100, size=Vector2(0, 0), speed=100):
        super().__init__(group)
        self.health_points = hp
        self.size = size
        self.pos = pos
        self.name = ""
        self.movement_speed = speed
        self.image = pygame.image.load(f"Assets/Textures/Units/{image}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.isSelected = False

    def update_rect(self, pos):
        self.pos = pos

    def select_unit(self, image=""):
        if self.isSelected:
            return
        self.isSelected = True
        self.image = pygame.image.load(f"Assets/Textures/Units/{image}.png")
        self.image = pygame.transform.scale(self.image, self.size)

    def move(self, pos):
        if self.rect.center != pos:
            # TO DO: Need to calculate the correct move offset from below to reach pos
            self.rect.move(self.movement_speed, self.movement_speed)
            self.move(pos)

