import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

N = 32
t = np.arange(N)
x = np.sin(2 * np.pi / N * t)
plt.plot(t,x,"x")
#plt.show()
plt.clf()

from scipy.fftpack import fft, ifft

X = fft(x)
print(X)
plt.plot(np.abs(X), "bo-")
plt.plot(np.real(X),"go-")
plt.plot(np.imag(X),"ro-")
#plt.show()
plt.clf()

f = 2
x = np.sin(2 * np.pi / N * f * t)
plt.plot(t, x,"x")
#plt.show()
plt.clf()

X = fft(x)
print(X)
plt.plot(np.abs(X), "bo-")
plt.plot(np.real(X),"go-")
plt.plot(np.imag(X),"ro-")
#plt.show()
plt.clf()

f0 = 1
f1 = 3
x = 0.3 * np.sin(2 * np.pi / N * f0 * t) + 0.7 * np.sin(2 * np.pi / N * f1 *t)
plt.plot(t,x,"x")
#plt.show()
plt.clf()
