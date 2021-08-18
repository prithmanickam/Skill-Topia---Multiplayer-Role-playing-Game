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
BLACK = (255,255,255)
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
#text = regularfont.render('LOAD' , True , color_light)


skills = {'attack':{'lvl':1,'xp':0},'mining':{'lvl':1,'xp':0},'fishing':{'l':1,'xp':0},'woodcutting':{'lvl':1,'xp':0}}

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
        self.image = pygame.image.load(os.path.join('assets',"Ground.png"))
        self.rect = self.image.get_rect(center = (450, 450))
        self.bgX1 = 0
        self.bgY1 = 390

    def render(self):
        window.blit(self.image, (self.bgX1, self.bgY1)) 

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




class Skills(pygame.sprite.Sprite): #draw square
      def __init__(self):
          super().__init__()
          image = pygame.image.load(os.path.join('assets','skill stats.png'))
          self.image = pygame.transform.scale(image, (230,313))
          self.rect = self.image.get_rect(center = (778, 320))
      def render(self):
          window.blit(self.image, (self.rect.x, self.rect.y))
          text = regularfont.render('Skill Stats', True , color_white)
          window.blit(text, (700, 170))
          
          #text, will keep getting updated every tick
          #mining
          text = smallerfont.render('mining', True , color_white)
          window.blit(text, (700, 200))
          text = tinyfont.render('lvl: ' + str(player.minelvl), True , color_white)
          window.blit(text, (700, 215))
          text = tinyfont.render('xp: ' + str(player.curminexp) + '/' + str(player.endminexp), True , color_white)
          window.blit(text, (700, 230))
          #text = tinyfont.render('tot: ' + str(player.totminexp) , True , color_white)
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

             
            
class Ore(pygame.sprite.Sprite):
      
      def __init__(self, orename, posx, posy):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets',orename))
            self.image = pygame.transform.scale(image, (65,55))
            self.rect = self.image.get_rect(center = (posx, posy))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y))

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

class Lake(pygame.sprite.Sprite):
      
      def __init__(self, lakename, posx, posy):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets',lakename))
            self.image = pygame.transform.scale(image, (210,200))
            self.rect = self.image.get_rect(center = (posx, posy))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y))

class Dungeon(pygame.sprite.Sprite):
      
      def __init__(self, dname, posx, posy):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets',dname))
            self.image = pygame.transform.scale(image, (190,180))
            self.rect = self.image.get_rect(center = (posx, posy))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y)) 



