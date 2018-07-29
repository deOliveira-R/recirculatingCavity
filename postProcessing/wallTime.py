# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.optimize import curve_fit
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
    
path = '../Documentation/3_results_and_discussion/figures/'
#path = ''

run = {'mesh': np.array([25, 50, 100, 200]),
       'wall time': np.array([43, 48, 180, 1946])}

# x = np.linspace(0, 500, 5)

wallTime = pd.DataFrame(run)
wallTime.set_index('mesh', inplace=True)

ax = wallTime.plot(legend=False, marker='o', figsize=figsize(0.7))
ax.set(xlabel='Mesh size',
       ylabel='Wall time (s)')
savefig(path + 'wallTime')
