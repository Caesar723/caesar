import random
import math
import pygame
pygame.init()
time=180
screen=pygame.display.set_mode([500,500])
b=0
o=random.randint(0,15)*20
x=20
oo=random.randint(0,15)*20
y=20
score=0
caesar=True
ba=0
ca=00

kl=0
def drawCircle(size,c,p):
    pygame.draw.circle(screen,c,p,size)
def showMessage(text,size,colour,p):
    fon=pygame.font.Font(None,size)
    sur=fon.render(text,True,colour)
    screen.blit(sur,p)
hh=0

fps=20

k=pygame.time.Clock()
running=True

while running:

    if hh == 0:
        screen.fill((0, 0, 0))

        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                running=False
            #if i.type==pygame.MOUSEBUTTONDOWN:
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_w:
                    if caesar==False:
                        y=y-20
                    #elif x <= oo + 70 and x >= oo - 70 and y >= o - 70 and y <= o + 70:
                        #y=y-random.randint(-10,10)
                    else:
                        y=y-20
                if i.key == pygame.K_a:
                    if caesar==False:
                        x=x-10
                    #elif x <= oo + 70 and x >= oo - 70 and y >= o - 70 and y <= o + 70:
                        #x=x-random.randint(-10, 10)
                    else:
                        x = x - 20
                if i.key == pygame.K_d:
                    if caesar==False:
                        x=x+20
                    #elif x <= oo + 70 and x >= oo - 70 and y >= o - 70 and y <= o + 70:
                        #x=x+random.randint(-10, 10)
                    else:
                        x = x + 20
                if i.key == pygame.K_s:
                    if caesar==False:
                        y=y+20
                    #elif x<=oo+70 and x>=oo-70 and y>=o-70 and y<=o+70:
                        #y=y+random.randint(-10,10)
                    else:
                        y = y + 20
                if i.key==pygame.K_q:
                    if kl==1:
                        o=o-20
                    if kl==2:
                        o=o+20
                    if kl==3:
                        oo=oo+20
                    if kl==4:
                        oo=oo-20
        hole = drawCircle(20, (255, 50, 255), [140, 60])
        cc = drawCircle(20, (255, 255, 255), [x, y])
        KKK = drawCircle(20, (255, 0, 0), [oo, o])
        showMessage("time="+str(time), 20, (0, 255, 29), [20, 20])
        showMessage("score= " + str(score), 20, (255, 255, 0), [180, 20])
        if y==o+40 and x==oo:
            kl = 1
            caesar=False

        elif y ==o-40 and x==oo:
            kl = 2
            caesar=False
        elif x ==oo-40 and y==o:
            kl = 3
            caesar=False
        elif x ==oo+40 and y==o:
            kl = 4
            caesar=False
        else:
            kl=0
        if oo==140 and o==60:
            oo=random.randint(0,15)*20
            o=random.randint(0,15)*20
            score=score+1
        if time==0:
            hh=1
    else:
        screen.fill((254, 254, 254))
        showMessage("score= "+str(score),30,(255,0,0),[150,150])
        showMessage("good game", 30, (255, 0, 0), [150, 200])
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                running=False
        #if i.type==pygame.MOUSEBUTTONDOWN:

    k.tick(fps)

    b = b + 1
    if b %20==0:
        time=time-1




    pygame.display.flip()

pygame.quit()