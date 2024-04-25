#Canon Unguren
import pygame
import math
import random
from experience import Orb
from circle import Circle
mousex, mousey = pygame.mouse.get_pos()
timeScore = 0
minuteScore =0
play = False
#Initialize timer variables
pygame.init()
score = 0
current_time = 0
timer_interval = 75
circle_count = 50
Orb_count = 3
level = 0
Orbs= [Orb() for _ in range(Orb_count)]
circles = [Circle() for _ in range(circle_count)]
size = 10
increaseCircleCount = 0


    
#pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w-300,pygame.display.Info().current_h-300))

clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None,20)

# Start Screen 
while not play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = True

    screen.fill((255, 255, 255))

    welcome = font.render("No Pain No Game", True, (0, 0, 0))
    screen.blit(welcome, (150, 250))

    begin_text = font.render("Click anywhere to start", True, (0, 0, 0))
    screen.blit(begin_text, (150, 300))

    pygame.display.flip()

    # Check for mouse click to start the game
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            play = True
            pygame.mouse.set_visible(False)





#Main Game loop
while play:
    #pygame.mouse.set_visible(False)
    screen.fill((255, 255, 255))

    if timeScore >= 10:
        timeRender = font.render(f"Time: {minuteScore}:{timeScore}", True, (0, 0, 0))
    if timeScore <= 9:
        timeRender = font.render(f"Time: {minuteScore}:0{timeScore}", True, (0, 0, 0))
    levelRender = font.render(f"Level(xp):{level}({level*5})",True,(0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = pygame.mouse.get_pos()
    pygame.draw.circle(screen,(0,0,0),(mousex,mousey), size)

    for circle in circles:
        circle.move()
        circle.draw(screen)

        mousex, mousey = pygame.mouse.get_pos()
        #if circle.x +circle.radius > mousex-size+2 and circle.x -circle.radius < mousex+size-2 and circle.y +circle.radius > mousey-size+2 and circle.y -circle.radius < mousey+size-2:
        distance = math.sqrt((circle.x - mousex)**2 + (circle.y - mousey)**2)
        if distance <= circle.radius+size:
            play = False
    for orb in Orbs:
        print(orb.x,orb.y)
        orb.draw(screen)
        mousex, mousey = pygame.mouse.get_pos()
        distance = math.sqrt((orb.x - mousex)**2 + (orb.y - mousey)**2)
        if distance <= orb.radius+size:
            score+=1
            increaseCircleCount +=1
            print(score)
            orb.x = random.randint(orb.radius, pygame.display.Info().current_w - orb.size)
            orb.y = random.randint(orb.radius, pygame.display.Info().current_h - orb.size)
            if increaseCircleCount >=10:
                increaseCircleCount = 0
                level +=1
                circle_count+=10
                circles = [Circle() for _ in range(circle_count)]
                

                
        #Check the elapsed time for the timer
    current_time += clock.get_rawtime()
    clock.tick()
    
    # Update score every second
    if current_time >= timer_interval:
        timeScore += 1
        
        if timeScore >= 60:
            timeScore -= 60
            minuteScore += 1
        print(f"TimeScore: {minuteScore}:{timeScore}")
        current_time = 0

    screen.blit(timeRender,(10,10))
    
    screen.blit(levelRender,(200,10))
    
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
