from pygame import Surface, SurfaceType

from characters import Character


class Coin:
    def __init__(self, x: int, y: int, image: Surface | SurfaceType):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen: Surface | SurfaceType):
        screen.blit(self.image, (self.x, self.y))

    def collid(self, character: Character) -> bool:
        return ((character.x + 25) - (self.x + 25)) ** 2 + ((character.y + 25) - (self.y + 25)) ** 2 < 50 ** 2