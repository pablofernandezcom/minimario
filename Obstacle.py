from Vector import *

class Obstacle:
    def __init__(self,x,y,vx,vy):
        self.pos = Vector(x,y)
        self.vel = Vector(vx,vy)
        self.acc = Vector(0,1)
        self.c = color(random(60),random(80),random(255))
        self.radius = 10
        self.elasticity = 0.9
        self.dead = False
        self.life = 0
        self.inc = 1
    
    def isDead(self):
        return self.dead
    
    def getX(self):
        return self.pos.getX()
    
    def getY(self):
        return self.pos.getY()
    
    def getR(self):
        return self.radius
    
    def render(self):
        fill(self.c)
        wall = loadImage("Wall.png")       
        image(wall, self.pos.getX(),self.pos.getY())    
    def update(self):
        #Lifetime
        self.life += self.inc
        if self.life > 1000:
            self.dead = True
        
        