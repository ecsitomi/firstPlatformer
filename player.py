import pygame
from support import import_folder
from settings import HEIGHT
from sounds import jump 

class Player(pygame.sprite.Sprite): #játékos osztály
    def __init__(self, pos):
        super().__init__()
        #self.image=pygame.image.load('img/player/Idle__000.png').convert_alpha() #kép
        self.animations={'idle':[],'run':[],'jump':[]} #különböző animációk listája egy listában (szótár szerkezet)
        self.import_character_assets()
        self.frame_index=0 #képek indexeinek száma
        self.animation_speed=0.15 #indexelés sebessége
        self.image=self.animations['idle'][self.frame_index] #kezdő kép
        self.rect=self.image.get_rect(topleft=pos)
        self.direction=pygame.math.Vector2(0,0) #x,y irányú vektoriális elmozdulás (lényeg, csak irányt mutat)
        self.speed=8
        self.gravity=0.8
        self.jump_speed=-16
        self.on_ground=True #földön van e
        self.counter=0
        self.status='idle' #kezdő státusz
        self.facing_right=True #jobbranéz

    '''
    def step_sounds(self): #mozgáshang lejátszás - sajnos rossz minőségű és viszhangzik
        if abs(self.direction.x)>0 and self.on_ground:
            step.play(-1)
        else:
            step.stop()
    '''
    
    def import_character_assets(self): #hogyan jussunk el a képekhez
        character_path='img/character/' #hol a karakter könyvtár
        for animation in self.animations.keys(): #animation szótárban hozzá akarom rendelni a keys-eket
            full_path=character_path+animation
            self.animations[animation]=import_folder(full_path) #ez a függvény visszaad egy listát a megfelelő animációhoz a szótárban
    
    def get_input(self): #gombnyomásra mit tegyen
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: #jobb
            self.direction.x=1 #iránymódosítás
            self.facing_right=True #jobbranéz

        elif keys[pygame.K_LEFT]: #bal
            self.direction.x=-1 #iránymódosítás
            self.facing_right=False #balranéz

        else:
            self.direction.x=0 #ha nincs elmozdulás nincs iránymódosítás

        if keys[pygame.K_SPACE] and self.on_ground: #ugrás
            self.on_ground=False #nem vagy a földön
            self.jump() #ugrás 
            jump.play() #ugrás hang

    def get_status(self): #karakter státusz változása
        if self.direction.y<0:
            self.status='jump' #ugrik
        else:
            if self.direction.x!=0: #vízszintes irányú mozgás
                self.status='run' #futás
            else:
                self.status='idle' #más esetben áll

    def animate(self): #státusznak megfelelő animálás
        animation=self.animations[self.status]
        self.frame_index+=self.animation_speed #indexelés növelése
        if self.frame_index>=len(animation): #hogy ne indexeljünk túl
            self.frame_index=0

        image=animation[int(self.frame_index)] #státusznak megfelelő kép indexelve
        if self.facing_right: #ha jobbranéz
            self.image=image #nem kell tükrözni
        else:
            flipped_image=pygame.transform.flip(image,True,False) #kép/horizontális/vertikális tükrözés
            self.image=flipped_image
    
    #ugrás
    def apply_gravity(self): #gravitáció hatása
        self.direction.y+=self.gravity #folyamatosan hat rá a gravitáció
        self.rect.y+=self.direction.y #lefelé
    def jump(self):
        self.direction.y=self.jump_speed #irányváltozás felfelé ekkora sebességgel

    def update(self): #játékos folyamatos frissítése
        self.get_input() #milyen billenytyű parancsot kapott
        self.get_status() #mozgás státusz
        self.animate() #animálás
        #self.step_sounds() #mozgáshang lejátszás 

