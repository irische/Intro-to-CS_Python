''' This program reads in type of lego wanted and quantity, and manipulate 
    current legos to get demanding legos and output remaining legos and type
    and quantity used.
'''
import hw4_util
legos=hw4_util.read_legos()
print 'Current legos %s'%legos

## function definitions used to find match for demanding legos
def match(legos,size,quantity):
    legos_=legos[:]
    n_1x1=legos_.count('1x1')
    n_2x1=legos_.count('2x1')
    n_2x2=legos_.count('2x2')
    n_4x2=legos_.count('4x2')
    if size=='1x1':
        if quantity>n_1x1:
            print "I don't have %d %s legos"%(quantity,size)
        else:
            i=0
            while i<quantity:
                legos_.remove('1x1')
                i+=1
            print 'I can use %d 1x1 legos for this'%quantity
            print 'Remaining legos %s'%legos_
    elif size=='2x1':
        if quantity>n_2x1:
            if quantity*2>n_1x1:
                print "I don't have %d %s legos"%(quantity,size)
            else:
                i=0
                while i<quantity:
                    legos_.remove('1x1')
                    legos_.remove('1x1')
                    i+=1                
                print 'I can use %d 1x1 legos for this'%(quantity*2)
                print 'Remaining legos %s'%legos_
        else:
            i=0
            while i<quantity:
                legos_.remove('2x1')
                i+=1            
            print 'I can use %d 2x1 legos for this'%quantity
            print 'Remaining legos %s'%legos_
    elif size=='2x2':
        if quantity>n_2x2:
            if quantity*2>n_2x1:
                if quantity*4>n_1x1:
                    print "I don't have %d %s legos"%(quantity,size)
                else:
                    i=0
                    while i<quantity:
                        legos_.remove('1x1')
                        legos_.remove('1x1')
                        legos_.remove('1x1')
                        legos_.remove('1x1')
                        i+=1                
                    print 'I can use %d 1x1 legos for this'%(quantity*4)
                    print 'Remaining legos %s'%legos_    
            else:
                i=0
                while i<quantity:
                    legos_.remove('2x1')
                    legos_.remove('2x1')
                    i+=1
                print 'I can use %d 2x1 legos for this'%(quantity*2)
                print 'Remaining legos %s'%legos_ 
        else:
            i=0
            while i<quantity:
                legos_.remove('2x2')
                i+=1
            print 'I can use %d 2x2 legos for this'%quantity
            print 'Remaining legos %s'%legos_            
    elif size=='4x2':
        if quantity>n_4x2:
            if quantity*2>n_2x2:
                if quantity*4>n_2x1:
                    if quantity*8>n_1x1:
                        print "I don't have %d %s legos"%(quantity,size)
                    else:
                        i=0
                        while i<quantity:
                            legos_.remove('1x1')
                            legos_.remove('1x1')
                            legos_.remove('1x1')
                            legos_.remove('1x1')
                            legos_.remove('1x1')
                            legos_.remove('1x1')
                            legos_.remove('1x1')
                            legos_.remove('1x1')
                            i+=1                
                        print 'I can use %d 1x1 legos for this'%(quantity*8)
                        print 'Remaining legos %s'%legos_    
                else:
                    i=0
                    while i<quantity:
                        legos_.remove('2x1')
                        legos_.remove('2x1')
                        legos_.remove('2x1')
                        legos_.remove('2x1')
                        i+=1
                    print 'I can use %d 2x1 legos for this'%(quantity*4)
                    print 'Remaining legos %s'%legos_ 
            else:
                i=0
                while i<quantity:
                    legos_.remove('2x2')
                    legos_.remove('2x2')
                    i+=1
                print 'I can use %d 2x2 legos for this'%(quantity*2)
                print 'Remaining legos %s'%legos_
        else:
            i=0
            while i<quantity:
                legos_.remove('4x2')
                i+=1
            print 'I can use %d 4x2 legos for this'%quantity
            print 'Remaining legos %s'%legos_    
            
## main program
if __name__=="__main__":
    size=raw_input('Type of lego wanted => ')
    print size
    quantity=int(raw_input('Quantity wanted => '))
    print quantity
    match(legos,size,quantity)