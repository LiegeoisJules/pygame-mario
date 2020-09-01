import pygame
pygame.init()

WIDTH = 600
HEIGHT = 400

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('PyGame')

carryOn = True

BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
WHITE   = (255, 255, 255)
GREY    = (200, 200, 200)
BLUE    = (0, 0, 255)
 
clock = pygame.time.Clock()
 
while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    

    screen.fill(WHITE)
    
    #Draw green rectangle in window edge
    pygame.draw.rect(screen, BLUE, [0, 0, int(WIDTH/3), HEIGHT])
    pygame.draw.rect(screen, WHITE, [200, 0, int(WIDTH/3), HEIGHT])
    pygame.draw.rect(screen, RED, [400, 0, int(WIDTH/3), HEIGHT])

 
 
 
    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()