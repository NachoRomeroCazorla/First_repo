#This is just a test to add to the GitHub repo

import numpy as np
import matplotlib.pyplot as plt


a = np.linspace(0, 30, 50)
b = np.cos(a)
print(a)
plt.figure()
plt.plot(a , b)
plt.show()
plt.savefig("Figure-1.jpg")