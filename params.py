fourier_params = {
    'lpf'             : 0,    # Strength of the low-pass filter,
                              # i.e. how many high-frequency waves to
                              # remove.

    'square_the_norms': True, # Whether the components of the vectors are
                              # the norms of the Fourier coefficients or
                              # the squared norms.
}

tsne_params = {
    'n_components': 2,  # Dimension of the output space

    'perplexity'  : 5,  # Big = focus on the big picture.
                        # Small = focus on making tiny clusters.
                       
    'random_state': 10, # For reproducibility (best: 10)
    
    'verbose'     : 2,

    'n_iter'      : 15000,
}

plotting_params = {
    'radius'    : 50,
    
    'color_by'  : 'groups', # 'groups'     : FRBs are colored blue if in
                            #                'blue_group' param, and red
                            #                otherwise.
                            #
                            # 'flux'       : FRBs are colored by peak
                            #                flux using 'cmap' param.
    
    'cmap'      : 'RdBu_r', # Ignored if 'color_by' is 'groups'.
    
    'max_color' : 3,        # If not None (and 'color_by' is not 'groups'),
                            # sets an upper bound for the colormap and
                            # colorbar.
    
    'blue_group': [
        'FRB010125', 'FRB010621', 'FRB110220', 'FRB130729', 'FRB131104',
        'FRB151206', 'FRB151230'
    ],
    
}
