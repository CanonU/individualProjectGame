import pygame
import random

pygame.init()
class Orb:

    def __init__(self):
        self.size = 15
        
        self.color = (random.randint(0, 200), random.randint(0, 200),random.randint(0, 200))
        self.x = random.randint(self.size, pygame.display.Info().current_w - 300 - self.size)
        self.y = random.randint(self.size, pygame.display.Info().current_h- 300 - self.size)

    def draw(self, screen):
        #pygame.draw.rect(screen, self.color, (self.x, self.y,self.size,self.size))
        pygame.draw.rect(screen,self.color, (self.x - self.size // 2, self.y - self.size // 2, self.size, self.size))
