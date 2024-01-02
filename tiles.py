import pygame
from pygame.sprite import _Group

class Tile(pygame.sprite.Sprite): #minden csempe egy objektum lesz
    def __init__(self, size, x, y): #tartalmazza a nagyságát, és a koordinátáját
        super().__init__()
        self.image=pygame.Surface((size,size)) #csak réteget hozunk létre, a size az a csempe pixelszáma, most 64*64
        self.rect=self.image.get_rect(topleft=(x,y)) #réteg elhelyezése az objektum koordinátája szerint

class TerrainTile(Tile):
    def __init__(self, size, x, y, terrain_type): #terrain csempe, származik a nagy csempe osztályból, lesznek típusai (terrain_type)
        super().__init__(size,x,y)
        self.image=pygame.image.load(f'img/terrain/{terrain_type}.png').convert_alpha()