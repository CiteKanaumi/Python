# -*- coding: utf-8 -*-

import numpy as np
from scipy.io.wavfile import write

def GenFreq(Fc, Fs, dur):
    x1 = ()
    i = 0
    for k in Fc:
        Amp = 4000
        delta = 1./Fs
        Nmax = Fs * dur
        t = np.arange(i*Nmax, (i+1)*Nmax) * delta
        i+=1
        x = Amp * np.sin(2. * np.pi * k * t)
        x1 = np.hstack((x1, x))
    return x1


# 以下に GenFreq を用いて "CDEFGAB" の音階を各 dur 秒間
# 生成するスクリプトコードを書く

Fs = 22100.        # サンプリング周波数
Fcs = (262, 294, 330, 349, 392, 440, 494, 523)

y = GenFreq(Fcs, Fs, 3)
Fs = int(Fs)

# y に音声波形を入れたものとしてファイルを保存
fname = 'MkSnd4Test.wav'
write(fname, Fs, y)
