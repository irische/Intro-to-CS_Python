'''This program illustrates a turtle in a grid that moves at most 250 times until 
   it fell off the grid and return its position and direction every 20 time steps.
'''
import random

## function of how the turtle move every time
def move_turtle(row,col,direction,turn_prob):
    ran_prob=random.random()
    if ran_prob<turn_prob:
        if direction=='right':
            direction='down'
        elif direction=='down':
            direction='left'
        elif direction=='left':
            direction='up'
        else:
            direction='right'
        return (row,col,direction)
    else:
        if direction=='right':
            col+=1
        elif direction=='down':
            row+=1
        elif direction=='left':
            col-=1
        else:
            row-=1
        return (row,col,direction)

## main body of program
if __name__ =="__main__":
    M=int(raw_input('Enter the integer number of rows => '))
    print M
    N=int(raw_input('Enter the integer number of cols => '))
    print N
    turn_prob=float(raw_input("Enter the turtle's turn probability (< 1.0) => "))
    print turn_prob
## call the seed random number generator
    seed_value=10*M+N
    random.seed(seed_value)
   
    dir_list = ['right', 'down', 'left', 'up']
    rand_index = random.randint(0,3)
    direction = dir_list[rand_index]
    print 'Initial direction: %s'%direction
    row=M/2
    col=N/2

## while loop how the turtle makes the step by calling the function
    i=1
    while i<=250:
        row,col,direction=move_turtle(row,col,direction,turn_prob)
        if row>-1 and row<M and col>-1 and col<N:
            if i%20==0:
                print 'Time step %d: position (%d,%d) direction %s.'%(i,row,col,direction)
            if i==250:
                print 'After 250 time steps the turtle ended at position (%d,%d) and direction %s.'%(row,col,direction)
        else:
            if row==-1:
                print 'After %d time steps the turtle fell off the top in column %d.'%(i,col)
                break
            elif row==M:
                print 'After %d time steps the turtle fell off the bottom in column %d.'%(i,col)
                break
            elif col==-1:
                print 'After %d time steps the turtle fell off the left in row %d.'%(i,row)
                break
            elif col==N:
                print 'After %d time steps the turtle fell off the right in row %d.'%(i,row)
                break
        i+=1