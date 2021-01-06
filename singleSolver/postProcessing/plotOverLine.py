# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
standard = True

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
    "figure.figsize": figsize(0.8),     # default fig size of 0.9 textwidth
#    "pgf.texsystem": "lualatex",        # change this if using xetex or luatex
    "pgf.preamble": [
    r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts
    r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
    ]
}
mpl.rcParams.update(pgf_with_latex)

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


if standard:
    sns.set()

    def savefig(filename):
        plt.savefig('{}.pgf'.format(filename), bbox_inches='tight')
        plt.savefig('{}.pdf'.format(filename), bbox_inches='tight')
else:
    sns.set(rc={'axes.facecolor':'#bbbbbb', 'figure.facecolor':'#bbbbbb'})

    def savefig(filename):
        plt.savefig('{}.pgf'.format(filename), bbox_inches='tight', transparent=True)
        plt.savefig('{}.pdf'.format(filename), bbox_inches='tight', transparent=True)


def plot_scalar_old(scalar):
    ax = scalar.plot(secondary_y=['error'], style=['-', '-', '--'])
    ax.set(xlabel='x ($ \mathrm{m} $)',
           ylabel='Velocity ($ \mathrm{m} \, \mathrm{s}^{-1} $) magnitude',
           xlim=(-1.75,1.75),
           ylim=(0,1.05))
    ax.yaxis.set_ticks(np.arange(0,1.2,0.2))
    ax.right_ax.set(ylabel='Relative error (\%)',
                    ylim=(0, 0.021))
    ax.right_ax.yaxis.set_ticks(np.arange(0,0.024,0.004))
    ax.grid(axis='x')


def plot_scalar(scalar, ylabel, ylim=None, y2lim=None, y2ticks=None):
    # This plotting gymnastics replaces the code above in order to get the plot
    # of the analytical and numerical values to appear on top of grid

    # fig, vel = plt.subplots()

    ax = scalar[['numerical', 'analytical']].plot(color=['tab:green', 'tab:blue'],legend=None)

    ax_err = scalar['error'].plot(ax=ax, secondary_y=True, style='--', color='tab:red')
    ax_err.set(ylabel='Relative error (\%)')
    if hasattr(type(y2lim), '__iter__'): ax_err.set(ylim=y2lim)
    if hasattr(type(y2ticks), '__iter__'): ax_err.yaxis.set_ticks(y2ticks)
    ax_err.grid(False)

    ax.set(xlabel='x ($ \mathrm{m} $)',
           ylabel=ylabel,
           xlim=(-1.75,1.75)),
    if hasattr(type(ylim), '__iter__'): ax.set(ylim=ylim)
    ax.grid(True)

    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax_err.get_legend_handles_labels()
    plt.legend(h1+h2, l1+l2, bbox_to_anchor=(0, 1, 1, 0), loc="lower left", mode="expand", ncol=3, frameon=False)

    
#path = '../Documentation/3_results_and_discussion/figures/'
path = ''

folder = '../mesh_100/postProcessing/'

file = 'fluidDynamicsSingleGraphAA/50/line_mag(U)_p_T_mag(UA)_pA_TA_UErrorAbsolute_pErrorAbsolute_TErrorAbsolute.xy'
scalar = pd.read_csv(folder + file, sep='\t', header=None, names=['x', 'mag(U)', 'p', 'T', 'mag(UA)', 'pA', 'TA', 'UError', 'pError', 'TError'])

# Turn errors into relative values and set index
scalar['UError'] = scalar['UError']/scalar['mag(UA)']*100
scalar['pError'] = scalar['pError']/scalar['pA']*100
scalar['TError'] = scalar['TError']/scalar['TA']*100
scalar = scalar.set_index('x')

velocity = pd.DataFrame(scalar[['mag(U)', 'mag(UA)', 'UError']])
velocity.columns = ['numerical', 'analytical', 'error']

ylim = np.array([0,1.05])
plot_scalar(velocity,
            ylabel='Velocity ($ \mathrm{m} \, \mathrm{s}^{-1} $) magnitude',
            ylim=ylim,
            y2lim=ylim / 50,
            y2ticks=np.arange(0,0.024,0.004))
savefig(path + 'velocity_mag')


pressure = pd.DataFrame(scalar[['p', 'pA', 'pError']])
pressure.columns = ['numerical', 'analytical', 'error']

plot_scalar(pressure,
            ylabel='Pressure ($ \mathrm{Pa} $)',
            ylim=(1e5-10,1.005e5+10),
            y2lim=(-10/2.5e6, ((1.005e5+10)-1e5)/2.5e6),
            y2ticks=np.arange(0,2.4e-4,4e-5))
savefig(path + 'pressure')



temperature = pd.DataFrame(scalar[['T', 'TA', 'TError']])
temperature.columns = ['numerical', 'analytical', 'error']

plot_scalar(temperature,
            ylabel='Temperature ($ \mathrm{K} $)',
            ylim=(1e3-3,1.1e3+3),
            y2lim=(-3/5e3, ((1.1e3+3)-1e3)/5e3),
            y2ticks=np.arange(0,2.4e-2,4e-3))
savefig(path + 'temperature')


#file = 'fluidRegionSingleGraphAA/fluidRegion/50/line_U_UA.xy'
#
#vector = pd.read_csv(folder + file, sep='\t', header=None, names=['x', 'Ux', 'Uy', 'Uz', 'UAx', 'UAy', 'UAz'])
#vector = vector.set_index('x')
#velocity = vector[['Uy', 'UAy']].plot()
#velocity.set(xlabel='x ($m$)',
#             ylabel='Velocity ($m \cdot s^{-1}$) y')
#savefig(path + 'velocity_y')


file = 'neutronTransportSingleGraphAA/50/line_flux0_flux0A_flux0ErrorAbsolute.xy'
scalar = pd.read_csv(folder + file, sep='\t', header=None, names=['x', 'flux0', 'flux0A', 'flux0Error'])
#print(scalar)
scalar['flux0Error'] = scalar['flux0Error']/scalar['flux0A']*100
scalar = scalar.set_index('x')
#print(scalar)

flux = pd.DataFrame(scalar[['flux0', 'flux0A', 'flux0Error']])
flux.columns = ['numerical', 'analytical', 'error']

plot_scalar(flux,
            ylabel='Flux ($ \mathrm{m}^{-2} \, \mathrm{s}^{-1} $)',
            ylim=(0-4e2,1e4+4e2),
            y2lim=(-4e2/5e5, (1e4+4e2)/5e5),
            y2ticks=np.arange(0,2.4e-2,4e-3))
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

