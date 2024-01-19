# Project Readme for TensorFlow-based Image Classification Project

## Project Name: Image Classification with TensorFlow

### Overview:
This repository contains the source code for an image classification project using the TensorFlow library. The model is trained to distinguish between two classes (in this case, "+" and "-").

### Table of Contents:
1. [File Structure](#file-structure)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [KI](#plusminus_ki)


### 1. File Structure <a name="file-structure"></a>
```
|- train/                    # Directory for training data
|  |- +/                     # Subfolder (e.g., "+")
|  |- -/                     # Subfolder (e.g., "-")
|- test/                     # Directory for test data
|  |- +/
|  |- -/
|- new_image.png             # Example image for prediction (+)
|- image.png                 # Example image for prediction (-)
|- plusminus_ki.py           # Script for training the model and for making predictions on new data
|- README.md                 # Project Readme (this file)
```

### 2. Prerequisites <a name="prerequisites"></a>
- Python (recommended: version 3.6 or higher)
- TensorFlow (installed via `pip install tensorflow`)
- Keras (installed via `pip install keras`)
- scipy (installed via `pip install scipy`)

### 3. Installation <a name="installation"></a>
1. Clone the repository: `git clone https://github.com/FHitzenberger/Mini-KI`
2. Navigate to the project directory: `cd Mini-KI`


### 4. plusminus_ki.py <a name="plusminus_ki"></a>
The `plusminus_ki.py` file is a Python script within this project, designed for easy execution and testing on new images.


Feel free to customize the information based on the actual content and purpose of the `plusminus_ki.py` script.
