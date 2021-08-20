#iteration6:
#created menu screen
#players can login 
#created new solution for calculating level and experience
#player can enter a house

import pygame
from pygame.locals import *
import os
import sys
import random
import time
from tkinter import filedialog
from tkinter import *

pygame.init()  # Begin pygame
 
# Declaring variables to be used through the program
vec = pygame.math.Vector2
GREEN = (173,255,47)
GREY = (128,128,128)
BLACK = (0,0,0)
WHITE = (255,255,255)
HEIGHT = 485
WIDTH = 900
VEL = 3
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Skill-Topia")

# light shade of the button 
color_light = (170,170,170)
color_dark = (100,100,100)
color_white = (255,255,255) 

# defining a font
headingfont = pygame.font.SysFont("Verdana", 40)
regularfont = pygame.font.SysFont('Corbel',25)
smallerfont = pygame.font.SysFont('Corbel',16)
tinyfont = pygame.font.SysFont('Corbel',11) 


#skills = {'attack':{'lvl':1,'xp':0},'mining':{'lvl':1,'xp':0},'fishing':{'l':1,'xp':0},'woodcutting':{'lvl':1,'xp':0}}

# Run animation for the RIGHT
run_ani_R = [pygame.image.load(os.path.join('assets',"Player_Sprite_R.png")), pygame.image.load(os.path.join('assets',"Player_Sprite2_R.png")),
             pygame.image.load(os.path.join('assets',"Player_Sprite3_R.png")),pygame.image.load(os.path.join('assets',"Player_Sprite4_R.png")),
             pygame.image.load(os.path.join('assets',"Player_Sprite5_R.png")),pygame.image.load(os.path.join('assets',"Player_Sprite6_R.png")),
             pygame.image.load(os.path.join('assets',"Player_Sprite_R.png"))]

# Run animation for the LEFT
run_ani_L = [pygame.image.load(os.path.join('assets',"Player_Sprite_L.png")), pygame.image.load(os.path.join('assets',"Player_Sprite2_L.png")),
             pygame.image.load(os.path.join('assets',"Player_Sprite3_L.png")), pygame.image.load(os.path.join('assets',"Player_Sprite4_L.png")),
             pygame.image.load(os.path.join('assets',"Player_Sprite5_L.png")),pygame.image.load(os.path.join('assets',"Player_Sprite6_L.png")),
             pygame.image.load(os.path.join('assets',"Player_Sprite_L.png"))]

# Run animation for the ATTACK
attack_ani_R = [pygame.image.load(os.path.join('assets',"Player_Sprite_R.png")), pygame.image.load(os.path.join('assets',"Player_Attack_R.png")),
                pygame.image.load(os.path.join('assets',"Player_Attack2_R.png")),pygame.image.load(os.path.join('assets',"Player_Attack2_R.png")),
                pygame.image.load(os.path.join('assets',"Player_Attack3_R.png")),pygame.image.load(os.path.join('assets',"Player_Attack3_R.png")),
                pygame.image.load(os.path.join('assets',"Player_Attack4_R.png")),pygame.image.load(os.path.join('assets',"Player_Attack4_R.png")),
                pygame.image.load(os.path.join('assets',"Player_Attack5_R.png")),pygame.image.load(os.path.join('assets',"Player_Attack5_R.png")),
                pygame.image.load(os.path.join('assets',"Player_Sprite_R.png"))]
 
# Attack animation for the LEFT
attack_ani_L = [pygame.image.load(os.path.join('assets',"Player_Sprite_L.png")), pygame.image.load(os.path.join('assets',"Player_Attack_L.png")),
                pygame.image.load(os.path.join('assets',"Player_Attack2_L.png")),pygame.image.load(os.path.join('assets',"Player_Attack2_L.png")),
                pygame.image.load(os.path.join('assets',"Player_Attack3_L.png")),pygame.image.load(os.path.join('assets',"Player_Attack3_L.png")),
                pygame.image.load(os.path.join('assets',"Player_Attack4_L.png")),pygame.image.load(os.path.join('assets',"Player_Attack4_L.png")),
                pygame.image.load(os.path.join('assets',"Player_Attack5_L.png")),pygame.image.load(os.path.join('assets',"Player_Attack5_L.png")),
                pygame.image.load(os.path.join('assets',"Player_Sprite_L.png"))]

# Animations for the Health Bar
health_ani = [pygame.image.load(os.path.join('assets',"heart0.png")), pygame.image.load(os.path.join('assets',"heart.png")),
              pygame.image.load(os.path.join('assets',"heart2.png")), pygame.image.load(os.path.join('assets',"heart3.png")),
              pygame.image.load(os.path.join('assets',"heart4.png")), pygame.image.load(os.path.join('assets',"heart5.png"))]

# Animations for the water fountain
fountain_ani = [pygame.image.load(os.path.join('assets',"fountain1.png")), pygame.image.load(os.path.join('assets',"fountain2.png")),
                pygame.image.load(os.path.join('assets',"fountain3.png")),pygame.image.load(os.path.join('assets',"fountain4.png")),
                pygame.image.load(os.path.join('assets',"fountain5.png")),pygame.image.load(os.path.join('assets',"fountain6.png")),
                pygame.image.load(os.path.join('assets',"fountain7.png")),pygame.image.load(os.path.join('assets',"fountain8.png")),
                pygame.image.load(os.path.join('assets',"fountain9.png")),pygame.image.load(os.path.join('assets',"fountain10.png"))]

# Animations for the teddy inside house in Map 1
teddy_ani = [pygame.image.load(os.path.join('assets',"teddy1.png")), pygame.image.load(os.path.join('assets',"teddy2.png"))]

class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load(os.path.join('assets','Background.png'))        
            self.bgY = 0
            self.bgX = 0
 
      def render(self):
            window.blit(self.bgimage, (self.bgX, self.bgY))     
 
# ground class when entering the dungeon
class Ground(pygame.sprite.Sprite):
    def __init__(self, a,b):#,c,d):
        super().__init__()
        self.x = int(a)
        self.y = int(b)
        #self.w = int(c)
        #self.h = int(d)
        self.image = pygame.image.load(os.path.join('assets',"Ground.png"))
        #self.image = pygame.transform.scale(self.image, (self.w,self.h))
        self.rect = self.image.get_rect(center = (450, 450))
        

    def render(self):
        window.blit(self.image, (self.x, self.y))


