import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        randomAngle = random.uniform(20, 50)
        newAngle1 = self.velocity.rotate(randomAngle)
        newAngle2 = self.velocity.rotate(-randomAngle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        newAsteroid1 = Asteroid(self.position[0], self.position[1], newRadius)
        newAsteroid2 = Asteroid(self.position[0], self.position[1], newRadius)
        newAsteroid1.velocity = newAngle1 * 1.2
        newAsteroid2.velocity = newAngle2 * 1.2

