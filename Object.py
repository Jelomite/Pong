import pygame, Colors, math


class Racket(pygame.sprite.Sprite):
    # is a sprite
    def __init__(self, color, x, y, (width, height)):
        super(Racket, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(Colors.clouds)
        self.image.set_colorkey(Colors.clouds)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 1

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
        self.set_position(self.x, self.y)

    def move_down(self, pixels):
        self.rect.y += self.speed * pixels

    def move_up(self, pixels):
        self.rect.y -= self.speed * pixels

    def move_right(self, pixels):
        self.rect.x += int(self.speed * pixels)

    def move_left(self, pixels):
        self.rect.x -= (self.speed * pixels)

    def move_angle(self, pixels, (x, y), mirrored):
        self.move_down(pixels * y)
        self.move_right(mirrored * pixels * x)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
