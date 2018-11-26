import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

N = 16
t = np.arange(N)
f = 1
x = np.cos(2*np.pi / N*f*t)
#plt.plot(t,x)
#plt.grid()
#plt.xlabel("t")
#plt.ylabel("x")
#plt.show() t-x cos-graph

X = fft(x) #xのふーりえ変換
plt.plot(np.abs(X), "bo-") #平均 power spectrum
plt.plot(np.real(X), "go-") #実部
plt.plot(np.imag(X), "ro-") #虚部
plt.grid()
plt.show() 結果 平均=実部