#player1 = Player(makeSprite("boyninjarun.png", 24), p1Proj, (800, 700), screenW, scrollRate, options.keysP1)
class Player(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            #P1Left = options.keysP1[0]
	    #P1Right = options.keysP1[1]
            self.image = pygame.image.load(os.path.join('assets',"Player_Sprite_R.png"))
            self.rect = self.image.get_rect() #rect defaults to a value of (0 , 0)
            
            # Position and direction
            self.vx = 0
            self.pos = vec((340, 240))
            self.vel = vec(0,0)
            self.acc = vec(0,0)
            self.direction = "RIGHT"
            self.map = 1 #player starts here on the map
            self.jumping = False
            self.running = True
            self.move_frame = 0

            self.upd = ''
            self.lvlupd = ''

            #using indexing to work out much xp is needed to level up
            self.lvls = [ 2, 3, 4, 5,  6,  7,  8,   9,  10,  11,  12,  13,  14,  15]
            self.xpcap =[10,20,40,80,160,320,640,1280,2560,3500,4500,5500,6500,8000]

            self.mining = False
            self.mine_frame = 0

            self.totminexp = 0
            self.curminexp = 0
            self.endminexp = self.xpcap[0]
            self.minelvl = 1
            self.mx = []

            self.wdcutting = False
            self.wcut_frame = 0

            self.totwcutxp = 0
            self.curwcutxp = 0
            self.endwcutxp = self.xpcap[0]
            self.wcutlvl = 1
            self.wx = []

            self.attacking = False
            self.attack_frame = 0
            
            
            self.totattxp = 0
            self.curattxp = 0
            self.endattxp = self.xpcap[0]
            self.attlvl = 1
            self.atx = []
            self.immune = False
            self.special = False
            self.experiance = 0
            self.cooldown = False
            self.health = 5
            self.magic_cooldown = 1
            self.mana = 0


      
      def move(self):

            self.acc = vec(0,0.5)

            # Returns the current key presses
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
                      
      

      def gravity_check(self):
            hits = pygame.sprite.spritecollide(player ,ground_group, False)
            if self.vel.y > 0:
                  if hits:
                        lowest = hits[0]
                        if self.pos.y < lowest.rect.bottom:
                              self.pos.y = lowest.rect.top + 1
                              self.vel.y = 0
                              self.jumping = False
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
                        #print(Enemies)
                        self.health = 5
                        health.image = health_ani[self.health]
                        #self.pos.x = 130
                        self.pos.y = 190
                        player.move()
                        
                        pygame.display.update()
                      
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
            
      def calattxp(self,a):
            
            self.totattxp += a
            self.curattxp += a
            
            
            for i,j in enumerate(self.xpcap):
                  
                  if self.xpcap[i] in self.atx:
                        #print('true')
                        continue
                  elif self.curattxp >= self.xpcap[i]:
                        self.atx.append(self.xpcap[i])
                        
                        self.curattxp = self.endattxp - self.xpcap[i]
                        
                        self.endattxp =  self.xpcap[i + 1]
                        
                        self.attlvl = self.lvls[i]
                        player.lvlupd = 'You achieved level ' + str(self.attlvl) + ' attack!'
                  break
            
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
            
            
      def calminexp(self,a):
            
            self.totminexp += a
            self.curminexp += a
            
            
            for i,j in enumerate(self.xpcap):
                  
                  if self.xpcap[i] in self.mx:
                        #print('true')
                        continue
                  elif self.curminexp >= self.xpcap[i]:
                        self.mx.append(self.xpcap[i])
                        
                        self.curminexp = self.endminexp - self.xpcap[i]
                        
                        self.endminexp =  self.xpcap[i + 1]
                        
                        self.minelvl = self.lvls[i]
                        player.lvlupd = 'You achieved level ' + str(self.minelvl) + ' in mining!'
                  break

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
            
            
      def calwcutxp(self,a):
            
            self.totwcutxp += a
            self.curwcutxp += a
            
            
            for i,j in enumerate(self.xpcap):
                  
                  if self.xpcap[i] in self.wx:
                        continue
                  elif self.curwcutxp >= self.xpcap[i]:
                        self.wx.append(self.xpcap[i])
                        
                        self.curwcutxp = self.endwcutxp - self.xpcap[i]
                        
                        self.endwcutxp =  self.xpcap[i + 1]
                        
                        self.wcutlvl = self.lvls[i]
                        player.lvlupd = 'You achieved lvl ' + str(self.wcutlvl) + ' wdcutting!'
                  break
                  
      
      def correction(self,a):
            
            # Function is used to correct an error
            # with character position on left attack frames
            if a == 1:
                  self.pos.x -= 20
            if a == 10:
                  self.pos.x += 20
                
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
            #print("fff")

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

      
                  
      def render(self):
            # Displayed the enemy on screen
            window.blit(self.image, (self.pos.x, self.pos.y))

      
            
        
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

            self.stage_enemies = []
            for x in range(1, 21):
                  self.stage_enemies.append(int((x ** 2 / 2) + 1))
                  #1,3,5,9,13,19
            
      def stage_handler(self):
            # Code for the Tkinter stage selection window
            self.root = Tk()
            self.root.geometry('200x170')
            
            button1 = Button(self.root, text = "Twilight Dungeon", width = 18, height = 2,
                            command = self.world1)
            button2 = Button(self.root, text = "Skyward Dungeon", width = 18, height = 2,
                            command = self.world2)
            button3 = Button(self.root, text = "Hell Dungeon", width = 18, height = 2,
                            command = self.world3)
             
            button1.place(x = 40, y = 15)
            button2.place(x = 40, y = 65)
            button3.place(x = 40, y = 115)
            
            self.root.mainloop()
      
      def world1(self):
            self.world = 1
            player.map == 0
            self.root.destroy()
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
            lake1.hide = True
            self.battle = True

      def world2(self):
            self.root.destroy()
            background.bgimage = pygame.image.load("desert.jpg")
            ground.image = pygame.image.load("desert_ground.png")
       
            pygame.time.set_timer(self.enemy_generation2, 2500)
       
            self.world = 2
            button.imgdisp = 1
            castle.hide = True
            
            self.battle = True
            
            

      def world3(self):
            self.battle = True
            button.imgdisp = 1

            
            
      def next_stage(self):  # Code for when the next stage is clicked            
            self.stage += 1
            if self.stage == 7:
                  handler.world = 0
                  player.upd = 'Completed all 6 stages in dungeon!'
                  self.enemy_count = 0
                  self.world = 0
                  player.map == 1 #so player can perform skilling in that map
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
            dungeon.hide = False
            lake1.hide = False
            
      def map2(self):
            
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
            dungeon.hide = True
            lake1.hide = True
            
            
class HealthBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load(os.path.join('assets',"heart5.png"))

      def render(self):
            window.blit(self.image, (10,10))
#Objects.
#passing arguments changes the type of object and its position quickly
intro_background = pygame.image.load(os.path.join('assets','skill stats.png'))

Enemies = pygame.sprite.Group()
player = Player()
Playergroup = pygame.sprite.Group()
Playergroup.add(player)

hit_cooldown = pygame.USEREVENT + 1

background = Background()
ground = Ground()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)

