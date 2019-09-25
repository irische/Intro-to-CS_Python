# simulating the position of a turtle moving on a grd, and tracking its position
# as the user commands it to turn or walk

# function taking in turtle's current location and returns the position after 
# its every move
def walk_or_turn(position_i,move,step):
    if move.lower()=='walk':
        if position_i[2]=='right':
            return position_i[0]+int(step),position_i[1],position_i[2]
        elif position_i[2]=='down':
            return position_i[0],position_i[1]+int(step),position_i[2]
        elif position_i[2]=='left':
            return position_i[0]-int(step),position_i[1],position_i[2]
        else:
            return position_i[0],position_i[1]-int(step),position_i[2]
    elif move.lower()=='turn':
        if position_i[2]=='right':
            return position_i[0],position_i[1],'down'
        elif position_i[2]=='down':
            return position_i[0],position_i[1],'left'
        elif position_i[2]=='left':
            return position_i[0],position_i[1],'up'
        elif position_i[2]=='up':
            return position_i[0],position_i[1],'right'
    else:
        print 'Illegal step choice.'
        return position_i

# main function
position_i=100,100,'right'
i=0
list_x=list()
list_y=list()
list_x.append(100)
list_y.append(100)

# while loop used to simulate turtle's move and output position on demand
while i<6:
    move=raw_input('Step choice (turn or walk) => ')
    print move    
    if move.lower()=='walk':
        step=int(raw_input('Number of steps => '))
        print step
        position_i=walk_or_turn(position_i,move,step)
    elif move.lower()=='turn':
        position_i=walk_or_turn(position_i,move,0)
    else:
        position_i=walk_or_turn(position_i,move,0)
    if i==2:
        print 'After three steps: position (%s,%s), direction %s'%(position_i[0],position_i[1],position_i[2])
    list_x.append(position_i[0])
    list_y.append(position_i[1])    
    i+=1
         
print 'After six steps: position (%s,%s), direction %s'%(position_i[0],position_i[1],position_i[2])
print 'Min x %d'%min(list_x)
print 'Min y %d'%min(list_y)
print 'Max x %d'%max(list_x)
print 'Max y %d'%max(list_y)