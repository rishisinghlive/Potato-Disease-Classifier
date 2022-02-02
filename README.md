# potato-disease-classifier
Potato Disease classifier Report

**Data Source: Kaggle   [Plant Village | Kaggle](https://www.kaggle.com/arjuntejaswi/plant-village)**

**The dataset is having 2152 images in 3 folders early blight, late blight, and normal.**

**Target: Create an app where you put the image of the plant and it will identify whether plant has early blight, late blight or normal**

**Approach: will load the images into  batches, preprocess it, create train test and split, do data augmentation and create a CNN model**
# Data Preprocessing
## Resizing images:
Problem: All image are not same size

Approach: load the image using tf module image\_from directory and define the image size and batch size.

Status Effective
### Split the images into train test Val
**Approach**: Create a function which will shuffle the data and take 80% of it split rest 10% for validation and rest 10% for testing.

`	`**Status**: Effective
### `	`Scale the data
`	`**Approach**: Will divide each pixel with 255  

`	`**Status**: Effective
### `	`Data Augmentation
`	`**Approach**: Will flip and rotate the images using tf RandomFlip and RandomRotation

`	`**Status**: Effective
# CNN Model:
- Layers: 14
- Convolution layer (3, 3)
- Max pooling (2, 2)
- Activation : Relu for input and hidden layer, Softmax for output layer
- Optimizer: Adam
- Loss function: Sparse categorical cross entropy 
- Metrics: Accuracy
- Epochs: 41
- Callback: monitor val\_loss and save the best 
# Model Accuracy:
- Training: 99.59%
- Validation: 98.96%
- Test: 99.22%
# Deployment
**Used Pycharm to create an app, streamlit module to create an API and deployed over Heroku platform.**

**Challenges**: Take input of an image and convert into a trainable array.

**Approach**: Read the image using image.open module and convert it into array using tf img\_to\_array, resize and rescale the array and match the model input dimension (1, 256, 256, 3)

**Status:** Effective.