#border class to split the skilltopia surface with the status and skills box
class Border(pygame.sprite.Sprite):
      def __init__(self):
            self.border = pygame.Rect(645,0,10,HEIGHT)

      def render(self):
            pygame.draw.rect(window,GREY, self.border)



#Displays a skills box with lvls and experience as text
class Skills(pygame.sprite.Sprite): 
      def __init__(self):
          super().__init__()
          image = pygame.image.load(os.path.join('assets','skill stats.png'))
          self.image = pygame.transform.scale(image, (230,313))
          self.rect = self.image.get_rect(center = (778, 320))
          self.border = pygame.Rect(655,0,260,HEIGHT)
          
      def render(self):
          pygame.draw.rect(window,BLACK, self.border)
          
          window.blit(self.image, (self.rect.x, self.rect.y))
          
          text = regularfont.render('Skill Stats', True , color_white)
          window.blit(text, (700, 170))
          
          #text, will keep getting updated after every tick
          #mining
          text = smallerfont.render('mining', True , color_white)
          window.blit(text, (700, 200))
          text = tinyfont.render('lvl: ' + str(player.minelvl), True , color_white)
          window.blit(text, (700, 215))
          text = tinyfont.render('xp: ' + str(player.curminexp) + '/' + str(player.endminexp), True , color_white)
          window.blit(text, (700, 230))
          
          #text = tinyfont.render('tot: ' + str(player.totminexp) , True , color_white)    #for highscores
          #window.blit(text, (700, 245))
          
          #woodcutting
          text = smallerfont.render('wdcutting', True , color_white)
          window.blit(text, (800, 200))
          text = tinyfont.render('lvl: ' + str(player.wcutlvl), True , color_white)
          window.blit(text, (800, 215))
          text = tinyfont.render('xp: ' + str(player.curwcutxp) + '/' + str(player.endwcutxp), True , color_white)
          window.blit(text, (800, 230))

          #attack
          text = smallerfont.render('attack', True , color_white)
          window.blit(text, (700, 260))
          text = tinyfont.render('lvl: ' + str(player.attlvl), True , color_white)
          window.blit(text, (700, 275))
          text = tinyfont.render('xp: ' + str(player.curattxp) + '/' + str(player.endattxp), True , color_white)
          window.blit(text, (700, 290))


          
#displays status box and gives infromation of players last general update e.g. escaped dungeon, and level update e.g. Achieved lvl 3 mining
class StatusBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            image = pygame.image.load(os.path.join('assets','status.png'))
            self.image = pygame.transform.scale(image, (230,155))
            self.rect = self.image.get_rect(center = (777, 80))
            
      def update(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
            text = regularfont.render('Update:', True , BLACK)
            window.blit(text, (685, 25))
            text = smallerfont.render(player.upd, True , BLACK)
            window.blit(text, (685, 50))
            text = regularfont.render('Level Update:', True , BLACK)
            window.blit(text, (685, 85))
            text = smallerfont.render(player.lvlupd, True , BLACK)
            window.blit(text, (685, 110))

             
#Ore class for displaying a type of ore rock e.g. copper, silver, emerald, from the parameters passed through  
class Ore(pygame.sprite.Sprite):
      
      def __init__(self, orename, posx, posy):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets',orename))
            self.image = pygame.transform.scale(image, (75,75))
            self.rect = self.image.get_rect(center = (posx, posy))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y))

#Tree class for displaying a type of tree e.g. oak, willow, maple, from the parameters passed through 
class Tree(pygame.sprite.Sprite):
      
      def __init__(self, treename, posx, posy):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets',treename))
            self.image = pygame.transform.scale(image, (150,140))
            self.rect = self.image.get_rect(center = (posx, posy))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y))

#--Will introduction fishing skill in later iterations--
                  
##class Lake(pygame.sprite.Sprite):
##      
##      def __init__(self, lakename, posx, posy):
##            super().__init__()
##            self.hide = False
##            image = pygame.image.load(os.path.join('assets',lakename))
##            self.image = pygame.transform.scale(image, (210,200))
##            self.rect = self.image.get_rect(center = (posx, posy))
##
##      def update(self):
##            if self.hide == False:
##                  window.blit(self.image, (self.rect.x, self.rect.y))

#fountain class displays a fountain and the animation
class Fountain(pygame.sprite.Sprite):
      def __init__(self):
            self.x = 30
            self.y = 20
            self.hide = False
            self.move_frame = 0
            self.image = pygame.image.load(os.path.join('assets',"fountain1.png"))
            image = pygame.image.load(os.path.join('assets',"fountain1.png"))
            image = pygame.transform.scale(image, (800,400))
            #self.image = pygame.transform.scale(self.image, (800,400))
            window.blit(image, (self.x, self.y))
            
      def update(self):
            if self.hide == False:
          
            # Return to base frame if at end of animation sequence 
                  if self.move_frame > 9:
                        self.move_frame = 0
                        return

                  
                  self.image = fountain_ani[self.move_frame]
                  self.image = pygame.transform.scale(self.image, (800,400))
                  window.blit(self.image, (self.x, self.y))
                  self.move_frame += 1
                  
#main tower class displays the main tower (when pressed q it asks the user if they want to play the tower defence gamemode)
class MainTower(pygame.sprite.Sprite):
      
      def __init__(self, towername, posx, posy):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets',towername))
            self.image = pygame.transform.scale(image, (270,270))
            self.rect = self.image.get_rect(center = (posx, posy))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y))
                  
#teddy class displays a teddy looking menacing and the animation (for the agiliy gamemode)
class Teddy(pygame.sprite.Sprite):
      def __init__(self):
            self.x = 230
            self.y = 20
            self.hide = True
            self.move_frame = 0
            self.image = pygame.image.load(os.path.join('assets',"teddy1.png"))
            #image = pygame.image.load(os.path.join('assets',"fountain1.png"))
            self.image = pygame.transform.scale(self.image, (180,180))
            #self.image = pygame.transform.scale(self.image, (800,400))
            window.blit(self.image, (self.x, self.y))
            
      def update(self):
            if self.hide == False:
          
            # Return to base frame if at end of animation sequence 
                  if self.move_frame > 1:
                        self.move_frame = 0
                        return

                  
                  self.image = teddy_ani[self.move_frame]
                  self.image = pygame.transform.scale(self.image, (180,180))
                  window.blit(self.image, (self.x, self.y))
                  self.move_frame += 1
                  
