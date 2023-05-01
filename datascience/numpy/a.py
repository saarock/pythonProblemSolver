import numpy as py

# a[start: end: step]
a = py.array([1,2,3,4,5,6], dtype='i')
print(a[0:3:2])
c = a.copy()
v = a.view()
v[0] = 100


print(c)
print(v)
print(c.base)
print(v.base)
print(a.dtype)


# TO check tje shape aray index no shoud be equal 
arr = py.array([[1, 2, 3, 4], [5, 6, 7, 8]])
c = py.array([[1,2,3,4,5,67], [34,49,59,67,7, 67]])



print(arr.shape)
print(c.shape)




# array reShape()
ar = py.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
v = ar.reshape(3,5)
print(v)




let_new_aarray = py.array([1,2,3,4,5,6,7,7,8,7,7]);

# It return the index in which index that given argument is present
c = py.where(let_new_aarray == 7)
print(c)




# here is another method in the numpy whiuch is best that is searchsorted() it follow the binary searches which means array should be sort manner
let_sorted_array = py.array([1,2,3,4,5,6,7,8,9,10])
let_search = py.searchsorted(let_sorted_array, 7)
print(let_search)

# To search the Numpy array;
ok = py.array([78,4,6,7,365456,567567,658])
l = py.sort(ok)
print(l) #This is the sorted array; and (NOTE: it can sort the alphabel also)
print(ok) #This is not sorted arrray which is orginal array



n = py.array([1,2,3,4,54,6])
m = [True, False, True, False, True, False]
# This is filtering array in the numpy where where true only return value from there
print(n[m])





p =  py.array([1,2,3])

# Makes the new array and then assign in then c variable or identifier
c = p*2
print(c)