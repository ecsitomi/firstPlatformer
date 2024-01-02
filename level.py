import pygame
from settings import tile_size
from tiles import TerrainTile
from player import Player

class Level: # szintek önálló osztály, nem sprite osztály
    def __init__(self, level_data, surface): #surface a felület, vagyis a képernyő, leveldata hogy melyik szint
        self.display_surface=surface #játékablak, hogy hol rajzolja meg az elemeket
        self.terrain_tiles=pygame.sprite.Group() #tároló amibe majd pakoljuk bele a csempéket
        self.player=pygame.sprite.GroupSingle()
        self.setup_level(level_data) #szintek legenerálásának elindítása

    def setup_level(self,layout): #szintek legenerálása metódus, itt a layout=level_data
        for row_index, row in enumerate(layout): #sorok és indexük
            for col_index, tile_type in enumerate(row): #oszlopok és indexük
                x=col_index*tile_size #csempe bal felső koordinátái
                y=row_index*tile_size
                if tile_type=='P': #játékos a pályán
                    player_sprite=Player((x,y))
                    self.player.add(player_sprite)

                elif tile_type!=' ': #csempe legenerálása
                    tile=TerrainTile(tile_size,x,y,tile_type) #csempe objektum(méret,koordináták,típus)
                    self.terrain_tiles.add(tile) #a létrejött csempét hozzáadjuk a csempegyűjtő grouphoz (lásd fentebb)

    def horizontal_movement_collision(self):
        player=self.player.sprite #játékosra hivatkozunk ami a groupban van
        player.rect.x+=player.direction.x*player.speed #mozgás -> irány*sebesség

        for sprite in self.terrain_tiles.sprites(): #a csempék vizsgálata
            if sprite.rect.colliderect(player.rect): #hogy ütköznek e a játékossal
                if player.direction.x<0: #ha balra megy
                    player.rect.left=sprite.rect.right #akkor a rect mindkettőnek azonos (tovább nem mehet a játékos)
                if player.direction.x>0: #ha jobbra megy
                    player.rect.right=sprite.rect.left #jobbra tovább már nem mehet, csempe megállítja

    def vertical_movement_collision(self):
        player=self.player.sprite #a játékos
        player.apply_gravity() #amire hat a gravitáció függőleges mozgásnál

        for sprite in self.terrain_tiles.sprites(): #a csempe vizsgálat
            if sprite.rect.colliderect(player.rect): #ütköznek e
                if player.direction.y>0: #ha földön van 
                    player.rect.bottom=sprite.rect.top #kontakt
                    player.direction.y=0 #hogy ne legyen folytonos zuhanás
                    player.on_ground=True #földön van
                elif player.direction.y<0: #ha ugrik
                    player.rect.top=sprite.rect.bottom #ütközés
                    player.direction.y=0 #megáll a mozgás irány változás


                

    
    def run(self): #elemek megrajzolása
        self.terrain_tiles.draw(self.display_surface) #játékablakban
        self.player.draw(self.display_surface) #játékos kirajzolása a (játékablakban)
        self.player.update() #játékos frissítése
        self.horizontal_movement_collision() #ütközések
        self.vertical_movement_collision()