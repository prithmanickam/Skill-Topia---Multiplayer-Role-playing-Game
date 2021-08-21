import pygame, sys, os, time, math

#initialising variables

scrwid = 800
scrhei = 600
squsize = 50
fps = 30

enemylist = []
towerlist = []
bulletlist = []
iconlist = []
senderlist = []

def imgLoad(file,size=None):
    #to enable pixel perfect collision for transparent images
    image = pygame.image.load(file).convert_alpha() 
    return pygame.transform.scale(image,size) if size else image

class Player_towerdef:
    #the towers that are available in a list form
    towers = [
        'Stone',
        'Gold',
        'Sniper',
        'Ninja',
        'Cannon',
        'Laser']
        #'ice']
    
   #player starts with 20 health and 450 money
    def __init__(self): 
        self.health = 20
        self.money = 450

player = Player_towerdef()

EnemyImageArray = dict()
TowerImageArray = dict()

#stores towers and enemies in seperate dictionaries 
def loadImages():
    
    for tower in player.towers:
        TowerImageArray[tower] = imgLoad('my_tower_defence_minigame/towers/'+tower+'.png')

    canoe = imgLoad('my_tower_defence_minigame/enemies/canoe.png')
    canoe = pygame.transform.scale(canoe, (40,35))
    EnemyImageArray['canoe'] = canoe 

    jetski = imgLoad('my_tower_defence_minigame/enemies/jetski.png')
    jetski = pygame.transform.scale(jetski, (50,45))
    EnemyImageArray['jetski'] = jetski

    pirateship = imgLoad('my_tower_defence_minigame/enemies/pirateship.png')
    pirateship = pygame.transform.scale(pirateship, (45,70))
    EnemyImageArray['pirateship'] = pirateship

    carrier = imgLoad('my_tower_defence_minigame/enemies/carrier.png')
    carrier = pygame.transform.scale(carrier, (45,80))
    EnemyImageArray['carrier'] = carrier

#function to get an angle between two 2d vector points
def get_angle(a,b):
    return 180-(math.atan2(b[0]-a[0],b[1]-a[1]))/(math.pi/180)

class Map:
    def __init__(self):
        self.map = 'sea harbour'
        self.loadmap()

    #reads the targers and waves file
    def loadmap(self):
        self.targets = eval(open('my_tower_defence_minigame/maps/%s/targets.txt' % self.map,'r').read())
        self.waves = eval(open('my_tower_defence_minigame/maps/%s/waves.txt' % self.map,'r').read())

    def getmovelist(self):
        self.pathpoints = []
        for i in range(len(self.targets)-1):
            a,b = self.targets[i:i+2]
            self.pathpoints+=[0]
        

    def get_background(self):
        background = pygame.image.load(os.path.join('my_tower_defence_minigame','maps','sea harbour',"tower defence sea.png"))
        background = pygame.transform.scale(background, (960,510))
        
        #draws line of the between each point in self.targets (path of enemy boats)
        for i in range(len(self.targets)-1):
            pygame.draw.line(background,(0,0,0),self.targets[i],self.targets[i+1])
        return background

mapvar = Map()

class EnemyBoat:
    
    #layers of the ship
    
    layers = [ # Name Health Speed CashPrize
              ('canoe',      1, 1.0, 2), 
              ('jetski',     1, 1.5, 2), 
              ('pirateship', 6, 0.7, 10),  
              ('carrier',   15, 1.0, 20)] 

    def __init__(self,layer):
        self.layer = layer
        self.setlayer()
        
        self.targets = mapvar.targets
        self.pos = list(self.targets[0])
        self.target = 0
        self.next_target()
        self.rect = self.image.get_rect(center=self.pos)
        self.distance = 0

        self.angle = 0

        enemylist.append(self)
        
    #initalises the next layer of the boat (if its not the final canoe layer) if its previous layer was destroyed
    def setlayer(self):
        self.name,self.health,self.speed,self.cashprize = self.layers[self.layer]
        self.image = EnemyImageArray[self.name]
        self.imagecopy = self.image.copy()

    def nextlayer(self):
        self.layer-=1
        self.setlayer()

    def next_target(self):
        #if the enemy boat has not reached the final target:
        #-change the angle of the image between its current point to its next
        #-transform the the enemy boat imagecopy so that it follows the path correctly and the resolution doesn't get progressivly worse
        if self.target<len(self.targets)-1:
            self.target+=1
            t=self.targets[self.target]
            self.angle = 180-(math.atan2(t[0]-self.pos[0],t[1]-self.pos[1]))/(math.pi/180)
            self.vx,self.vy = math.sin(math.radians(self.angle)),-math.cos(math.radians(self.angle))
            self.image = pygame.transform.rotate(self.imagecopy,-self.angle)
            
        #if the enemy boat reaches the final target (dock - end territory),
        #it would be removed and the health would be take away from the player depending on the layer of the boat
        else:
            self.kill()
            player.health-=self.layer+1

    def hit(self,damage):
        self.health -= damage
        #if enemy dies move on to the next layer
        #if it dies at the final layer (canoe), the object will be removed
        if self.health<=0:
            player.money+=self.cashprize
            if self.layer>0: 
                self.nextlayer() 
            else:
                self.kill()

    def kill(self):
        enemylist.remove(self)

    #allows the enemy boat move to each target point
    def move(self,frametime):
        speed = frametime*fps*self.speed
        a,b = self.pos,self.targets[self.target]
        
        a[0] += self.vx*speed
        a[1] += self.vy*speed
        
        if (b[0]-a[0])**2+(b[1]-a[1])**2<=speed**2:
            self.next_target()
        self.rect.center = self.pos
        self.distance+=speed

