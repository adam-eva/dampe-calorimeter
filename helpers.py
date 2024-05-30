import pdb
import os
import json
import numpy as np
import matplotlib.pyplot as plt

from utils import get_input_data

DATA_FOLDER= './models/' 

def get_data_dict():
    """Get the data and order in a dictionary"""
    dampe_data = {}
    calorimeter_images, calorimeter_data, data_target, benchmark_data = get_input_data()
    
    # Sower images
    dampe_data['images'] = calorimeter_images / 255. 
    # [Total energy, max pixel energy]
    dampe_data['calorimeter_data'] = calorimeter_data
    # [x_bot, x_top, y_bot, y_top] Real values (from the simulation)
    dampe_data['data_target'] = data_target
    # [x_bot, x_top, y_bot, y_top] Standart fitting reconstruction 
    dampe_data['benchmark_data'] = benchmark_data     

    return dampe_data


def sort_data_by_energy(energy='total'):
    """Order the data based on the total shot energy or the max pixel shot energy"""
    dampe_dic  = get_data_dict()
    output_dic = {}

    if energy.lower() == 'total':
        col = 0
    elif energy.lower() in ['max', 'maximum']:
        col = 1
    else:
        raise ValueError('\'{}\' unknown. Please choose \'total\' or \'max\''.format(energy))
    sorted_energy_idx = [index for index, nrj in sorted(enumerate(dampe_dic['calorimeter_data'][:,col]), key=lambda x: x[-1])]

    for key in dampe_dic.keys():
        output_dic[key] =  dampe_dic[key][sorted_energy_idx]

    #output_dic['images'] = dampe_dic['images'][sorted_energy_idx]
    #output_dic['calorimeter_data'] = dampe_dic['calorimeter_data'][sorted_energy_idx]
    #output_dic['data_target'] = dampe_dic['data_target'][sorted_energy_idx]
    #output_dic['benchmark_data'] = dampe_dic['benchmark_data'][sorted_energy_idx]

    return output_dic, sorted_energy_idx

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

def save_model(model, name, overwrite=True):
    """Save keras model"""
    tf_models_dir = os.path.join(os.getcwd(),'models')

    if not os.path.isdir(tf_models_dir):
        os.mkdir(tf_models_dir)
        
    model.save(os.path.join(tf_models_dir, name+'.keras'), overwrite=True)
    

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


#####################################################################################

def split_dico(dico : dict, frac : list = [1]) -> list:
    """Return a list of splited dictionary"""

    # Renormalized to 1
    #frac = [fr / sum(frac) for fr in frac]

    output_list = []
    data_len = dico['calorimeter_data'].shape[0]

    p_old = 0
    p = 0
    for fr in frac:
        p = p + int(round(fr*data_len))
        dico_frac = dico.copy()
        for key in dico.keys():
            dico_frac[key] = dico[key][p_old:p]
        p_old = p

        output_list.append(dico_frac)

    return output_list


