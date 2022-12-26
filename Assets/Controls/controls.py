import pygame
import sys
from pygame.math import Vector2
from Assets.Buildings.house import House
from Assets.Controls.states import ControlStates


class Controls:
    selectedObjects = []
    _building: House
    state = ControlStates.NOTHING

    @staticmethod
    def event_handler(camera, unit_group, ui_group, building_group):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Turn on/off game pause
                ui_group.set_pause()
            # Check if left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if __class__.state == ControlStates.BUILDING:
                    __class__._building.construct()
                    __class__.state = ControlStates.NOTHING
                mouse_pos = Vector2(pygame.mouse.get_pos())
                selected_count = 0
                for unit in unit_group.sprites():
                    if unit.pos.x + unit.rect.w > mouse_pos.x > unit.pos.x - unit.rect.w and \
                       unit.pos.y + unit.rect.h > mouse_pos.y > unit.pos.y - unit.rect.h:
                        __class__.state = ControlStates.UNIT
                        unit.select(ui_group)
                        __class__.selectedObjects.append(unit)
                        selected_count += 1
                if selected_count == 0 and len(__class__.selectedObjects):
                    # if there aren't any selected object in the last left mouse click deselect
                    # the ones that were previously selected
                    for obj in __class__.selectedObjects:
                        obj.deselect(ui_group=ui_group)
                    __class__.selectedObjects.clear()

            # Check if right mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                mouse_pos = Vector2(pygame.mouse.get_pos())
                if __class__.state == ControlStates.UNIT:
                    for obj in __class__.selectedObjects:
                        obj.set_move(mouse_pos)

                elif __class__.state == ControlStates.BUILDING:
                    __class__._building

            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                __class__.state = ControlStates.BUILDING
                __class__._building = House(camera)
                __class__._building.add(building_group)

