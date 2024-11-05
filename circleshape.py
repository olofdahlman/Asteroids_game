#File containing a class object for circle shaped enteties

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes will override this method with their own
        pass

    def update(self, dt):
        # sub-classes will override this method with their own
        pass

    def collide(self, object):
        return (self.position.distance_to(object.position) <= self.radius + object.radius)