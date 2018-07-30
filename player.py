import pygame
from pygame import *

weight = 800
height = 640
display = (weight,height)
blackground_color = "#004400"

#blocks
block_weight = 32
block_height = 32
block_color = "#FF6262"
block_dysplay=(block_weight,block_height)

pygame.init()
screen=pygame.display.set_mode(display)
pygame.display.set_caption("First game")
blackground=Surface(display)
blackground.fill(Color(blackground_color))

hero = Player(55,55) 
left =  False
right = False

level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]

while 1:
    for e in pygame.event.get():
        if e.type == QUIT:
            raise SystemExit, "QUIT"
        if e.type == KEYDOWN and e.key == K_LEFT:
            left = True
	    if e.type == KEYDOWN and e.key == K_RIGHT:
            right = True
		if e.type == KEYUP and e.key == K_RIGHT:
            right = False
		if e.type == KEYUP and e.key == K_LEFT:
            left = False

    screen.blit(blackground, (0,0))      


    x=y=0

    for row in level:
    	for col in row:
    		if  col== "-":
    			block=Surface(block_dysplay)
    			block.fill(Color(block_color))
    			screen.blit(block,(x,y))

    		x+=block_weight
    	y+=block_height
    	x=0

    
    pygame.display.update()
    hero.update(left, right)
    hero.draw(screen)