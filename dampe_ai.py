import numpy as np
import tensorflow as tf
# ML tools 
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models, Input, losses

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
