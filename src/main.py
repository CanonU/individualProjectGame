#Canon Unguren
import pygame
import math
import random
import time
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
circle_count = 10
Orb_count = 5
level = 0
Orbs= [Orb() for _ in range(Orb_count)]
circles = [Circle() for _ in range(circle_count)]
size = 10
increaseCircleCount = 0
waiting = False


    
#pygame.init()
screen = pygame.display.set_mode((pygame.display.Info().current_w-300,pygame.display.Info().current_h-300))


clock = pygame.time.Clock()
startfont = pygame.font.Font(None, 100)
font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None,20)
font3 = pygame.font.Font(None,40)
instruction = 0
# Start Screen 
while not play:

    screen.fill((255, 255, 255))
    if instruction == 0:
        welcome = startfont.render("No Pain No Game", True, (0, 0, 0))
        screen.blit(welcome, (175, 250))
        begin_text = font3.render("Click anywhere to start instructions", True, (0, 0, 0))
        screen.blit(begin_text, (175, 400))
    elif instruction == 1:
        screen.fill((255,255,255))
        welcome = startfont.render("In this game you are a ball", True, (0, 0, 0))
        pygame.draw.circle(screen,(0,0,0),(100,300), size)
        otherText = font.render("you are this ball",True, (0,0,0))
        begin_text = font3.render("Click anywhere to continue", True, (0, 0, 0))
        screen.blit(begin_text, (175, 400))
        screen.blit(welcome, (175, 250))
        screen.blit(otherText, (45, 250))
        pygame.display.update()
    elif instruction == 2:
        screen.fill((255,255,255))
        welcome = startfont.render("Your goal is to avoid the other balls", True, (0, 0, 0))
        begin_text = font3.render("Click anywhere to continue", True, (0, 0, 0))
        screen.blit(begin_text, (175, 400))
        screen.blit(welcome, (175, 250))
    elif instruction == 3:
        screen.fill((255,255,255))
        welcome_line1 = startfont.render("While collecting the squares found around", True, (0, 0, 0))
        welcome_line2 = startfont.render("the map", True, (0, 0, 0))
        begin_text = font3.render("Click anywhere to continue", True, (0, 0, 0))
        screen.blit(begin_text, (175, 400))
        screen.blit(welcome_line1, (175, 250))
        screen.blit(welcome_line2, (175, 310))
    elif instruction == 4:
        screen.fill((255,255,255))
        welcome_line1 = startfont.render("But every 5 of them you collect increases", True, (0, 0, 0))
        welcome_line2 = startfont.render("the amount of balls by 10", True, (0, 0, 0))
        begin_text = font3.render("Click anywhere to continue", True, (0, 0, 0))
        screen.blit(begin_text, (175, 400))
        screen.blit(welcome_line1, (175, 250))
        screen.blit(welcome_line2, (175, 310))
    elif instruction == 5:
        screen.fill((255,255,255))
        welcome_line1 = startfont.render("Good Luck", True, (0, 0, 0))
        begin_text = font3.render("Click anywhere to start", True, (0, 0, 0))
        screen.blit(begin_text, (175, 400))
        screen.blit(welcome_line1, (175, 250))
        
    else:
        play = True
        pygame.mouse.set_visible(False)


    # Check for mouse click to start the game
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            instruction += 1
        elif event.type == pygame.QUIT:
            play = True
    pygame.display.update()



#Main Game loop
while play:
    
    while waiting == True:
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                play = False
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
                pygame.mouse.set_visible(False)
                break

    
    #pygame.mouse.set_visible(False)
    screen.fill((255, 255, 255))

    if timeScore >= 10:
        timeRender = font.render(f"Time: {minuteScore}:{timeScore}", True, (0, 0, 0))
    if timeScore <= 9:
        timeRender = font.render(f"Time: {minuteScore}:0{timeScore}", True, (0, 0, 0))
    levelRender = font.render(f"Level(xp):{level}({score})",True,(0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                waiting = True
        elif event.type == pygame.MOUSEMOTION:
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
        orb.draw(screen)
        mousex, mousey = pygame.mouse.get_pos()
        distance = math.sqrt((orb.x - mousex)**2 + (orb.y - mousey)**2)
        if distance <= orb.size/2+size:
            score+=1
            increaseCircleCount +=1
            print(score, level)
            #orb.x = mousex
            #orb.y = mousey
            orb.x = random.randint(orb.size, pygame.display.Info().current_w - orb.size)
            orb.y = random.randint(orb.size, pygame.display.Info().current_h - orb.size)
            if increaseCircleCount >=5:
                increaseCircleCount = 0
                level +=1
                for _ in range(10):
                    circles.append(Circle())
                

                
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
screen.fill((255, 255, 255))
end= False
pygame.mouse.set_visible(True)
screen.fill((255,255,255))
welcome = startfont.render("Unfortunately you have perished", True, (0, 0, 0))
begin_text = font3.render("Click to end", True, (0, 0, 0))
begin_text2 = font3.render(f"You survived for {minuteScore} minutes and {timeScore} seconds", True, (0, 0, 0))
screen.blit(begin_text2, (175, 400))
screen.blit(begin_text, (175, 600))
screen.blit(welcome, (175, 250))
pygame.display.update()
while not end:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            end = True
        elif event.type == pygame.QUIT:
            end = True
        
