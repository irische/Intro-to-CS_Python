'''This program reads in a file of Internet Movie Database, and asks an integer 
   N from the user, then outputs N top individuals involved in the most movies 
   using dictionaries and proper loops
'''
## main body of program
if __name__=="__main__":
    
    ## raw input method to ask the user values
    imdb_file=raw_input('Enter the name of the IMDB file ==> ').strip()
    print imdb_file
    N=raw_input('Enter the number of top individuals ==> ')
    print N
    
    ## read in the file and construct a dictionary with the use of for loop
    d=dict()
    d_helper=dict()
    for line in open(imdb_file):
        words=line.strip().split('|')
        name=words[0].strip()
        movie=words[1].strip()
        if name not in d:
            d[name]=1
            d_helper[name]=[]
            d_helper[name].append(movie)
        if movie not in d_helper[name]:
            d[name]+=1
            d_helper[name].append(movie)
    d_result=dict()
    
    ## after aquiring a dictionary, construct another dictionary with the keys 
    ## and values the other way around and using while loop to print the outputs
    for name in d:
        if d[name] not in d_result:
            d_result[d[name]]=[]
        d_result[d[name]].append(name)
    l_times=sorted(d_result.keys())
    count=int(N)
    i=0
    while count>0:
        num=l_times[-1-i]
        count-=len(d_result[num])
        st=''
        names=sorted(d_result[num])
        j=0
        while j<len(names):
            st+=names[j]
            if len(names)>1 and len(names)-j>1:
                st+='; '
            j+=1
        print '%3d: %s'%(num,st)
        i+=1