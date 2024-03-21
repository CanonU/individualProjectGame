#Canon Unguren
import pygame
import random
from target import Target

timeScore = 0
minuteScore =0
targetScore = 0
play = False

#Initialize timer variables
current_time = 0
timer_interval = 75


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
    screen.fill((255, 255, 255))
    targetButton = Target(100, 300, pebblebutton1_image, pebbleclick)
    if timeScore >= 10:
        timeRender = font.render(f"Time: {minuteScore}:{timeScore}", True, (0, 0, 0))
    if timeScore <= 10:
        timeRender = font.render(f"Time: {minuteScore}:0{timeScore}", True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
        current_time = 0

        
    screen.blit(timeRender,(10,10))

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
