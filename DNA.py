import numpy as n
import pygame as pg
#import Nucleozid
import pygame.freetype


def a_draw(coord, size):
    pg.draw.rect(screen,RED, (coord[0],coord[1],size,size))
    pg.draw.polygon(screen,RED,[(coord[0],coord[1]),
                                    (coord[0]+size,coord[1]),(coord[0]+size//2,coord[1]-size//2)] )
    FONT.render_to(screen, (coord[0]+2,coord[1]+1), "A", (255, 255, 255))

def t_draw(coord, size):
    pg.draw.rect(screen,GREEN, (coord[0],coord[1],size,size))
    pg.draw.polygon(screen,GREEN, [(coord[0],coord[1]),
                                    (coord[0]+size//2,coord[1]),(coord[0],coord[1]-size//2)] )
    pg.draw.polygon(screen,GREEN, [(coord[0]+size,coord[1]),
                                    (coord[0]+size//2,coord[1]),(coord[0]+size,coord[1]-size//2)] )
    FONT.render_to(screen, (coord[0]+2,coord[1]+1), "T", (255, 255, 255))
    
def c_draw(coord, size):
    pg.draw.rect(screen,MAGENTA, (coord[0],coord[1],size,size))
    pg.draw.rect(screen,MAGENTA, (coord[0]+size//3,coord[1]-size//2, size//3, size//2))
    FONT.render_to(screen, (coord[0]+2,coord[1]+1), "C", (255, 255, 255))

def g_draw(coord, size):
    pg.draw.rect(screen,YELLOW, (coord[0],coord[1],size,size))
    pg.draw.rect(screen,YELLOW, (coord[0],coord[1]-size//2, size//3, size//2))
    pg.draw.rect(screen,YELLOW, (coord[0]+2*size//3,coord[1]-size//2, size//3, size//2))
    FONT.render_to(screen, (coord[0]+2,coord[1]+1), "G", (255, 255, 255))
        
def DNA(coord):
    pg.draw.line(screen,CYAN, [c0,SCREEN_SIZE[1]-200+size],[c0+len(seq)*(size+PO4),SCREEN_SIZE[1]-200+size],5)
    pg.draw.line(screen,CYAN, [c0,SCREEN_SIZE[1]-150+size],[c0+len(seq)*(size+PO4),SCREEN_SIZE[1]-150+size],5)
    a = pg.Surface((SCREEN_SIZE))
    pg.draw.ellipse(a,ORANGE, (0, 0, 80, 50))
    FONT.render_to(a, (0,0), "topoisomerase", (255, 255, 255))
    a.set_colorkey(BLACK)
    a = pg.transform.rotate(a, 90)
    screen.blit(a, (0, 0))
def Pasa(coord):
    #pg.draw.ellipse(screen, BROWN, ())
    pass
 
    
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
ORANGE = (255,165,0)    
    
FPS = 10
size = 18
org = 60
c0 = 120
PO4 = 5
FONT = pg.freetype.Font(None, size)
seq = "ACGTAATGCTCGATGGATGCTAGCTACGTACGCGTAGCGCATGCTAGCATGATCGATCGACTAGCTACGTCAGCGTAGCTAGCATG"
DNA(org)
Pasa(c0)

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
pg.display.update()
finished = False

while not finished:
    clock.tick(FPS)
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
    pg.display.flip()

pg.quit()
