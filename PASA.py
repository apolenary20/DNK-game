import numpy as n
import pygame as pg
#import Nucleozid
import pygame.freetype


def a_draw(coord, size):
    pg.draw.rect(screen,RED, (coord[0],coord[1],size,size))
    pg.draw.polygon(screen,RED,[(coord[0],coord[1]),
                                    (coord[0]+size,coord[1]),(coord[0]+size//2,coord[1]-size//2)] )
    FONT.render_to(screen, (coord[0]+2,coord[1]+1), "A", BLACK)

def t_draw(coord, size):
    pg.draw.rect(screen,GREEN, (coord[0],coord[1],size,size))
    pg.draw.polygon(screen,GREEN, [(coord[0],coord[1]),
                                    (coord[0]+size//2,coord[1]),(coord[0],coord[1]-size//2)] )
    pg.draw.polygon(screen,GREEN, [(coord[0]+size,coord[1]),
                                    (coord[0]+size//2,coord[1]),(coord[0]+size,coord[1]-size//2)] )
    FONT.render_to(screen, (coord[0]+2,coord[1]+1), "T", BLACK)
    
def c_draw(coord, size):
    pg.draw.rect(screen,MAGENTA, (coord[0],coord[1],size,size))
    pg.draw.rect(screen,MAGENTA, (coord[0]+size//3,coord[1]-size//2, size//3, size//2))
    FONT.render_to(screen, (coord[0]+2,coord[1]+1), "C", BLACK)

def g_draw(coord, size):
    pg.draw.rect(screen,YELLOW, (coord[0],coord[1],size,size))
    pg.draw.rect(screen,YELLOW, (coord[0],coord[1]-size//2, size//3, size//2))
    pg.draw.rect(screen,YELLOW, (coord[0]+2*size//3,coord[1]-size//2, size//3, size//2))
    FONT.render_to(screen, (coord[0]+2,coord[1]+1), "G", BLACK)
        
def DNA(coord):
    pg.draw.arc(screen, CYAN, (org-80,SCREEN_SIZE[1]-178 , 70, 50), n.pi/2, n.pi*3/2, 5)
    a = pg.Surface((SCREEN_SIZE))
    a.fill(ORANGE)
    pg.draw.ellipse(a,BLACK, (0, 0, 100, 70))
    a.set_colorkey(ORANGE)
    a = pg.transform.rotate(a, 90)
    screen.blit(a, (c1-(size+PO4),-420))
    
    pg.draw.rect(screen,YELLOW, (org//5,SCREEN_SIZE[1]-170,size,size))
    pg.draw.rect(screen,MAGENTA, (org//5,SCREEN_SIZE[1]-150,size,size))
    pg.draw.rect(screen,YELLOW, (org,SCREEN_SIZE[1]-200,size*3,size))
    pg.draw.rect(screen,MAGENTA, (org,SCREEN_SIZE[1]-150,size*3,size))
    pg.draw.line(screen,CYAN, [org//2,SCREEN_SIZE[1]-200+size],[c0+len(seq)*(size+PO4),SCREEN_SIZE[1]-200+size],5)
    pg.draw.line(screen,CYAN, [org//2,SCREEN_SIZE[1]-150+size],[c0+len(seq)*(size+PO4),SCREEN_SIZE[1]-150+size],5)
    #topoasa
    a = pg.Surface((SCREEN_SIZE))
    pg.draw.ellipse(a,BROWN, (0, 0, 90, 60))
    FONT.render_to(a, (6,10), "topoiso", WHITE)
    FONT.render_to(a, (6,28), "merase", WHITE)
    a.set_colorkey(BLACK)
    a = pg.transform.rotate(a, 90)
    screen.blit(a, (org//4,-425))
    #seq
    for i in range(len(seq)):
        if seq[i]=='A':
            a_draw([c0+(size+PO4)*i,SCREEN_SIZE[1]-200],size)
            t_draw([c0+(size+PO4)*i,SCREEN_SIZE[1]-150],size)
        if seq[i]=='G':
            g_draw([c0+(size+PO4)*i,SCREEN_SIZE[1]-200],size)
            c_draw([c0+(size+PO4)*i,SCREEN_SIZE[1]-150],size)
        if seq[i]=='T':
            t_draw([c0+(size+PO4)*i,SCREEN_SIZE[1]-200],size)
            a_draw([c0+(size+PO4)*i,SCREEN_SIZE[1]-150],size)
        if seq[i]=='C':
            c_draw([c0+(size+PO4)*i,SCREEN_SIZE[1]-200],size)
            g_draw([c0+(size+PO4)*i,SCREEN_SIZE[1]-150],size)
def Pasa(coord):
    a = pg.Surface((SCREEN_SIZE))
    pg.draw.ellipse(a,ORANGE, (0, 0, 100, 70))
    FONT.render_to(a, (6,10), "RNA poly", WHITE)
    FONT.render_to(a, (6,28), "merase", WHITE)
    a.set_colorkey(BLACK)
    a = pg.transform.rotate(a, 90)
    screen.blit(a, (c1,-420))
 
    
SCREEN_SIZE = (800,500)
pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()


BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BROWN = (210,105,30)
WHITE = (255, 255,255)
ORANGE = (255,165,0)    
    
FPS = 10
size = 18
org = 80
c0 = 140
c1=org
PO4 = 5
FONT = pg.freetype.Font(None, size)
seq = "ACGTAATGCTCGATGGATGCTAGCTACGTACGCGTAGCGCATGCTAGCATGATCGATCGACTAGCTACGTCAGCGTAGCTAGCATG"



pg.display.update()
finished = False

while not finished:
    clock.tick(FPS)
    DNA(org)
    Pasa(c0)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_u:
                Nucleozid.Ura.conect()
            elif event.key == pg.K_a:
                Nucleozid.Arg.conect() 
            elif event.key == pg.K_c:
                Nucleozid.Cyt.conect()
            elif event.key == pg.K_g:
                Nucleozid.Gua.conect()
            c1+=(size+PO4)
    if c1>=SCREEN_SIZE[0]-100:
        org-=SCREEN_SIZE[0]*2//3
        c0-=SCREEN_SIZE[0]*2//3
        c1-=SCREEN_SIZE[0]*2//3
        pg.draw.rect(screen, BLACK, (0,SCREEN_SIZE[1]-220,SCREEN_SIZE[0],SCREEN_SIZE[1]))
    pg.display.flip()
    
pg.quit()
