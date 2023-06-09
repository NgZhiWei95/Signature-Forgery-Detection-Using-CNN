# -*- coding: utf-8 -*-
"""DataAugmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gQGaPT2h7nwZJnJe83W0-2GbsW7gibe8
"""

#Mount drive
from google.colab import drive
drive.mount('/content/drive')

#Data augmentation for training dataset

#Imports
from PIL import Image
from skimage import io
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np

#Forged

#Use Tensorflow's ImageDataGenerator for data augmentation
dataGenerator = ImageDataGenerator(        
            rotation_range = 90,
            width_shift_range = 0.5,  
            height_shift_range = 0.1,            
            zoom_range = 0.15,        
            vertical_flip = True,         
            fill_mode = 'nearest')

#Forged training set directory, set images size, and declare dataset array
directory = '/content/drive/MyDrive/SignatureDataSet(jpg)/training/forged/'
imgSize = 256
datasetArray = []

#Take in each images, resize it, and put it into dataset array
my_images = os.listdir(directory)
for i, image_name in enumerate(my_images):    
   if (image_name.split('.')[1] == 'jpg'):        
       image = io.imread(directory + image_name)        
       image = Image.fromarray(image, 'RGB')        
       image = image.resize((imgSize,imgSize)) 
       datasetArray.append(np.array(image))

#By ImageDataGenerator, create 2 new images for each forged training image
x = np.array(datasetArray)
i = 0
for batch in dataGenerator.flow(x, batch_size = 2,
                          save_to_dir = '/content/drive/MyDrive/forgery/',
                          save_prefix = 'aug',
                          save_format = 'png'):
    i = i + 1
    if i > 119:
        break

#Use Tensorflow's ImageDataGenerator for data augmentation
dataGenerator = ImageDataGenerator(        
            rotation_range = 180,
            width_shift_range = 0.24,  
            height_shift_range = 0.12,            
            zoom_range = 0.11,        
            horizontal_flip = True,         
            fill_mode = 'wrap')

#Forged training set directory, set images size, and declare dataset array
directory = '/content/drive/MyDrive/forged/'
imgSize = 256
datasetArray = []

#Take in each images, resize it, and put it into dataset array
my_images = os.listdir(directory)
for i, image_name in enumerate(my_images):    
   if (image_name.split('.')[1] == 'jpg'):        
       image = io.imread(directory + image_name)        
       image = Image.fromarray(image, 'RGB')        
       image = image.resize((imgSize,imgSize)) 
       datasetArray.append(np.array(image))

#By ImageDataGenerator, create 2 new images for each forged training image
x = np.array(datasetArray)
i = 0
for batch in dataGenerator.flow(x, batch_size = 5,
                          save_to_dir = '/content/drive/MyDrive/forgery/',
                          save_prefix = 'dataAug',
                          save_format = 'png'):
    i = i + 1
    if i > 119:
        break

#Genuine

#Use Tensorflow's ImageDataGenerator for data augmentation
dataGenerator = ImageDataGenerator(        
            rotation_range = 30,
            width_shift_range = 0.2,  
            height_shift_range = 0.4,            
            zoom_range = 0.25,        
            vertical_flip = True,         
            fill_mode = 'reflect')

#Genuine training set directory, set images size, and declare dataset array
directory = '/content/drive/MyDrive/SignatureDataSet(jpg)/training/genuine/'
imgSize = 256
datasetArray = []

#Take in each images, resize it, and put it into dataset array
my_images = os.listdir(directory)
for i, image_name in enumerate(my_images):    
   if (image_name.split('.')[1] == 'jpg'):        
       image = io.imread(directory + image_name)        
       image = Image.fromarray(image, 'RGB')        
       image = image.resize((imgSize,imgSize)) 
       datasetArray.append(np.array(image))

#By ImageDataGenerator, create 2 new images for each genuine training image
x = np.array(datasetArray)
i = 0
for batch in dataGenerator.flow(x, batch_size = 2,
                          save_to_dir = '/content/drive/MyDrive/genuine/',
                          save_prefix = 'aug',
                          save_format = 'png'):
    i = i + 1
    if i > 119:
        break

#Use Tensorflow's ImageDataGenerator for data augmentation
dataGenerator = ImageDataGenerator(        
            rotation_range = 270,
            width_shift_range = 0.35,  
            height_shift_range = 0.13,            
            zoom_range = 0.34,        
            horizontal_flip = True,         
            fill_mode = 'wrap')

#Genuine training set directory, set images size, and declare dataset array
directory = '/content/drive/MyDrive/training/genuine/'
imgSize = 256
datasetArray = []

#Take in each images, resize it, and put it into dataset array
my_images = os.listdir(directory)
for i, image_name in enumerate(my_images):    
   if (image_name.split('.')[1] == 'jpg'):        
       image = io.imread(directory + image_name)        
       image = Image.fromarray(image, 'RGB')        
       image = image.resize((imgSize,imgSize)) 
       datasetArray.append(np.array(image))

#By ImageDataGenerator, create 2 new images for each genuine training image
x = np.array(datasetArray)
i = 0
for batch in dataGenerator.flow(x, batch_size = 5,
                          save_to_dir = '/content/drive/MyDrive/genuine/',
                          save_prefix = 'dataAug',
                          save_format = 'png'):
    i = i + 1
    if i > 119:
        break