# class recursion():
#     def recurson(self, a):
#         if(a==0):
#             return 1
#         # print(a)
#         b  =  a * self.recurson(a-1)
#         return b

# a = recursion()
# n = a.recurson(4)
# print(n)



# def b():
#     return 12


# print(3+b())


l = []
def a(n):
    if(n==0):
        return 1
    b = n+ a(n-1)
    return b

b= a(3)
print(b)
