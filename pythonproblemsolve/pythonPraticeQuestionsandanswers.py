#   QUESTION  NO: 1 ==>> python program to find the comman elements in three list.
# QUESTION NO: 2 ==>>  find missing and additional value in two list.


# lets make the three list
list1 = [1,2,3,4,5,692]
list2 = [3,5,6,8,9,0]
list3 = [12, 46, 3, 5, 8,0]

# lets find the comman Value

def find_comman(l1,l2, l3):
    # This process is simple but it increase the time Complexity which is very poor try;
    for i in l1:
        for j in l2:
            for k in l3:
                if i == j == k:
                    print('Element is matched and elements are the',[ i , j, k])
                else:
                    print('Not matched...')
                    pass


find_comman(list1, list2, list3)



# Question number 2 ==>> Find the missing and the additional value from the list
# pratice your self; 