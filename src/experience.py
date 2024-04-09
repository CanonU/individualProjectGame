import pygame

pygame.init()
class Orb:

    def __init__(self):
        self.color = (random.randint(0, 200), random.randint(0, 200),random.randint(0, 200))
        self.x = pygame.display.Info().current_w + self.radius
