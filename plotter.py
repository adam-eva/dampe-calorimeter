import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import colors
import numpy as np

from helpers import benchmarked_error

figpath = './figures/'
colors  = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2',
'#7f7f7f', '#bcbd22', '#17becf']
fs = 15

############################################################################################	

def plot_image(image, loglevel=False, savefig=False,figname=None,image_name=None):
    """Plot particle image"""
    fig, ax = plt.subplots(figsize=(12,7), ncols=1)
    if loglevel:
        im = ax.imshow(image, cmap='Blues')
    else:
        im = ax.imshow(image, cmap='Blues')
    fig.colorbar(im, ax=ax, shrink=0.8)

    plt.xlabel('X, Y [BGO bars]', fontsize=fs)
    plt.ylabel('Z [BGO layers]', fontsize=fs)
    plt.xticks(np.arange(0, 22, int(1)))
    plt.yticks(np.arange(0, 14, int(1)))
    plt.grid()

    if image_name:
        ax.set_title(image_name)
    if savefig:
        plt.savefig(figpath+'/dampe_'+figname+'.png')
    else:
        plt.show()
    
    return fig, ax

############################################################################################	

def plot_model_history(models, metrics=['mean_squared_error'], loglevel = False, savefig=False, figname=None, label_str=None, bme = None):
    """Plot loss of the model VS epoch"""
    if not isinstance(models, list):
        models = [models]
    
    fig = plt.figure(figsize=(12,7)) 
    
    if loglevel == True:
        plt.yscale('log')
    
    for col_idx, history in enumerate(models): 
        for loss in metrics: 
            plt.plot(
            history[loss],
            label = loss+label_str[col_idx],
            color=colors[col_idx]
            )
            plt.plot(
            history['val_'+loss],
            label = 'val_'+loss+label_str[col_idx],
            color=colors[col_idx],
            linestyle='dashed'
            )
    if bme:
        plt.plot(
        len(history[loss])-1,
        bme,
        label='benchmarked MSE',
        marker='D',
        markersize=20,
        color=colors[col_idx+1]
        ) 
    
    # Force integer x axis  
    ax = fig.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    plt.xlabel('Epoch',fontsize=fs)
    plt.ylabel('Metrics',fontsize=fs)
    plt.legend(loc='best',fontsize=fs)
    plt.grid()
    
    if savefig:
        if not os.path.isdir(figpath):
            os.mkdir(figpath)
        if figname == None: 
            figname = 'model_history'
        plt.savefig(figpath+'dampe_'+figname+'.png')
    else:
        plt.show()

    return fig


def plot_split_distribution(dampe_data, train, val, test, figname=None):
    """Bar plot for split of the data distribution"""
    plt.figure(figsize=(12,7))
    sample_size = dampe_data['images'].shape[0]
    try:
        plt.bar(
        ['train', 'validation', 'test'],
        [train.shape[0] / sample_size, val.shape[0] / sample_size, test.shape[0] / sample_size],
        width=0.1,
        color='gray'
        )
    except: 
        plt.bar(
        ['train', 'validation'],
        [xy_train.shape[0] / sample_size, xy_val.shape[0] / sample_size],
        width=0.1,
        color='gray'
        )

    plt.ylabel('Ratio')

    if figname:
        plt.savefig(figpath+figname)
    else:
        plt.show()

def plot_energy(dampe_data, loglevel=False, figname=None):
    """Energy distribution"""

    plt.figure(figsize=(12,7))

    plt.plot(
    dampe_data['calorimeter_data'][:,0],
    color=colors[2],
    label='Total Energy'
    )
    plt.plot(
    dampe_data['calorimeter_data'][:,1],
    color=colors[3],
    label='Max Energy'
    )
    
    if loglevel == True:
        plt.yscale('log')
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    plt.xlabel('image index',fontsize=fs)
    plt.ylabel('Energy [MeV]',fontsize=fs)
    plt.legend(loc='best',fontsize=fs)
    plt.grid()

    if figname:
        plt.savefig(figpath+figname)
    else:
        plt.show()
    

