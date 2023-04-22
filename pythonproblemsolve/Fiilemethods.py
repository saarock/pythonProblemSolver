
a = open('a.html', 'w')
# append the text by the write methos anf the "a" argument on the append file
c = open('aa.txt', 'a')
c.write("My name is aaysh basnet")


# Flush method it clear the internals buffer  buffer means=> defination of the buffer temporary storage in the main memory (RAM) is called buffer
c.flush()
c.close()
b = open('aa.txt', 'r')

# check that is readable or not if file in in read format 'r' then it return true otherwise false
print(b.readable())

# check the writeable format or not if there is attribute with 'w' then it will reutrn the true otherwise return false
print(b.writable())

print(b.read())
# The fileno() method returns the file descriptor of the stream, as a numb
print(b.fileno())

# isatty() return true if the the stream is connecrted with the terminal device and does same in os also
print(b.isatty())


# readline() it read one line from the file
print('this', b.readline(), 'this')


# seek()    => this methoid tells that donot read the file from the initial point just read the file according to the attributes given to the seek method
b.seek(10)
data = b.read(12) #=> 12 is telling read only the 12 bytes after seeking the file
print(data)
print(b.tell(), "self") # tells where the file read is finished or tells the current file position



# writable() return true if the file is in writeable mode othewise false




# he close() method closes an open file. we should always close the file after read
b.close()


a = open('aayush.txt', 'a')
a.write('12345Aayush')
# truncate(size) =>  method gives read the file according to it's size
a.truncate(5)
b = open('aayush.txt', 'r')
daat =b.read()
print(daat)


f = open("demofile3.txt", "a")
# write the list of the string in teh file for example
# See you soon!
# Over and out. => Like this way

f.writelines(["See you soon!", "Over and out."])
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
