#File for the Player class that contains the class features that the player interacts with

import pygame
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.lvlup_time = 8
        self.lvlup_timer = 0
        self.next_shot_timer = SHOT_COOLDOWN

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        player_shape = pygame.draw.polygon(screen, 'white', self.triangle(), 2)
        return player_shape
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        facing = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += facing * PLAYER_SPEED * dt

    def shoot(self):
        self.cooldown = self.next_shot_timer
        vector = pygame.Vector2(0, 1)
        directional_vector = vector.rotate(self.rotation)
        velocity = directional_vector * SHOT_SPEED
        Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt
        self.lvlup_timer += dt

        if self.lvlup_timer >= self.lvlup_time: #Simple lvlup function I added, decreases the time between shots by 20% every 8 seconds
            self.next_shot_timer /= 1.2
            self.lvlup_timer = 0
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if not self.cooldown > 0:
                self.shoot()    
            