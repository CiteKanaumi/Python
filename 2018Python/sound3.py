# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
from scipy.io.wavfile import write

import matplotlib.pylab as plt

class SoundObj( object ):
    
    def __init__( self, Fs, dur ):
        self.Fcs = {'C':262., 'D':294., 'E':330., 'F':349., 'G':392., 'A':440., 'B':494.}
        self.Amp = 2000

        self.Fs = Fs
        self.dur = dur
        self.N = int( dur * Fs )
        self.x = np.zeros( self.N )

        delta = 1./Fs
        self.t = np.arange( self.N ) * delta

    def getSound( self ):
        return self.x

    def getLen( self ):
        return self.N

    def setTone( self, code='C' ):
        f = self.Fcs[code]
        self.x = self.Amp * np.sin( 2. * np.pi * f * self.t )




Fs = 22100.
dur = 1.0

fname = 'OOPmksnd.wav' 

s = SoundObj( Fs, dur )
s.setTone( 'E' )


write( fname, Fs, np.int16( s.getSound() ).reshape( s.getLen(), 1 ) )
