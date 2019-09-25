"""Author: <Boliang Yang and yangb5@rpi.edu>

   Purpose: This program reads a yelp file about the businesses, counts all 
   categories that co-occur with the given category and prints those
   categories with counts greater than the given cutoff in sorted order.

"""

## all imports
import json

## main body of the program
if __name__ == "__main__":
    category_name=raw_input('Enter a category ==> ')
    print category_name
    cutoff=int(raw_input('Cutoff for displaying categories => '))
    print cutoff    
    
    business_list=[]
    category_all=set()
    for line in open('businesses.json'):
        business = json.loads(line)
        business_list.append(business)
        for category in business['categories']:
            category_all.add(category)

    categories_dictionary={}   
    for business_name in business_list:
        if category_name in business_name['categories']:
            for category in business_name['categories']:
                if category_name!=category:
                    if category not in categories_dictionary.keys():
                        categories_dictionary[category]=0
                    categories_dictionary[category]+=1
    
    output_list=[]
    for category in categories_dictionary.keys():
        if categories_dictionary[category]>=cutoff:
            output_list.append((category,categories_dictionary[category]))
       
    if category_name not in category_all:
        print 'Searched category is not found'
    elif len(output_list)==0:
        print 'None above the cutoff'
    else:
        print 'Categories co-occurring with %s:' %category_name
        output_list.sort()    
        for output in output_list:
            string='%s: %d' %(output[0],output[1])
            space=' '*(30-len(output[0]))
            string=space+string
            print string
            
    
