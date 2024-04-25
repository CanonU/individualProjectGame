import pygame
import random

pygame.init()
class Orb:

    def __init__(self):
        self.size = 10
        
        self.color = (random.randint(0, 200), random.randint(0, 200),random.randint(0, 200))
        self.x = pygame.display.Info().current_w + self.radius
        self.x = random.randint(self.radius, pygame.display.Info().current_w - 300 - self.radius)
        self.y = random.randint(self.radius, pygame.display.Info().current_h- 300 - self.radius)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y,size,size))