#teddy class displays in a happy state 
class teddyStill(pygame.sprite.Sprite):
      def __init__(self):
            self.x = 180
            self.y = 5
            self.hide = True
            self.move_frame = 0
            self.image = pygame.image.load(os.path.join('assets',"teddy neutral.png"))
            
            self.image = pygame.transform.scale(self.image, (250,250))
            
            window.blit(self.image, (self.x, self.y))
            
      def update(self):
            if self.hide == False:
          
            # Return to base frame if at end of animation sequence 
                  if self.move_frame > 1:
                        self.move_frame = 0
                        return

                  
                  self.image = teddy_ani[self.move_frame]
                  self.image = pygame.transform.scale(self.image, (250,250))
                  window.blit(self.image, (self.x, self.y))
                  self.move_frame += 1

#dungeon class displays the dungeon
class Dungeon(pygame.sprite.Sprite):
      
      def __init__(self, dname, posx, posy):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets',dname))
            self.image = pygame.transform.scale(image, (140,130))
            self.rect = self.image.get_rect(center = (posx, posy))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y)) 



#player class
class Player(pygame.sprite.Sprite):

      #initalises the skill levels and experience      
      def __init__(self,a,b,c,d,e,f,g,h,i):
            #parameters totalminexp,curminexp,minelvl,totwcutxp,curwcutxp,wcutlvl,totattxp,curattxp,attlvl
            
            super().__init__()
            self.image = pygame.image.load(os.path.join('assets',"Player_Sprite_R.png"))
            self.rect = self.image.get_rect() #rect defaults to a value of (0 , 0)
            
            # position and direction
            self.vx = 0
            self.pos = vec((340, 240))
            self.vel = vec(0,0)
            self.acc = vec(0,0)
            self.direction = "RIGHT"
            self.map = 1 #player starts here on the map
            self.jumping = False
            self.running = True
            self.move_frame = 0
            
            #the player's general and level update (set to nothing when logged on or when account created)
            self.upd = ''
            self.lvlupd = ''

            #using indexing to work out much xp is needed to level up
            self.lvls = [ 2, 3, 4, 5,  6,  7,  8,   9,  10,  11,  12,  13,  14,  15]
            self.xpcap =[10,20,40,80,160,320,640,1280,2560,3500,4500,5500,6500,8000]
            
            #for mining function, loading in skill lvls and xp
            self.mining = False
            self.mine_frame = 0

            self.totminexp = int(a)
            self.curminexp = int(b)
            self.endminexp = self.xpcap[int(c)-1]
            self.minelvl = int(c)           #if lvl 3 mining (c) is loaded, endminexp is self.xpcap[int(c)-1]
            self.mx = []

            #for wooding function, loading in skill lvls and xp
            self.wdcutting = False
            self.wcut_frame = 0

            self.totwcutxp = int(d)
            self.curwcutxp = int(e)
            self.endwcutxp = self.xpcap[int(f)-1]
            self.wcutlvl = int(f)
            self.wx = []

            #for attacking function, loading in skill lvls and xp
            self.attacking = False
            self.attack_frame = 0
            
            self.totattxp = int(g)
            self.curattxp = int(h)
            self.endattxp = self.xpcap[int(i)-1]
            self.attlvl = int(i)
            self.atx = []
            self.immune = False
            self.special = False
            self.experiance = 0
            self.cooldown = False
            self.health = 5
            self.magic_cooldown = 1
            self.mana = 0


      #player move function
      def move(self):

            self.acc = vec(0,0.5)

            # gets the current key pressed
            pressed_keys = pygame.key.get_pressed()
          
 
            # Accelerates the player in the direction of the key press
            if pressed_keys[K_LEFT] and self.pos.x - 10 > 0: #collision with borders!!!!!
                  self.pos.x -= VEL
                  self.acc.x = -ACC
            if pressed_keys[K_RIGHT] and self.pos.x < 640:
                  self.pos.x += VEL
                  self.acc.x = ACC
            if pressed_keys[K_UP] and self.pos.y - 40 > 0:
                  self.pos.y -= VEL
                  self.acc.x = -ACC
            if pressed_keys[K_DOWN] and self.pos.y < HEIGHT:
                  self.pos.y += VEL
                  self.acc.x = ACC

            #move to map 2
            if pressed_keys[K_UP] and self.map == 1 and 230 < self.pos.x < 330 and 0 <= self.pos.y < 50:
                  self.map = 2
                  handler.map2()
                  self.pos.y = HEIGHT
                  
            #move to map 1 from map 2
            if pressed_keys[K_DOWN] and self.map == 2 and 230 < self.pos.x < 330 and HEIGHT -50 <= self.pos.y < HEIGHT:
                  self.map = 1
                  handler.map1()
                  self.pos.y = 0

            #move to map 3
            if pressed_keys[K_LEFT] and self.map == 1 and 0 < self.pos.x < 35 and 270 <= self.pos.y < 330:
                  self.map = 3
                  handler.map3()
                  self.pos.x = 610

            #move to map 1 from map 3
            if pressed_keys[K_RIGHT] and self.map == 3 and 610 < self.pos.x < 700 and 270 <= self.pos.y < 330:
                  self.map = 1
                  handler.map1()
                  self.pos.x = 0
                        
            # Formulas to calculate velocity while accounting for friction
            self.acc.x += self.vel.x * FRIC
            self.vel += self.acc
            

            self.rect.midbottom = self.pos  # Update rect with new pos

      #movement in the dungeon, uses acceleration 
      def dungeonmove(self):
            # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
            self.acc = vec(0,0.5)

            # Will set running to False if the player has slowed down to a certain extent
            if abs(self.vel.x) > 0.3:
                  self.running = True
            else:
                  self.running = False

            # Returns the current key presses
            pressed_keys = pygame.key.get_pressed()

            # Accelerates the player in the direction of the key press
            if pressed_keys[K_LEFT]:
                  self.acc.x = -ACC
            if pressed_keys[K_RIGHT]:
                  self.acc.x = ACC 

            # Formulas to calculate velocity while accounting for friction
            self.acc.x += self.vel.x * FRIC
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values

            # This causes character warping from one point of the screen to the other
            if self.pos.x > WIDTH:
                  self.pos.x = 0
            if self.pos.x < 0:
                  self.pos.x = WIDTH

            self.rect.midbottom = self.pos  # Update rect with new pos

      #player movement animation
      def update(self):
          
            # Return to base frame if at end of movement sequence 
            if self.move_frame > 6:
                  self.move_frame = 0
                  return

            # Move the character to the next frame if conditions are met 
            if self.jumping == False and self.running == True:
                
                  if self.vel.x > 0:
                        self.image = run_ani_R[self.move_frame]
                        self.direction = "RIGHT"
                  else:
                        self.image = run_ani_L[self.move_frame]
                        self.direction = "LEFT"
                  self.move_frame += 1

            # Returns to base frame if standing still and incorrect frame is showing
            if abs(self.vel.x) < 0.2 and self.move_frame != 0:
                  self.move_frame = 0
                  if self.direction == "RIGHT":
                      
                        self.image = run_ani_R[self.move_frame]
                  elif self.direction == "LEFT":
                        self.image = run_ani_L[self.move_frame]
                      
      
      #In the dungeon, there is gravity if the player is not touching the ground
      def gravity_check(self):
            hits = pygame.sprite.spritecollide(player ,ground_group, False)
            if self.vel.y > 0:
                  if hits:
                        lowest = hits[0]
                        if self.pos.y < lowest.rect.bottom:
                              self.pos.y = lowest.rect.top + 1
                              self.vel.y = 0
                              self.jumping = False
                              
      #function for player to jump
      def jump(self):
            
            self.rect.x += 1

            # Check to see if player is in contact with the ground
            hits = pygame.sprite.spritecollide(self, ground_group, False)

            self.rect.x -= 1

            # If touching the ground, and not currently jumping, cause the player to jump.
            if hits and not self.jumping:
                  self.jumping = True 
                  self.vel.y = -12

      def player_hit(self):
            if self.cooldown == False:      
                  self.cooldown = True # Enable the cooldown
                  pygame.time.set_timer(hit_cooldown, 1000) # Resets cooldown in 1 second

                  self.health = self.health - 1
                  health.image = health_ani[self.health]
            
                  if self.health <= 0: #take back to the surface and update status e.g. beat all 5 stages!
                        
                        player.upd = 'You died at stage ' + str(handler.stage) + 'in dungeon' 
                        
                        
                        
                        handler.enemy_count = 0
                        handler.dead_enemy_count = 0
                        handler.world = 0
                        player.map == 1 #so player can perform skilling in that map
                        handler.map1()  #so object sprites of the map renders
                        
                        self.health = 5
                        health.image = health_ani[self.health]
                        #self.pos.x = 130
                        self.pos.y = 190
                        player.move()
                        
                        pygame.display.update()
                      
      #player mine animation
      def mine(self):
            # If attack frame has reached end of sequence, return to base frame      
            if self.mine_frame > 10:
                  self.mine_frame = 0
                  self.mining = False
       
            # Check direction for correct animation to display  
            if self.direction == "RIGHT":
                   self.image = attack_ani_R[self.mine_frame]
            elif self.direction == "LEFT":
                   self.correction(self.mine_frame)
                   self.image = attack_ani_L[self.mine_frame] 
 
            # Update the current attack frame  
            self.mine_frame += 1
            
      #to calculate player mine xp
      def calminexp(self,a):
            
            #new solution
            self.totminexp += a
            self.curminexp += a
            #handling if lvl =15
            
            if self.curminexp >= self.endminexp:
                  self.curminexp = 0
                  self.endminexp = self.xpcap[self.minelvl]
                  self.minelvl += 1
                  player.lvlupd = 'You achieved level ' + str(self.minelvl) + ' in mining!'

            if self.minelvl == 15:
                  self.curminexp = 0
                  self.endminexp = 0
                  self.minelvl = 15
                  player.lvlupd = "Already max mining lvl"
                  
            #old solution (not time efficient)
                  
