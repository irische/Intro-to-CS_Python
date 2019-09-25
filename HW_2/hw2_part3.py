def reverse3(number):
    n_1=number/100
    n_2=number%100
    n_3=n_2/10
    n_4=n_2%10
    number=n_4*100+n_3*10+n_1
    return number
def reverse5(number):
    n_1=number/100
    n_2=reverse3(n_1)
    n_3=number%100
    n_4=n_3/10
    n_5=n_3%10
    number=n_5*10000+n_4*1000+n_2
    return number
value=int(raw_input('Enter a value ==> '))
print value
print '\nHere is the computation:\n%d reversed is %d'%(value, reverse5(value))
a=value/100
b=reverse5(value)%1000
print '%d - %d = %d'%(max(a,b),min(a,b),max(a,b)-min(a,b))
print '%d + %d = %d'%(max(a,b)-min(a,b), reverse3(max(a,b)-min(a,b)),max(a,b)-min(a,b)+reverse3(max(a,b)-min(a,b)))
if max(a,b)-min(a,b)+reverse3(max(a,b)-min(a,b))==1089:
    print 'You see, I told you.'
else:
    print 'Are you sure your input is valid?'