import pygame
import random

pygame.init()

class Circle:

    def __init__(self):
        self.dodgescore = 0
        self.radius = random.randint(10, 20)
        
        # Randomly determine the side of the screen
        side = random.randint(0, 3)  # 0: top, 1: right, 2: bottom, 3: left
        
        if side == 0:  # Top side
            self.x = random.randint(0, pygame.display.Info().current_w)
            self.y = -self.radius
        elif side == 1:  # Right side
            self.x = pygame.display.Info().current_w + self.radius
            self.y = random.randint(0, pygame.display.Info().current_h)
        elif side == 2:  # Bottom side
            self.x = random.randint(0, pygame.display.Info().current_w)
            self.y = pygame.display.Info().current_h + self.radius
        else:  # Left side
            self.x = -self.radius
            self.y = random.randint(0, pygame.display.Info().current_h)
        
        self.color = random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)
        self.xspeed = random.uniform(-3, 3)
        self.yspeed = random.uniform(-3, 3)
        
        if self.xspeed == 0:
            self.xspeed = 1
        if self.yspeed == 0:
            self.yspeed = 1

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius + 2)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        
        if self.x >= pygame.display.Info().current_w + self.radius or self.x <= -self.radius:
            self.radius = random.randint(10, 30)
            self.dodgescore += 1
            
            side = random.randint(0, 1)  # 0: top/bottom, 1: left/right
            if side == 0:  # Top or bottom side
                self.x = random.randint(0, pygame.display.Info().current_w + self.radius)
                if random.randint(0, 1) == 0:
                    self.y = -self.radius
                else:
                    self.y = pygame.display.Info().current_h + self.radius
            else:  # Left or right side
                self.y = random.randint(0, pygame.display.Info().current_h + self.radius)
                if random.randint(0, 1) == 0:
                    self.x = -self.radius
                else:
                    self.x = pygame.display.Info().current_w + self.radius
                    
            self.color = random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)
            self.xspeed = random.uniform(-3, 3)
            self.yspeed = random.uniform(-3, 3)
            if self.xspeed == 0:
                self.xspeed = 1
            if self.yspeed == 0:
                self.yspeed = 1

        if self.y >= pygame.display.Info().current_h + self.radius or self.y <= -self.radius:
            self.radius = random.randint(10, 30)
            side = random.randint(0, 1)  # 0: top/bottom, 1: left/right
            if side == 0:  # Top or bottom side
                self.x = random.randint(0, pygame.display.Info().current_w + self.radius)
                if random.randint(0, 1) == 0:
                    self.y = -self.radius
                else:
                    self.y = pygame.display.Info().current_h + self.radius
            else:  # Left or right side
                self.y = random.randint(0, pygame.display.Info().current_h + self.radius)
                if random.randint(0, 1) == 0:
                    self.x = -self.radius
                else:
                    self.x = pygame.display.Info().current_w + self.radius
                    
            self.color = random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)
            self.xspeed = random.uniform(-3, 3)
            self.yspeed = random.uniform(-3, 3)
            if self.xspeed == 0:
                self.xspeed = 1
            if self.yspeed == 0:
                self.yspeed = 1