##            for i,j in enumerate(self.xpcap):
##                  
##                  if self.xpcap[i] in self.mx:
##                        #print('true')
##                        continue
##                  elif self.curminexp >= self.xpcap[self.minelvl -1]:
##                        self.mx.append(self.xpcap[i])
##                        
##                        self.curminexp = self.endminexp - self.xpcap[self.minelvl - 1]
##                        
##                        self.endminexp =  self.xpcap[self.minelvl]
##                        
##                        self.minelvl += self.lvls[i] - 1 #if loaded lvl was 3, when levling up: 3 + 2 - 1 = lvl4
##                                                         #note to self: might add 1 to self.lvls and to self.lvls[i+1]
##                        player.lvlupd = 'You achieved level ' + str(self.minelvl) + ' in mining!'
##                  break
                  
      #for woodcutting animation
      def wcut(self):
            # If attack frame has reached end of sequence, return to base frame      
            if self.wcut_frame > 10:
                  self.wcut_frame = 0
                  self.wdcutting = False
       
            # Check direction for correct animation to display  
            if self.direction == "RIGHT":
                   self.image = attack_ani_R[self.wcut_frame]
            elif self.direction == "LEFT":
                   self.correction(self.mine_frame)
                   self.image = attack_ani_L[self.wcut_frame] 
 
            # Update the current attack frame  
            self.wcut_frame += 1
            
      #to calculate player woodcutting xp  
      def calwcutxp(self,a):
            
            
            self.totwcutxp += a
            self.curwcutxp += a
            
            if self.curwcutxp >= self.endwcutxp:
                  self.curwcutxp = 0
                  self.endwcutxp = self.xpcap[self.wcutlvl]
                  self.wcutlvl += 1
                  player.lvlupd = 'You achieved lvl ' + str(self.wcutlvl) + ' woodcutting!'

            if self.wcutlvl == 15 and self.curwcutxp > 0:
                  self.curwcutxp = 0
                  self.endwcutxp = 0
                  self.wcutlvl = 15
                  player.lvlupd = "Already max wdcutting lvl"

      #player attack animation         
      def attack(self):
            # If attack frame has reached end of sequence, return to base frame      
            if self.attack_frame > 10:
                  self.attack_frame = 0
                  self.attacking = False
       
            # Check direction for correct animation to display  
            if self.direction == "RIGHT":
                   self.image = attack_ani_R[self.attack_frame]
            elif self.direction == "LEFT":
                   self.correction(self.attack_frame)
                   self.image = attack_ani_L[self.attack_frame] 
 
            # Update the current attack frame  
            self.attack_frame += 1

      #to calculate player attacking xp
      def calattxp(self,a):
            
            self.totattxp += a
            self.curattxp += a

            
            
            if self.curattxp >= self.endattxp:
                  self.curattxp = 0
                  self.endattxp = self.xpcap[self.attlvl]
                  self.attlvl += 1
                  player.lvlupd = 'You achieved lvl ' + str(self.attlvl) + ' in attack!'

            #handling when players level is 15 (max)
            if self.attlvl == 15 and self.curattxp > 0:
                  self.curattxp = 0
                  self.endattxp = 0
                  self.attlvl = 15
                  player.lvlupd = "Already max attack lvl"

      
      def correction(self,a):
            
            # Function is used to correct an error
            # with character position on left attack frames
            if a == 1:
                  self.pos.x -= 20
            if a == 10:
                  self.pos.x += 20


