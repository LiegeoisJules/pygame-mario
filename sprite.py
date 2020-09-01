from mario import Mario
from cube import Cube
from weed import Weed
import pygame

pygame.init()

WIDTH = 700
HEIGHT = 400
WHITE = (255, 255, 255)

backgroundImage = pygame.image.load("background.png")
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('PyGame')

all_sprites_list = pygame.sprite.Group()

# Mario
mario = Mario(0, HEIGHT - (60 + 33))

# Cube
cube1 = Cube(95, 170)
cube2 = Cube(160, 170)

cubeG1 = pygame.sprite.Group()
cubeG1.add(cube1)
cubeG2 = pygame.sprite.Group()
cubeG2.add(cube2)

# Weed
weed1 = Weed(95, 170)
weed2 = Weed(160, 170)


all_sprites_list.add(weed1, cube1, weed2, cube2, mario)

carryOn = True

clock = pygame.time.Clock()

while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and mario.rect.x > 0:
        mario.move_left()
    elif keys[pygame.K_RIGHT] and mario.rect.x < (WIDTH - mario.image.get_width()):
        mario.move_right()
    elif not mario.isJumping:
        if keys[pygame.K_SPACE]:
            mario.jump()

    # Handle Collision
    if pygame.sprite.collide_rect(mario, cube1):
        # all_sprites_list.remove(cube1)
        # weed1.reveal()
        print(f"Collision detected")

    all_sprites_list.update()
    screen.fill(WHITE)
    screen.blit(backgroundImage, [0, 0])
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
