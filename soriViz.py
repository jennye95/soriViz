import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import sys
import time


"""
AudioStream for streaming data from a microphone in realtime

pyaudio -> for capturing the audio sound
struct  -> for coverting the binary data into ints
matplotlib -> for displaying the data 

scipy.fftpack -> for computing the FFT


"""


class AudioStream(object):
    def __init__(self):


        # stream constants

        self.CHUNK = 1024 * 2
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.pause = False

        # stream object
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                output=True,
                frames_per_buffer=self.CHUNK,
                )
        self.init_plots()
        self.start_plot()

   # def init_plots(self):


