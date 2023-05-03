#This is just a test to add to the GitHub repo

import numpy as np
import matplotlib.pyplot as plt


a = np.linspace(0, 20, 50)
b = np.sin(a)
print(a)
plt.figure()
plt.plot(a , b)
plt.show()
plt.savefig("Figure.jpg")