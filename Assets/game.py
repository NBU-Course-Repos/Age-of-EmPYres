import sys
import pygame
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.map import Map
from Assets.Tiles.groups import *
from Assets.Units.villager import Villager
from Assets.controls import Controls

# Generate the Map before the pygame windows is started
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Age of Empyres")
pygame.display.set_icon(pygame.image.load("Assets/Textures/grail.png"))
camera = CameraGroup()
ui_group = UIGroup()

world = Map(camera)

clock = pygame.time.Clock()
camera.custom_draw()
villager = Villager(camera)
unit_group = pygame.sprite.Group()
villager.add(unit_group)

while True:
    Controls.event_handler(unit_group=unit_group, ui_group=ui_group)
    if not ui_group.isPaused:
        screen.fill((0, 204, 0))
        camera.update()
        camera.custom_draw()
    for unit in unit_group.sprites():
        unit.custom_update()

    ui_group.update()
    ui_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
