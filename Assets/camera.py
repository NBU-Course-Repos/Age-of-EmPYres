import pygame
from Assets.settings import SCREEN_WIDTH,SCREEN_HEIGHT

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self)
        self.displaySurface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.offsetX = self.offsetY = 0

    @staticmethod
    def __update_offset(self):
        # By How much should the screen move
        offset_pixels = 10
        mouse_pos = pygame.mouse.get_pos()
        mouseX = mouse_pos[0]
        mouseY = mouse_pos[1]

        # Left side of screen
        if mouseX <= 3:
            self.offsetX += offset_pixels
        # Right side of screen
        elif mouseX >= SCREEN_WIDTH - 3:
            self.offsetX -= offset_pixels
        # Top of the screen
        if mouseY <= 3:
            self.offsetY += offset_pixels
        # Bottom of the screen
        elif mouseY >= SCREEN_HEIGHT - 3:
            self.offsetY -= offset_pixels

        self.offset.update(self.offsetX, self.offsetY)

    def print(self):
        print(len(self.sprites()))

    def custom_draw(self):
        self.__update_offset(self)
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft + self.offset
            self.displaySurface.blit(sprite.image, offset_pos)
