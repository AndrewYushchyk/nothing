import pygame
from pygame import *
pygame.init()
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and Draw")

done =True
RED=(255,0,0)
radius=15

while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            spot=event.pos
            pygame.draw.circle(screen,RED,spot,radius)
        pygame.display.update()

pygame.quit()
