import pygame
import os
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.map import Map
from Assets.camera import CameraGroup
from Assets.Controls.controls import Controls
from Assets.Player.player import Player
from Assets.SaveSystem.savable_object import SavableObject



# Generate the Map before the pygame windows is started
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Age of Empyres")
pygame.display.set_icon(pygame.image.load(f"{os.getcwd()}/Textures/grail.png"))
camera = CameraGroup()
world = Map(camera)
clock = pygame.time.Clock()
camera.custom_draw()
start_ticks = pygame.time.get_ticks()
player = Player(team=1, camera=camera)

for unit in camera.unit_group:
    SavableObject.pickle(unit)

while True:
    new_ticks = pygame.time.get_ticks()
    player.custom_update()
    Controls.event_handler(camera)
    if not camera.ui_group.isPaused:
        screen.fill((0, 204, 0))
        camera.update()
        camera.custom_draw()
        for unit in camera.unit_group.sprites():
            unit.custom_update()
        for building in camera.buildings_group:
            building.custom_update()
        for resource in camera.resources:
            resource.custom_update()
    camera.ui_group.custom_update()
    # screen.blit(text, (0, 0))
    pygame.display.update()
    clock.tick(60)
