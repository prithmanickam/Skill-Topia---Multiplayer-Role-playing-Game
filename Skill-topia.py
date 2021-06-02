import pygame
from pygame.locals import *
import os
import sys
import random
from tkinter import filedialog
from tkinter import *

pygame.init()  # Begin pygame
 
# Declaring variables to be used through the program
vec = pygame.math.Vector2
GREEN = (173,255,47)
GREY = (128,128,128)
HEIGHT = 485
WIDTH = 900
VEL = 3
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Skill-topia")

#guyani1 = pygame.image.load(os.path.join('assets','Player_Sprite_R.png'))


skills = {'attack':{'lvl':1,'xp':0},'mining':{'lvl':1,'xp':0},'fishing':{'l':1,'xp':0},'woodcutting':{'lvl':1,'xp':0}}

class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load(os.path.join('assets','Background.png'))        
            self.bgY = 0
            self.bgX = 0
 
      def render(self):
            window.blit(self.bgimage, (self.bgX, self.bgY))     
 

class Ground(pygame.sprite.Sprite):
      def __init__(self):
          super().__init__()
          self.image = pygame.image.load(os.path.join('assets','Ground.png'))
          self.rect = self.image.get_rect(center = (350, 350))
      def render(self):
          window.blit(self.image, (self.rect.x, self.rect.y))

'''
Using the get_rect() method on the image object will return a rectangle object
of the same dimensions as the image. So if the image is 500 by 200,
the rectangle representing it will also be 500 by 200.
Passing the center argument into get_rect() determines the center position
of the rect on the pygame window.
'''
      



class Border(pygame.sprite.Sprite):
      def __init__(self):
            self.border = pygame.Rect(645,0,10,HEIGHT)

      def render(self):
            pygame.draw.rect(window,GREY, self.border)

class Ore(pygame.sprite.Sprite):
      
      def __init__(self):
            super().__init__()
            image = pygame.image.load(os.path.join('assets','ores.png'))
            self.image = pygame.transform.scale(image, (190,120))
            self.rect = self.image.get_rect(center = (550, 420))

      def render(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Trees(pygame.sprite.Sprite):
      
      def __init__(self):
            super().__init__()
            image = pygame.image.load(os.path.join('assets','trees.png'))
            self.image = pygame.transform.scale(image, (190,180))
            self.rect = self.image.get_rect(center = (550, 90))

      def render(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Dungeon(pygame.sprite.Sprite):
      
      def __init__(self):
            super().__init__()
            image = pygame.image.load(os.path.join('assets','dungeon.png'))
            self.image = pygame.transform.scale(image, (190,180))
            self.rect = self.image.get_rect(center = (70, 90))

      def render(self):
            window.blit(self.image, (self.rect.x, self.rect.y)) 
 
class Player(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__() 
            self.image = pygame.image.load(os.path.join('assets','Player_Sprite_R.png'))
            self.rect = self.image.get_rect() #rect defaults to a value of (0 , 0)
        
            # Position and direction
            self.vx = 0
            self.pos = vec((340, 240))
            self.vel = vec(0,0)
            self.acc = vec(0,0)
            self.direction = "RIGHT"
        
      def move(self):
            
          
          
            # Returns the current key presses
            pressed_keys = pygame.key.get_pressed()
          
 
            # Accelerates the player in the direction of the key press
            if pressed_keys[K_LEFT] and self.pos.x - VEL > 0:
                  self.pos.x -= VEL
            if pressed_keys[K_RIGHT] and self.pos.x + VEL < 640:
                  self.pos.x += VEL
            if pressed_keys[K_UP] and self.pos.y - VEL > 0:
                  self.pos.y -= VEL
            if pressed_keys[K_DOWN] and self.pos.y + VEL < HEIGHT:
                  self.pos.y += VEL
          
                
            self.rect.midbottom = self.pos  # Update rect with new pos
        
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()

#objects
background = Background()
ground = Ground()
player = Player()
ore = Ore()
trees = Trees()
dungeon = Dungeon()
border = Border()

while True:
    #mouse = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        # Will run when the close window button is clicked    
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
             
        # For events that occur upon clicking the mouse (left click) 
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass
 
        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
              pass
       
        
    window.fill(GREEN)
    border.render()
    #player.update()         
    player.move()
    #background.render()
    ore.render()
    trees.render()
    dungeon.render()
    window.blit(player.image, player.rect)
    pygame.display.update()
    FPS_CLOCK.tick(FPS)