#enemy class when the player enters the dungeon
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load(os.path.join('assets',"Enemy.png"))
            self.rect = self.image.get_rect()     
            self.pos = vec(0,0)
            self.vel = vec(0,0)

            self.direction = random.randint(0,1) # 0 for Right, 1 for Left
            self.vel.x = random.randint(2,6) / 2  # Randomised velocity of the generated enemy

            # Sets the intial position of the enemy  
            if self.direction == 0:
                  self.pos.x = 0
                  self.pos.y = 340   #can make new enemies (arial) by changing y
            if self.direction == 1:
                  self.pos.x = 700
                  self.pos.y = 340


      def move(self):
            
        # Causes the enemy to change directions upon reaching the end of screen    
            if self.pos.x >= (WIDTH-20):
                  self.direction = 1
            elif self.pos.x <= 0:
                    self.direction = 0

        # Updates positon with new values     
            if self.direction == 0:
                  self.pos.x += self.vel.x
            if self.direction == 1:
                  self.pos.x -= self.vel.x
            
            self.rect.center = self.pos # Updates rect
               
      def update(self):
            # Checks for collision with the Player
            hits = pygame.sprite.spritecollide(self, Playergroup, False)
            pressed_keys = pygame.key.get_pressed()
            
            # Activates upon either of the two expressions being true
            if (hits and player.attacking == True):
                  player.calattxp(5)
                  player.upd = 'You killed an enemy! + 5xp'
                  print("Enemy Killed")
                  self.kill()
                           
                   
            #once the player died (hearts <=0), handler.world = 0 (surface), once that happens all enemies are cleared
            elif handler.world != 1:
                  self.kill()
                  
            # Escape the dungeon
            elif pressed_keys[K_ESCAPE] and handler.world == 1:
                  player.upd = 'Escaped dungeon at stage ' + str(handler.stage)
                  handler.enemy_count = 0
                  handler.world = 0
                  player.map == 1 #so player can perform skilling in that map
                  handler.map1()  #so object sprites of the map renders
                  self.health = 5
                  health.image = health_ani[self.health]
                  #player.pos.x = 130
                  player.pos.y = 190
                  #self.jumping == False
                  #self.running == True
                  
                  
                  #change the vel so that the animation keep going
            
            
                  handler.stage = 1
                  self.kill()
            

            # If collision has occured and player not attacking, call "hit" function            
            elif hits and player.attacking == False:
                  player.upd = 'You got hit and lost a heart'
                  player.player_hit()
                  
            #to exit house
            if pressed_keys[K_ESCAPE] and handler.house == 1:
                  player.upd = 'Escaped house'
                  handler.house = 0
                  player.map = 1
                  handler.map1()
                  player.pos.x = 450
                  player.pos.y = 330

      
                  
      def render(self):
            # Displayed the enemy on screen
            window.blit(self.image, (self.pos.x, self.pos.y))

      
            
