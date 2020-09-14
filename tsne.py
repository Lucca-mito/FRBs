import os
import numpy as np
from sklearn.manifold import TSNE
from pickle_shortcuts import *
from params import tsne_params as params

frbs, ft = pload("fourier_output.pickle")

emb = TSNE(n_components = params['n_components'],
           verbose      = params['verbose'],
           perplexity   = params['perplexity'],
           random_state = params['random_state'],
           n_iter       = params['n_iter']
      ).fit_transform(ft)

pdump((frbs, emb), "tsne_output.pickle")
