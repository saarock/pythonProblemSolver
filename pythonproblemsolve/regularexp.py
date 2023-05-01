# reglular expres contains the Some sequences  of the Character that forma search of character
import re as r
txt = "The hero is who present the the main mathmatic calculation"
# search method returns the  object of the math in which index sccording to in which it is located
x = r.search("calculation$", txt)
if x:
    print("Matched", x.start())
else: 
    print('Donot matched')

# Split the string at every white space character
x = r.split('\s', txt)
print(x)
y = r.search('[T]', txt)
print(y)


l = r.finditer('the', txt)
for k in l:
    # Start method for get the matches index'
    print(k.start())

    # Span method return the matches index in the tuple
    print(k.span())



# escape 