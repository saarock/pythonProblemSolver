# Note string are ummutable we cannot change the string in the pythin and almost all the programminga  language





# capatilized
my_string = "my namme is aayush basnet"
print(my_string.capitalize())

# upper
# makes the whole string in the upper case
print(my_string.upper())

# makes all the String in the lower case
print(my_string.lower())

# center

print(my_string.center(2)) # Simpley it will print --2-- (NOTE -- IS THE indent/White space)

# encode
# return the string in the specifix prefix Encoding (b => Which means treat that values as a Strings)
print(my_string.encode())

# replace
# Help to replace the value from the String
print(my_string.replace('my', 'MY'))

# startswith
print(my_string.startswith('m')) #If my String is start with m then it return the true if not simple return the False

# endswith
print(my_string.endswith('t')) #If my String is end with t then it return the true if not simple return the False


my_another_string = 'my\tname\tAayush\tBasnet'
print(my_another_string.expandtabs(3)) # When ever the exapndstabs method found the \t modifier then it will create a indent accoriding the argument which we passed 
# in the expandstabs(3)


# find th value from the string if found then it will return the postion/index of the value if not found return -1
print(my_string.find('my'))
print(my_string.find('mrty'))


# anothere index method also work same as a find  but if value not found it simple throwe the error
print(my_string.index('my'))
# print(my_string.index('myrtr'))


# return true if all teh character are the alphanumeric means (alphabet (a-z) and numer (0-9))  with no indent/whiteSpace
let = 'my2323'
print(let.isalnum())


# isalpha
# return true if all the value are the alphapet wihout the  indent/whitespace
let = "mynamis"
print(let.isalpha())


# isascii
# to understand about this methos you have to what is  the ascii means 
let = 'my34'
print(let.isascii())


let = 'Myanothernameissaarockbasnet'
# if the string is the valid idenitier then it will return true otherwise false.A string is called valid identifier when the string is start with
# the alphabet (a-z) and number(0-9). IF the string is started with the white sapce or Contain any white space and if the String is Started with the nummber then
# that is no the identifier
print(let.isidentifier())

# isnumeric
let = '5654654'
# if all the character are the number in the sting then it will return the True otherWise false
print(let.isnumeric())


# isprintable => return true if the string is printable then it will return TRUE otherwise false
print(let.isprintable())


# isspace => if in string there is the space then it will return true other wise false
let = " "
print(let.isspace())


# istitle => if all word in the string start withs Upper/capital then it will return true otherwise false
let = "My Name Is Aayush Basnet"
print(let.istitle())


# isupper => if string is in the uppercase then it will return true otherwise false;
let = "MY NAME IS AAYUSH BASENT"
print(let.isupper())




# Simply join() methos works String.join(iterable)
let = ("aaysh", 'banet')
print('Saarock'.join(let))
let = "Aaysh basnet is the hero"
print(let.join('Saarock'))



# ljust
l = let.ljust(20)
print(l, "And my another name is Saarock BASNET")



# lower
let = 'I LOVE TO READ FOR UNDERSTAND NOT FOR EXAM AND THE FUCKING COMPETITION'
# makes the string in two the lower
print(let.lower())



# lstrip
a= '     I love my Country and my country name is Nepal.                '
print(a.lstrip(), a) #trim/remove the white space the left one
print(a.strip(), a) #trim the space from the left and the right from the both side.
print(a.rstrip(), end='') #trim the white space  the right first one
print(1)



let = 'ab c def'
print(let.split(' '))  #makes the list according to the seperater which is space;


let = 'a b\n c d \ne ' #makes a list accoring to the escape character \n
print(let.splitlines())



# partition = >return the tuple if the value matched give as a argument

let = 'i love to read to understand deeply'
print(let.partition('to')) #check from the left and catch the first one
print(let.rpartition('to')) #check from the right and catch the first one


let = 'name aayush basnet'
l = {2:3}
print(let.translate(l))
print(type(let.translate(l)))


# Note  to check the address of the specific datatypes in the memory id function is useful

print(f"{id(let)} this is the ud" )

# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
let = "12"
a = let.zfill(10)
print(a)