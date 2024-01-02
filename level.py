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

    def run(self): #elemek megrajzolása
        self.terrain_tiles.draw(self.display_surface) #játékablakban
        self.player.draw(self.display_surface) #játékos kirajzolása a (játékablakban)
        self.player.update()