import os
import numpy as np
import matplotlib.pyplot as plt
from pickle_shortcuts import *
from params import fourier_params as params
                
start_and_stop = {} # Maps FRB names to:
                    # 0. Start time
                    # 1. Stop time

data = {}           # Maps FRB names to:
                    # 0. Time data (x)
                    # 1. Signal data (fx)

n = 1               # Largest number of sample points across all FRBs.
                    # Used for all FFTs; bursts with fewer sample
                    # points are zero-padded until they have n_max
                    # sample points.

zero_pad = True     # Debug variable

with open("start_and_stop.csv") as fp:
    for line in fp.readlines():
        frb, start, stop = line.split(',')
        
        start = float(start)
        stop = float(stop)
        
        start_and_stop[frb] = (start, stop)
        
    pdump(start_and_stop, "start_and_stop.pickle")

peaks = {}
for filename in os.listdir('data'):
    if not filename.endswith('.txt'): continue
    frb = filename[:-4]
    
    with open('data/'+filename) as fp:
        x = []
        fx = []
        
        lines = [line.split() for line in fp.readlines()]
        dx = float(lines[1][0]) - float(lines[0][0])
        
        start, stop = start_and_stop[frb]
        
        for time, flux in lines:
            time = float(time)
            if start < time < stop:
                x.append(time)
                fx.append(float(flux))
        
        n = max(n, len(x))
        
        peak = max(fx)
        peaks[frb] = peak
        data[frb] = (x, fx)
        
pdump(data, "trimmed_data.pickle")
pdump(peaks, "peaks.pickle")
        
fourier_output = []
for frb, (x, fx) in data.items():
    # First, zero-pad any bursts with fewer than n sample points.
    stop = x[-1]
    if zero_pad:
        while len(x) < n:
            stop += dx
            x.append(stop)
            fx.append(0)
    
    fx = [fx / peaks[frb] for fx in fx] # Normalize bursts by peak flux.
    
    Fk = np.fft.fft(fx) / len(x) # Fourier coefficients (divided by n).
                                 # It's probably not necessary to divide
                                 # by n since all bursts are forced to
                                 # have the same number of sample points,
                                 # but whatever.
    
    nu = np.fft.fftfreq(len(x), dx) # Natural frequencies
    Fk = np.fft.fftshift(Fk)        # Shift zero freq to center
    nu = np.fft.fftshift(nu)        # Shift zero freq to center
    
    # Apply the low-pass filter
    lpf = params['lpf']
    if lpf:
        Fk = Fk[:n-lpf][lpf:]
        nu = nu[:n-lpf][lpf:]

    ft = np.absolute(Fk) # Spectral power
    if params['square_the_norms']: ft **= 2
    fourier_output.append(ft)
    
#    fig, ax = plt.subplots()
#    fig.suptitle(frb)
#    ax.plot(nu, ft)

frbs = list(data.keys())
pdump((frbs, fourier_output), "fourier_output.pickle")

plt.show()