#Eventer handler class which stores if the player is in a house or dungeon (including the stage and a function to move on the next one)
#Also creates tkinter pop-up to confirm if the player wants to enter the place
#Has functions which hides/unhides objects for each map location and place
class EventHandler():
      def __init__(self):
            self.enemy_count = 0
            self.dead_enemy_count = 0
            self.battle = False
            self.enemy_generation = pygame.USEREVENT + 2
            self.enemy_generation2 = pygame.USEREVENT + 3
            self.stage = 1
            self.money = 0
            self.world = 0
            self.house = 0

            self.stage_enemies = []
            for x in range(1, 21):
                  self.stage_enemies.append(int((x ** 2 / 2) + 1))
                  #1,3,5,9,13,19
            
      def stage_handler(self):
            # Code for the Tkinter stage selection window
            self.root = Tk()
            self.root.geometry('200x170')
            
            button1 = Button(self.root, text = "Enter Dungeon", width = 18, height = 2,
                            command = self.world1)
            #button2 = Button(self.root, text = "Skyward Dungeon", width = 18, height = 2,
            #                command = self.world2)
            #button3 = Button(self.root, text = "Hell Dungeon", width = 18, height = 2,
            #                command = self.world3)
             
            button1.place(x = 40, y = 15)
            #button2.place(x = 40, y = 65)
            #button3.place(x = 40, y = 115)
            
            self.root.mainloop()

      def house_handler(self):
            # Entering house tkinter
            
            # create the tkinter window
            self.root = Tk()
            self.root.title("House.")                  
            #self.root.geometry('400x170')

            inLabel = Label(self.root, text="You feel an ominous presence from the house.")
            inLabel.grid(row=0,column=0)
            inLabel2 = Label(self.root, text="Do you still want to enter?", font=2)
            inLabel2.grid(row=1,column=0)

            # yes and no button
            noButton = Button(self.root, text="  No  ", bg="green", fg="white", command=self.root.destroy)
            noButton.grid(row=2, column=0, padx=5, pady=5)
            enterButton = Button(self.root, text="  Yes  ", bg="red", fg="black", command=self.house1) 
            enterButton.grid(row=3, column=0, padx=5, pady=5)

            self.root.mainloop()

      def towerdef_handler(self):
            # Entering house tkinter
            
            # create the tkinter window
            self.root = Tk()
            self.root.title("Tower defence minigame menu.")                  
            #self.root.geometry('400x170')

            inLabel = Label(self.root, text="Do you want to play Tower Defence minigame?", font=2)
            inLabel.grid(row=0,column=0)
            inLabel2 = Label(self.root, text="You will gain tower defence experience.") #note to self: put description about the game
            inLabel2.grid(row=1,column=0)

            # enter button
            enterButton = Button(self.root, text="  Yes  ", fg="black", command=self.house1) 
            enterButton.grid(row=3, column=0, padx=5, pady=5)

            self.root.mainloop()

            
      def world1(self):
            self.root.destroy()
            self.world = 1
            player.map == 0
            
            pygame.time.set_timer(self.enemy_generation, 2000)
            
            c_ore1.hide = True
            c_ore2.hide = True
            c_ore3.hide = True
            s_ore1.hide = True
            d_ore1.hide = True
            otree1.hide = True
            otree2.hide = True
            otree3.hide = True
            wtree1.hide = True
            mtree1.hide = True
            dungeon.hide = True
            #lake1.hide = True
            fountain.hide = True
            main_tower.hide = True
            teddy.hide = True
            self.battle = True
            
      
      def house1(self):
            self.root.destroy()
            #print('accessed house')
            self.house = 1

            c_ore1.hide = True
            c_ore2.hide = True
            c_ore3.hide = True
            s_ore1.hide = True
            d_ore1.hide = True
            otree1.hide = True
            otree2.hide = True
            otree3.hide = True
            wtree1.hide = True
            mtree1.hide = True
            dungeon.hide = True
            #lake1.hide = True
            fountain.hide = True
            main_tower.hide = True
            teddy.hide = False
            #self.battle = True

            
      def next_stage(self):  # Code for when the next stage is clicked            
            self.stage += 1
            if self.stage == 7:
                  handler.world = 0
                  player.upd = 'Completed all 6 stages in dungeon!'
                  self.enemy_count = 0
                  self.world = 0
                  player.map == 1 #returns player back to the surface
                  self.map1()  #so object sprites of the map renders
                  self.health = 5
                  health.image = health_ani[self.health]
                  player.pos.x = 130
                  player.pos.y = 190
                  player.move()
            else:      
                  print("Stage: "  + str(self.stage))
                  self.enemy_count = 0
                  pygame.time.set_timer(self.enemy_generation, 1500 - (50 * self.stage))      



      def map1(self):
            
            #objects in map1
            main_tower.hide = False
            c_ore1.hide = False
            c_ore2.hide = False
            c_ore3.hide = False
            s_ore1.hide = False
            d_ore1.hide = False
            otree1.hide = False
            otree2.hide = False
            otree3.hide = False
            wtree1.hide = False
            mtree1.hide = False
            fountain.hide = False
            teddy.hide = True
            dungeon.hide = False
            #lake1.hide = False

      #note to self: have objects in an array and use for loop to hide them
      def map2(self):
            
            #objects in map1
            main_tower.hide = True
            c_ore1.hide = True
            c_ore2.hide = True
            c_ore3.hide = True
            s_ore1.hide = True
            d_ore1.hide = True
            otree1.hide = True
            otree2.hide = True
            otree3.hide = True
            wtree1.hide = True
            mtree1.hide = True
            fountain.hide = True
            
            teddy.hide = True
            dungeon.hide = True
            #lake1.hide = True

      def map3(self):
            
            #objects in map1
            c_ore1.hide = True
            c_ore2.hide = True
            c_ore3.hide = True
            s_ore1.hide = True
            d_ore1.hide = True
            otree1.hide = True
            otree2.hide = True
            otree3.hide = True
            wtree1.hide = True
            mtree1.hide = True
            fountain.hide = True
            main_tower.hide = True
            teddy.hide = True
            dungeon.hide = True
            #lake1.hide = True
            
            
            
class HealthBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load(os.path.join('assets',"heart5.png"))

      def render(self):
            window.blit(self.image, (10,10))

class MapImg(pygame.sprite.Sprite):
      def __init__(self,a):
            super().__init__()
            self.mapimg = pygame.image.load(os.path.join('assets',a))
      def render(self):
            self.mapimg = pygame.transform.scale(self.mapimg, (WIDTH,HEIGHT))
            window.blit(self.mapimg, (0, 0))

class Button2:
      def __init__(self,x,y,width,height,fg,bg,content,fontsize):
            self.font = regularfont 
            self.content = content
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.fg = fg
            self.bg = bg

            self.image = pygame.Surface((self.width, self.height))
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            self.text = self.font.render(self.content,True,self.fg)
            self.text_rect = self.text.get_rect(center=(self.width/2,self.height/2))

            #drawing the text onto the image
            self.image.blit(self.text, self.text_rect)

      def is_pressed(self, pos, pressed):
            if self.rect.collidepoint(pos):
                  if pressed[0]:
                        return True
                  return False
            return False

#petals for the intro screen (will be using this for agility gamemode soon)
class Petal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        rand_num = random.uniform(1,100)

        if rand_num >= 0 and rand_num <= 40:
              self.image = pygame.image.load(os.path.join('assets',"pinkpetal1.png")).convert_alpha()
              self.image = pygame.transform.scale(self.image, (17,17))
        if rand_num > 40 and rand_num <= 66:
              self.image = pygame.image.load(os.path.join('assets',"pinkpetal2.png")).convert_alpha()
              self.image = pygame.transform.scale(self.image, (20,20))
        if rand_num > 66 and rand_num <= 100:
              self.image = pygame.image.load(os.path.join('assets',"pinkpetal3.png")).convert_alpha()
              self.image = pygame.transform.scale(self.image, (20,20))
        
        self.rect = self.image.get_rect()
        self.speedy = random.randrange(1,5)
        self.speedx = random.randrange(-2,2)
        
    def update(self):
        self.rect.centery += self.speedy
        self.rect.centerx += self.speedx
        if self.rect.right>WIDTH or self.rect.left<0 or self.rect.bottom>HEIGHT:
            self.kill()

#input box class used in my game for typing username and password to login              
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
          
          if event.type == pygame.MOUSEBUTTONDOWN:
                
                
                 
            # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False
                
            # Change the current color of the input box.
                self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
          if event.type == pygame.KEYDOWN:
                
                
                if self.active:
                #if event.key == pygame.K_RETURN:
                    #print(self.text)
                    #self.text = ''
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                # Re-render the text.
                    self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
          
        # Resize the box if the text is too long.
          width = max(200, self.txt_surface.get_width()+10)
          self.rect.w = width

    def draw(self, window):
        # Blit the text.
          window.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
          pygame.draw.rect(window, self.color, self.rect, 2)


#window = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('ghostwhite')
COLOR_ACTIVE = pygame.Color('grey7')
FONT = pygame.font.Font(None, 32)
PETALSPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(PETALSPAWN, 500)
#start_music = pygame.mixer.Sound(os.path.join('audio',"soundtrack1.mp3"))
#ingamemusic = pygame.mixer.Sound(os.path.join('audio',"soundtrack2.mp3"))

