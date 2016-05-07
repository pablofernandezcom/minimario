class Target:
"""
Target Class
Defines the star, which is the objective of the game
"""

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.steps = 25/3

    def render(self):
        star = loadImage("Star.png")       
        image(star, self.x,self.y)

                
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getR(self):
        return 30
    
    def score(self):
        print("Score")
        """ Nothing needed here right now """
        
