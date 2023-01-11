import pygame
import sys
from pygame.math import Vector2

from Assets.Buildings.town_center import TownCenter
from Assets.Units.villager import Villager
from Assets.Buildings.house import House
from Assets.Buildings.building import Building
from Assets.Controls.states import ControlStates
from Assets.Buildings.states import BuildingState
from Assets.Units.unit import Unit
from Assets.Resources.resource import Resource


class Controls:
    selectedObjects = []
    building: Building
    state = ControlStates.NOTHING

    # Used to deselect object of class_type. For ex. we want only one resource selected, only one building, etc.
    @staticmethod
    def __deselect_same(class_type):
        for selected in Controls.selectedObjects:
            if issubclass(type(selected), class_type):
                selected.deselect()
                Controls.selectedObjects.remove(selected)

    @staticmethod
    def is_clicked(obj, mouse_pos):
        obj_x = obj.pos.x
        obj_y = obj.pos.y
        if obj_x < mouse_pos.x < obj_x + obj.rect.w and \
                obj_y < mouse_pos.y < obj_y + obj.rect.h:
            return True
        return False

    @staticmethod
    def __clear_selected():
        for obj in Controls.selectedObjects:
            obj.deselect()
        Controls.selectedObjects.clear()

    @staticmethod
    def event_handler(camera):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Turn on/off game pause
                camera.ui_group.set_pause()
            # Check if left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if Controls.state == ControlStates.PLACING:
                    # If in Building placement mode
                    Controls.building.construct()  # Here if the building is not built, its state is set to CONSTRUCTING
                    Controls.state = ControlStates.UNIT
                    for unit in Controls.selectedObjects:
                        if type(unit) == Villager:
                            unit.set_construct(Controls.building)

                mouse_pos = Vector2(pygame.mouse.get_pos())
                selected_count = 0

                for resource in camera.resources.sprites():
                    if Controls.is_clicked(resource, mouse_pos):
                        Controls.__clear_selected()
                        resource.select()
                        selected_count += 1
                        Controls.selectedObjects.append(resource)
                        break

                # Selected Units
                for unit in camera.unit_group.sprites():
                    if Controls.is_clicked(unit, mouse_pos):
                        Controls.__clear_selected()
                        Controls.state = ControlStates.UNIT
                        unit.select()
                        Controls.selectedObjects.append(unit)
                        selected_count += 1
                        break

                # If any of the ui is clicked, don't deselect the selected objects
                for ui in camera.ui_group.sprites():
                    if Controls.is_clicked(ui, mouse_pos):
                        selected_count += 1

                # If button has been clicked, perform its action
                for button in camera.ui_group.rendered_buttons:
                    if Controls.is_clicked(button, mouse_pos):
                        selected_count += 1
                        button.action(camera, camera.buildings_group)
                        break

                if selected_count == 0 and len(Controls.selectedObjects):
                    # if there aren't any selected object in the last left mouse click deselect
                    # the ones that were previously selected
                    for obj in Controls.selectedObjects:
                        obj.deselect()
                    Controls.selectedObjects.clear()

            # Check if right mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                mouse_pos = Vector2(pygame.mouse.get_pos())
                target = None
                # If a foundation is selected set it as a target
                for building in camera.buildings_group.sprites():
                    if Controls.is_clicked(building, mouse_pos) and building.state != BuildingState.BUILT:
                        target = building
                        building.highlight_foundation()
                        break
                    elif Controls.is_clicked(building, mouse_pos) and type(building) == TownCenter:
                        target = building
                        break

                for resource in camera.resources.sprites():
                    if Controls.is_clicked(resource, mouse_pos):
                # Controls.__deselect_same(Resource)
                        target = resource
                        break

                if Controls.state == ControlStates.UNIT:
                    for obj in Controls.selectedObjects:
                        # if the Unit is a villager and there the target is a foundation,
                        # finish constructing it
                        if type(obj) == Villager:
                            if issubclass(type(target), TownCenter):
                                obj.set_deposit()
                            elif issubclass(type(target), Building):
                                obj.set_construct(target)
                            elif issubclass(type(target), Resource):
                                obj.set_gather(target)
                        elif issubclass(type(obj), Unit):
                            obj.set_move(mouse_pos)

                elif Controls.state == ControlStates.PLACING:
                    Controls.building.kill()  # Stop placing the building

            # House building shortcut
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                Controls.state = ControlStates.PLACING
                Controls.building = House(camera)
                Controls.building.add(camera.buildings_group)

