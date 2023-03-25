import pygame
import random
import math
from pygame import mixer
pygame.init()
green=(0,255,0)
white=(255,255,255)
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Test game")
icon=pygame.image.load('test game/loading.png')
pygame.display.set_icon(icon)
background=pygame.image.load('test game/background.jpg')
running=True
clock=pygame.time.Clock()

#player
playerImg=pygame.image.load('test game/spaceship.png')
playerX=300
playerY=400
playerX_change=0
playerY_change=0

#enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enimies=6

for i in range(num_of_enimies):
    enemyImg.append(pygame.image.load('test game/alien.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.1)
    enemyY_change.append(20)


#bullet
bulletImg=pygame.image.load('test game/bullet.png')
bulletX=0
bulletY=400
bulletX_change=0
bulletY_change=0.5
bullet_state="ready"

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

#game over text
text_over_font=pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,white)
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10)) #cho dan ra giua may bay 
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    return False
def game_over_text():
    over_font=text_over_font.render("GAME OVER",True,white)
    screen.blit(over_font,(200,250))
    
#vong lap game
while running:
    # screen.fill(green)
    screen.blit(background,(0,0))
    # playerX+=0.1
    # print(playerX)
    
    # clock.tick(20)
    # pygame.draw.rect(screen,white,(100,50,50,50))
    # pygame.draw.rect(screen,white,(200,50,50,50))
    # pygame.draw.rect(screen,white,(100,200,50,50))
    # pygame.draw.rect(screen,white,(200,200,50,50))
    # pygame.draw.rect(screen,white,(300,50,100,50))
    # pygame.draw.rect(screen,white,(300,150,100,50))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:     #nhan chuot trai
                print("Hello")
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("left arrow is pressed")
                playerX_change=-0.3
            if event.key==pygame.K_RIGHT:
                print("right arrow is pressed")
                playerX_change=0.3
            # if event.key==pygame.K_UP:
            #     print("up arrow is pressed")
            #     playerY_change=-0.1
            # if event.key==pygame.K_DOWN:
            #     print("down arrow is pressed")
            #     playerY_change=0.1
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('test game/shoot.wav')
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(playerX,bulletY)
            
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
            # if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
            #     playerY_change=0
             
    # pygame.display.flip()   #doi mau nen 
    playerX+=playerX_change
    # playerY+=playerY_change
     #checking for boundaries of spaceship 
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736

    #enemy movement 
    for i in range(num_of_enimies):

        #game over
        if enemyY[i]>200:
            for j in range(num_of_enimies):
                enemyY[j]=2000 #gan toa do cho enemy di ra khoi man hinh
                bulletY=2000
            game_over_text()
            break

        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=0.1
            enemyY[i]+=enemyY_change[i]   
        elif enemyX[i]>=736:
            enemyX_change[i]=-0.1
            enemyY[i]+=enemyY_change[i]

        #Collision
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            collision_sound=mixer.Sound('test game/explosion.ogg')
            collision_sound.play()
            bulletY=400
            bullet_state="ready"
            score_value+=1
            print(score_value)
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)
        
        enemy(enemyX[i],enemyY[i],i)
        
    #Bullet Movement
    if bulletY<=0:
        bulletY=400
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
   
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()



pygame.quit()