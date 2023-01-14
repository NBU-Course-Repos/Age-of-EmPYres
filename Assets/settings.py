from pygame.math import Vector2
# Global vars used across the different python files
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 704
MAP_SETTINGS = {
    "Tiles": {
        "Count": {  # Total Map Dimensions in Tiles Count
            "x": 60,
            "y": 60
        },
        "Size": {  # Single Tile Dimensions
            "x": 64,
            "y": 64
        }
    }
}
MAP_SIZE = Vector2((MAP_SETTINGS["Tiles"]["Count"]["x"],
                    MAP_SETTINGS["Tiles"]["Count"]["y"]))

TILE_SIZE = Vector2((MAP_SETTINGS["Tiles"]["Size"]["x"],
                     MAP_SETTINGS["Tiles"]["Size"]["y"]))