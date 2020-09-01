import pygame


class Cube(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("cube.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
