import pygame
import random

pygame.init()
class Orb:

    def __init__(self):
        self.radius = 10
        self.color = (random.randint(0, 200), random.randint(0, 200),random.randint(0, 200))
        self.x = random.randint(self.radius, pygame.display.Info().current_w - self.radius)
        self.y = random.randint(self.radius, pygame.display.Info().current_h - self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
