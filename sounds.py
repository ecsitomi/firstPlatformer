import pygame

pygame.mixer.init() #pygame zenelejátszó modul

jump=pygame.mixer.Sound('sound/jump.mp3') #ugrás
#step=pygame.mixer.Sound('sound/step.mp3') #járás
hit=pygame.mixer.Sound('sound/hit.mp3') #ütközés
win=pygame.mixer.Sound('sound/win.mp3') #győzelem
dead=pygame.mixer.Sound('sound/dead.mp3') #halál
background=pygame.mixer.Sound('sound/background.mp3') #háttér zene