#Objects.
#passing arguments changes the type of object and its position quickly
intro_background = pygame.image.load(os.path.join('assets','intro screen.png'))
intro_background = pygame.transform.scale(intro_background, (WIDTH,HEIGHT))
input_box1 = InputBox(650, 90, 140, 32)
input_box2 = InputBox(650, 150, 140, 32)
input_boxes = [input_box1, input_box2]
    
Enemies = pygame.sprite.Group()
#player = Player(0,0,1,0,0,1,0,0,1)
#Playergroup = pygame.sprite.Group()
#Playergroup.add(player)

hit_cooldown = pygame.USEREVENT + 1

background = Background()
ground = Ground(0,390)#,WIDTH, 390)
#ground2 = Ground(0,0)#, 250,300)
ground_group = pygame.sprite.Group()
ground_group.add(ground)
#ground_group.add(ground2)
map1img = MapImg('map1.png')
map2img = MapImg('map2.png')
map3img = MapImg('map3.png')

#map 1 objects

fountain = Fountain()
teddy = Teddy()

c_ore1 = Ore('copper ore.png', 600, 450)
c_ore2 = Ore('copper ore.png', 610, 410)
c_ore3 = Ore('copper ore.png', 550, 460)
s_ore1 = Ore('silver ore.png', 460, 400)
d_ore1 = Ore('diamond ore.png', 35, 150)
otree1 = Tree('oak tree.png',590,80)
otree2 = Tree('oak tree.png',550,130)
otree3 = Tree('oak tree.png',330,430)
wtree1 = Tree('willow tree.png',240,410)
mtree1 = Tree('maple tree.png',200,40)
#lake1 = Lake('lake2.png',90,400)
dungeon = Dungeon('dungeon.png', 60, 20)
house1img = MapImg('house room1.png')
main_tower = MainTower('main tower.png',260,310)


border = Border()
handler = EventHandler()
health = HealthBar()
skills = Skills()
status_bar = StatusBar()

#button on the intro screen
play_button = Button2(650,290,150,50,WHITE, BLACK, 'Play as guest',32)
login_button = Button2(650,200,100,50,WHITE, BLACK, 'Login',32)



def create_player(a,b,c,d,e,f,g,h,i):
      global player
      global Playergroup
      player = Player(a,b,c,d,e,f,g,h,i)
      Playergroup = pygame.sprite.Group()
      Playergroup.add(player)
      

#start_music.play()
#ingamemusic.play()

#The intro/menu screen
def intro_screen():
      intro = True
      #ingamemusic.set_volume(.0)
      #start_music.set_volume(.2)

      menu_petal = pygame.sprite.Group()

      usertext = smallerfont.render('Usename', True , WHITE) 
      user_rect = usertext.get_rect(x=650,y=75)

      passtext = smallerfont.render('Password', True , WHITE) 
      pass_rect = passtext.get_rect(x=650,y=135)


      with open("playerdatabase.txt") as f:
            while intro:
                  hide = False
                  for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                              pygame.quit()
                              sys.exit()
                        if event.type == PETALSPAWN:
                              petal = Petal()
                              petal.rect.centery = random.randint(0,10)
                              petal.rect.centerx = random.randint(WIDTH/2+300,WIDTH-5)
                              menu_petal.add(petal)
                        for box in input_boxes:
                              box.handle_event(event)
                  mouse_pos = pygame.mouse.get_pos()
                  mouse_pressed = pygame.mouse.get_pressed()
                  
                  if play_button.is_pressed(mouse_pos,mouse_pressed):
                        
                        intro = False
                        hide = True
                        global guest
                        guest = True
                        create_player(0,0,1,0,0,1,0,0,1)
                  
                  if login_button.is_pressed(mouse_pos,mouse_pressed):
                        print('login pressed')
                        for i in f:
                        
                              l = i.strip().split(',')
                              if str(l[0]) == str(input_box1.text) and str(l[1]) == str(input_box2.text):
                                    print('correct login')
                                    global username, password
                                    username = input_box1.text
                                    password = input_box2.text
                                    intro = False
                                    hide = True
                                    
                                    guest = False
                                    create_player(l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10])
                                    
                  
                  if hide == False:
                        window.blit(intro_background, (0,0))

                        menu_petal.draw(window)
                        menu_petal.update()                              
                        for box in input_boxes:
                              box.update()
                        #window.fill((130, 130, 130))
                        for box in input_boxes:
                              box.draw(window)
                        
                        window.blit(usertext,user_rect)
                        window.blit(passtext,pass_rect)
                        window.blit(play_button.image,play_button.rect)
                        window.blit(login_button.image,login_button.rect)
                        
                       
                        
                  FPS_CLOCK.tick(FPS)
                  pygame.display.update()
            
                  

