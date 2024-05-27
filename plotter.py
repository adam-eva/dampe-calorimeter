import matplotlib.pyplot as plt
import numpy as np

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
