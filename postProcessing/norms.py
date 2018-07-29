# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib as mpl
mpl.use('pgf')

def figsize(scale):
    fig_width_pt = 417.68646                        # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width,fig_height]
    return fig_size

pgf_with_latex = {                      # setup matplotlib to use latex for output
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "font.size": 10,
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "legend.fontsize": 8,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
#    "font.size": 20,
#    "axes.labelsize": 20,               # LaTeX default is 10pt font.
#    "legend.fontsize": 16,               # Make the legend/label fonts a little smaller
#    "xtick.labelsize": 16,
#    "ytick.labelsize": 16,
    "figure.figsize": figsize(0.9),     # default fig size of 0.9 textwidth
#    "pgf.texsystem": "lualatex",        # change this if using xetex or luatex
    "pgf.preamble": [
    r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
    r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
    ]
}
mpl.rcParams.update(pgf_with_latex)

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()

def savefig(filename):
    plt.savefig('{}.pgf'.format(filename), bbox_inches='tight')
    plt.savefig('{}.pdf'.format(filename), bbox_inches='tight')

meshes = np.array([25, 50, 100, 200])
spacing = meshes/meshes[0]
parameters = {'file': ['U', 'p', 'T', 'flux'],
              'title': ['Velocity', 'Pressure', 'Temperature', 'Flux']
              }

norms = {}
show = ['L1','L2']
path = '../Documentation/3_results_and_discussion/figures/'
#path = ''

for file, title in zip(parameters['file'], parameters['title']):
    # Read norm files into a list of dataframes
    norms_list = [pd.read_csv("../energyTransport" + "_{}/".format(mesh) + "norms{}.dat".format(file), sep=';') for mesh in meshes]
    # Concatenate the dataframes into one
    norms[file] = pd.concat(norms_list, ignore_index=False)
    norms[file]['mesh'] = meshes
    norms[file].set_index('mesh', inplace=True)
    # Add an Order of accuracy column and calculate from L2 norm
    norms[file]['OoA'] = np.nan
    for i in range(len(norms[file])):
        print()
        if i is 0:
            continue
        else:
            ratio = norms[file]['L2'].iloc[i-1]/norms[file]['L2'].iloc[i]
            refinement = norms[file].index.values[i] / norms[file].index.values[i-1]
            norms[file]['OoA'].iloc[i] = np.log(ratio)/np.log(refinement)
    
    print(norms[file])
    norm = norms[file][show].plot(marker='o', figsize=figsize(0.7))
    norm.set(xlabel='Mesh size',
             ylabel=title + ' ($ \mathrm{m} \cdot \mathrm{s}^{-1} $)' + ' norm')
    savefig(path + 'norms{}'.format(file))

