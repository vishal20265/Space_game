import pygame
import random
import math
import time

# intialization 
pygame.init()

#Create the dispay
screen=pygame.display.set_mode((800,600)) 

#set the images for background and bullet
background_img=pygame.image.load("Background2.png")

bullet_img=pygame.image.load("bullet1.png")

white=(255,255,255)
pygame.display.set_caption("Space Game")
icon=pygame.image.load("jetpack.png")
pygame.display.set_icon(icon)

jet_image=pygame.image.load("space-ship.png")

#intial position of the jet
jet_xS=380
jet_yS=400
jet_change=0

#it just set the loaction of jet that means image
def jet_location(jet_x,jet_y):
    screen.blit(jet_image,(jet_x,jet_y))




#enemy intialization from random function
enemy_img=[]
enmy_xS=[]
enmy_yS=[]
enemy_changeX=[]
enemy_changeY=[]
no_of_enemy=10
for i in range(no_of_enemy):
    enemy_img.append(pygame.image.load("enemy.png"))
    enmy_xS.append(random.randint(30,730))
    enmy_yS.append(random.randint(20,200))
    #enemy change the loaction step
    enemy_changeX.append(10)
    enemy_changeY.append(20)



def enmy_loaction(emy_X,emy_y,i):
    screen.blit(enemy_img[i],(emy_X,emy_y))
    


bullet_xS=0
bullet_yS=400
bullet_state="ready"
bullet_changeY=10

#score text
score_val=0
font=pygame.font.Font("freesansbold.ttf",32)
textloc_x=10
textloc_y=10


#game over
over_font=pygame.font.Font("freesansbold.ttf",64)

def game_over():
    score=over_font.render("GAME OVER :(",True,(255,0,0))
    screen.blit(score,(200,200))


def score(x,y):
    score=font.render("Score: "+ str(score_val),True,(38,238,204))
    screen.blit(score,(x,y))



def bullet_fire(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img,(x+16,y-10))

#colllision function
def iscollision(bullet_xS,bulletyS,enemy_xS,enemy_yS):
    distance=math.sqrt((bullet_xS-enemy_xS)**2 + (bullet_yS-enemy_yS)**2)
    if(distance<27):
        return True
    else:
        return False

def distance_over(emyX,emyY,jetX,jetY):
    distance_jetemy=math.sqrt((emyX-jetX)**2 + (emyY-jetY)**2)
    if(distance_jetemy<30):
        return True
    else:
        return False

game_overbol=False
bullet_on=True

while True:
    screen.fill(white)
    # background Image
     
    screen.blit(background_img,(0,0))


    jet_location(jet_xS,jet_yS)

    

    
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                jet_change=-4
            if(event.key==pygame.K_RIGHT):
                jet_change=4
            if(event.key==pygame.K_SPACE):
                if(bullet_on):
                    bullet_xS=jet_xS
                    bullet_fire(bullet_xS,bullet_yS)

                # bullet_xS=jet_xS
                # bullet_fire(bullet_xS,bullet_yS)
        if(event.type==pygame.KEYUP):
            if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT ):
                jet_change=0  



    if bullet_state is "fire":
        bullet_fire(bullet_xS,bullet_yS)
        bullet_yS-=bullet_changeY

    if(bullet_yS<=0):
        bullet_yS=400
        bullet_state="ready"


    if(game_overbol):
        bullet_on=False
        game_over()

    for i in range(no_of_enemy):
        #Game over 
         if(distance_over(enmy_xS[i], enmy_yS[i],jet_xS,jet_yS)):
            for j in range(no_of_enemy):
                enmy_yS[j]=5000
            game_overbol=True
            break
        #  if(enmy_yS[i]>350):
        #     for j in range(no_of_enemy):
        #         enmy_yS[j]=5000
        #         game_over()
        #     break
         
         enmy_xS[i]+=enemy_changeX[i]

         if(enmy_xS[i]>730):
            enemy_changeX[i]=-3
            enmy_yS[i]+= enemy_changeY[i]
         elif(enmy_xS[i]<5):
            enemy_changeX[i]=3
            enmy_yS[i]+= enemy_changeY[i]


        
        #collision between bullet and enemy
         collision=iscollision(bullet_xS,bullet_yS,enmy_xS[i],enmy_yS[i])
         if(collision):
            null=0
            bullet_yS=400
            bullet_state="ready"
            enmy_xS[i]=random.randint(30,730)
            enmy_yS[i]=random.randint(20,40)
            score_val+=1
            # time.sleep(0.001)
         enmy_loaction(enmy_xS[i],enmy_yS[i],i)
        
        

    if(jet_xS>720):
        jet_xS=720
    elif(jet_xS<30):
        jet_xS=30  
    
    
        


    jet_xS+=jet_change
    score(textloc_x,textloc_y)
    pygame.display.update()

    
    
