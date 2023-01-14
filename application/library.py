import os
import random

import cv2
import inline as inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# setting the path to the directory containing the pics
path = "Images/Dark_winter/Aritzia"
# path2 = "Images/Dark_winter/Aritzia"
# path3 =


# appending the pics to the training data list
training_data = []
for img in os.listdir(path):
    pic = cv2.imread(os.path.join(path, img))
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
    pic = cv2.resize(pic, (80, 80))
    training_data.append([pic])

# training_data2 = []
# for img in os.listdir(path2):
#     pic = cv2.imread(os.path.join(path2,img))
#     pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
#     pic = cv2.resize(pic,(80,80))
#     training_data.append([pic])
#
# training_data3 = []
# for img in os.listdir(path3):
#     pic = cv2.imread(os.path.join(path3,img))
#     pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
#     pic = cv2.resize(pic,(80,80))
#     training_data.append([pic])
#
# #converting the list to numpy array and saving it to a file using #numpy.save
# np.save(os.path.join(path3,'preppy'),np.array(training_data3))
# np.save(os.path.join(path2,'dark_ac'),np.array(training_data2))
# np.save(os.path.join(path, 'floral'), np.array(training_data))


def floral():
    # print(np.array(random.choices(training_data, k=3)).reshape(80, 80, 3))
    i = 0
    while i < 3 :
        i += 1
        plt.imshow(np.array(random.choice(training_data)).reshape(80, 80, 3))
# def dark_ac():
#     plt.show(np.array(random.choices(training_data, k=3)).reshape(80, 80, 3))
# def preppy():
#     plt.show(np.array(random.choices(training_data, k=3)).reshape(80, 80, 3))
