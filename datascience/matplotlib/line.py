import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1, 2,3 ,4])
xpoints = np.array([1, 2,3 ,4])

font1 = {'family':'serif','color':'blue','size':20}
plt.title("Welcome to the laiga financial process", fontdict=font1)
plt.ylabel("The left margin.", size=20)
plt.xlabel("The Right margin.", size=20)

plt.plot(ypoints,linestyle = 'dotted', marker='o')
x = np.array([34,45,45])
y = np.array([12,34,456])
plt.plot(x,linestyle = 'dotted', marker='o')
plt.grid()
plt.show()