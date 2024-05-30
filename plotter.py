import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

figpath = './figures/'
colors  = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2',
'#7f7f7f', '#bcbd22', '#17becf']

############################################################################################	

def plot_image(image, savefig=False,figname=None,image_name=None):
    """Plot particle image"""
    fig, ax = plt.subplots(figsize=(9,7), ncols=1)
    im = ax.imshow(image, cmap='hot')
    fig.colorbar(im, ax=ax, shrink=0.7)
    if image_name:
        ax.set_title(image_name)
    if savefig:
        plt.savefig('./figures/dampe_'+figname+'.png')
    else:
        plt.show()
    
    return fig, ax

############################################################################################	

def plot_model_history(models, metrics=['mean_squared_error'], loglevel = False, savefig=False, figname=None):
    """Plot loss of the model VS epoch"""
    if not isinstance(models, list):
        models = [models]
    
    fig = plt.figure(figsize=(7,5)) 
    
    if loglevel == True:
        plt.yscale('log')
    
    for col_idx, history in enumerate(models): 
        for loss in metrics: 
            plt.plot(
            history[loss],
            label = loss,
            color=colors[col_idx]
            )
            plt.plot(
            history['val_'+loss],
            label = 'val_'+loss,
            color=colors[col_idx],
            linestyle='dashed'
            )
    
    # Force integer x axis  
    ax = fig.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    plt.xlabel('Epoch')
    plt.ylabel('Metrics')
    plt.legend(loc='best')
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
