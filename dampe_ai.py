import os
import numpy as np
import tensorflow as tf
# ML tools 
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models, Input, losses

import models

#####################################################
################## DATA PROCESSING ################## 
#####################################################

def split_train_val_test(dampe_data : dict, val_size : float = 0.2, test_size : float = None):
    """Split train, validation and test. If test is None or empty 
       do not create a test sample"""

    calorimeter_images = dampe_data['images']
    data_target        = dampe_data['data_target']

    # Validation split 
    Im_train, Im_val, xy_train, xy_val = train_test_split(
    calorimeter_images, data_target, test_size = val_size
    )
    # Test split
    if test_size:
        Im_val , Im_test , xy_val , xy_test  = train_test_split(
        Im_val, xy_val, test_size = test_size
        )
    else:
        Im_test, xy_test = None, None

    return Im_train, Im_val, Im_test, xy_train, xy_val, xy_test

#####################################################
##################### TF MODELS ##################### 
#####################################################

def calorimeter_model(dampe_data : dict, model_type):
    if type == 1:
        cal_model = models.model1(dampe_data) 
    elif type == 2:
        cal_model = models.model2(dampe_data) 
    elif type == 3:
        cal_model = models.model3(dampe_data) 
    else:
        raise ValueError('Undefined model type : model {}'.format(model_type))
    
    return cal_model


def std_compile(cal_model):
    """Compile and fit with default parameters"""
    cal_model.compile(
    optimizer='adam',
    loss=losses.MeanSquaredError(),
    metrics=['mean_squared_error', 'mean_absolute_error']
    )

    return cal_model

def std_fit(cal_model, Im_train, Im_val, xy_train, xy_val, epochs):
    """fit the model with standart parameters"""
    history = cal_model.fit(Im_train_high, xy_train_high, epochs=epochs, 
                     validation_data=(Im_val_high, xy_val_high))

    return cal_model, history 

def std_compile_fit(cal_model, Im_train, Im_val, xy_train, xy_val, epochs):
    """compile + fit"""
    std_fit(std_compile(cal_model), Im_train, Im_val, xy_train, xy_val, epochs)
  
    return cal_model, history