class Tower:
    def __init__(self,pos):
        self.targetTimer = 0
        self.rect = self.image.get_rect(center=pos)
        towerlist.append(self)

    #It sets the time when the tower can fire (firerate)
    #When its time for the tower to fire, it draws the line from the tower to the enemy boat to indicate that it has been hit
    def takeTurn(self,frametime,screen):
        self.startTargetTimer = self.firerate
        self.targetTimer -= frametime
        if self.targetTimer<=0:
            enemypoint = self.target()
            if enemypoint:
                pygame.draw.line(screen,(255,255,255),self.rect.center,enemypoint)
                self.targetTimer=self.startTargetTimer
                
    def target(self):
        #iterates through the list of enemies on the screen sorted by closest distance:
        #-get the angle and rotate the image of the tower to point towards the enemy boat
        #-(similarly with enemy boats) transform the the tower imagecopy so that the resolution doesn't get progressivly worse
        #-gives certain amount of damage to the enemy boat depending on the tower
        for enemy in sorted(enemylist,key=lambda i: i.distance,reverse=True):
            if (self.rect.centerx-enemy.rect.centerx)**2+(self.rect.centery-enemy.rect.centery)**2<=self.rangesq:
                self.angle = int(get_angle(self.rect.center,enemy.rect.center))
                self.image = pygame.transform.rotate(self.imagecopy,-self.angle)
                self.rect = self.image.get_rect(center=self.rect.center)
                enemy.hit(self.damage)
                return enemy.rect.center

class createTower(Tower):
    def __init__(self,tower,pos,info):
        self.tower = tower
        self.cost,self.firerate,self.range,self.damage = info
        self.rangesq = self.range**2
        
        self.image = TowerImageArray[tower]
        self.imagecopy = self.image.copy()
        self.angle = 0
        Tower.__init__(self,pos) #creates the tower object

#Icons on the right panel to buy the towers
class Icon:
    towers = { # Cost FireRate Range Damage
        'Stone'         : [ 180, 1.0, 100, 0.4],
        'Gold'        : [ 300, 1.0, 60, 1],
        'Sniper'       : [ 400, 3.5, 200, 1.5],
        'Ninja'        : [ 400, 0.1, 80, 0.1],  #dps is still 1 (useful for chip damage)
        'Cannon'          : [ 500, 2.0, 60, 3],
        'Laser'         : [ 900, 1.5, 120, 2]}
        #'Ice'           : [ 400, 0.1, 80, 1] #make ice slow down
        
        

    def __init__(self,tower):
        self.tower = tower
        self.cost,self.firerate,self.range,self.damage = self.towers[tower]
        iconlist.append(self)
        self.img = pygame.transform.scale(TowerImageArray[tower],(41,41))
        i = player.towers.index(tower)
        x,y = i%2,i//2
        self.rect = self.img.get_rect(x=700+x*(41+6)+6,y=100+y*(41+6)+6)


def dispText(screen,wavenum):
    font = pygame.font.SysFont("Verdana", 20)
    h = font.get_height()+2
    
    #list of tuples ((string),(pos))...
    #to efficiently display text
    strings = [('Round: %d/%d' % (wavenum,len(mapvar.waves)),(50,490)), #<= pos
               (str(player.money),(730,15)),
               (str(max(player.health,0)),(730,45)),
               ('Towers:',(710,95))]
    for string,pos in strings:
        text = font.render(string,2,(0,0,0))
        screen.blit(text,text.get_rect(midleft=pos))


