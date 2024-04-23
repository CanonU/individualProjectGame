import pygame
import random

pygame.init()

class Orb:
    def __init__(self):
        self.image = pygame.image.load("clock.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.radius = 10

        # Randomize initial position
        self.x = random.randint(0, pygame.display.Info().current_w - self.radius)
        self.y = random.randint(0, pygame.display.Info().current_h - self.radius)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_size(self):
        # Change the size of the image
        new_size = 10
