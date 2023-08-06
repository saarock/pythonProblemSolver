# # Factorial of 4
# # This is the simple example of the recursive function to find the factor of 4 
def fact(n):
    if(n==1):
        return 1
    b = n * fact(n-1)
    return b
    
fact_of_given_number = fact(4)
print(fact_of_given_number)





def fact(n):
    if n <= 1:  # Base case: Fibonacci numbers 0 and 1 are the same as n
        return n
    else:
        return fact(n - 1) + fact(n - 2)  # Recursive call to find the sum of previous two Fibonacci numbers

# Example usage:
num = 6
fib_num = fact(num)
print("The Fibonacci number at index", num, "is:", fib_num)



# # Let's see another example to find the factor of the 4 without using the recursion

# l = 4
# ke = 1
# def fact_o():
#     global ke,l
#     while l>0:
#         ke =  ke*l
#         l-=1
#     return ke
        

# v= fact_o()
# print(v)
