import pygame
from circleshape import CircleShape
from constants import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)

        #self.position = pygame.Vector2(x, y)


    def update(self, dt):
        self.position += self.velocity * dt


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255, 0) , self.position, self.radius, 2)

