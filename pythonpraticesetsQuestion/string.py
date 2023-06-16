# What is string in the python
# => A sequesnce of the character which are enclosed in single or in the douoble quotes is knows as the string in the python.

# Is there is differences between 'a' and "a"
# => No

# Print softwarica 10 times
# for i in range(1,11):
#     print('Softwarica',i)


# 2sum of thelist
# lli = [1,2,3,4,5,6,7,8]
# n = 0
# for i in lli:
#     n += i
# print(n)



# let = [1,'a', "c", 2,3,4]
# n = []
# for i in let:
#     if(type(i) == int):
#         n.append(i)
#     else:
#         print('string')

# print(n)        



# multiplication of the each element
# let = [3,3]
# n = 1
# for i in let:
#     n*=i
# print(n)    


# reverse a list
# l = [1,2,3,4,5,6,7,8,9,10]
# n = []
# for i in l:
#     n.insert(0,i)
# print(n)

# given a llist 1 2 3 4 but expected  2 3 4 5
l = [1,2,3,4]
p = []
for i in l:
    if(i==1):
        l.remove(1)
    p.append(i)    
    # l.append(5)
p.append(5)
print(5, 'i')        