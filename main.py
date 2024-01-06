if __name__ == "__main__": #chatgpt szerint ez hasznos, hogy jól fussanak le a fájlok
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
                                #levelmap = Level classban ez a layout
    

    start=True #legyen e kezdőképernyő
    running=True #futtatás
    while running:
        for event in pygame.event.get(): #események loop
            if event.type==pygame.QUIT: #kilépés
                running=False

        screen.fill(BG_COLOR) #háttérszín
        screen.blit(bg_surf,bg_rect) #háttérkép
        #keys=pygame.key.get_pressed() #lehet lenyomni billentyűt

        if start: #kezdőképernyő
            font=level.setup_font(72)
            text=font.render('My First Platformer', True, DESERT)
            text_rect=text.get_rect(center=(WIDTH/2,HEIGHT/3))
            screen.blit(text,text_rect)
            pygame.display.update()
            pygame.time.delay(2000)
            start=False
        else: #játék indítása
            level.run() #szint megrajzolása a képernyőn és az azon történő események futtatása

        pygame.display.update() #frissítés
        clock.tick(FPS)

    pygame.quit()