def drawTower(screen,tower,selected):
    screen.blit(tower.image,tower.rect)
    font = pygame.font.SysFont("Verdana", 15)

    sell = imgLoad('my_tower_defence_minigame/images/sell.png')
    sell = pygame.transform.scale(sell, (100,40))
    sellrect = sell.get_rect()
    pos = pygame.mouse.get_pos()
    
    #condition true when the tower is selected after placed
    if tower==selected:
        rn = tower.range
        surface = pygame.Surface((2*rn,2*rn)).convert_alpha(); surface.fill((0,0,0,0))
        pygame.draw.circle(surface,(0,255,0,85),(rn,rn),rn)
        screen.blit(surface,tower.rect.move((-1*rn,-1*rn)).center)
        screen.blit(sell,(550,530))
        text = font.render(str(selected.tower) + " Tower, for $" + str(int(selected.cost*0.8)),2,(0,0,0))
        textpos = text.get_rect(right=700-6,centery=580)#(right=700-6,centery=selected.rect.centery)
        screen.blit(text,textpos)
  
    #condition true when tower is being dragged from the icon panel to be placed
    elif tower.rect.collidepoint(pygame.mouse.get_pos()):
        rn = tower.range
        surface = pygame.Surface((2*rn,2*rn)).convert_alpha()
        surface.fill((0,0,0,0))
        pygame.draw.circle(surface,(255,255,255,85),(rn,rn),rn)
        screen.blit(surface,tower.rect.move((-1*rn,-1*rn)).center)

        

#function when you select the tower icons on the right
def selectedIcon(screen,selected):
    mpos = pygame.mouse.get_pos()
    image = TowerImageArray[selected.tower]
    rect = image.get_rect(center=mpos)
    screen.blit(image,rect)

    collide = False
    rn = selected.range
    surface = pygame.Surface((2*rn,2*rn)).convert_alpha()
    surface.fill((0,0,0,0))
    #if statement inside the function pygame.draw.circle()
    pygame.draw.circle(surface,(255,0,0,75) if collide else (0,0,255,75),(rn,rn),rn)
    screen.blit(surface,surface.get_rect(center=mpos))
    
    
    
def selectedTower(screen,selected,mousepos):
    selected.genButtons(screen)
    
    for img,rect,info,infopos,cb in selected.buttonlist:
        screen.blit(img,rect)
        #diplays the name and cost of the tower when players mouse is hovered on the icon
        if rect.collidepoint(mousepos):
            screen.blit(info,infopos)

def drawIcon(screen,icon,mpos,font):
    #displays icon on screen
    screen.blit(icon.img,icon.rect)
    
    #if you hover over the icon, displays the name of tower and cost
    if icon.rect.collidepoint(mpos): 
        text = font.render("%s Tower (%d)" % (icon.tower,icon.cost),2,(0,0,0))
        textpos = text.get_rect(right=700-6,centery=icon.rect.centery)
        screen.blit(text,textpos)

class Sender:
    def __init__(self,wave):
        self.wave = wave
        self.timer = 0
        self.rate = 1
        self.enemies = []
        
        enemies = mapvar.waves[wave-1].split(',') #e.g. round 2 = ['9*1', '1*2', '9*1', '1*2']
        
        for enemy in enemies:
            amount,layer = enemy.split('*')
            self.enemies += [eval(layer)-1]*eval(amount)
            #e.g. round 2 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            
        senderlist.append(self)

    #sends the wave of enemies
    def update(self,frametime,wave):
        if not self.enemies:
            if not enemylist:
                senderlist.remove(self)
                wave+=1 
                player.money+=99+self.wave #cash bonus after end of round
        elif self.timer>0:
            self.timer -= frametime
        else:
            self.timer = self.rate
            EnemyBoat(self.enemies[0]) #creates an enemy boat
            del self.enemies[0]
        return wave

def workEvents(selected,wave,speed):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            selected = None
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:

            if selected in towerlist:
                selected = None

            #if player selects an icon in the right panel
            elif selected in iconlist:
                if player.money>=selected.cost:
                    rect = selected.img.get_rect(center=event.pos)
                    collide = False
                    #if the tower does not colide with the borders, money is exchanged for the tower and is places
                    if not collide:
                        player.money-=selected.cost
                        selected = createTower(selected.tower,event.pos,selected.towers[selected.tower])

            for obj in iconlist + (towerlist if not selected else []):
                if obj.rect.collidepoint(event.pos):
                    selected = obj
                    break
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            #selling towers
            if 540<event.pos[0]<650 and 520<event.pos[1]<570 and selected in towerlist:
                print('Sold tower')
                player.money+=int(selected.cost*0.8) 
                towerlist.remove(selected)
                selected = None

            #begin round        
            if 50<event.pos[0]<160 and 520<event.pos[1]<590 and not enemylist:
                print('round begun')
                if wave<=len(mapvar.waves):
                    Sender(wave)
                else:
                    print('More rounds coming soon.')


        #increase or decrese speed of round by pressing w or s
        if event.type == pygame.KEYDOWN:

            #speed of round can only go between 1 to 10
            if event.key == pygame.K_w and speed<10:
                speed+=1
            if event.key == pygame.K_s and speed>1:
                speed-=1
    return selected,wave,speed

