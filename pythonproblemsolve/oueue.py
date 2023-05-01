# python collection for queue first in first out
from collections import deque 
q = deque(["Aaysh", "Banet"])
q.appendleft("Saarock")
print(q[1])

#  List Comprehensions¶
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# We can import pi also from the python
from math import pi
# a = round(12.4)
print(pi)
from math import ceil
print(round(12.4)) #return rounf value 12
print(round(12.6)) #return round value 13
print(ceil(12.1)) # return 12

a = [1,2,3,4,5,6,7,8]
# del a
print(a)


basket = {'Aaysh', 'Basnet', 'Is', 'The', 'Main', 'Things'}
print(basket)
for a in basket:
    print(a)


# python while Loop 
i=1
while(i<=10):
    print(i) 
    i= i+1

print('Another starting ', end=' ')
# range() python sequences datatypes
for i in range(10):print(i)    
x = lambda a: a+2
print(x(3))


def abC():
    # The power of lambda is better shown when you use them as an anonymous function inside another function.
    # Python lambda function
    print("Welcome")
a = lambda a: a()
a(abC)

# If we neeed array in the python we can import python builtin array
import array
a  = array.array('i', [1,2,3,4,5,6])
print(a)