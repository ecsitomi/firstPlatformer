import pygame
from settings import others
#from pygame.sprite import _Group

class Tile(pygame.sprite.Sprite): #minden csempe egy objektum lesz
    def __init__(self, size, x, y): #tartalmazza a nagyságát, és a koordinátáját
        super().__init__()
        self.image=pygame.Surface((size,size)) #csak réteget hozunk létre, a size az a csempe pixelszáma, most 64*64
        self.rect=self.image.get_rect(topleft=(x,y)) #réteg elhelyezése az objektum koordinátája szerint

    def update(self,shift):
        self.rect.x+=shift

class TerrainTile(Tile): #terrain csempe
    def __init__(self, size, x, y, terrain_type): #terrain csempe, származik a nagy csempe osztályból, lesznek típusai (terrain_type)
        super().__init__(size,x,y)
        self.image=pygame.image.load(f'img/terrain/{terrain_type}.png').convert_alpha()

class Crate(Tile): #láda
    def __init__(self,size,x,y,):
        super().__init__(size,x,y)
        self.image_list=[] #ládák listája
        for index in range(1,4): #indexelés az elérési útvonalhoz
            self.image_list.append(pygame.image.load(f'img/crate/crate_{index}.png').convert_alpha()) #elérési útvonal
        self.image_index=0 #kép indexe
        self.image=self.image_list[self.image_index] #indexelt kép
        offset_y=y+size #hogy ne a levegőben lógjon hozzáadjuk a csempe méretét
        self.rect=self.image.get_rect(bottomleft=(x,offset_y)) #kordináta bal alul mert a csempe bal felül számol, ezért adjuk hozzá a csempe méretét

    def update(self,shift): #a csempék indexváltozása és elmozdulása a kamerával
        self.rect.x+=shift
        self.image_index+=0.05 #indexváltás sebessége
        if self.image_index>len(self.image_list): #ne indexeljünk túl
            self.image_index=0
        self.image=self.image_list[int(self.image_index)]


class OtherTile(Tile): #díszítőelemek
    def __init__(self,size,x,y,type):
        super().__init__(size,x,y)
        self.image=pygame.image.load(f'img/others/{others[type]}.png').convert_alpha()
        offset_y=y+size
        self.rect=self.image.get_rect(bottomleft=(x,offset_y))
    
    def update(self, shift):
        self.rect.x+=shift