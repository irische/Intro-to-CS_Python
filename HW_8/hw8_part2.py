''' Purpose: This program reads a yelp file about the businesses and a reviews 
   file, finds the reviews for all the stores of the given business and prints 
   the reviews in order they are found in the file, formatted with four spaces 
   on the left and broken into lines using textwrap.
'''

## all imports
import json
import textwrap


## main body of the program
if __name__ =="__main__":
    name=raw_input('Enter a business name => ')
    print name
    l_business=[]
    l_name=[]
    for line in open('businesses.json'):
        business=json.loads(line)
        l_business.append((business['name'],business['business_id']))
        l_name.append(business['name'])
    l_review=[]
    for line in open('reviews.json'):
        review=json.loads(line)
        l_review.append((review['business_id'],review['text']))
    l_id=[]
    for i in l_business:
        if name==i[0]:
            l_id.append(i[1])
    review=[]
    for i in l_review:
        for ID in l_id:
            if i[0]==ID:
                review.append(i[1])
    if name not in l_name:
        print 'This business is not found'
    elif len(review)==0:
        print 'No reviews for this business is found'
    else:
        for i in range(len(review)):
            print 'Review %d:'%(i+1)
            l_text=review[i].strip().split('\n\n')
            for text in l_text:
                l_wrap=textwrap.wrap(text,70)
                for words in l_wrap:
                    print ' '*4+words
                print