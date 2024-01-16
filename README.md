# Incidence angle prediction of astroparticles passing through a detector
With the DAMPE detector we hope to find evidence of Dark Matter in space. The detector is a satelite in space with a calorimeter, but being in space particles could come from any direction, perfect for a regression task!

## Dataset
In this project you will be looking at calorimeter images and energies measured in the [DAMPE](http://dpnc.unige.ch/dampe/) space telescope calorimeter. DAMPE is a satellite based experiment designed to search for dark matter signatures.

This dataset consists of (simulated) hits in the DAMPE calorimeter, which can be visualised as an image! Each pixel in the image is one readout-cell of the calorimeter, think of it as a camera with a very coarse granularity, but which is sensitive to particles not light. 

The images are tricky, however, as each row is only sensitive to one direction, so as you move down in z, you alternate between x and y coordinate information.

As the data is simulated, the true location of the incoming particle is known, and it's trajectory can be inferred from the x-y coordinates at the top and bottom of the calorimeter.

### Download and unzip data
**Download the data from [here](https://drive.switch.ch/index.php/s/RrWjbj1UxhO5FKV).**
First download the data, and then un-zip the data with `tar -zxvf dampe.tar.gz` into a `data/` folder.
- You can use `get_input_data.py` function in utils.py, however you may need to change the path.

### Training data
Here you get calorimeter images, as well as some additional information about the calorimeter.
The calorimeter data has the total energy of the corresponding image in the first column, and the calorimeter energy of the maximum bar.

### Target data
The target here is a vector of length four, where the first two columns are the x coordinates at the bottom and top, and then the y positions at the top and the bottom. To simplify the task, you can try predicting each layer individually, before attempting both layers together.
Top and bottom is relative to the tracker in the detector at -40mm and -200mm in z.


## Aims
Infer the x-y coordinates of the incident particle at the top and bottom of the calorimeter using the image and scalar values.

### Exercises
Train a CNN to predict the x and y coordinates at the top and bottom of the calorimeter.
- You can train a network directly on this image and get reasonable results, is there another way to use the information?
- You have additional information from calorimeter_data, how can you incorporate this into the model?
- Do you have any dependences or biases in the performance?

### Studies
* Check if your model is biased to certain areas of the calorimeter.
* Can all four coordinates sensibly be regressed together? Or are there better ways of regressing the target?
* How accurately can the true trajectory be inferred from the values your model predicts? How can you measure this?
