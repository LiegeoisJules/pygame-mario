from mario import Mario
from cube import Cube
from score import Score
from weed import Weed
import pygame

pygame.init()

WIDTH = 700
HEIGHT = 400
WHITE = (255, 255, 255)

backgroundImage = pygame.image.load("background.png")
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mario')

all_sprites_list = pygame.sprite.Group()

# Mario
mario = Mario(0, HEIGHT - (60 + 33))

# Cube
cube1 = Cube(95, 170)
cube2 = Cube(160, 170)

# Weed
weed1 = Weed(95, 170)
weed2 = Weed(160, 170)

# Score
score = Score(WHITE)

all_sprites_list.add(weed1, cube1, weed2, cube2, mario, score)

carryOn = True

# Collision temp variable
collideCube1 = False
collideCube2 = False
collideWeed1 = False
collideWeed2 = False

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
        if collideCube1:
            all_sprites_list.remove(cube1)
            weed1.reveal = True
        else:
            collideCube1 = True

    if pygame.sprite.collide_rect(mario, cube2):
        if collideCube2:
            all_sprites_list.remove(cube2)
            weed2.reveal = True
        else:
            collideCube2 = True

    # if pygame.sprite.collide_rect(mario, weed1):
    #     if collideWeed1:
    #         all_sprites_list.remove(weed1)
    #         # mario.score('ADD')
    #     else:
    #         collideWeed1 = True
    #
    # if pygame.sprite.collide_rect(mario, weed2):
    #     if collideWeed2:
    #         all_sprites_list.remove(weed2)
    #         # mario.score('ADD')
    #     else:
    #         collideWeed2 = True

    all_sprites_list.update()
    screen.fill(WHITE)
    screen.blit(backgroundImage, [0, 0])
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(40)

pygame.quit()
