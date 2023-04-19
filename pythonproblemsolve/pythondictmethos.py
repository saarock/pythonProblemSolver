# python dictionary method

a = {
    'fruit': 'Apple',
    'vechicle': 'car',
    'car': 'rolls royce',
    }


# Same like the list method it remove all the keys and values from the a dict
# a.clear()
# print(a)

# copy method => make the copy version of the Copy method
print(a.copy())


# fromkeys

x = ('key1', 'key2', 'key3')
y = 2
print(dict.fromkeys(x,y))




# get method

# simply get the value  from the dict witih the help of keys
print(a.get('car'))

# items
# makes tuble in a list
print(a.items())
for i in a.items():
    for j in i:
        print(j)


# keys => return the keys in the form of list under tuple
print(a.keys())


# pop()
# it simply delete the value by passing the key
# a.pop('car')
# print(a)


# update
a.update({'bike': 'ninja'})
print(a)


# popitem() => Simply delete the last one only
print('Printing')
a.popitem()
print(a)

# setdefault => simply return the deafault value 

b = a.setdefault('car', 'aayush')
c = a.setdefault('cars', 'farare')
print(b)
print(c)


# vallues => return the only value of keys in the form of list under tuple
print(a.values())

