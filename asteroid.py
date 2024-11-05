#This file contains the class for the asteroid npc/environment objects
import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid_shape = pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)
        return asteroid_shape
    
    def update(self, dt):
        self.position += (self.velocity * dt)