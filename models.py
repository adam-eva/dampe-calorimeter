import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models, Input, losses

def model1(dampe_data : dict):
    """CNN on all data with max pooling"""
    model = models.Sequential()
    
    model.add(Input(shape=dampe_data['images'][0].shape))
    model.add(layers.Conv2D(filters=52, kernel_size=(5, 3), activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2,2))) # Pooling 
    model.add(layers.Conv2D(filters=42, kernel_size=(5, 3), activation='relu'))
    model.add(layers.MaxPooling2D(1,2)) # Pooling on x-y axis
    model.add(layers.Conv2D(filters=32, kernel_size=(1, 4), activation='relu'))
    
    # Dense Feedforward neural network of the features 
    model.add(layers.Flatten())
    model.add(layers.Dense(units=64,activation='relu'))
    model.add(layers.Dense(units=4,activation='linear'))
    
    return model 


def model2(dampe_data : dict):
    """CNN on all data without pooling"""

    model = models.Sequential()
    model.add(Input(shape=dampe_data['images'][0].shape))
    model.add(layers.Conv2D(filters=32, kernel_size=(5, 4), activation='relu'))
    model.add(layers.Conv2D(filters=32, kernel_size=(5, 4), activation='relu'))
    model.add(layers.Conv2D(filters=8, kernel_size=(6, 16), activation='relu'))
    
    # Dense Feedforward neural network of the features 
    model.add(layers.Flatten())
    model.add(layers.Dense(units=64,activation='relu'))
    #model.add(layers.Dense(units=128,activation='relu'))
    model.add(layers.Dense(units=4,activation='linear'))
    
    return model 


def model3(dampe_data : dict):
    """CNN for low and high separation"""
    model_small = models.Sequential()
    model_small.add(Input(shape=dampe_data['images'][0].shape))
    model_small.add(layers.Conv2D(filters=8, kernel_size=(5, 4), activation='relu'))
    model_small.add(layers.Conv2D(filters=16, kernel_size=(5, 4), activation='relu'))
    model_small.add(layers.Conv2D(filters=16, kernel_size=(6, 16), activation='relu'))
    
    # Dense Feedforward neural network of the features 
    model_small.add(layers.Flatten())
    model_small.add(layers.Dense(units=64,activation='relu'))
    #model_small.add(layers.Dense(units=64,activation='relu'))
    model_small.add(layers.Dense(units=4,activation='linear'))
    
    return model_small






