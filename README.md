# Incidence angle prediction of astroparticles passing through a detector
With the DAMPE detector we hope to find evidence of Dark Matter in space. The detector is a satelite in space with a calorimeter, but being in space particles could come from any direction, perfect for a regression task!

## Dataset
In this project you will be looking at calorimeter images and energies measured in the [DAMPE](http://dpnc.unige.ch/dampe/) space telescope calorimeter. DAMPE is a satellite based experiment designed to search for dark matter signatures.

This dataset consists of (simulated) hits in the DAMPE calorimeter, which can be visualised as an image! Each pixel in the image is one readout-cell of the calorimeter, think of it as a camera with a very coarse granularity, but which is sensitive to particles not light. 

The images are tricky, however, as each row is only sensitive to one direction, so as you move down in z, you alternate between x and y coordinate information.

As the data is simulated, the true location of the incoming particle is known, and it's trajectory can be inferred from the x-y coordinates at the top and bottom of the calorimeter.

You can download the data from [here](https://drive.switch.ch/index.php/s/RrWjbj1UxhO5FKV).

## Aims
Infer the x-y coordinates of the incident particle at the top and bottom of the calorimeter using the image and scalar values.

### Studies
* Check if your model is biased to certain areas of the calorimeter.
* Can all four coordinates sensibly be regressed together? Or are there better ways of regressing the target?
* How accurately can the true trajectory be inferred from the values your model predicts? How can you measure this?
