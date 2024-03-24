import pygame
from pygame import Surface, SurfaceType


class Character:
    def __init__(self, x: int, y: int, image: Surface | SurfaceType):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.direction = 'right'
        self.image = image

    # обновление координат
    def update_coordinates(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 1

        self.border()

    # проверка на границу
    def border(self):
        if self.x < 0:
            self.x = 0
        if self.x > 800:
            self.x = 600
        if self.y < 0:
            self.y = 20
        if self.y > 600:
            self.y = 550

    # Рисуем персонажа
    def draw(self, screen: Surface | SurfaceType):
        if self.direction == 'right':
            screen.blit(self.image, (self.x, self.y))
        else:
            flipped = pygame.transform.flip(self.image, True, False)
            screen.blit(flipped, (self.x, self.y))


class Osel(Character):
    def __init__(self, x: int, y: int, image: Surface | SurfaceType):
        super().__init__(x, y, image)

    def border(self):
        if self.x < 0:
            self.x = 800
        if self.x > 800:
            self.x = 0
        if self.y < 0:
            self.y = 20
        if self.y > 600:
            self.y = 550


class Bird(Character):
    def __init__(self, x: int, y: int, image: Surface | SurfaceType):
        super().__init__(x, y, image)

    def border(self):
        if self.x < 0:
            self.x = 800
        if self.x > 800:
            self.x = 0
        if self.y < 0:
            self.y = 20
        if self.y > 600:
            self.y = 550