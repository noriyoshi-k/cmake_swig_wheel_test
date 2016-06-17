# coding:utf-8

import pyaudio
from numpy import *
from scikits.audiolab import Sndfile,Format

def _main():
    outwav = Sndfile("test.flac",'w',
                   Format("flac"),
                   1, 16000)
    p = pyaudio.PyAudio()
    input_stream  = p.open(format=pyaudio.paInt16,
                           channels=1,
                           rate=16000,
                           input=True)
    x=zeros(320,dtype=int16)
    N=16000*5;n=0
    while n<N:
        x[:]=fromstring(input_stream.read(x.shape[0]),dtype=int16)
        n+=x.shape[0]
        outwav.write_frames(x)
    input_stream.close()
    p.terminate()
    outwav.close()
    return

if __name__ == "__main__" : _main()
