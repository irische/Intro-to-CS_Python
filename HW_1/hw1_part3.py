width=raw_input("Width of box ==> ")
print width
height=raw_input("Height of box ==> ")
print height
character=raw_input("Enter frame character ==> ")
print character
print "\nBox"
row_1=character*int(width)
print row_1
each=character+" "*(int(width)-2)+character
n=len(width+height)+2
print (each+"\n")*(int(height)-3)+character+" "*(int(width)-2-n)+width+"x"+height+" "+character
print character*int(width)





