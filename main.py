import pygame
import sys
import os
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *


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
    lives = 3
    lives_decrement = 1
    score_increment = 1
    font = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 60)
    game_start = True
    game_over_timer = 30

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable,)
    Shot.containers = (updateable, drawable, shots)
    player = Player(SCREEN_WIDTH/ 2, SCREEN_HEIGHT /2)
    AsteroidField()
    while game_start == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        updateable.update(dt)

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
            
        for asteroid in asteroids:
            if asteroid.is_on_screen() and player.collision(asteroid) == True:
                if lives > 0:
                    if player.collidable == True:
                        player.collidable = False
                        player.collision_timer = 3
                        lives_lost_text = font2.render(f'Oh No!', True, (255, 255, 255))
                        screen.blit(lives_lost_text, (100, 100))
                        lives -= lives_decrement
            if lives <= 0:
                game_over_timer -= dt
                game_over_text = font2.render(f'Game Over!', True, (255, 255, 255))
                screen.blit(game_over_text, (200, 200))
                print(game_over_timer, game_start)
                if game_over_timer <= 0:
                    game_start = False
                    sys.exit()

        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_on_screen() and asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    score += score_increment

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        lives_text = font.render(f'Lives: {lives}', True, (255, 255, 255))
        screen.blit(lives_text, (10, 50))
        # print(asteroids)
        # print(f"collision timer: {player.collision_timer}, score = {score}") 
        #testingcode

        pygame.display.flip()

if __name__ == "__main__":
    main()