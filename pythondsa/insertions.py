# Insertions sort
import time
class insertions:
    def __init__(self, arr):
        self.arr = arr

    def insert(self):
        self.r = self.arr
        for i in range(1, len(self.r)):
            print('I amstart')
            print(i)
            print('I am send')
            current = self.r[i]
            m = i-1
            while m >=0 and current < self.r[m]:
                self.r[m+1] = self.r[m]
                self.r[m] = current
                print(self.r[m+1] , self.r[m])
                m-=1
    def allthestring(self):
        print(self.r)

            

        

a = insertions([1,28,1,0,7,4,8])
star_time= time.time()

a.insert()
a.allthestring()
end_time= time.time()
print(star_time-end_time)