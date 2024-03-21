#Canon U

import pygame
import sys

class Target:
    def __init__(self, x, y, image, function):
        self.rect = image.get_rect(topleft=(x, y))
        self.image = image
        self.function = function

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.function()
