'''This program concerns about simulation of the turtle move is repeated a 
   user-specified number of times and outputs several summary statistics and
   the counting grid.
'''
import random

## function of how the turtle move 
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
    
## function of one silulation 
def run_one_simulation(count_grid,row,col,turn_prob):
    i=1
    dir_list = ['right', 'down', 'left', 'up']
    rand_index = random.randint(0,3)
    direction = dir_list[rand_index]
    while i<=250:
        row,col,direction=move_turtle(row,col,direction,turn_prob)
        if row==-1 or row==M or col==-1 or col==N:
            return (i,True)
        count_grid[row][col]+=1
        i+=1
    return (250,False)

## main body of program
if __name__ =="__main__":
    M=int(raw_input('Enter the integer number of rows => '))
    print M
    N=int(raw_input('Enter the integer number of cols => '))
    print N
    turn_prob=float(raw_input("Enter the turtle's turn probability (< 1.0) => "))
    print turn_prob
    num=int(raw_input('Enter the number of simulations to run => '))
    print num
    
    row=M/2
    col=N/2    

## call seed random number generator  
    seed_value=10*M+N
    random.seed(seed_value)

## loops needed to get the statistics  
    count_grid = []
    for i in range(M):
        count_grid.append( [0]*N )
    l_result=[]
    for i in range(num):
        l_result.append(run_one_simulation(count_grid,row,col,turn_prob))
    sum_time=0
    sum_time2=0
    min_time=100
    max_time=0
    for i in range(len(l_result)):
        sum_time+=l_result[i][0]
        if l_result[i][0]<min_time:
            min_time=l_result[i][0]
        if l_result[i][0]>max_time:
            max_time=l_result[i][0]
        if l_result[i][1]:
            sum_time2+=1
    average=float(sum_time)/num
    perc=float(sum_time2)/num*100
    print
    print 'Completed simulation.'
    print 'Min time to end: %d.'%min_time
    print 'Max time to end: %d.'%max_time
    print 'Average time to end: %.1f. '%average
    print 'Percentage that ended when the turtle fell off is %.1f.'%perc
    print
    print 'Grid of counts:'
    count_grid[M/2][N/2]+=num
    for i in range(M):
        st_grid=''       
        for j in range(N):
            st_grid+='%4d'%count_grid[i][j]
        print st_grid
    
    max_count=0  
    sum_count=0
    for i in range(M):
        for j in range(N):
            sum_count+=count_grid[i][j]
            if count_grid[i][j]>max_count:
                max_count=count_grid[i][j]
                row,col=i,j
    perc_count=float(max_count)/sum_count*100
    print 'Max count occurs at (%d,%d) with percentage %.2f.'%(row,col,perc_count)
        