import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
from pickle_shortcuts import *
from params import plotting_params as params

frbs, emb = pload("tsne_output.pickle")
data = pload("trimmed_data.pickle")
start_and_stop = pload("start_and_stop.pickle")

if params['dark_mode']:
    plt.style.use('dark_background')

fig, (ax1, ax2) = plt.subplots(nrows=2)

ax1.set_xticks([])
ax1.set_yticks([])

ax1.set_title('t-SNE output space')

# Set each FRB's color
if params['color_by'] == 'groups':
    cmap = 'RdBu'
    color = [int(frb in params['blue_group']) for frb in frbs]
else:
    cmap = params['cmap']
    
    if params['color_by'] == 'flux':
        peaks = pload("peaks.pickle")
        color = [peaks[frb] for frb in frbs]
        
    if params['max_color']:
        color = np.minimum(color, params['max_color'])
    
# Plot the 2D embedding
sc = ax1.scatter(emb[:, 0], emb[:, 1],
                 s=params['radius'],
                 c=color,
                 cmap=cmap)
                 
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
    
    text = frb + '\n'
    if params['color_by'] == 'flux':
        text += str(peaks[frb]) + ' Jy'
    
    annot.set_text(text)
    
def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax1:
        cont, ind = sc.contains(event)
        if cont:
            ind = ind['ind'][0] # Index of the mouseovered FRB.
            
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

if params['color_by'] != 'groups':
    fig.colorbar(sc,
                 ax=ax1,
                 orientation=params['cbar_orientation']
    )

plt.show()
