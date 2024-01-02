import pygame
from settings import * #settings.py fájlból behúz mindent
from level import Level

pygame.init() #inicializálja magát a pygame
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #meghatározza az ablakot
pygame.display.set_caption('My Firs Platformer') #főcím
clock=pygame.time. Clock() #időzítő

#háttérkép
bg_surf=pygame.image.load(BG_IMAGE).convert_alpha()
bg_rect=bg_surf.get_rect(bottomleft=(0,HEIGHT))

#szint
level=Level(level_map,screen)#hozz létre egy szint objektumot a levelmap(ami most settingsben van) alapján a screenre

running=True #futtatás
while running:
    for event in pygame.event.get(): #események loop
        if event.type==pygame.QUIT: #kilépés
            running=False

    screen.fill(BG_COLOR) #háttérszín
    screen.blit(bg_surf,bg_rect) #háttérkép

    level.run() #szint megrajzolása a képernyőn és az azon történő események futtatása

    pygame.display.update() #frissítés
    clock.tick(FPS)

pygame.quit()