import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH/ 2, SCREEN_HEIGHT /2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return




        dt = clock.tick(60) / 1000
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()




if __name__ == "__main__":
    main()