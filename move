import pygame as pg
import sys
import random
import pygame.freetype
 
class Animation:
    def __init__(self, screenSize):
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)
        self.MAGENTA = (255, 0, 255)
        self.screenSize=screenSize
        self.rectsize = 18
        self.x = random.randint(0, screenSize[0]-18)
        self.y = random.randint(0, screenSize[1]-18)
        self.xSpeed=random.randint(-100,100)
        self.ySpeed=random.randint(-100,100)
        
    def move(self, sec):
        self.x+=sec*self.xSpeed
        self.y+=sec*self.ySpeed
        if self.x + self.rectsize > self.screenSize[0]:
            self.xSpeed=-self.xSpeed
            self.x=self.screenSize[0]-self.rectsize
        if self.x<0:
            self.xSpeed=-self.xSpeed
            self.x=0
        if self.y + self.rectsize > self.screenSize[1]:
            self.ySpeed=-self.ySpeed
            self.y=self.screenSize[1]-self.rectsize
        if self.y<0:
            self.ySpeed=-self.ySpeed
            self.y=0

    def getXCoordinates(self):
        return self.x

    def getYCoordinates(self):
        return self.y
        
    def changeSpeed(self, speed):
        self.xSpeed = 0
        self.ySpeed = 0

    def setCoordinates(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def drawA(self,screen):
        pg.draw.rect(screen, self.RED, (self.x, self.y ,self.rectsize, self.rectsize))
        pg.draw.polygon(screen, self.RED, [(self.x, self.y), (self.x + 18, self.y), (self.x + 18 // 2, self.y - 18 // 2)])
        pg.freetype.Font(None, 18).render_to(screen, (self.x + 2, self.y + 1), "A", (0,0,0))
        
    
    def drawT(self,screen):
        pg.draw.rect(screen, self.GREEN, (self.x, self.y, self.rectsize, self.rectsize))
        pg.draw.polygon(screen, self.GREEN, [(self.x, self.y),(self.x + 18 // 2, self.y), (self.x, self.y - 18 // 2)])
        pg.draw.polygon(screen, self.GREEN, [(self.x + 18, self.y),(self.x + 18 // 2, self.y), (self.x + 18, self.y - 18 // 2)])
        pg.freetype.Font(None, 18).render_to(screen, (self.x + 2, self.y + 1), "T",  (0,0,0))
        
    def drawС(self,screen):
        pg.draw.rect(screen, self.MAGENTA, (self.x, self.y, self.rectsize, self.rectsize))
        pg.draw.rect(screen, self.MAGENTA, (self.x + 18 // 3, self.y - 18 // 2, 18 // 3, 18 // 2))
        pg.freetype.Font(None, 18).render_to(screen, (self.x + 2, self.y + 1), "C", (0,0,0))
        
    def drawG(self,screen):
        pg.draw.rect(screen, self.YELLOW, (self.x, self.y, self.rectsize, self.rectsize))
        pg.draw.rect(screen, self.YELLOW, (self.x, self.y - 18 // 2, 18 // 3, 18 // 2))
        pg.draw.rect(screen, self.YELLOW, (self.x + 2 * 18 // 3, self.y - 18 // 2, 18 // 3, 18 // 2))
        pg.freetype.Font(None, 18).render_to(screen, (self.x + 2, self.y + 1), "G", (0,0,0))



pg.init()
timer = pygame.time.Clock()
screenSize = (800,600)
screenColor = (255,255,255)
screen = pygame.display.set_mode (screenSize)
 
rectList=[]
for i in range(4):
    rect = Animation(screenSize)
    rectList.append(rect)
rectList1=[]
for i in range(4):
    rect = Animation(screenSize)
    rectList1.append(rect)
rectList2=[]
for i in range(4):
    rect = Animation(screenSize)
    rectList2.append(rect)
rectList3=[]

for i in range(4):
    rect = Animation(screenSize)
    rectList3.append(rect)
while 1:
    sec = timer.tick() / 1000.
    for rect in rectList:
        rect.move(sec)
    for rect in rectList1:
        rect.move(sec)
    for rect in rectList2:
        rect.move(sec)
    for rect in rectList3:
        rect.move(sec)
    

    pg.draw.rect (screen, screenColor, pygame.Rect((0,0), screenSize))

    for rect in rectList:
        rect.drawA(screen)
    for rect in rectList1:
        rect.drawT(screen)
    for rect in rectList2:
        rect.drawC(screen)
    for rect in rectList3:
        rect.drawG(screen)
   
    pg.display.update()
for event in pg.event.get():
    if event.type == pg.QUIT:
        finished = True
