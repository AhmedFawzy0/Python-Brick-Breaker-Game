#Ahmed Fawzy and Sam
#Bomb Sheild Game Summative
#Level 1

import pygame
import random
#define colors and set screen size
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
brown=(200,200,200)
yellow=(230,215,0)
size=(width,height)= (600,600)

#initialize pygame and create screen
pygame.init()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Bomb Sheild")
x,y=300,500
r=25
x1,y1=200,200
color=green
xspeed,yspeed=0,0
clock=pygame.time.Clock()
xball=0
yball=1
score=0
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pic=pygame.image.load("assets/back.jpg")
sound=pygame.mixer.Sound("assets/sound.ogg")
lava=pygame.image.load("assets/lava.jpg")
death=pygame.mixer.Sound("assets/Death Spike.ogg")
OneLives=3
#main game loop
running= True
while running:
    #event loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #check for keydown (press) event
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
                xspeed=3
        if event.key==pygame.K_LEFT:
                xspeed=-3

            
            
        #check for keyup (release) event
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_RIGHT:
                xspeed=0
        if event.key==pygame.K_LEFT:
                xspeed=0
        if event.key==pygame.K_UP:
                yspeed=0
        if event.key==pygame.K_DOWN:
                xspeed=0

           
                
    #ball - slider bounce
    if x1+r>=x and y1+r==500: #if hits left side of slider bounce left
        if x1-r<=x+49:
            u=random.randint(-3,-1)
            n=random.randint(-3,-1)
            yball=u
            xball=n
    
    if x1+r>=x+50 and y1+r==500: #if hits right side of slider bounce right
        if x1-r<=x+100:
            u=random.randint(-3,-1)
            l=random.randint(1,3)
            yball=u
            xball=l
    if x1+r>=x and y1+r==500: #score and sound
        if x1-r<=x+100:
            score=score+1
            sound.play()
    
    #wall bounce
    if y1-r<=0:  #top 
        yball=1
    
    if x1-r<=0:  #left side
        xball=1
        yball=1
    
    if x1+r>=600: #right side
        xball=-1
        yball=1
    
    #game logic
    x=x+xspeed
    x1=x1+xball
    y1=y1+yball
    #slider restrictions
    if x<=0:
        x=0
    if x>=500:
        x=500
    #if ball dies
    if y1+r>=525:
        OneLives=OneLives-1
        x1=250
        y1=50
        death.play()

             
    #score text box
    textbox=myfont.render(("Score:"+str(score)),True,black)
    textlives=myfont.render(("Lives:"+str(OneLives)),True,black)
    lose1=myfont.render(("You Lose / Die to restart / Score to quit"),True,black)
    win1=myfont.render(("You Win ! / Die to restart / Score to quit"),True,black)
        
    #draw section
    screen.fill(brown)
    screen.blit(lava,(0,500))
    screen.blit(pic,(0,0))
    pygame.draw.circle(screen,red,[x1,y1],r)
    pygame.draw.rect(screen, color,[x,y,100,25] )
    screen.blit(textbox,[75,30])
    screen.blit(textlives,[415,30])
    #check if lives=0
    if OneLives==0:  
        screen.blit(lose1,[20,300])
    if OneLives==-1: #if die then restart
        OneLives=3
        score=0
    if OneLives==0:
        if x1+r>=x and y1+r==500: #if player score, game ends 
            if x1-r<=x+100:
                running=False
    #check if score=10
    if score==10 and OneLives>0:
        screen.blit(win1,[20,300])
    if score==10 and OneLives>0:
        if y1+r>=510: #if die then restart
            score=0
            OneLives=4  #score rests at 4 and dies which makes it back to 3
    if score==11:  #if score then end
        running=False

    clock.tick(300)    
    pygame.display.flip()
