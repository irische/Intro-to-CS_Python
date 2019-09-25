# this program generates a fancy framing on a name diagonally with 
# background pattern and frame pattern on demand

name=raw_input('Enter the name => ')
print name
frame_c=raw_input('Enter the frame character => ')
print frame_c
back_c=raw_input('Enter the background character => ')
print back_c
if len(frame_c)!=1 or len(back_c)!=1:
    if len(frame_c)!=1:
        print 'Error: need a single frame char.'
    if len(back_c)!=1:
        print 'Error: need a single background char.'
    print 'At least one error so quitting.'
else:
    # using while loop to generate the whole framing
    frame_0=frame_c
    back_c+=' '
    frame_c+=' '
    print frame_c*(len(name)+3)+frame_0
    print frame_c+back_c*(len(name)+2)+frame_0
    i=0
    list_line=[]
    while i<len(name)/2:
        tmp_string=frame_c+back_c*(i+1)+name[i]+' '+back_c*(len(name)-(i+1)*2)+\
            name[(len(name)-(i+1))]+' '+back_c*(i+1)+frame_0
        list_line.append(tmp_string)
        print tmp_string
        i+=1
    if len(name)%2==1:
        print frame_c+back_c*(len(name)/2+1)+name[len(name)/2]+' '+back_c*\
              (len(name)/2+1)+frame_0
    i=len(list_line)-1
    while i>=0:
        print list_line[i]
        i-=1
    print frame_c+back_c*(len(name)+2)+frame_0
    print frame_c*(len(name)+3)+frame_0