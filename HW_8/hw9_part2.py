"""Author: <Boliang Yang and yangb5@rpi.edu>

   Purpose: This program reads a yelp file about the businesses and a reviews 
   file, finds the reviews for all the stores of the given business and prints 
   the reviews in order they are found in the file, formatted with four spaces 
   on the left and broken into lines using textwrap.

"""

## all imports
import json
import textwrap

## main body of the program
if __name__ == "__main__":
    business_name=raw_input('Enter a business name => ')
    print business_name
    
    business_list=[]
    name_list=[]
    for line in open('businesses.json'):
        business = json.loads(line)
        business_list.append((business['name'],business['business_id']))
        name_list.append(business['name'])
            
    review_list=[]    
    for line in open('reviews.json'):
        review = json.loads(line)
        review_list.append((review['business_id'],review['text']))
    
    id_list=[]
    for i in range(len(business_list)):
        if business_name==business_list[i][0]:
            id_list.append(business_list[i][1])
            
    review=[]
    for i in range(len(review_list)):
        for business_id in id_list:
            if review_list[i][0]==business_id:
                review.append(review_list[i][1])
                
    if business_name not in name_list:
        print 'This business is not found'
    elif len(review)==0:
        print 'No reviews for this business is found'
    else:    
        for i in range(len(review)):
            print 'Review %d:' %(i+1)
            text_list=review[i].split('\n\n')
            for text in text_list:
                wrap_list=textwrap.wrap(text,70)
                for words in wrap_list:
                    print ' '*4+words
                print '\n'        
                