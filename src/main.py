#Canon Unguren
import pygame
import random
from target import Target
from circle import Circle
mousex, mousey = pygame.mouse.get_pos()
timeScore = 0
minuteScore =0
targetScore = 0
play = False
#Initialize timer variables
current_time = 0
timer_interval = 75
circle_count = 50
circles = [Circle() for _ in range(circle_count)]
size = 10

def targetfunc():
    global targetScore
    targetScore += 1
    targetButton.x = random.randint(50,450)

    
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
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



target_image = pygame.image.load("images/target.png")
#Main Game loop
while play:
    #pygame.mouse.set_visible(False)
    screen.fill((255, 255, 255))
    targetButton = Target(100, 300, target_image, targetfunc)
    if timeScore >= 10:
        timeRender = font.render(f"Time: {minuteScore}:{timeScore}", True, (0, 0, 0))
    if timeScore <= 9:
        timeRender = font.render(f"Time: {minuteScore}:0{timeScore}", True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        targetButton.handle_event(event)
        if event.type == pygame.MOUSEMOTION:
            mousex, mousey = pygame.mouse.get_pos()
    pygame.draw.circle(screen,(0,0,0),(mousex,mousey), size)

    for circle in circles:
        circle.move()
        circle.draw(screen)

        mousex, mousey = pygame.mouse.get_pos()
        #if circle.x +circle.radius > mousex-size+2 and circle.x -circle.radius < mousex+size-2 and circle.y +circle.radius > mousey-size+2 and circle.y -circle.radius < mousey+size-2:
        distance = ((circle.x-(mousex-size))**2 + (circle.y - (mousey-size))**2)**0.5
        if distance <= circle.radius:
            play = False
     # Check the elapsed time for the timer
    current_time += clock.get_rawtime()
    clock.tick()
    
    # Update score every second
    if current_time >= timer_interval:
        timeScore += 1
        if timeScore >= 60:
            timeScore -= 60
            minuteScore += 1
        print(f"TimeScore: {minuteScore}:{timeScore}")
        print(f"DodgeScore: {circle.dodgescore}")
        current_time = 0

    screen.blit(timeRender,(10,10))
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
