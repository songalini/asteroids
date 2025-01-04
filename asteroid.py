from circleshape import *
from constants import *
from main import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid = pygame.draw.circle(screen, "white", self.position, self.radius, width=2)


    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)