#map 1 objects

c_ore1 = Ore('copper ore.png', 600, 450)
c_ore2 = Ore('copper ore.png', 610, 410)
c_ore3 = Ore('copper ore.png', 550, 460)
s_ore1 = Ore('silver ore.png', 460, 400)
d_ore1 = Ore('diamond ore.png', 35, 150)
otree1 = Tree('oak tree.png',570,80)
otree2 = Tree('oak tree.png',530,130)
otree3 = Tree('oak tree.png',330,430)
wtree1 = Tree('willow tree.png',240,410)
mtree1 = Tree('maple tree.png',230,60)
lake1 = Lake('lake2.png',90,400)
dungeon = Dungeon('dungeon.png', 100, 75)


border = Border()
handler = EventHandler()
health = HealthBar()
skills = Skills()
status_bar = StatusBar()
t = ''

print('handler.stage is ' + str(handler.stage))
print('handler.enemy_count is ' + str(handler.enemy_count))


while True:
      if handler.world == 1:
            player.gravity_check()
            player.dungeonmove()
      window.fill(GREEN)
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

                  #silver ore ####
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

                        if rand_num >= 0 and rand_num <= 20:  # 1 / 4 chance for an item (health) drop
                              print('rare')
                              player.upd = 'Swung and got oak logs! + 5xp'
                              player.calwcutxp(5)
                              #do updatemusic which plays sound once
                              
                        elif rand_num >20 and rand_num <= 100:
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
                                    player.calwcutxp(5)
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
                  
                   
      
      
      border.render()
      
      player.update()
      
      if player.mining == True:     
            player.mine()

      if player.wdcutting == True:     
            player.wcut()
             
      if player.attacking == True:
            player.attack()
            
##      if handler.world == 1:
##            player.dungeonmove() #if in dungeon, include jumping and acceleration
##      else:
##            player.move()

      
      
      if handler.world == 1:
            background.render()
            ground.render()
            if player.health > 0:
                  window.blit(player.image, player.rect)
            health.render()

      for entity in Enemies:
          entity.update()
          entity.move()
          entity.render()
      
      
      c_ore2.update()
      c_ore1.update()
      
      c_ore3.update()
      s_ore1.update()
      dungeon.update()
      d_ore1.update()
      otree1.update()
      otree2.update()
      otree3.update()
      wtree1.update()
      mtree1.update()
      lake1.update()
      

      
      skills.render()
      status_bar.update()
      #window.blit(status_bar.surf, (675, 20))
      #print(t)
##      text = regularfont.render(t , True , color_white)
##      window.blit(text, (675, 20))
            
      #status_bar.update_draw()
      window.blit(player.image, player.rect)

      pygame.display.update()
      FPS_CLOCK.tick(FPS)
