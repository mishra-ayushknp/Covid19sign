#importing libraries
import numpy as np 
import os
import cv2
import random
import pickle

t_d = []
ddir = "C:\\Users\\AYUSH MISHRA\\Desktop" # Path directory where the dataset is stored. 
categories = ["COVID19","NORMAL"]  # covid19 and Normal datset .
for c in categories :
    path = os.path.join(ddir, c)  # joining the path of the covid19 and normal image to the Path directory .
    c_n = categories.index(c)    
    for i in os.listdir(path):
        img = cv2.imread(os.path.join(path,i),cv2.IMREAD_GRAYSCALE)  
        img_resize = cv2.resize(img,(150,150))   #  resizing the image into (150,150)
        t_d.append([img_resize,c_n])
random.shuffle(t_d)                # shuffling the data in random manner
print(len(t_d))      # printing the length of the training data
x = []
y = []
for f , l in t_d :
    x.append(f)
    y.append(l)
xe = np.array(x).reshape(-1,150,150,1)    # reshaping the image into four dimension
ye = np.array(y)
# saving the training dataset using pickle
pickle_o = open("xe.pickle","wb")              
pickle.dump(xe,pickle_o)
pickle_o.close()
pickle_o = open("ye.pickle","wb")
pickle.dump(ye,pickle_o)
pickle_o.close()
print(xe.shape,ye.shape) # shape of the training data


