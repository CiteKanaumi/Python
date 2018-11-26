import numpy as np
import matplotlib.pyplot as plt

e = np.eye(3)
plt.imshow(e)
#plt.show()

plt.imshow(e, interpolation="none")
#plt.show()

img = np.random.rand(32,32)
plt.imshow(img)
plt.gray()
#plt.show()

plt.imshow(img)
plt.hot()
plt.cool()
#plt.show()

image = np.random.rand(32,32)
plt.subplot(2,2,1)
plt.imshow(image)
plt.jet()

plt.subplot(2,2,2)
plt.imshow(image)
plt.gray()

plt.subplot(2,2,3)
plt.imshow(image)
plt.hot()

plt.subplot(2,2,4)
plt.imshow(image)
plt.cool()

plt.show()

