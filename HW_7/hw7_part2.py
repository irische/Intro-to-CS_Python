'''This program asks user for two imput files for birds and pigs each, and constructs
   a simple simulation of the game Angry Bird, where birds move one by one and 
   when they hit a pig, it slows down and changes direction.Then the program 
   outputs number of time each bird hit a pig or left the plane, and either the 
   birds win or the pigs win. In the process, methods of class are used and loops 
   are used also.
'''

## import calsses
import math
from Pig import *
from Bird import *

## main body of program
if __name__=="__main__":
    
    ## asks the user for two files
    bird=raw_input('Enter the bird file ==> ')
    print bird
    pig=raw_input('Enter the pigs file ==> ')
    print pig
    
    ## parsing the two files to lists 
    f_bird=open(bird)
    f_pig=open(pig)
    l_bird=[]
    l_pig=[]
    d_bird={}
    for line in f_bird:
        l_bird.append(line.strip().split('|'))
    for line in f_pig:
        l_pig.append(line.strip().split('|'))
        
    ## basic outputs of birds and pigs
    print 'Num birds %d:'%len(l_bird)
    for i in l_bird:
        print '%s (%.1f,%.1f)'%(i[0],float(i[1]),float(i[2]))
    print '....'
    print 'Num pigs %d:'%len(l_pig)
    print 'Time 0: %s starts at (%.1f,%.1f)'%(l_bird[0][0],float(l_bird[0][1]),float(l_bird[0][2]))
    t=1
    n_b=0
    n_pop=0
    b=Bird(l_bird[0][0],float(l_bird[0][1]),float(l_bird[0][2]),float(l_bird[0][3]),float(l_bird[0][4]),float(l_bird[0][5]))
    l_pigclass=[]
    for i in range(len(l_pig)):
        p=Pig(l_pig[i][0],float(l_pig[i][1]),float(l_pig[i][2]),float(l_pig[i][3]))
        l_pigclass.append(p)
    n_bird=len(l_bird)
    n_pig=len(l_pig)
    
    ## main loop of how the bird moves and its intersection with pigs
    ## class are being called and if, else conditions are used
    while True:        
        b.move()
        for i in range(len(l_pigclass)):
            if (b.check_intersection(l_pigclass[i])):
                p=l_pigclass[i]
                print 'Time %d: %s at (%.1f,%.1f) pops %s'%(t,b.name,float(b.x),float(b.y),p.name)
                b.dx-=1./2*float(b.dx)
                n_pop+=1
                remove=l_pigclass.pop(i)
                print 'Time %d: %s at (%.1f,%.1f) has (dx,dy) = (%.1f,%.1f)'%(t,b.name,float(b.x),float(b.y),float(b.dx),float(b.dy))
                break
        if b.check_boundary():
            print 'Time %d: %s at (%.1f,%.1f) has left the game'%(t,b.name,float(b.x),float(b.y))
            n_b+=1
            if n_b!=len(l_bird):
                b=Bird(l_bird[n_b][0],float(l_bird[n_b][1]),float(l_bird[n_b][2]),float(l_bird[n_b][3]),float(l_bird[n_b][4]),float(l_bird[n_b][5]))
                print 'Time %d: %s starts at (%.1f,%.1f)'%(t,b.name,float(b.x),float(b.y))
        if b.check_speed():
            print 'Time %d: %s at (%.1f,%.1f) with speed %.1f stops'%(t,b.name,float(b.x),float(b.y),math.sqrt(float(b.dx)**2+float(b.dy)**2))
            n_b+=1
            if n_b!=len(l_bird):
                b=Bird(l_bird[n_b][0],float(l_bird[n_b][1]),float(l_bird[n_b][2]),float(l_bird[n_b][3]),float(l_bird[n_b][4]),float(l_bird[n_b][5]))
                print 'Time %d: %s starts at (%.1f,%.1f)'%(t,b.name,float(b.x),float(b.y))            
        if n_pop==n_pig:
            print 'Time %d: All pigs are popped. The birds win!'%t
            break
        if n_b==n_bird:
            print 'Time %d: No more birds. The pigs win!'%t
            print 'Remaining pigs:'
            for i in l_pigclass:
                print i.name
            break        
        t+=1