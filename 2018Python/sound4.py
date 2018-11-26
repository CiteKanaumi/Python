# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf
from scipy.io.wavfile import read
import matplotlib.pyplot as plt


def PlotFunc( x ):
    N = len(x)
    t = np.arange(N)
    plt.subplot( 2, 1, 1 )
    plt.plot( t, x )
    plt.title( 'Signal' )
    plt.xlim( 0, N )
    plt.grid()

    X = spf.fft( x )
    f = np.arange(N) - N/2
    plt.subplot( 2, 1, 2 )
    plt.semilogy( f, np.abs( spf.fftshift(X) ) )
    plt.title( 'Power' )
    plt.xlim( -N/2, N/2 )
    plt.grid()


def LowPass( x, f = 10 ):
    N = len(x)
    X = spf.fft( x )
    flt = np.zeros( N )
    flt[0:f] = 1          # 0:f までの信号 と -f+1: の信号が
    flt[-f+1:] = 1        # 対応する低周波なので 1 を掛けるようにする．残りの成分は 0 を掛けるようにする
    Xflt = X * flt        # 原信号に周波数成分の重みを書けてやる

    return spf.ifft( Xflt ).real

    
N = 128
delta = 1./N
t = np.arange( N ) * delta

f1 = 8
f2 = 15
x = np.sin( 2 * np.pi * f1 * t ) + np.cos( 2 * np.pi * f2 * t )

# とりあえず表示させてみる
plt.figure()
PlotFunc( x )
plt.show()


xflt = LowPass( x, 10 )

# 新しい図を作って表示させる
plt.figure()
PlotFunc( xflt )
plt.show()
