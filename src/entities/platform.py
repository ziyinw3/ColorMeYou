# platform class
# drawn with rect
# toggle opacity levels

# one of the following colors:

# cyan = (1, 176, 239)
# yellow = (255, 247, 1)
# magenta = (237, 0, 140)
# blue (cyan + magenta) = (11, 41, 181)
# red (magenta + yellow) = (169, 0, 46)
# green (cyan + yellow) = (0, 173, 32)

import pygame

from src.entities.entity import Entity


class Platform(Entity):
    def __init__(self, color, x_coord, y_coord, width, height, state):
        super().__init__(x_coord, y_coord, width, height)
        self.color = color
        self.state = state

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
