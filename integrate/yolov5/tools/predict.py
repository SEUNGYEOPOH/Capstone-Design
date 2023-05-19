#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
    
class predict_Dataset:
    
    def __init__(
            self, 
            images,
            augmentation=None, 
            preprocessing=None,
    ):
#         self.ids = os.listdir(images_dir)
#         self.images_fps = [os.path.join(images_dir, image_id) for image_id in self.ids]
        self.images = images
        
        # convert str names to class values on masks
        self.augmentation = augmentation
        self.preprocessing = preprocessing
    
    def __getitem__(self, i):
        
        # read data
#         image = cv2.imread(self.images_fps[i])
        image = cv2.cvtColor(self.images, cv2.COLOR_BGR2RGB)
        
        # apply augmentations
        if self.augmentation:
            sample = self.augmentation(image=image)
            image = sample['image']
        
        # apply preprocessing
        if self.preprocessing:
            sample = self.preprocessing(image=image)
            image = sample['image']
            
        return image
        
    def __len__(self):
        return len(self.ids)