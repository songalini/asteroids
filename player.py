from circleshape import *
from constants import *
from main import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.collidable = True
        self.collision_timer = 0
        self.colour = "blue"


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.colour, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
        

    def update(self, dt):
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt
        if self.collision_timer > 0:
            self.colour = "red"
            self.collision_timer -= dt
        if self.collision_timer <= 0:
            self.collidable = True
            self.colour = "blue"
            
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.check_boundaries()

    def check_boundaries(self):
        if self.position.x - self.radius < 0:
            self.position.x = self.radius
        if self.position.x + self.radius > SCREEN_WIDTH:
            self.position.x = SCREEN_WIDTH - self.radius
        if self.position.y - self.radius < 0:
            self.position.y = self.radius
        if self.position.y + self.radius > SCREEN_HEIGHT:
            self.position.y = SCREEN_HEIGHT - self.radius


    def shoot(self):
        if self.shot_cooldown > 0:
            return
        else:
            direction = pygame.Vector2(0,1).rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED
            bullet = Shot(self.position.x, self.position.y)
            bullet.velocity = velocity
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
