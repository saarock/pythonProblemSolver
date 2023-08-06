# Linear sort with non key argument
find = 5
j= 0
def lets_apply_linear_sort(*a):
    global j
    for i in a:
        if(find==i):
            print(find, i)
            print(f'found the {find} number in the index no {j}')
        j+=1
        


lets_apply_linear_sort(2,1,3,6,8,3,5,6,7)














