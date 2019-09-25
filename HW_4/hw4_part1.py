'''this program reads in a word and checks whether the word is a palindrome
   reads the same forward and backward)
'''
## function that removes all whitespace and non-alphabetic characters, changes to lower case
## and returns the modified string
def remove_extra(word):
    word=word.lower()
    list_word=list(word)
    new_word=''
    for every_word in list_word:
        if every_word.isalpha():
            new_word+=every_word
    return new_word

## function that reverses a given word or sentence
def reverse(word):
    word=remove_extra(word)
    list_word=list(word)
    i=len(list_word)-1
    reversed_word=''
    while i>=0:
        reversed_word+=list_word[i]
        i-=1
    return reversed_word

## main body of program
if __name__=="__main__":
    word=raw_input('Enter a word or a sentence => ')
    print word
    print
    print 'String after removing non-alphabetic characters: %s'%remove_extra(word)
    print 'String reversed: %s'%reverse(word)
    if remove_extra(word)==reverse(word):
        print 'Palindrome'
    else:
        list_original=list(remove_extra(word))
        list_reverse=list(reverse(word))
        i=0
        while i<len(list_original):
            if list_original[i]!=list_reverse[i]:
                word_original=list_original[i]
                word_reverse=list_reverse[i]
                position=i
                break
            i+=1
        if word_original>word_reverse:
            print 'Not a palindrome: %s comes after %s at position %d'%(word_original,word_reverse,position)
        else:
            print 'Not a palindrome: %s comes before %s at position %d'%(word_original,word_reverse,position)