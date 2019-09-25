'''This program is class for bird. The basic initial conditions of bird class 
   and other relative methods inside the class.
'''
import math
from Pig import*
class Bird(object):
    def __init__(self,n,x0,y0,r0,dx0,dy0):
        self.name=n
        self.x=x0
        self.y=y0
        self.radius=r0  
        self.dx=dx0
        self.dy=dy0
    
    ## method of how the bird moves each time
    def move(self):
        self.x+=self.dx
        self.y+=self.dy
        
    ## method to check if the bird intersect with a pig
    def check_intersection(self,pig):
        d=math.sqrt((float(self.x)-float(pig.x))**2+(float(self.y)-float(pig.y))**2)
        if d<=(float(pig.radius)+float(self.radius)):
            return True
        else:
            return False
    
    ## method to check if the bird flies out of the board
    def check_boundary(self):
        if (self.x-self.radius)<0 or (self.x+self.radius)>1000 or \
           (self.y-self.radius)<0 or (self.y+self.radius)>1000:
            return True
        else:
            return False
        
    ## method to check if the bird flies too slow that it stops
    def check_speed(self):
        if math.sqrt(float(self.dx)**2+float(self.dy)**2)<6:
            return True
        else:
            return False