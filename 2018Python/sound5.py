# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

ifname = 'HAL0002noiseColored.wav'   # 入力ファイル名
o1fname = 'HAL0002noiseColored2.wav'         # 出力ファイル名


def LowPass( x, f, Fs=44100. ):
    N = len(x)
    fdelta = float(Fs)/N
    X = spf.fft( x )
    Ncut = int(f/fdelta)  # カットオフ周波数対応添字
    flt = np.zeros(N)
    flt[0:Ncut] = 1
    flt[-Ncut+1:] = 1

    xflt = spf.ifft( X * flt ) # フィルタ処理
    return xflt.real # 実部だけを返す


y = read( ifname )

Fs = y[0]          # サンプリングレート
Nmax = 262144       # FFT のため 2 のベキにしておく
yl = y[1][:Nmax] # 左音声の 0〜Nmax-1 までを信号とする
fc = 4000# 500Hz で遮断してみる

yflt = LowPass( yl, fc, Fs )

write(o1fname, Fs, 30*np.int16( np.real(yflt) ).reshape(Nmax) ) 

class ShowWav(object):
    def __init__( self, fname ):
        self.fname = fname
        y = read( fname )
        Fs = y[0]
        self.ydat = y[1]
        self.Nmax = self.ydat.shape[0]
        if( self.ydat.ndim > 1 ):
            self.channel = self.ydat.shape[1]
        else:
            self.channel = 1
            self.ydat = self.ydat.reshape( (self.Nmax, 1) )
        self.Nmax = int(pow(2, int(np.log2(self.Nmax)) )) # FFT の為，2のベキに調整
        self.delta = 1./Fs
        self.fdelta = 1./(self.Nmax*self.delta)
        self.t = np.arange( self.Nmax ) * self.delta
        self.f = np.arange(-self.Nmax/2, self.Nmax/2) * self.fdelta


    def plot( self ):
        for k in range( self.channel ):
            plt.subplot( 2, self.channel, 2*k+1 )
            plt.plot( self.t, self.ydat[:self.Nmax, k] )
            plt.xlim( 0, self.t[-1] )
            plt.title( 'Amplitude Ch.%d' % k )
            plt.grid()

            Y = spf.fft( self.ydat[:self.Nmax, k] )
            plt.subplot( 2, self.channel, 2*k+2 )
            plt.xlim( self.f[0], self.f[-1] )
            plt.semilogy( self.f, np.abs(spf.fftshift(Y)) )
            plt.title( 'Power Ch.%d' % k )
            plt.grid()

        plt.show()


y = read( o1fname )
s = ShowWav( o1fname )
s.plot()
