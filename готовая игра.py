import numpy as n
import pygame as pg
#from Nucleozid import *
import pygame.freetype
#from Iscander import *
import thorpy
SCREEN_SIZE = (1000, 700)
pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BROWN = (210, 105, 30)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

FPS = 10
size = 18
org = 80
c0 = 140
c1 = org
PO4 = 5
FONT = pg.freetype.Font(None, size)
seq = "ACGTAATGCTCGATGGATGCTAGCTACGTACTGGTAACGTCGATCATTTGCAC"

'''Часть Артема
   Задает параметры построения РНК при нажатии клавишь
   фунцкия Ad-строит аденин
           Cyt строит цитозин
           Gua-строит гуанин
           Ura-строит урацил'''
def Ad(a,y,h):
    pg.draw.polygon(screen, RED,[(a,y),(a+h,y),(a+h,y+h),(a+int(h/2),y+int(h*1.5)),(a,y+h)])
    pg.draw.line(screen, CYAN,(a+h,y+int(h/2)),(a+int(h*1.5),y+int(h/2)),5)
    FONT.render_to(screen, (a+4,y+2), "A", (255, 255, 255))
    pg.display.update()

def Cyt(a,y,h):
    pg.draw.polygon(screen, MAGENTA,[(a,y),(a+h,y),(a+h,y+h),(a+int(0.7*h),y+h),(a+int(0.7*h),y+int(1.5*h)),
                                     (a+int(0.3*h),y+int(1.5*h)),(a+int(0.3*h),y+h), (a,y+h)])
    pg.draw.line(screen, CYAN,(a+h,y+int(0.5*h)),(a+int(h*1.5),y+int(h/2)),5)
    FONT.render_to(screen, (a+4,y+2), "C", (255, 255, 255))
    pg.display.update()

def Gua( a, y,h):
    pg.draw.polygon(screen, YELLOW, [(a, y), (a + h, y), (a + h, y + int(1.5*h)), (a + int(0.7*h), y + int(1.5*h)),
                                     (a+int(0.7*h), y + h),(a+int(0.3*h),y+h),(a+int(0.3*h),y+int(1.5*h)),(a,y+int(1.5*h))])
    pg.draw.line(screen, CYAN, (a + h, y + int(0.5 * h)), (a + int(h*1.5), y + int(h / 2)), 5)
    FONT.render_to(screen, (a + 4, y + 2), "G", (255, 255, 255))
    pg.display.update()
def Ura(a, y,h):
    pg.draw.polygon(screen, GREEN, [(a, y), (a + h, y), (a + h, y + int(1.5*h)), (a + int(h / 2), y + h),
                                    (a, y + int(1.5*h)),(a+int(0.3*h),y+h)])
    pg.draw.line(screen, CYAN, (a + h, y + int(0.5 * h)), (a + int(h*1.5), y + int(h / 2)), 5)
    FONT.render_to(screen, (a + 4, y + 2), "U", (255, 255, 255))
    pygame.display.update()
def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True

'''Часть Искандера
    отвечает за построение ДНК и 
    РНК-полимиразы'''
