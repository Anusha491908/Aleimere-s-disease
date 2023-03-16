# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nOS2jIrQH0WdWY8M4j1opgXetxSj8Pq1
"""

import pandas as pd 
import numpy as np 
import os
import cv2
import matplotlib.pyplot as plt
import warnings

from tensorflow.keras.layers import Input, Lambda, Dense, Flatten, Dropout

from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.preprocessing import image, image_dataset_from_directory

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow import keras
import tensorflow 
import tensorflow as tf

train_ds = tf.keras.preprocessing.image_dataset_from_directory
( "/kaggle/input/alzheimers-dataset-4-class-of-images/Alzheimer_s Dataset/train",)

train_ds = tf.keras.preprocessing.image_dataset_from_directory
("/kaggle/input/alzheimers-dataset-4-class-of-images/Alzheimer_s Dataset/train",)
validation_split=0.2,
subset="training"
seed=1337,
image_size=[180, 180],
batch_size=16,

val_ds = tf.keras.preprocessing.image_dataset_from_directory
"/kaggle/input/alzheimers-dataset-4-class-of-images/Alzheimer_s Dataset/train",

validation_split=0.2,
subset="validation",
seed=1337,
image_size=[180, 180],
batch_size=16,

test_ds = tf.keras.preprocessing.image_dataset_from_directory
"/kaggle/input/alzheimers-dataset-4-class-of-images/Alzheimer_s Dataset/test",
seed=1337,
image_size=[180, 180],
batch_size=16 ,

def image_dataset_from_directory(directory, labels='inferred', 
label_mode='int', class_names=None, color_mode='rgb', 
batch_size=32, image_size=(256, 256), shuffle=True, seed=None, 
validation_split=None, subset=None, interpolation="bilinear"):":"