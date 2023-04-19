# (NOTE: PYTHON SET ARE NOT IN ORDER, UNMUTABLE AND DUPLICATED NOT ALLOWED)

# we have to wrte the sets in the curly braces
a = {1,2,3,4,56,6,7,8}
print(a)

# clear methos does same like in the list dict it clear all the elements
# a.clear()

# copy => it makes a copy from the orginals sets with differerent address
print(a.copy())


b = {1,2,3,4,54,6,7,8,}
c = a.difference(b) # it mekes a new set after removing the common one from the set a
print(c)


# differerence_update() => it is also same like the difference but it does not make the new set after removing the common set from the set a
# it just remove return the orginal set
a.difference_update(b)
print(a)


# discard() => The discard() method removes the specified item from the set.
# This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

a = {1,2,3,4,5,6,7}
a.discard(1)
print(a)
print('REMOVING IS WORKING')
a.remove(2)
print(a)


# intersetion it is same like out math set intersection
# it give the Coman value from the set a and b
a = {1,2,3,6,7,8}
b = {1,2,3,"d"}
c = a.intersection(b)
print(c)

# intersetion update
# The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).
# The intersection_update() method is different from the intersection() method, because the intersection() method returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.

a.intersection_update(b)
print(a)


# isdisjoint(seta, setb) => returun True if non of the value are similar in the both set otherwise return false
a = {1,2,3,4,5}
b = {7,8,9,10}
c = a.isdisjoint(b)
print(c)



# issubset(seta, setb) => it return the True if all seta is found in the set b otherwise false
a = {1,2,3}
b = {4,5,1,4,2,9,3}
c = a.issubset(b)
print(c)


# issuperset(seta, setb) => just opposite of the subset all all the setb element should be present in the set a
a = {1,2,3,4,5,6,7,8,9}
b = {1,2,3}
c = a.issuperset(b)
print(c)


# pop removes the random items from the set and return the deleteted items from the set
a = {1,2,3,4,5,6}
print(a.pop())
print(a)


# return all the value after removinf the similar element from the set
c = a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b) # update in the orginal set
print(a)




# union() => returns a set that contains all the elements but not duplicated
c = a.union(b)
print(c)


# update() => simply update the set with another set , or any other iterable But not makes a duplicated  and also does not makes a new set 
# simply make change in the orginal set
a = {1,2,3,4,5}
b = {4,5,6,7,8,9,0}
a.update(b)
print(a)