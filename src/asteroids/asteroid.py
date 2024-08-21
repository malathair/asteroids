import pygame
import random

import constants

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)

        new_velocities = [self.velocity.rotate(angle), self.velocity.rotate(-angle)]
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        for velocity in new_velocities:
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity * 1.2
