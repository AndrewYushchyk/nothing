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

#hero
move_speed=7
wigth1=22
height1=32
player_display=(wigth1,height1)
color="#888888"


#jump power

jump_power=10
gravitation=0,35

pygame.init()
screen=pygame.display.set_mode(display)
pygame.display.set_caption("First game")
blackground=Surface(display)
blackground.fill(Color(blackground_color))

class Player (sprite.Sprite):
  def __init__(self,x,y):
    sprite.Sprite.__init__(self)
    self.xvel=0
    self.startX=x
    self.startY=y
    self.image=Surface(player_display)
    self.image.fill(Color(color))
    self.rect=Rect(x,y,wigth,height)
    self.yvel = 0 
    self.onGround = False

  def update(self,left,right,up):
    if left:
      self.xvel=-move_speed
    if right:
      self.xvel=move_speed
    if not(left or right):
      self.xvel=0
    if up:
      if self.onGround:
        self.yvel=-jump_power
    if not self.onGround:
      self.yvel+=gravitation
    self.onGround=False
    self.rect.y+=self.yvel
    self.rect.x+=self.xvel


  def draw(self, screen):
    screen.blit(self.image,(self.x,self.y))

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

timer = pygame.time.Clock()

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

    timer.tick(60)

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