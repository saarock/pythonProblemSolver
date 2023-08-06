# Insertions sort
class insertions:
    find = 5
    def __init__(self, arr):
        self.arr = arr
# At first sort the array in the increasing order (NOTE: we can use decreasing order also.)
    def insert(self):
        self.r = self.arr
        for i in range(1, len(self.r)):
            current = self.r[i]
            m = i-1
            while m >=0 and current < self.r[m]:
                self.r[m+1] = self.r[m]
                self.r[m] = current
                m-=1

        
                # After teh sorting the array by using the insertion seRCH
    def allthestring(self):
        print(self.r)


    def binary_search(self):
        print(self.r, 'This is the sorted array')
        half = int(len(self.r)/2)-1
        print(half)
        print(self.r[half], self.find, 'Which is big')
        if(self.r[half]<= self.find):
            for i in range(half,len(self.r)):
                if(self.r[i]==self.find):
                    print(f'Found the {self.find} number in the index no {i}')
                    return
                 
        else:
            while half>=0:
                if(self.r[half]==self.find):
                    print(f'Found the {self.find} number in the index no {half}')
                    return
                half-=1
        print('NotFound')
              
    
                
                    


            

        


a = insertions([2,1,3,6,8,3,5,7,7,8,9,10,12])
a.insert()
a.allthestring()
a.binary_search()
