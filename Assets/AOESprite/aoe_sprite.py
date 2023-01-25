from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.math import Vector2


"""A custom implementation of pygame.sprite. Used for organizing common attributes and
   methods between the different Sprites
"""


class AOESprite(Sprite):

    def __init__(self):
        super().__init__()

    def draw(self, surface: Surface, pos=Vector2(0, 0)):
        surface.blit(self.image, pos)

