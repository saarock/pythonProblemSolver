# import matplotlib
# print(matplotlib.__version__) #This is for the matplotlib

import matplotlib.pyplot as plt
import numpy as np
xpoint = np.array([0,5,2])
ypoint = np.array([0,250,220])


# ms = markersize
# mfc = markerfacecolor

plt.plot(xpoint, ypoint, marker='o', ms=19, mfc='blue') #o, * , .
plt.show()


