# -*- coding: utf-8 -*-

import numpy as np


def SpecGram(x):
    # 時系列 x のスペクトログラムを表示する関数
    pass




# 以下に SpecGram() を用いてスペクトログラムを表示させる
# スクリプトコードを書く

fname = 'KykoSampling.wav'
y = read(fname)

if len(y[1].shape) > 1:    # ステレオ音声の場合，左音声を使う
    yl = y[1][:0]
else:
    yl = y[1]

# スペクトログラム表示
SpecGram(yl)
