#Class for the player's shots - these destroy asteroid class objects

from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        shot_shape = pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
        return shot_shape
    
    def update(self, dt):
        self.position += self.velocity * dt
