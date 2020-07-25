# importing libraries
import cv2
from tensorflow import keras
import numpy as np

categories = ["covid19_scan","normal_scan"]
img_array = cv2.imread('0.png',cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img_array,(150,150)) # resizing the image for predicting .
img = img.reshape(-1,150,150,1)  # reshaping into 4D  
model = keras.models.load_model('covidpd.model') #loading the trained model 
prediction = model.predict([img])                # predicting the image
print(categories[int(prediction[0][0])])        
print(prediction)