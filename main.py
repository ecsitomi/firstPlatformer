import pygame
from settings import * #settings.py fájlból behúz mindent

pygame.init() #inicializálja magát a pygame
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #meghatározza az ablakot
pygame.display.set_caption('My Firs Platformer') #főcím
clock=pygame.time.Clock() #időzítő

#háttérkép
bg_surf=pygame.image.load(BG_IMAGE).convert_alpha()
bg_rect=bg_surf.get_rect(bottomleft=(0,HEIGHT))

running=True #futtatás
while running:
    for event in pygame.event.get(): #események loop
        if event.type==pygame.QUIT: #kilépés
            running=False

    screen.fill(BG_COLOR) #háttérszín
    screen.blit(bg_surf,bg_rect) #háttérkép

    pygame.display.update() #frissítés
    clock.tick(FPS)

pygame.quit()