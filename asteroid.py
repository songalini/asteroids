from circleshape import *
from constants import *
from main import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.entered_screen = False
        self.velocity = pygame.Vector2()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)


    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)
        self.check_entered_screen()
        self.bounce()
    
    def check_entered_screen(self):
        if not self.entered_screen:
            if (self.radius <= self.position.x <= SCREEN_WIDTH - self.radius) and (self.radius <= self.position.y <= SCREEN_HEIGHT - self.radius):
                self.entered_screen = True

    def bounce(self):
        if self.entered_screen:
            if self.position.x - self.radius <= 0 or self.position.x + self.radius >= SCREEN_WIDTH:
                self.velocity.x = -self.velocity.x
            if self.position.y - self.radius <= 0 or self.position.y + self.radius >= SCREEN_HEIGHT:
                self.velocity.y = -self.velocity.y

    def is_on_screen(self):
        return (0 <= self.position.x <= SCREEN_WIDTH) and (0 <= self.position.y <= SCREEN_HEIGHT)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_a = Asteroid(self.position.x, self.position.y, new_radius)
            split_b = Asteroid(self.position.x, self.position.y, new_radius)
            split_a.velocity = self.velocity.rotate(angle)
            split_b.velocity = self.velocity.rotate(-angle)