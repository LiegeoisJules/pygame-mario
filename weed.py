import pygame


class Weed(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("weed.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.x = x
        self.y = y

        self.reveal = False

    def update(self):
        if self.reveal:
            self.x += 10
            self.y = 400 - (self.height + 33)

            if self.x > 700:
                self.kill()

        self.rect.x = self.x
        self.rect.y = self.y

