'''In this program,i read through a given file about Dr Who Villains and find 
   the names and stories of each villain and doctors associated using knowlege 
   about set,list,string,loops,functions and others we have learned before.
'''
## this function is used to parse the villain file by taking a single line
## parameter and returns a list with four elements
def parse_line(line):
    line=line.split('\t')
    l=[]
    num_stories=len(line[7].split(','))
    l.append(num_stories)
    l.append(line[0].strip())
    s_title=set()
    for t in line[7].split(','):
        s_title.add(t.strip())
    l.append(s_title)
    s_doc=set()
    for doc in line[4].split(','):
        s_doc.add(doc.strip())
    l.append(s_doc)
    return l

## main body of program
if __name__== '__main__':
    
    ## read the file
    f=open('DrWhoVillains.tsv')
    l=[]
    l_line=[]
    for line in f:
        l_line.append(line)
        l.append(parse_line(line))
    l.sort()
    
    ## using a while loop to generate the conditions when asking for a raw input
    ## from user and react according to the value.When finding the values being
    ## asked, set is being used and set&set and set-set are used to find the common
    ## values in two set and values that are in one set but not the other.
    while True:    
        i=-1
        print
        while i>=-10:
            print '%d. %s'%(-i,l[i][1].strip())
            i-=1
        print
        number=raw_input('Please enter a number between 1 and 10, or -1 to end\nEnter a villain ==> ')
        print number
        if number=='-1':
            print 'Exiting'
            break
        elif number.isdigit()==False or int(number)<1 or int(number)>10:
            continue
        elif int(number)>=1 and int(number)<=10:
            name=l[-(int(number))][1].strip()
            num_stories=0
            stories=set()
            for i in l:
                if i[1].strip()==name:
                    num_stories+=i[0]
                    st=','.join(i[2])
                    list_=st.split(',')
                    for m in list_:
                        stories.add(m)
            print
            print '%s in %d stories, with the following other villains:'%(name,num_stories)
            print '='*50
            names=set()
            for i in l:
                if len(i[2]&stories)!=0:
                    if i[1]!=name:
                        names.add(i[1])
            for i in range(len(sorted(names))):
                sorted(names)[i]=sorted(names)[i][:50]
                print '%d. %s'%(i+1,sorted(names)[i][:50])
            other_stories=set()
            for i in l:
                if i[1]!=name:
                    st=','.join(i[2])
                    list__=st.split(',')
                    for n in list__:
                        other_stories.add(n)
            if len(stories-other_stories)==0:
                print
                print 'There are no stories with only this villain'
                print '='*50
            else:
                print
                print 'The stories that only features %s are:'%name
                print '='*50
                j=1
                for i in (sorted(stories-other_stories)):
                    print '%d. %s'%(j,i)
                    j+=1
            doctors=set()
            n=0
            for i in l:
                if i[1]==name:
                    st=','.join(i[3])
                    lt=st.split(',')
                    for n in lt:
                        doctors.add(n)
            print 
            print 'This villain was foiled by %d doctor(s):'%(len(doctors))
            print '='*50
            j=1
            for i in sorted(doctors):
                print '%d. %s'%(j,i)
                j+=1