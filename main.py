import pygame
import sys
import os
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *
from score import *

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score = 0
    score_increment = 1
    font = pygame.font.Font(None, 36)

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable,)
    Shot.containers = (updateable, drawable, shots)
    player = Player(SCREEN_WIDTH/ 2, SCREEN_HEIGHT /2)
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        updateable.update(dt)

        for i in asteroids:
            if player.collision(i) == True:
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    score += score_increment
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        print(shots, asteroids, score)

        

        pygame.display.flip()

if __name__ == "__main__":
    main()