gameover = False

def main_towerdef():
    pygame.init()
    
    #places the pygame screen in the middle
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    
    pygame.display.set_caption('Tower Defence Minigame')
    screen = pygame.display.set_mode((scrwid,scrhei))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,20)

    mapvar.getmovelist()

    background = pygame.Surface((800,600))
    background.set_colorkey((0,0,0))
    heart,money = imgLoad('my_tower_defence_minigame/images/heart.png'),imgLoad('my_tower_defence_minigame/images/money.png')
    heart,money = pygame.transform.scale(heart, (20,20)),pygame.transform.scale(money, (20,20))
    
    level_img = mapvar.get_background()
    loadImages()
    for tower in player.towers:
        Icon(tower)
    selected = None
    speed = 3
    wave = 1
    
    while True:
        starttime = time.time()
        clock.tick(fps)
        frametime = (time.time()-starttime)*speed
        screen.blit(level_img,(0,0))
        mpos = pygame.mouse.get_pos()


        if senderlist:
            wave = senderlist[0].update(frametime,wave)
            
        # add enemies to enemylist depending on the distance traveled
        z0,z1 = [],[]
        for enemy in enemylist:
            d = enemy.distance
            if d<580:
                z1+=[enemy]
            elif d<950:
                z0+=[enemy]
            elif d<2392:
                z1+=[enemy]
            elif d<2580:
                z0+=[enemy]
            else:
                z0+=[enemy]
                
        #the enemyboat is displayed and moves
        for enemy in z0:
            enemy.move(frametime)
            screen.blit(enemy.image,enemy.rect)
        
        for enemy in z1:
            enemy.move(frametime)
            screen.blit(enemy.image,enemy.rect)


        screen.blit(background,(0,0))

        #displaying side panels
        panel = imgLoad('my_tower_defence_minigame/images/panel.png')
        panel = pygame.transform.scale(panel, (100,600))
        screen.blit(panel,(702,0))
        panel = pygame.transform.scale(panel, (800,100))
        screen.blit(panel,(0,513))
       
        #displaying money and heart pictures before the number
        screen.blit(money,(705,5))
        screen.blit(heart,(705,40))
        
        towersinfo = imgLoad('my_tower_defence_minigame/images/towersinfo.png')
        towersinfo = pygame.transform.scale(towersinfo, (80,50))
        screen.blit(towersinfo,(710,260))

        enemiesinfo = imgLoad('my_tower_defence_minigame/images/enemiesinfo.png')
        enemiesinfo = pygame.transform.scale(enemiesinfo, (80,50))
        screen.blit(enemiesinfo,(710,340))

        quitbutton = imgLoad('my_tower_defence_minigame/images/quit.png')
        quitbutton = pygame.transform.scale(quitbutton, (80,50))
        screen.blit(quitbutton,(710,460))

        ##Begin round will be displayed if no enemy boats are on the screen
        if not enemylist:
            nextroundimg = imgLoad('my_tower_defence_minigame/images/next round.png')
            nextroundimg = pygame.transform.scale(nextroundimg, (110,60))
            screen.blit(nextroundimg,(50,525))

        for tower in towerlist:
            tower.takeTurn(frametime,screen)
            drawTower(screen,tower,selected)

        for icon in iconlist:
            drawIcon(screen,icon,mpos,font)
            
        selected,wave,speed = workEvents(selected,wave,speed)
        if selected and selected.__class__ == Icon:
            selectedIcon(screen,selected)
        dispText(screen,wave)

        mpos = pygame.mouse.get_pos()

        rect1 = towersinfo.get_rect(x=710,y=260) #rect of tower info button
        rect2 = enemiesinfo.get_rect(x=710,y=340) #rect of enemy info button
        rect3 = quitbutton.get_rect(x=710,y=460)  #rect of quit button

        #if player hovers over either towers info button, the towers info image with all details will be displayed
        if rect1.collidepoint(mpos):
            towerinfo = imgLoad('my_tower_defence_minigame/images/tower info.png')
            towerinfo = pygame.transform.scale(towerinfo, (600,420))
            screen.blit(towerinfo,(50,40))

        #if player hovers over either enemies info button, the enemies info image with all details will be displayed
        if rect2.collidepoint(mpos):
            enemyinfo = imgLoad('my_tower_defence_minigame/images/enemies info.png')
            enemyinfo = pygame.transform.scale(enemyinfo, (600,420))
            screen.blit(enemyinfo,(50,40))
        
        mouse_pressed = pygame.mouse.get_pressed()

        #If the quit button is pressed the tower def minigame main loop will end
        #and it would resume the main loop for Skill-Topia.py
        if rect3.collidepoint(mpos):
            if mouse_pressed[0]:
                global gameover
                gameover = True
                print(gameover)
                break
                     

        pygame.display.flip()
