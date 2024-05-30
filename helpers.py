import os
import json
import numpy as np
import matplotlib.pyplot as plt

DATA_FOLDER= './models/' 

def get_data_dict():
    """Get the data and order in a dictionary"""
    dampe_data = {}
    calorimeter_images, calorimeter_data, data_target, benchmark_data = get_input_data()

    dampe_data['images'] = calorimeter_images
    dampe_data['calorimeter_data'] = calorimeter_data
    dampe_data['data_target'] = data_target
    dampe_data['benchmark_data'] = benchmark_data
    
    return dampe_data

#####################################################################################

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

#####################################################################################

def save_model_history(history, filename='history'):
    """Save the fiting history to a json format"""
    if not os.path.isdir(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)
    with open(DATA_FOLDER+filename+'.json', 'w') as ff:
        json.dump(history.history, ff)


def load_model_history(filename):
    """Load the fiting history from the json file"""
    with open(filename,'r') as ff:
        history = json.load(ff)
        
    return history

