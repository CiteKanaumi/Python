import numpy as np
import matplotlib.pyplot as plt

a = np.arange(28)

plt.plot(a,a**2,"x")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