def main():
      
      #start_music.set_volume(.0)
      #ingamemusic.set_volume(.2)
      
      while True:
                       
            if player.map == 1:
                  map1img.render()
                  image1 = pygame.image.load(os.path.join('assets',"fountain1.png"))
                  image1 = pygame.transform.scale(image1, (800,400))
                  window.blit(image1, (30, 20))
            elif player.map == 2:
                  map2img.render()
            elif player.map ==3:
                  map3img.render()
            
            if handler.world == 1:
                  player.gravity_check()
                  player.dungeonmove()
            
            #window.blit(status_bar.surf, (675, 20))
            
            if handler.world == 0:
                  handler.stage = 1
                  handler.enemy_count = 0
                  handler.dead_enemy_count = 0
                  
                  player.move()
                  
                  
            
            #start_time = get_current_time()
          #mouse = pygame.mouse.get_pos()
          
            for event in pygame.event.get():
                  if event.type == hit_cooldown:
                        player.cooldown = False
                  
                  # Will run when the close window button is clicked    
                  if event.type == QUIT:
                        pygame.quit()
                        sys.exit() 
                  if event.type == handler.enemy_generation:
                        if handler.enemy_count < handler.stage_enemies[handler.stage - 1]:
                              #print(handler.enemy_count)
                              #print(handler.stage_enemies[handler.stage - 1])
                              enemy = Enemy()
                              Enemies.add(enemy)
                              handler.enemy_count += 1
                        
                  # For events that occur upon clicking the mouse (left click) 
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        pass
       
                  # Event handling for a range of different key presses    
                  if event.type == pygame.KEYDOWN:

                        #if player presses n in dungeon, it moves onto the next stage
                        if handler.world == 1:
                              if event.key == pygame.K_n:
                                    if handler.battle == True and len(Enemies) == 0:
                                          handler.next_stage()

                                          
                        if event.key == pygame.K_SPACE:
                              player.jump()
                        if event.key == pygame.K_RETURN:
                              if player.attacking == False:
                                    player.attack()
                                    player.attacking = True 
                        
                        #mining 
                        
                        #copper ore
                        if event.key == pygame.K_q and player.map ==1 and 480 < player.rect.x < 650 and 345 < player.rect.y < 500:
                              rand_num = random.uniform(1,100)

                              if rand_num >= 0 and rand_num <= 25:  # 1 / 4 chance for an item (health) drop
                                    print('rare')
                                    player.upd = 'You swung and got ore! + 5xp'
                                    player.calminexp(5)
                                    #do updatemusic which plays sound once
                                    
                              elif rand_num >25 and rand_num <= 100:
                                    print('comman')
                                    player.upd = 'You swing and miss the rock.'

                              if player.mining == False:
                                    
                                    player.mine()
                                    player.mining = True

                        #silver ore 
                        if event.key == pygame.K_q and player.map ==1 and 400 < player.rect.x < 480 and 330 < player.rect.y < 400:
                              if player.minelvl < 5:
                                    player.upd = 'Need lvl 5 mining to mine silver.'
                              else:
                                    rand_num = random.uniform(1,100)

                                    if rand_num >= 0 and rand_num <= 20:  # 1 / 4 chance for an item (health) drop
                                          print('rare')
                                          player.upd = 'Swung and got silver ore! + 5xp'
                                          player.calminexp(20)
                                          #do updatemusic which plays sound once
                                          
                                    elif rand_num >20 and rand_num <= 100:
                                          print('comman')
                                          player.upd = 'You swing and miss the rock.'

                                    if player.mining == False:
                                          
                                          player.mine()
                                          player.mining = True

                        #trees                 
                        #oak tree
                        if event.key == pygame.K_q and player.map ==1 and ((480 < player.rect.x < 650 and 20 < player.rect.y < 160)or(270 < player.rect.x < 360 and 360 < player.rect.y < HEIGHT)):
                              rand_num = random.uniform(1,100)

                              if rand_num >= 0 and rand_num <= 25:  # 1 / 4 chance for an item (health) drop
                                    print('rare')
                                    player.upd = 'Swung and got oak logs! + 5xp'
                                    player.calwcutxp(5)
                                    #do updatemusic which plays sound once
                                    
                              elif rand_num >25 and rand_num <= 100:
                                    print('comman')
                                    player.upd = 'You swing and miss the tree.'

                              if player.wdcutting == False:
                                    
                                    player.wcut()
                                    player.wdcutting = True

                        #willow tree
                        if event.key == pygame.K_q and player.map ==1 and 180 < player.rect.x < 250 and 360 < player.rect.y < 470:
                              if player.wcutlvl < 5:
                                    player.upd = 'Need lvl 5 wdcut to cut willow.'
                              else:      
                                    rand_num = random.uniform(1,100)

                                    if rand_num >= 0 and rand_num <= 20:  # 1 / 4 chance for an item (health) drop
                                          print('rare')
                                          player.upd = 'Swung & got willow logs! + 5xp'
                                          player.calwcutxp(10)
                                          #do updatemusic which plays sound once
                                          
                                    elif rand_num >20 and rand_num <= 100:
                                          print('comman')
                                          player.upd = 'You swing and miss the tree.'

                                    if player.wdcutting == False:
                                          
                                          player.wcut()
                                          player.wdcutting = True

                        #to enter dungeon           
                        if event.key == pygame.K_q and player.map == 1 and 0 < player.rect.x < 155 and 0 < player.rect.y < 150:
                              
                              handler.stage_handler()

                        #to play tower defence minigame           
                        if event.key == pygame.K_q and player.map == 1 and 260< player.rect.x < 310 and 260< player.rect.y < 350:
                              
                              handler.towerdef_handler()

                        #to enter house1 (in map1)
                        if event.key == pygame.K_q and player.map == 1 and 480 < player.rect.x < 650 and 230 < player.rect.y < 330:
                              
                              handler.house_handler()
                              
                        #to go back to menu screen
                        if event.key == pygame.K_b:
                              
                              intro_screen()
                              #start_music.set_volume(.0)
                              #ingamemusic.set_volume(.05)
                        
                         
            border.render()
            
            player.update()
            
            if player.mining == True:     
                  player.mine()

            if player.wdcutting == True:     
                  player.wcut()
                   
            if player.attacking == True:
                  player.attack()
                  
           
            
            if handler.world == 1:
                  background.render()
                  ground.render()
                  
                  if player.health > 0:
                        window.blit(player.image, player.rect)
                  health.render()

            for entity in Enemies:
                entity.update()
                entity.move()
                if handler.world == 1:
                  entity.render()

            if handler.house == 1:
                  house1img.render()
                  
            #rendering surface objects
            c_ore2.update()
            c_ore1.update()
            c_ore3.update()
            s_ore1.update()
            dungeon.update()
            d_ore1.update()
            main_tower.update()
            otree1.update()
            otree2.update()
            otree3.update()
            wtree1.update()
            mtree1.update()
            #lake1.update()
            fountain.update()
            teddy.update()

                  
            skills.render()
            status_bar.update()
            
            window.blit(player.image, player.rect)
            
            #if the user plays as a guest, no data needs to be stored
            if guest == False:
                  with open("playerdatabase.txt") as f:
                        playerdatabase = f.readlines()

                  with open("playerdatabase.txt") as f:
                        line = 0
                        for i in f:
                              l = i.strip().split(',')
                              if str(l[0]) == username and str(l[1]) == password:
                                    playerdatabase[line] = str(username)+','+str(password)+','+str(player.totminexp)+','+str(player.curminexp)+','+str(player.minelvl)+','+str(player.totwcutxp)+','+str(player.curwcutxp)+','+str(player.wcutlvl)+','+str(player.totattxp)+','+str(player.curattxp)+','+str(player.attlvl)
                                    with open("playerdatabase.txt",'w') as g:
                                          g.writelines(playerdatabase)
                              line+=1

            pygame.display.update()
            FPS_CLOCK.tick(FPS)

intro_screen()
main()


