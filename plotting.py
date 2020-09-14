import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
from pickle_shortcuts import *
from params import plotting_params as params

frbs, emb = pload("tsne_output.pickle")
data = pload("trimmed_data.pickle")
start_and_stop = pload("start_and_stop.pickle")
peaks = pload("peaks.pickle")

fig, (ax1, ax2) = plt.subplots(nrows=2)

ax1.set_xticks([])
ax1.set_yticks([])

ax1.set_title('FRB output space')

#durations_list = [ for frb in frbs]
    
sc = ax1.scatter(emb[:, 0], emb[:, 1],
                 s=params['radius'],
                 c=[min(peaks[frb], 3) for frb in frbs],
                 cmap=params['cmap'])
                 
annot = ax1.annotate('', xy=(0, 0), xytext=(20, 20),
                     textcoords='offset points',
                     bbox=dict(boxstyle='round', fc='w'),
                     arrowprops=dict(arrowstyle='->'))

annot.set_visible(False)

def draw_lightcurve(frb):
    ax2.clear()
    time_data, flux_data = data[frb]
    ax2.plot(time_data, flux_data)

def update_annot(ind):
    pos = sc.get_offsets()[ind]
    annot.xy = pos
    
    frb = frbs[ind]
    text = frb + '\n' + str(peaks[frb])
    annot.set_text(text)
    
def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax1:
        cont, ind = sc.contains(event)
        if cont:
            ind = ind['ind'][0] # Index of the mouseovered FRB.
                                # Hopefully, no two FRBs end up
                                # in the same spot.
            update_annot(ind)
            annot.set_visible(True)
            
            draw_lightcurve(frbs[ind])
            
            ax2.set_title('Light curve of ' + frbs[ind])
            
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', hover)

fig.colorbar(sc, ax=ax1)

plt.show()
