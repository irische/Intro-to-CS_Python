def encrypt(word):
    word=word.replace(' a', '%4%')
    word=word.replace('he', '7!')
    word=word.replace('e', '9(*9(')
    word=word.replace('y', '*%$')
    word=word.replace('u', '@@@')
    word=word.replace('an', '-?')
    word=word.replace('th', '!@+3')
    word=word.replace('o', '7654')
    return word
def decrypt(word):
    word=word.replace('%4%', ' a')
    word=word.replace('7!', 'he')
    word=word.replace('9(*9(', 'e')
    word=word.replace('*%$', 'y')
    word=word.replace('@@@', 'u')
    word=word.replace('-?', 'an')
    word=word.replace('!@+3', 'th')
    word=word.replace('7654', 'o')
    return word
enter=raw_input("Enter 'E' for encrypt or 'D' for decrypt ==> ")
print enter
if enter.lower()=='e':
    regular=raw_input('Enter regular text ==> ')
    print regular
    print '\nEncrypted as ==> %s'%encrypt(regular)
    d_length=abs(len(regular)-len(encrypt(regular)))
    print 'Difference in length ==> %d'%d_length
elif enter.lower()=='d':
    cipher=raw_input('Enter cipher text ==> ')
    print cipher
    print '\nDeciphered as ==> %s'%decrypt(cipher)
    d_length=abs(len(cipher)-len(decrypt(cipher)))
    print 'Difference in length ==> %d'%d_length
elif enter.lower()!='e'or'd':
    print "I didn't understand ... exiting"

    