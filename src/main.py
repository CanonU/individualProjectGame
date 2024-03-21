#Canon Unguren
import pygame

timeScore = 0
targetScore = 0
equationScore = 0
arrowScore = 0


play = False

#Initialize timer variables
current_time = 0
timer_interval = 100

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
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
