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
    #model.add(layers.Dense(units=64,activation='relu'))
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


def model4(dampe_data : dict):
    """CNN on all data without pooling
       Include energy data in the MLP part"""

    image_input  = layers.Input(shape=dampe_data['images'][0].shape, name='calo_images')
    energy_input = layers.Input(shape=dampe_data['calorimeter_data'][0].shape, name='calo_energy')

    # CNN block
    conv2d_1  = layers.Conv2D(filters=32, kernel_size=(5, 4), activation='relu')(image_input)
    conv2d_2  = layers.Conv2D(filters=32, kernel_size=(5, 4), activation='relu')(conv2d_1)
    conv2d_3  = layers.Conv2D(filters=8, kernel_size=(6, 16), activation='relu')(conv2d_2)
    conv_flat = layers.Flatten()(conv2d_3)

    # MLP block
    concat  = layers.Concatenate()([conv_flat, energy_input]) # MLP input 
    dense_1 = layers.Dense(units=64,activation='relu')(concat)
    output  = layers.Dense(units=4,activation='linear')(concat)

    model = keras.Model(
        inputs  = [image_input, energy_input],
        outputs = [output]
    )
    
    return model

def model5(dampe_data : dict):
    """Model for the reordered XY data"""
    
    model = models.Sequential()
    model.add(Input(shape=dampe_data['images'][0].shape))
    model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu'))
    model.add(layers.Conv2D(filters=16, kernel_size=(5, 5), activation='relu'))
    model.add(layers.Conv2D(filters=16, kernel_size=(5,12), activation='relu'))
        
    # Dense Feedforward neural network of the features 
    model.add(layers.Flatten())
    model.add(layers.Dense(units=64,activation='relu'))
    model.add(layers.Dense(units=64,activation='relu'))
    model.add(layers.Dense(units=4 ,activation='linear')) 

    return model


