import pygame
import circleshape
import constants


class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius=constants.SHOT_RADIUS):
        super().__init__(x, y, radius=radius)

        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
