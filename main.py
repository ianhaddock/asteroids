import pygame
from constants import *
from player import *

def main():
    pygame.init()

    clck = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # player object
    y = SCREEN_WIDTH / 2
    x = SCREEN_HEIGHT / 2
    p = player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()

        p.draw(screen)
    
        clck.tick(60)


if __name__ == "__main__":
    main()

