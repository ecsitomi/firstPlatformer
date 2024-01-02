import pygame

class Player(pygame.sprite.Sprite): #játékos osztály
    def __init__(self, pos):
        super().__init__()
        self.image=pygame.image.load('img/player/Idle__000.png').convert_alpha() #kép
        self.rect=self.image.get_rect(topleft=pos)
        self.direction=pygame.math.Vector2(0,0) #x,y irányú vektoriális elmozdulás (lényeg, csak irányt mutat)
        self.speed=8
        self.gravity=0.8
        self.jump_speed=-16
        self.on_ground=True #földön van e
    
    def get_input(self): #gombnyomásra mit tegyen
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: #jobb
            self.direction.x=1 #iránymódosítás
        elif keys[pygame.K_LEFT]: #bal
            self.direction.x=-1 #iránymódosítás
        else:
            self.direction.x=0 #ha nincs elmozdulás nincs iránymódosítás

        if keys[pygame.K_SPACE] and self.on_ground: #ugrás
            self.on_ground=False
            self.jump()

    #ugrás
    def apply_gravity(self): #gravitáció hatása
        self.direction.y+=self.gravity #folyamatosan hat rá a gravitáció
        self.rect.y+=self.direction.y #lefelé
    def jump(self):
        self.direction.y=self.jump_speed #irányváltozás felfelé ekkora sebességgel

    def update(self): #játékos folyamatos frissítése
        self.get_input() #milyen billenytyű parancsot kapott

