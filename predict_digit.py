#!/usr/bin/env python
# coding: utf-8

# 1. Install Dependencies
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("keras")
install("tensorflow")

import os
import pandas as pd
import pickle
import argparse
import json
import base64
import numpy as np
import io
import scipy
import imageio
from keras.models import load_model
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
  
# Read input image
input_file = os.path.join(os.environ['DATA_PATH'], 'four.jpg') if os.getenv('DATA_PATH') else "Digits/four.jpg"
print ("input file path - ", input_file)
img = mpimg.imread(input_file)
  
# print Image locally
plt.imshow(img)
data = img

# load the model from disk
model_file = os.path.join(os.environ['MODEL_PATH'], 'kerasDigitRecognizer.h5') 
print ("Model file path - ", model_file)
model = load_model(model_file)

testInput = np.array(data, dtype=np.float32)
nrPixels = testInput.shape[0] * testInput.shape[1] # 28 * 28 = 784 pixels
testInput_processed = testInput.reshape(1, nrPixels).astype('float32')

pred = model.predict(testInput_processed)
print ("Predicted image is ", pred.argmax())
result = { "prediction" : str(pred.argmax()) }

if os.getenv('OUTPUT_PATH'):
    output_file=os.path.join(os.environ['OUTPUT_PATH'], 'result.json')
    with open (output_file, 'w') as result_file:
        json.dump(result, result_file)
