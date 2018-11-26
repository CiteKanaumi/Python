# -*- coding: utf-8 -*-

import numpy as np
import scipy.fftpack as spf

from scipy.io.wavfile import write
import matplotlib.pylab as plt

# 設定
Fs = 22050.  # サンプリング周波数 22 KHz
Fc = 1000.   # 1000Hz(とりあえず)
fname = 'Sin1KHz.wav'
dur = 5.     # 5 秒くらいのデータを作ってみる
Amp = 4000.  # 振幅 (とりあえず)


delta = 1./Fs  # サンプリング間隔
Nmax = Fs * dur   # サンプル点の数

t = np.arange(Nmax) * delta
x = Amp * np.sin(2. * np.pi * Fc * t)


# 確認用

X = spf.fft(x)
fdelta = 1./(Nmax*delta)
f = np.arange(Nmax) * fdelta

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t[:100], x[:100])
plt.grid()

plt.subplot(2, 1, 2)
plt.semilogy(f, np.abs(X))
plt.grid()

plt.show()

# 確認ここまで

# モノラルでファイルに書き込んでみる
write(fname, int(Fs), x)
