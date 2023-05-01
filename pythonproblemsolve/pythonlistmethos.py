# python list  are the mutable, inordered and the duplicated allowed
my_list = ['AAYSH', 'Basnet',23, 23]
my_list[0] = 12
print(my_list)


# There are many list method in the python from which we can do divert the list;
# append => it simple set the element in the last
let = [1,2,3,4,5]
let.append('Aaysh')
print(let)


# insert => This also does same like append but is set  the element like the according to the index based which we ppassed as a argument in the 
# insert method
let.insert(0, 'AAYUSH')
print(let)


# clear methos simply clear all the elements from the set
# let.clear()
# print(let)
# reverse  method in list to reverse the list eleement node it doesnot work in the String for string there is reversed method and also we have to used for loop t get poper result'

let.reverse()
print(let)


# pop => By deafult it delete the last element => (BUT WE CAN GIVE THE ARGUMENT THAT WHICH INDEX ELEMENT WE WANT TO DELETE)
let.pop()
let.pop(2) # delete the element which is in the index 2;
print(let)


# Count how many time the element is present as a duplicated
print(let.count(3))

# copy => simple makes a copy of the list and also change the address in the memory
a = let.copy()
print(a, "THis is t6he  copy array")
print(id(a))
print(id(let))
print(id(let))

# extend suppose i have to list
a = [1,2,3,4]
b = [5,6,7,8]
a.extend(b)
print(a)



# sort
# It sorted the list in the insending and desening in both order
a = [25,1,56,8]
b = ['a', 'n', 'v', 'b']
a.sort(reverse=True)
b.sort()
print(a)
print(b)


# remove() => remove the first item whose value is mathced with x
