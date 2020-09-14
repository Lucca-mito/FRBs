fourier_params = {
    'lpf'             : 0,    # Strength of the low-pass filter,
                              # i.e. how many high-frequency waves to remove

    'square_the_norms': True, # Whether the components of the vectors are
                              # the norms of the Fourier coefficients or the
                              # squared norms.
}

tsne_params = {
    'n_components': 2, # Dimension of the output space

    'perplexity'  : 5, # Big = focus on the big picture,
                       # small = focus on making tiny clusters
                       
    'random_state': 10, # For reproducibility (best: 10)
    
    'verbose'     : 2,

    'n_iter'      : 15000,
}

plotting_params = {
    'radius'  : 30,
    'cmap'    : 'viridis',
}
