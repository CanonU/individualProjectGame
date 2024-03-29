
import pygame
import random


pygame.init()
class Circle:

  def __init__(self):
    self.dodgescore = 0
    #Declare radius
    self.radius = random.randint(10,20)
    #decide side
    if random.randint(0,1) == 0:
      #left or right 
      self.x = random.randint(0,pygame.display.Info().current_w)
      if random.randint(0,1) == 0:
        #left 
        self.y = -self.radius
      else:
        #right 
        self. y = pygame.display.Info().current_h + self.radius
    else:
      #top or bottom
      self.y = random.randint(0,pygame.display.Info().current_h)
      if random.randint(0,1) == 0:
        #top
        self.x = -self.radius
      else:
        #bottom
        self.x = pygame.display.Info().current_w + self.radius
    self.color = random.randint(0, 200), random.randint(0, 200),random.randint(0, 200)
    self.xspeed = random.uniform(-3,3)
    self.yspeed = random.uniform(-3,3)
    #make sure they will always move
    if self.xspeed == 0:
      self.xspeed = 1
    if self.yspeed == 0:
      self.yspeed = 1    
    
  #make the circle visible
  def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    
    
  #circle movement
  def move(self):
    self.x += self.xspeed
    self.y += self.yspeed
    #disapear when outside of screen
    if self.x >= pygame.display.Info().current_w+self.radius or self.x <= -self.radius:
      self.radius = random.randint(10,30)
      self.dodgescore += 1

      if random.randint(0,1) == 0:
        self.x = random.randint(0,pygame.display.Info().current_w+self.radius)
        self.y = -self.radius
      else:
        self.y = random.randint(0,pygame.display.Info().current_h+self.radius)
        self.x = -self.radius
      self.color = random.randint(0, 200), random.randint(0, 200),random.randint(0, 200)
      self.xspeed = random.uniform(-3,3)
      self.yspeed = random.uniform(-3,3)
      if self.xspeed == 0:
        self.xspeed = 1
      if self.yspeed == 0:
        self.yspeed = 1
    if self.y >= pygame.display.Info().current_h+self.radius or self.y <= -self.radius:
      self.radius = random.randint(10,30)
      if random.randint(0,1) == 0:
        self.x = random.randint(0,pygame.display.Info().current_w+self.radius)
        self.y = -self.radius
      else:
        self.y = random.randint(0,pygame.display.Info().current_h+self.radius)
        self.x = -self.radius
      self.color = random.randint(0, 200), random.randint(0, 200),random.randint(0, 200)
      self.xspeed = random.uniform(-3,3)
      self.yspeed = random.uniform(-3,3)
      if self.xspeed == 0:
        self.xspeed = 1
      if self.yspeed == 0:
        self.yspeed = 1
