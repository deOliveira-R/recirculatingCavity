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

path = '../Documentation/3_results_and_discussion/figures/'
#path = ''

folder = '../energyTransport_100_sym/postProcessing/'
file = 'fluidRegionSingleGraphAA/fluidRegion/50/line_mag(U)_p_T_mag(UA)_pA_TA_UErrorAbsolute_pErrorAbsolute_TErrorAbsolute.xy'
scalar = pd.read_csv(folder + file, sep='\t', header=None, names=['x', 'mag(U)', 'p', 'T', 'mag(UA)', 'pA', 'TA', 'UError', 'pError', 'TError'])
scalar['UError'] = scalar['UError']/scalar['mag(UA)']*100
scalar['pError'] = scalar['pError']/scalar['pA']*100
scalar['TError'] = scalar['TError']/scalar['TA']*100
scalar = scalar.set_index('x')

velocity = pd.DataFrame(scalar[['mag(U)', 'mag(UA)', 'UError']])
velocity.columns = ['numerical', 'analytical', 'error']

vel = velocity.plot(secondary_y=['error'], style=['-', '-', '--'], figsize=figsize(0.7))
vel.set(xlabel='x ($ m $)',
        ylabel='Velocity ($ \mathrm{m} \cdot \mathrm{s}^{-1} $) magnitude')
vel.right_ax.set(ylabel='Relative error (\%)',
                 ylim=(0, 0.02))
vel.grid(axis='x')
savefig(path + 'velocity_mag')


pressure = pd.DataFrame(scalar[['p', 'pA', 'pError']])
pressure.columns = ['numerical', 'analytical', 'error']

pres = pressure.plot(secondary_y=['error'], style=['-', '-', '--'], figsize=figsize(0.7))
pres.set(xlabel='x ($ m $)',
         ylabel='Pressure ($ \mathrm{Pa} $)')
pres.right_ax.set(ylabel='Relative error (\%)',
                  ylim=(0, 0.0002))
pres.grid(axis='x')
savefig(path + 'pressure')

temperature = pd.DataFrame(scalar[['T', 'TA', 'TError']])
temperature.columns = ['numerical', 'analytical', 'error']

temp = temperature.plot(secondary_y=['error'], style=['-', '-', '--'], figsize=figsize(0.7))
temp.set(xlabel='x ($ m $)',
             ylabel='Temperature ($ \mathrm{K} $)')
temp.right_ax.set(ylabel='Relative error (\%)',
                  ylim=(0, 0.02))
temp.grid(axis='x')
savefig(path + 'temperature')


#file = 'fluidRegionSingleGraphAA/fluidRegion/50/line_U_UA.xy'
#
#vector = pd.read_csv(folder + file, sep='\t', header=None, names=['x', 'Ux', 'Uy', 'Uz', 'UAx', 'UAy', 'UAz'])
#vector = vector.set_index('x')
#velocity = vector[['Uy', 'UAy']].plot(figsize=figsize(0.7))
#velocity.set(xlabel='x ($m$)',
#             ylabel='Velocity ($m \cdot s^{-1}$) y')
#savefig(path + 'velocity_y')


file = 'neutroRegionSingleGraphAA/neutroRegion/50/line_flux0_flux0A_flux0ErrorAbsolute.xy'
scalar = pd.read_csv(folder + file, sep='\t', header=None, names=['x', 'flux0', 'flux0A', 'flux0Error'])
print(scalar)
scalar['flux0Error'] = scalar['flux0Error']/scalar['flux0A']*100
scalar = scalar.set_index('x')

print(scalar)

flux = pd.DataFrame(scalar[['flux0', 'flux0A', 'flux0Error']])
flux.columns = ['numerical', 'analytical', 'error']
flu = flux.plot(secondary_y=['error'], style=['-', '-', '--'], figsize=figsize(0.7))
flu.set(xlabel='x ($ m $)',
        ylabel='Flux ($ \mathrm{m}^{-2} \cdot \mathrm{s}^{-1} $)')
flu.right_ax.set(ylabel='Relative error (\%)',
                 ylim=(0, 0.02))
flu.grid(axis='x')
savefig(path + 'flux0')



#for file, title in zip(parameters['file'], parameters['title']):
#    #read them into pandas
#    norms_list = [pd.read_csv("../energyTransport" + "_{}/".format(mesh) + "norms{}.dat".format(file), sep=';') for mesh in meshes]
#    #concatenate them together
#    norms[parameter] = pd.concat(norms_list, ignore_index=False)
#    # use grid spacing to reindex
#    norms[parameter].index = spacing
#    norms[parameter].index.name = "Grid refinement"
#    print(norms[parameter])
#    norms[parameter][show].plot(marker='o', title="{} norms".format(title), figsize=figsize(0.5))
#    savefig(path + 'norms{}'.format(file))

