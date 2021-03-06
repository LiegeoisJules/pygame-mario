import pygame


class Mario(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("mario.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x = x
        self.y = y

        self.isJumping = False

        self.v = 8
        self.m = 1

    def move_right(self):
        self.x += self.v

    def move_left(self):
        self.x -= self.v

    def jump(self):
        self.isJumping = True

    def update(self):
        if self.isJumping:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if self.v > 0:
                force = (0.5 * self.m * (self.v * self.v))
            else:
                force = -(0.5 * self.m * (self.v * self.v))

            # Change position
            self.y = self.y - force

            # Change velocity
            self.v = self.v - 1

            # If ground is reached, reset variables.
            if self.y >= 400 - (self.height + 33):
                self.y = 400 - (self.height + 33)
                self.isJumping = 0
                self.v = 8

        self.rect.x = self.x
        self.rect.y = self.y
