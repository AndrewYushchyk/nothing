from pygame import *

move_speed=7
wigth1=22
height1=32
player_display=(wigth1,height1)
color="#888888"

class Player (sprite.Sprite):
	def __init__(self,x,y):
		sprite.Sprite.__init__(self)
		self.xvel=0
		self.startX=x
		self.startY=y
		self.image=Surface(player_display)
		self.image.fill(Color(color))
		self.rect=Rect(x,y,wigth,height)

	def update(self,left,right):
		if left:
			self.xvel=-move_speed
		if right:
			self.xvel=move_speed
		if not(left or right):
			self.xvel=0

		self.rect+=self.xvel


	def draw(self, screen):
		screen.blit(self.image,(self.x,self.y))