'''This program reads in the death statistics for areas of NYS from 2003 to 2013
   and ouput the trend in a single line.
'''
import hw4_util

## function definition to output the trend of death statistics.
def read_deaths(county,data):
    data_=data[:]
    sum=0
    for r in range(len(data_)):
        sum+=data_[r]
    average=sum/11
    high=average*105/100
    low=average*95/100
    data__=''
    for d in range(len(data_)):
        if float(data_[d])>=high:
            data_[d]='+'
            data__+=data_[d]
        elif float(data_[d])<=low:
            data_[d]='-'
            data__+=data_[d]
        else:
            data_[d]='='
            data__+=data_[d]
    print county.ljust(15)+data__

## main body of program
if __name__=="__main__":
    county_1=raw_input('First county => ')
    print county_1
    data_1 = hw4_util.read_deaths(county_1) 
    county_2=raw_input('Second county => ')
    print county_2
    data_2= hw4_util.read_deaths(county_2)
    print
    
## conditional statements for different cases
    if data_1!=[] and data_2!=[]:
        print ' '*15+'2013'+' '*3+'2003'
        read_deaths(county_1,data_1)
        read_deaths(county_2,data_2)
    elif data_1!=[] and data_2==[]:
        print 'I could not find county %s'%county_2
    elif data_1==[] and data_2!=[]:
        print 'I could not find county %s'%county_1
    else:
        print 'I could not find county %s'%county_1
        print 'I could not find county %s'%county_2