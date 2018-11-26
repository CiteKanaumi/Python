# -*- coding: utf-8 -*-

import numpy as np
from scipy.io.wavfile import write


class GenFreq(object):
    def __init__(self, Fs=44100., dur=1.):
        # 諸々の初期化
        self.fs = Fs
        pass

    def getSound(self):
        # 波形データ配列を返す
        return self.tone

    def getLen(self):
        # データ配列長を返す
        pass

    def addTone(self, code='C'):
        # おとを重ねる
        x1 = ()
        if code ==  "C":
            self.fc = 262
            i = 0
        elif code == "E":
            self.fc = 330
            i = 1
        elif code == "G":
            self.fc = 392
            i = 2
        Amp = 4000
        delta = 1./self.fs
        Nmax = self.fs * 3
        t = np.arange(i*Nmax, (i+1)*Nmax) * delta
        x = Amp * np.sin(2. * np.pi * self.fc * t)
        x1 = np.hstack((x1, x))
        self.tone = x1
        pass


# ここからテストコード
# ド・ミ・ソの和音(CEG) を作ってみる

Fs = 44100
s = GenFreq(Fs, dur=1.)
s.addTone('C')
s.addTone('E')
s.addTone('G')
N = s.getLen()

# scipy.wav.iofile の write をインポートしておくこと
write('hogehoge.wav', Fs, s.getSound())
