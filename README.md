# Incidence Angle Prediction of Astroparticles Passing Through a Detector
With the DAMPE detector, we hope to find evidence of Dark Matter in space. The detector is a satellite in space with a calorimeter. However, being in space, particles could come from any direction, making it perfect for a regression task!

## Dataset
In this project, you will be looking at calorimeter images and energies measured in the DAMPE space telescope calorimeter. DAMPE is a satellite-based experiment designed to search for dark matter signatures.

This dataset consists of (simulated) hits in the DAMPE calorimeter, which can be visualized as an image! Each pixel in the image is one readout-cell of the calorimeter. Think of it as a camera with a very coarse granularity, but which is sensitive to particles, not light. 

The images are tricky, however, as each row is only sensitive to one direction. So, as you move down in z, you alternate between x and y coordinate information.

As the data is simulated, the true location of the incoming particle is known, and its trajectory can be inferred from the x-y coordinates at the top and bottom of the calorimeter.

### Data Preparation
**Download the data from [here](https://drive.switch.ch/index.php/s/RrWjbj1UxhO5FKV)** and then unzip the data with `tar -zxvf dampe.tar.gz` into a `data/` folder.

We have provided some initial code for data loading in `Introduction.ipynb` which uses `utils.py` to import the data:
- `get_input_data` : Returns the `images`, `scalar` variables, and the `target`.

- `prepare_data` and `load_numpy_data_multifile` : Used by `get_input_data` to process the data.

### Input Data
The `images` and `scalar` from `get_input_data` are your measured calorimeter images, as well as some additional information about the calorimeter. 
The calorimeter data has the total energy of the corresponding image in the first column, and the calorimeter energy of the maximum bar.

### Target Data
The `target` is a vector of length four, where the first two columns are the x coordinates at the bottom and top, and then the y positions at the top and the bottom. To simplify the task, you can try predicting each layer individually, before attempting both layers together.
Top and bottom are relative to the tracker in the detector at -40mm and -200mm in z.

## Aims
Infer the x-y coordinates of the incident particle at the top and bottom of the calorimeter using the `image` and `scalar` values.

### Data Exploration
Familiarize yourself with the data and create some diagnostic plots.
- Identify any potential issues with the data.

- Discuss possible problems with the data recording process.

If you implement any, remember to report them!

### Exercises
Train a network to predict the x and y coordinates at the top and bottom of the calorimeter.
- You can train a network directly on this image and get reasonable results. Is there another way to use the information?

- You have additional information in the `scalar` variables. Can you incorporate this into the model?

- Can all four coordinates sensibly be regressed together? Or are there better ways of regressing the target?

- How accurately can the true trajectory be inferred from the values your model predicts? How can you measure this?

- Do you have any dependencies or biases in the performance? For example, is your model biased to certain areas of the calorimeter?

Remember to report key metrics in your report. 