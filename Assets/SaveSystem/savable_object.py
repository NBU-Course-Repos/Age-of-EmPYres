import pickle
import pygame
from pprint import pprint


class SavableObject:

    def __init__(self):
        return


    @staticmethod
    def pickle(obj):
        data = dict(obj.__dict__)
        for key in list(data.keys()):
            if issubclass(type(data[key]), pygame.Surface):
                # wh = [data[key].get_width(), data[key].get_height()] # Get Width and height of the surface
                data[key] = pygame.image.tobytes(data[key], "RGB")
                # data[key] = pygame.image.frombytes(data[key], wh, "RGB")  # Convert from bytes to a Surface
            # pprint(pickle.dumps(data[key]))

        return data
