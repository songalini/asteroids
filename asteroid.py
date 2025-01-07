from circleshape import *
from constants import *
from main import *
import random

class Asteroid(CircleShape):
    SHAPES = ["Circle", "Square", "Triangle", "Pentagon", "Hexagon"]
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2()
        self.entered_screen = False
        self.shape = random.choice(self.SHAPES)

    def draw(self, screen):
        if self.shape == "Circle":
            pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        elif self.shape == "Square":
            half_side = self.radius / 1.414  # side length of the square
            points = [
                (self.position.x - half_side, self.position.y - half_side),
                (self.position.x + half_side, self.position.y - half_side),
                (self.position.x + half_side, self.position.y + half_side),
                (self.position.x - half_side, self.position.y + half_side)
            ]
            pygame.draw.polygon(screen, "white", points, width=2)
        elif self.shape == "Triangle":
            points = [
                (self.position.x, self.position.y - self.radius),
                (self.position.x - self.radius, self.position.y + self.radius),
                (self.position.x + self.radius, self.position.y + self.radius)
            ]
            pygame.draw.polygon(screen, "white", points, width=2)
        elif self.shape == "Pentagon":
            points = self.generate_polygon(5)
            pygame.draw.polygon(screen, "white", points, width=2)
        elif self.shape == "Hexagon":
            points = self.generate_polygon(6)
            pygame.draw.polygon(screen, "white", points, width=2)

    def generate_polygon(self, num_sides):
        angle_step = 360 / num_sides
        vertices = []
        for i in range(num_sides):
            angle = i * angle_step
            x = self.position.x + self.radius * pygame.math.Vector2(1, 0).rotate(angle).x
            y = self.position.y + self.radius * pygame.math.Vector2(1, 0).rotate(angle).y
            vertices.append((x, y))
        return vertices
    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)
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