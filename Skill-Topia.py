#iteration3
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
          text = tinyfont.render('tot: ' + str(player.totminexp) , True , color_white)
          window.blit(text, (700, 245))
          
            
class Ore(pygame.sprite.Sprite):
      
      def __init__(self):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets','ores.png'))
            self.image = pygame.transform.scale(image, (190,120))
            self.rect = self.image.get_rect(center = (550, 420))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y))

class Trees(pygame.sprite.Sprite):
      
      def __init__(self):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets','trees.png'))
            self.image = pygame.transform.scale(image, (190,180))
            self.rect = self.image.get_rect(center = (550, 90))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y))

class Dungeon(pygame.sprite.Sprite):
      
      def __init__(self):
            super().__init__()
            self.hide = False
            image = pygame.image.load(os.path.join('assets','dungeon.png'))
            self.image = pygame.transform.scale(image, (190,180))
            self.rect = self.image.get_rect(center = (70, 90))

      def update(self):
            if self.hide == False:
                  window.blit(self.image, (self.rect.x, self.rect.y)) 


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
            #self.map = 1
            self.jumping = False
            self.running = True
            self.move_frame = 0

            

            self.attacking = False
            self.attack_frame = 0

            self.mining = False
            self.mine_frame = 0

            #using indexing to work out much xp is needed to level up
            self.lvls = [ 2, 3, 4, 5,  6,  7,  8,   9,  10,  11,  12,  13,  14,  15]
            self.xpcap =[10,20,40,80,160,320,640,1280,2560,3500,4500,5500,6500,8000]

            self.totminexp = 0
            self.curminexp = 0
            self.endminexp = self.xpcap[0]
            self.minelvl = 1
            self.x = []


      
      def move(self):

            self.acc = vec(0,0.5)

            
            pressed_keys = pygame.key.get_pressed()
          
 
            # Accelerates the player in the direction of the key press
            if pressed_keys[K_LEFT] and self.pos.x - 10 > 0:
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
            # Formulas to calculate velocity while accounting for friction
            self.acc.x += self.vel.x * FRIC
            #print('self.moveframe = ' +str(self.move_frame))
            self.vel += self.acc
            #self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values
            #self.vel += self.pos
                
            self.rect.midbottom = self.pos  # Update rect with new pos


                      
      def update(self):
          #print('self.moveframe = ' +str(self.move_frame))
          # Return to base frame if at end of movement sequence 
          if self.move_frame > 6:
                self.move_frame = 0
                return
          
          # Move the character to the next frame if conditions are met 
          if self.jumping == False and self.running == True:
                #print(abs(self.vel.x))
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
                  
                  if self.xpcap[i] in self.x:
                        print('true')
                        continue
                  elif self.curminexp >= self.xpcap[i]:
                        self.x.append(self.xpcap[i])
                        
                        self.curminexp = self.endminexp - self.xpcap[i]
                        
                        self.endminexp =  self.xpcap[i + 1]
                        
                        self.minelvl = self.lvls[i]
                  break
            

      def correction(self,a):
            
            # Function is used to correct an error
            # with character position on left attack frames
            if a == 1:
                  self.pos.x -= 20
            if a == 10:
                  self.pos.x += 20
                  
class StatusBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((205, 140))
            self.rect = self.surf.get_rect(center = (850, 30))
            #self.last = pygame.time.get_ticks()
            #self.statuscooldown = 2000 #2 sec
            self.text = regularfont.render('' , True , color_white)
            window.blit(self.text, (675, 20))
            
            #self.exp = player.experiance
            
      def update_draw(self,a):
            # Create the text to be displayed

            
            self.text = regularfont.render(a , True , color_white)
            #text1 = smallerfont.render("STAGE: " + str(handler.stage) , True , color_white)
            #text2 = smallerfont.render("EXP: " + str(player.experiance) , True , color_white)
            
            #print('printing')
            # Draw the text to the status bar
            window.blit(self.text, (675, 20))
            
            #displaysurface.blit(text1, (585, 7))
            #displaysurface.blit(text2, (585, 22))
            
      
                   
                
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()


        
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
            self.root.destroy()
            pygame.time.set_timer(self.enemy_generation, 2000)
            #button.imgdisp = 1
            ore.hide = True
            trees.hide = True
            dungeon.hide = True
            #self.battle = True

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

##      def map1(self):
##            
##            #button.imgdisp = 1
##            ore.hide = True
##            trees.hide = True
##            dungeon.hide = True
##            #self.battle = True
 
            
#objects

background = Background()
ground = Ground()
player = Player()
ore = Ore()      #can pass in values to create different type of ores
trees = Trees()
dungeon = Dungeon()
border = Border()
handler = EventHandler()
skills = Skills()
status_bar = StatusBar()
#dts = DisplayToScr()
t = ''
while True:
      window.fill(GREEN)
      window.blit(status_bar.surf, (675, 20))
      
      #start_time = get_current_time()
    #mouse = pygame.mouse.get_pos()
    
      for event in pygame.event.get():
            start_time = pygame.time.get_ticks()
            # Will run when the close window button is clicked    
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit() 
             
            # For events that occur upon clicking the mouse (left click) 
            if event.type == pygame.MOUSEBUTTONDOWN:
                  pass
 
            # Event handling for a range of different key presses    
            if event.type == pygame.KEYDOWN:

                  
                  #mining   #also if there in certain map  
                  if event.key == pygame.K_q and 450 < player.rect.x < 650 and 300 < player.rect.y < 500:
                        rand_num = random.uniform(1,100)

                        if rand_num >= 0 and rand_num <= 25:  # 1 / 4 chance for an item (health) drop
                              print('rare')
                              t = 'You got ore. +5xp.'
                              player.calminexp(5)
                              #do updatemusic which plays sound once
                              
                              
                        elif rand_num >25 and rand_num <= 100:
                              print('comman')
                              t = 'You hit the rock.'
                              #status_bar.update_draw("You hit the rock.")

                        
                        if player.mining == False:
                              
                              player.mine()
                              
                              
            
                                                            #time.sleep(1)
                              player.mining = True
                              
                  if event.key == pygame.K_q and 0 < player.rect.x < 155 and 0 < player.rect.y < 150:
                        handler.stage_handler()        
      
      
      border.render()
      player.update()
      
      if player.mining == True:
                                  #call a display function and pass in the text?
            
            
                  
            player.mine()
            
            
      if player.attacking == True:
            player.attack()
            
      player.move()
      #background.render()
      
      ore.update()
      trees.update()
      dungeon.update()
      skills.render()
      #window.blit(status_bar.surf, (675, 20))
      #print(t)
      text = regularfont.render(t , True , color_white)
      window.blit(text, (675, 20))
            
      #status_bar.update_draw()
      window.blit(player.image, player.rect)

      pygame.display.update()
      FPS_CLOCK.tick(FPS)
