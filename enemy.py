import pygame
from random import randint
from tiles import Tile

class Enemy(Tile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y)
        self.image=pygame.image.load('img/enemy/enemy.png').convert_alpha()
        offset_y=y+size #hogy a csempe alján legyen
        self.rect=self.image.get_rect(bottomleft=(x,offset_y))
        self.speed=randint(1,3) #random mozgás

    def remove(self): #mozgás
        self.rect.x+=self.speed 
        
    def reverse(self): #visszafordulás
        self.speed*=-1 #irányváltás
        self.image=pygame.transform.flip(self.image,True,False) #kép megfordítás

    def update(self, shift):
        self.rect.x+=shift
        self.remove()