def a_draw(coord, size):
    pg.draw.rect(screen, RED, (coord[0], coord[1], size, size))
    pg.draw.polygon(screen, RED, [(coord[0], coord[1]),
                                  (coord[0] + size, coord[1]), (coord[0] + size // 2, coord[1] - size // 2)])
    FONT.render_to(screen, (coord[0] + 2, coord[1] + 1), "A", BLACK)


def t_draw(coord, size):
    pg.draw.rect(screen, GREEN, (coord[0], coord[1], size, size))
    pg.draw.polygon(screen, GREEN, [(coord[0], coord[1]),
                                    (coord[0] + size // 2, coord[1]), (coord[0], coord[1] - size // 2)])
    pg.draw.polygon(screen, GREEN, [(coord[0] + size, coord[1]),
                                    (coord[0] + size // 2, coord[1]), (coord[0] + size, coord[1] - size // 2)])
    FONT.render_to(screen, (coord[0] + 2, coord[1] + 1), "T", BLACK)


def c_draw(coord, size):
    pg.draw.rect(screen, MAGENTA, (coord[0], coord[1], size, size))
    pg.draw.rect(screen, MAGENTA, (coord[0] + size // 3, coord[1] - size // 2, size // 3, size // 2))
    FONT.render_to(screen, (coord[0] + 2, coord[1] + 1), "C", BLACK)


def g_draw(coord, size):
    pg.draw.rect(screen, YELLOW, (coord[0], coord[1], size, size))
    pg.draw.rect(screen, YELLOW, (coord[0], coord[1] - size // 2, size // 3, size // 2))
    pg.draw.rect(screen, YELLOW, (coord[0] + 2 * size // 3, coord[1] - size // 2, size // 3, size // 2))
    FONT.render_to(screen, (coord[0] + 2, coord[1] + 1), "G", BLACK)


def DNA(coord):
    pg.draw.arc(screen, CYAN, (org - 80, SCREEN_SIZE[1] - 178, 70, 50), n.pi / 2, n.pi * 3 / 2, 5)
    a = pg.Surface((SCREEN_SIZE))
    a.fill(ORANGE)
    pg.draw.ellipse(a, BLACK, (0, 0, 100, 70))
    a.set_colorkey(ORANGE)
    a = pg.transform.rotate(a, 90)
    screen.blit(a, (c1 - (size + PO4), -420))

    pg.draw.rect(screen, YELLOW, (org // 5, SCREEN_SIZE[1] - 170, size, size))
    pg.draw.rect(screen, MAGENTA, (org // 5, SCREEN_SIZE[1] - 150, size, size))
    pg.draw.rect(screen, YELLOW, (org, SCREEN_SIZE[1] - 200, size * 3, size))
    pg.draw.rect(screen, MAGENTA, (org, SCREEN_SIZE[1] - 150, size * 3, size))
    pg.draw.line(screen, CYAN, [org // 2, SCREEN_SIZE[1] - 200 + size],
                 [c0 + len(seq) * (size + PO4), SCREEN_SIZE[1] - 200 + size], 5)
    pg.draw.line(screen, CYAN, [org // 2, SCREEN_SIZE[1] - 150 + size],
                 [c0 + len(seq) * (size + PO4), SCREEN_SIZE[1] - 150 + size], 5)
    # topoasa
    a = pg.Surface((SCREEN_SIZE))
    pg.draw.ellipse(a, BROWN, (0, 0, 90, 60))
    FONT.render_to(a, (6, 10), "topoiso", WHITE)
    FONT.render_to(a, (6, 28), "merase", WHITE)
    a.set_colorkey(BLACK)
    a = pg.transform.rotate(a, 90)
    screen.blit(a, (org // 4, -425))
    # seq
    for i in range(len(seq)):
        if seq[i] == 'A':
            a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
            t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
        if seq[i] == 'G':
            g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
            c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
        if seq[i] == 'T':
            t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
            a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
        if seq[i] == 'C':
            c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
            g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)


def Pasa(coord):
    a = pg.Surface((SCREEN_SIZE))
    pg.draw.ellipse(a, ORANGE, (0, 0, 100, 70))
    FONT.render_to(a, (6, 10), "RNA poly", WHITE)
    FONT.render_to(a, (6, 28), "merase", WHITE)
    a.set_colorkey(BLACK)
    a = pg.transform.rotate(a, 90)
    screen.blit(a, (c1, -420))

'''Часть Артема 
   в этой части уже идет взаимодействие с клавиатурой
   и само построение РНК
   при нажатии клавиши 'G,U,C,A' 
   появляются соответственно гуанин,
   урацил, цитозин и Аденин'''
button_play = thorpy.make_button("Play",start_execution)
timer = thorpy.OneLineText("Seconds passed")
box = thorpy.Box(elements=[
    button_play,
    timer])
my_reaction = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                              reac_func=start_execution)
menu = thorpy.Menu(box)
for element in menu.get_population():
    element.surface = screen

box.set_topleft((0, 0))
box.blit()
box.update()

pg.draw.line(screen,WHITE,(0,int(SCREEN_SIZE[1]/2)),(SCREEN_SIZE[0],int(SCREEN_SIZE[1]/2)))
pg.display.update()
x=110
z=450
h=15
count=0
finished = False
str1=''
perform_execution = False
while not finished:
    clock.tick(FPS)
    DNA(org)
    Pasa(c0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            menu.react(event)
            if perform_execution:
                for i in range(len(seq)):
                    if seq[i] == 'A':
                        a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                        t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
                    if seq[i] == 'G':
                        g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                        c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
                    if seq[i] == 'T':
                        t_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                        a_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)
                    if seq[i] == 'C':
                        c_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 200], size)
                        g_draw([c0 + (size + PO4) * i, SCREEN_SIZE[1] - 150], size)

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_u:
                Ura(x, z, h)
                x += int(h * 1.5)
                str1 += 'A'
            elif event.key == pg.K_a:
                Ad(x, z, h)
                x += int(h * 1.5)
                str1 += 'T'
            elif event.key == pg.K_c:
                Cyt(x, z, h)
                x += int(h * 1.5)
                str1 += 'G'
            elif event.key == pg.K_g:
                Gua(x, z, h)
                x += int(h * 1.5)
                str1 += 'C'
            c1 += (size + PO4)
            count += 1
    if x > 800:
        pg.draw.rect(screen, BLACK, (0, z, SCREEN_SIZE[0], 2 * h))
        x = 10
    if c1 >= SCREEN_SIZE[0] - 100:
        org -= SCREEN_SIZE[0] * 2 // 3
        c0 -= SCREEN_SIZE[0] * 2 // 3
        c1 -= SCREEN_SIZE[0] * 2 // 3
        pg.draw.rect(screen, BLACK, (0, SCREEN_SIZE[1] - 220, SCREEN_SIZE[0], SCREEN_SIZE[1]))
    if count == len(seq):
        finished = True
pg.quit()
pg.init()
FPS = 30
popal=0
screen = pygame.display.set_mode((1000, 800))
for i in range(len(seq)):
    if seq[i]==str1[i]:
        popal+=1
procent=int(popal/len(seq)*100)

FONT=pygame.freetype.Font(None, 20)
FONT.render_to(screen, (50, 50), "Истинная строка " + seq, ORANGE)
FONT.render_to(screen, (50, 150), "Ваша  строка " + str1, ORANGE)
FONT1=pygame.freetype.Font(None, 20)
FONT1.render_to(screen, (50, 250), "Вы биотехнолог на " + str(procent)+'%', ORANGE)
pg.display.update()
clock = pygame.time.Clock()
clock.tick(1)

finished = False
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
