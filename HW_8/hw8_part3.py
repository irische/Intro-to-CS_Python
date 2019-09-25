'''purpose: This program reads a file that stores information about all battleship
    and all player moves. And it determines whether the player win or not.
'''


## battleship class
class Battleship(object):
    ## constructor
    def __init__(self,name0,x0,y0,len0,h0,health0):
        self.name=name0
        self.x=x0
        self.y=y0
        self.length=len0
        self.height=h0
        self.health=health0
    ## function that prints relevant information of battleship
    def __str__(self):
        return '%s: (%s,%s,%s,%s) Health: %s' %(self.name.rjust(12),\
            self.x,self.y,self.x+self.length,self.y+self.height,self.health)
    ## function that determines whether the battleship is hit or not
    def hit(self,x0,y0):
        if self.x<=x0 and x0<=self.x+self.length:
            if self.y<=y0 and y0<=self.y+self.height:
                return True
        return False
    ## function that decrease the health by one
    def health_decrease(self):
        self.health-=1
    ## function that determines whether the ship sinks or not
    def sink(self):
        return self.health==0

## main body of program
if __name__=='__main__':
    f=raw_input('File name => ')
    print f
    open_f=open(f)
    n_bs=int(open_f.readline().strip())
    bs_list=[]
    for i in range(n_bs):
        line=open_f.readline()
        l_line=line.strip().split('|')
        b=Battleship(l_line[0],int(l_line[1]),int(l_line[2]),\
                     int(l_line[3]),int(l_line[4]),int(l_line[5]))
        bs_list.append(b)
        print b
    for line in open_f:
        l_line=line.strip().split('|')
        p_name=l_line[0]
        x=int(l_line[1])
        y=int(l_line[2])
        miss=True
        for bs in bs_list:
            if bs.hit(x,y):
                miss=False
                bs.health_decrease()
                print '%s fires (%s, %s) hits' %(p_name,x,y), bs
                if bs.sink():
                    print '%s is sinking!' %bs.name
                    bs_list.remove(bs)
        if miss:
            print '%s misses at (%s,%s)' %(p_name,x,y)
        if len(bs_list)==0:
            print p_name,"won"
            break
    if len(bs_list)!=0:
        print "No player won!"
    
    
            