import pygame
from settings import tile_size, WIDTH, others
from tiles import TerrainTile, Crate, Tile, OtherTile
from player import Player
from enemy import Enemy

class Level: # szintek önálló osztály, nem sprite osztály
    def __init__(self, level_data, surface): #surface a felület, vagyis a képernyő, leveldata hogy melyik szint
        self.display_surface=surface #játékablak, hogy hol rajzolja meg az elemeket
        self.terrain_tiles=pygame.sprite.Group() #tároló amibe majd pakoljuk bele a csempéket
        self.player=pygame.sprite.GroupSingle() #a játékos sprite csoportja
        self.crates=pygame.sprite.Group() #a ládák csoportja
        self.enemys=pygame.sprite.Group() #ellenségek csoportja 
        self.constraints=pygame.sprite.Group() #térelemek csoportja
        self.other_tiles=pygame.sprite.Group() #díszítő elemek
        self.setup_level(level_data) #szintek legenerálásának elindítása
        self.world_shift=0 #platform mozgatás kameranézet

    def setup_level(self,layout): #szintek legenerálása metódus, itt a layout=level_data
        for row_index, row in enumerate(layout): #sorok és indexük
            for col_index, tile_type in enumerate(row): #oszlopok és indexük
                x=col_index*tile_size #csempe bal felső koordinátái
                y=row_index*tile_size
                if tile_type=='P': #játékos a pályán
                    player_sprite=Player((x,y))
                    self.player.add(player_sprite)
                elif tile_type=='T': #ha ládát talál
                    tile=Crate(tile_size,x,y)
                elif tile_type=='E': #ha ellenséget talál
                    tile=Enemy(tile_size,x,y)
                    self.enemys.add(tile) #hozzáadás az enemys csoporthoz
                elif tile_type=='C': #térelemek
                    constraint=Tile(tile_size,x,y)
                    self.constraints.add(constraint)
                elif tile_type in others: #díszítőelemek
                    tile=OtherTile(tile_size,x,y,tile_type) #itt a tile_type az others kódja, ami majd segít kiolvasni a fájlt
                    self.other_tiles.add(tile)
                elif tile_type!=' ': #csempe legenerálása
                    tile=TerrainTile(tile_size,x,y,tile_type) #csempe objektum(méret,koordináták,típus)
                    self.terrain_tiles.add(tile) #a létrejött csempét hozzáadjuk a csempegyűjtő grouphoz (lásd fentebb)

    def scroll_x(self): #platform mozgás beállítása kamera
        player=self.player.sprite
        player_x=player.rect.centerx
        direction_x=player.direction.x

        if player_x<WIDTH/4 and direction_x<0: #balra mozgás
            self.world_shift=8
            player.speed=0
        elif player_x>WIDTH/4*3 and direction_x>0: #jobbra mozgás
            self.world_shift=-8
            player.speed=0
        else:
            self.world_shift=0
            player.speed=8

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
    
    def enemy_collision_reverse(self): #ha az enemy ütközik vmivel akkor visszaforduljon
        for enemy in self.enemys.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraints, False): #ha ellenség ütközik a térelemmel, akkor nem törlődik, hanem...
                enemy.reverse() #megfordul az enemy
    
    def run(self): #elemek megrajzolása
        self.horizontal_movement_collision() #ütközések
        self.vertical_movement_collision()
        self.scroll_x() #kamera mozgás jobbra balra
        self.terrain_tiles.update(self.world_shift) #kamera mozgásnál a csempék mozgatása
        self.terrain_tiles.draw(self.display_surface) #játékablakban
        self.crates.update(self.world_shift) #ládák elmozgatása 
        self.constraints.update(self.world_shift) #térelemek frissítése kameramozgáskor
        self.enemy_collision_reverse() #ellenség megfordítása
        self.enemys.update(self.world_shift) #ellenség update
        self.enemys.draw(self.display_surface) #ellenség kirajzolása
        self.other_tiles.update(self.world_shift) #díszítőelemek frissítése
        self.other_tiles.draw(self.display_surface) #díszítőelemek kirajzolása
        self.player.update() #játékos frissítése
        self.player.draw(self.display_surface) #játékos kirajzolása a (játékablakban)