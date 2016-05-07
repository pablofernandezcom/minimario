"""
Pablo Fernandez
Mario MiniGame
------------------------

Instructions:
Press A to drop a ball into the game. Be careful, you are limited to 40 balls, 
and limited to 4 bounce bricks on the bottom 60% of the screen. Click on the 
screen to add a bounce brick onto the map. Use the bricks to bounce balls 
into the target. 

Be careful, you need to get 20 out of the 40 balls into the target to win the game.

Newly Added:
    Teleportation: accidentally hit the bullet? You will be teleported to wherever the
    bird is flying in the game.
    Bowser: Be careful, bowser will eat any balls that come close to it
    Star: Hit the flying star with a ball and you will win a point. 

A&B: Randomly Moving Target, Obstacle Physics
Balls disappear after a while to prevent overloading 
"""

from Ball import *
from Target import *
from Vector import *
from Obstacle import *

import time
import random

def setup():
    global Balls, score, source, setObject, Obstacles, ballsUsed, ballsMaximum, ballsTemTurn, ballsMaxTurn, targetmove, targetdirection, targetaxis, platUsed, platMaximum, platMaxTurn, platTemTurn, horizon, portal_bottom, portalmove, portal_top, portalmove_top, birdb, pipe,bullet, bulletb,threat, bird
    size(800,800)
    Balls = []
    Obstacles = []

    source = loadImage("BACK.PNG")
    bird = loadImage("Bird.png")
    birdb = loadImage("BirdB.png")
    pipe = loadImage("Pipe.png")
    bullet = loadImage("Bullet.png")
    bulletb = loadImage("BulletB.png")  
    threat = loadImage("Bowser.gif")    
  
    score = 0
    setObject ="false"
    
    ballsUsed = 0
    ballsMaximum = 40
    ballsMaxTurn = 1
    ballsTemTurn = 0
    portalmove = 0
    portalmove_top=750
    
    platUsed = 0
    platMaximum = 4
    platMaxTurn = 1
    platTemTurn = 0
    
    targetmove = random.randrange(10,99)/100.0
    targetaxis = random.randrange(10,99)/100.0
    targetdirection = "down"
    horizon = "right"
    portal_bottom = "right"
    portal_top = "left"

def draw():
    global Balls, source, score, setObject, Obstacles, ballsUsed, ballsMaximum, ballsTemTurn, ballsMaxTurn, targetmove, targetdirection, targetaxis, horizon, portal_bottom, portalmove, portal_top, portalmove_top, bird, birdb, pipe, bullet, bulletb,threat
    background(source)
        
    if score < 20:
        temp = random.randrange(3,5)
        temp = temp /1000.0
        targetaxis = targetaxis + temp
        print(targetaxis)

        if(targetaxis<=0.05):
            targetaxis = targetaxis + 0.10
        if(targetaxis>=0.60):
            targetaxis = targetaxis - 0.99

        if(targetdirection=="down"):
            a = Target(width*targetaxis,height*targetmove)
            a.render()
            temp2 = random.randrange(2,5)
            temp2 = temp2 /1000.0
            targetmove = targetmove + temp2
            switch = random.randrange(1,90)
            if(switch==88):
                targetdirection="up"
            if(targetmove>=0.55):
                targetdirection="up"

        if(targetdirection=="up"):
            a = Target(width*targetaxis,height*targetmove)
            a.render()           
            temp3 = random.randrange(3,6)
            temp3 = temp3 /1000.0
            
            switch = random.randrange(1,70)
            if(switch==33):
                targetdirection="down"
            targetmove = targetmove - temp3
            if(targetmove<=0.05):
                targetdirection="down"
     
        if(portal_top=="left"):
            temp6 = random.randrange(6,10)
            temp6 = temp6 /1.0
            portalmove_top = portalmove_top - temp6
            image(birdb, portalmove_top, 40)
            if(portalmove_top<=10):
                portal_top="right"
                
        if(portal_top=="right"):
            temp7 = random.randrange(6,10)
            temp7 = temp7 /1.0
            portalmove_top = portalmove_top + temp7
            image(bird, portalmove_top, 40)
            if(portalmove_top>=550):
                portal_top="left"
                             
        for o in Obstacles:
            o.render()
            o.update()
            
        if(portal_bottom=="left"):
            temp4 = random.randrange(6,14)
            temp4 = temp4 /1.0
            portalmove = portalmove - temp4
            image(bullet, portalmove, 700)
            if(portalmove<=10):
                portal_bottom="right"
                
        if(portal_bottom=="right"):
            temp5 = random.randrange(6,18)
            temp5 = temp5 /1.0
            portalmove = portalmove + temp5
            image(bulletb, portalmove, 700)
            if(portalmove>=700):
                portal_bottom="left"
                    
        image(threat, 700, 700)

        for b in Balls:
            b.render()
            b.update()
            
            if portalmove < b.getX() < (portalmove+100) and (700-10) < b.getY() < (700+20):
                print("Teleport!")
                b.portal(portalmove_top)
            
            if 700 < b.getX() < (700+100) and (700-80) < b.getY() < (700+80):
                print("Eaten!")
                Balls.remove(b)
            
            if b.isDead() == True:
                Balls.remove(b)
            
            for o in Obstacles:
                if o.getX() < b.getX() < (o.getX()+100) and (o.getY()-10) < b.getY() < (o.getY()+20):
                    b.bounce(o.getY())
                                
            if pow(a.getX() - b.getX(), 2) + pow(a.getY() - b.getY(), 2) < pow(a.getR(), 2):
                score += 1
                a.score()
                Balls.remove(b)
        
    
        
        fill(0,100,0)
        image(pipe, 640, 0)
        stroke(0)
        fill(0)
        textSize(22);
        text("Score: {0}".format(score),10,30)
        text("Balls: {0}".format(ballsMaximum-ballsUsed),115,30)

        if(ballsUsed>=ballsMaximum):
            fill(0,100,0)
            text("You Lose! You ran out of balls",200,30)
    else:
        fill(0,100,0)
        text("You Win!",130,30)

def mouseClicked():
    global platUsed, platMaximum, platTemTurn, platMaxTurn
    if((platTemTurn<platMaxTurn) and (platUsed<platMaximum)):
        if(mouseY<400):
            text("Invalid Bounce Position",200,30)

        else:
            Obstacles.append(Obstacle(mouseX,mouseY,100,20))
            platUsed = platUsed +1
            platTemTurn = platTemTurn +1
    if(platTemTurn>=platMaxTurn):
        platTemTurn = 0
        
def keyPressed():
    global Balls, source, score, setObject, Obstacles, ballsUsed, ballsMaximum, ballsTemTurn, ballsMaxTurn, targetmove,targetdirection, targetaxis, portal_bottom
    if ((key == 'A') | (key == 'a')):
        if((ballsTemTurn<ballsMaxTurn) and (ballsUsed<ballsMaximum)):
            Balls.append(Ball(750, 75, random.randrange(-8, -1), random.randrange(-8, -1)))
            ballsUsed = ballsUsed +1
            ballsTemTurn = ballsTemTurn +1
        if(ballsTemTurn>=ballsMaxTurn):
            ballsTemTurn = 0
            
    

    
            
            
