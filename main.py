import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (updatable, drawable)

    dt = 0


    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print('Game over!')
                raise SystemExit
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()

        #player.update(dt)

        screen.fill((0, 0, 0))

        #player.draw(screen)

        for obj in drawable:
            obj.draw(screen) 

        pygame.display.flip()
    
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

