import sys
import pygame
from Assets.camera import CameraGroup
from Assets.tile import Tile, TILE_SIZE
from Assets.Scene.base_scene import MAP_LAYOUT
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.UserInterface.ui import UI

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Age of Empyres")

clock = pygame.time.Clock()
camera = CameraGroup()
ui_group = pygame.sprite.Group()

for row_index, row in enumerate(MAP_LAYOUT):
    for col_index, col in enumerate(row):
        x = col_index * TILE_SIZE;
        y = row_index * TILE_SIZE;
        Tile(pos=(x, y), group=camera, tile_type="sand")

ui = UI(ui_group)

while True:
    print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 204, 0))

    camera.update()
    camera.custom_draw()
    ui_group.update()
    ui_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
