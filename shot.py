import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2()
        

    def draw(self, screen):
        shot = pygame.draw.circle(screen, "red", self.position, self.radius, width=2)


    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)