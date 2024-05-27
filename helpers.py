import numpy as np
import matplotlib.pyplot as plt

def split_xy_intercept(image):
    """Split the image in two images.
       x_image with x intercept
       y_image with y intercept"""

    if image.shape[0] == 1:
        try:
            x_projection = image[::2 ,:,:]
            y_projection = image[1::2,:,:]
        except:
            x_projection = image[::2 ,:]
            y_projection = image[1::2,:]
    else:
        try:
            x_projection = image[:,::2 ,:,:]
            y_projection = image[:,1::2,:,:]
        except:
            x_projection = image[:,::2 ,:]
            y_projection = image[:,1::2,:]

    return x_projection, y_projection
