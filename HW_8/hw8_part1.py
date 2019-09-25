''' Purpose: This program reads a yelp file about the businesses, counts all 
   categories that co-occur with the given category and prints those
   categories with counts greater than the given cutoff in sorted order.

'''
## all imports
import json

## main body of the program
if __name__ =="__main__":
    category=raw_input('Enter a category ==> ').capitalize()
    print category
    cutoff=int(raw_input('Cutoff for displaying categories => '))
    print cutoff
    l_dic=[]
    s_category=set()
    for line in open('businesses.json'):
        business=json.loads(line)
        l_dic.append(business)
        for cate in business['categories']:
            s_category.add(cate)
    D={}
    for i in l_dic:
        if i['name'] not in D:
            D[i['name']]=i['categories']
        else:
            for j in i['categories']:
                D[i['name']].append(j)
    D_cooccur={}
    for key in sorted(D.keys()):
        if category in D[key]:
            for i in D[key]:
                if i!=category:
                    if i not in D_cooccur.keys():
                        D_cooccur[i]=0
                    D_cooccur[i]+=1
    i=0
    for key in sorted(D_cooccur.keys()):
        if D_cooccur[key]>=cutoff:
            i+=1                    
    if category not in s_category:
        print 'Searched category is not found'
    elif i==0:
        print 'Categories co-occurring with %s:'%category
        print 'None above the cutoff'
    else:
        print 'Categories co-occurring with %s:'%category
        for key in sorted(D_cooccur.keys()):
            if D_cooccur[key]>=cutoff:
                print '%s: %d'%(key.rjust(30),D_cooccur[key])
                    