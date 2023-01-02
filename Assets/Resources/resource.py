import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.sprite import Group
from Assets.Resources.types import ResourceType
from Assets.Resources.states import ResourceStatus


class Resource(Sprite):
    def __init__(self, pos: Vector2, group: Group, rtype: ResourceType, image_enum=1, amount=20, tile=None):
        super().__init__(group)
        self._workers = Group()     # Sprite.Group to store the workers gathering this resource
        self.pos = Vector2(pos)
        self.resource_type = rtype
        self.amount = amount
        self.tile = tile
        self.state = ResourceStatus.UNTOUCHED
        self._start_ticks = 0
        self._time_passed = 0
        try:
            self.image = pygame.image.load(f"Assets/Textures/Resources/{self.resource_type.value}_{image_enum}.png")
        except FileNotFoundError:
            self.image = pygame.image.load(f"Assets/Textures/Resources/{self.resource_type}_1.png")
        if self.resource_type == ResourceType.WOOD or self.resource_type == ResourceType.STONE:
            self.image = self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(midbottom=tile.rect.center)
        self.add(group.resources)

    def get_workers(self):
        return self._workers.sprites()

    def get_position(self):
        return self.pos

    def add_worker(self, worker):
        if self._workers.has(worker):
            return
        else:
            self.state = ResourceStatus.GATHERED
            self._workers.add(worker)

    def remove_worker(self, worker):
        if self._workers.has(worker):
            self._workers.remove(worker)
        if not self._workers:
            self._start_ticks = 0
            self.state = ResourceStatus.UNTOUCHED

    def select(self):
        self.tile.draw_border()
        # print(self)
        # print(self.amount)
        # To do: Give information on self.amount

    def deselect(self):
        self.tile.delete_border()

    def _being_gathered(self):
        gather_rate = 0
        self.select()
        if self._start_ticks == 0:
            self._start_ticks = pygame.time.get_ticks()
        time_stamp = int((pygame.time.get_ticks() - self._start_ticks)/1000)
        if time_stamp - self._time_passed == 1:
            self._time_passed = time_stamp
            for worker in self._workers.sprites():
                if worker.resource_carrying[self.resource_type] == worker.resource_capacity[self.resource_type]:
                    print("offloading")
                    worker.set_offload()
                else:
                    gather_rate += worker.gather_rate
                    worker.resource_carrying[self.resource_type] += worker.gather_rate
            self.amount -= gather_rate
            print(self.amount)
        if self.amount == 0:
            self.kill()

    def custom_update(self):
        if self.state == ResourceStatus.UNTOUCHED:
            return
        if self.state == ResourceStatus.GATHERED:
            self._being_gathered()

