# Qianqian Che (cheq@rpi.edu)
# Purpose: output the table about top 250 ranked female and male names on demand.

# read and access the names and counts
import read_names
import sys

# function to find if a value is in the list and the index and return required values
def table(name,list_name,list_counts):
    position=list_name.index(name)
    count='%5d'%int(list_counts[position])
    percent_top='%7.3f'%(100.*int(count)/list_counts[0])
    percent_sum='%7.3f'%(100.*int(count)/sum(list_counts))
    rank='%3d'%int(position+1)
    name=name.ljust(11)
    return '%s %s %s %s %s'%(rank,name,count,percent_top,percent_sum)

# function to print out required table of rank, name, count, and percentage information
def table_(name,list_name,list_counts):
    if name in list_name:
        position=list_name.index(name)
        if position==0:
            name_1=name
            name_2=list_name[position+1]
            name_3=list_name[position+2]
            print table(name_1,list_name,list_counts)
            print table(name_2,list_name,list_counts)
            print table(name_3,list_name,list_counts)
        elif position==1:
            name_1=name
            name_2=list_name[position+1]
            name_3=list_name[position+2]
            name_4=list_name[position-1]
            print table(name_4,list_names,list_counts)
            print table(name_1,list_names,list_counts)
            print table(name_2,list_names,list_counts)   
            print table(name_3,list_names,list_counts)
        elif position==249:
            name_1=name
            name_2=list_name[position-1]
            name_3=list_name[position-2]
            print table(name_3,list_name,list_counts)
            print table(name_2,list_name,list_counts)   
            print table(name_1,list_name,list_counts)  
        elif position==248:
            name_1=name
            name_2=list_name[position+1]
            name_3=list_name[position-1]
            name_4=list_name[position-2]
            print table(name_4,list_name,list_counts)
            print table(name_3,list_name,list_counts)
            print table(name_1,list_name,list_counts)   
            print table(name_2,list_name,list_counts)        
        else:
            name_1=list_name[position-2]
            name_2=list_name[position-1]
            name_3=list_name[position]
            name_4=list_name[position+1]
            name_5=list_name[position+2]
            print table(name_1,list_name,list_counts)
            print table(name_2,list_name,list_counts)
            print table(name_3,list_name,list_counts)
            print table(name_4,list_name,list_counts)
            print table(name_5,list_name,list_counts)
    else:
        print '%s is not in top 250.'%name    

# read in year and names from the user and call the functions above to output the table required.
read_names.read_from_file('top_names_1880_to_2014.txt')
year=raw_input('Enter the year to check => ')
print year
if int(year)<1880 or int(year)>2014:
    print 'Year must be at least 1880 and at most 2014'
    sys.exit()
print
female_name=raw_input('Enter a female name => ')
print female_name
print 'Data about female names'
(female_names,female_counts)=read_names.top_in_year(int(year), 'f')
print 'Top ranked name %s'%female_names[0]
print '250th ranked name %s'%female_names[249]
list_250_female=female_names[0:250]

female=table_(female_name,female_names,female_counts)
print 
male_name=raw_input('Enter a male name => ')
print male_name
print 'Data about male names'
(male_names,male_counts)=read_names.top_in_year(int(year), 'M')
print 'Top ranked name %s'%male_names[0]
print '250th ranked name %s'%male_names[249]
list_250_male=male_names[0:250]
male=table_(male_name,male_names,male_counts)
