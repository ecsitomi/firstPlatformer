from os import walk #beépített modulból csak a walk kell
import pygame

def import_folder(path):
    surface_list=[]
    for _, _, img_files in walk(path): # _ _ azok a változók amiket a for kiszámol, de nem fog kelleni
                                        #walk kiszámolja a mappa linkjét, almappáit és a fájlait, most nekünk az első kettő nem kell
        for image in img_files: #a szöveges lista megadja a fájlok neveit
            full_path=path+'/'+image #a képfájlok teljes elérési útvonala
            image_surf=pygame.image.load(full_path).convert_alpha() #létrehozza képként az adott fájlt a játékban
            surface_list.append(image_surf)
            
    return surface_list
