import pygame


class Entity:
    def __init__(self, x_coord, y_coord, width, height):
        self.rect = pygame.Rect(x_coord, y_coord, width, height)
        self.initial_rect = pygame.Rect(x_coord, y_coord, width, height)
    def draw(self, screen):
        pass
    # reset to init position
    def reset(self):
        self.rect = self.initial_rect.copy()
    
    # def respawn(self, last_obtained):
        
