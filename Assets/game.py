import pygame
import os
from Assets.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from Assets.map import Map
from Assets.camera import Camera
from Assets.Controls.controls import Controls
from Assets.Player.player import Player
from Assets.SaveSystem.savable_object import SavableObject


pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Age of Empyres")
pygame.display.set_icon(pygame.image.load(f"{os.getcwd()}/Assets/Textures/grail.png"))
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
camera = Camera()
world = Map(camera)
camera.custom_draw()
player = Player(team=1, camera=camera)

while True:
    new_ticks = pygame.time.get_ticks()
    player.custom_update()
    Controls.event_handler(camera)
    if not camera.ui_group.isPaused:
        screen.fill((0, 204, 0))
        camera.custom_draw()
        camera.update()
    camera.ui_group.custom_update()
    # screen.blit(text, (0, 0))
    pygame.display.update()
    clock.tick(60)
