import pygame
import circleshape
import constants
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius=radius)

        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        new_angle = random.uniform(20, 50)
        plus_vel = self.velocity.rotate(+new_angle)
        minus_vel = self.velocity.rotate(-new_angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        sub_asteriod_plus = Asteroid(self.position.x, self.position.y, new_radius)
        sub_asteriod_negative = Asteroid(self.position.x, self.position.y, new_radius)

        sub_asteriod_plus.velocity = 1.2 * plus_vel
        sub_asteriod_negative.velocity = 1.2 * minus_vel
