import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#setting the path to the directory containing the pics
path = '/media/ashwinhprasad/secondpart/pics'
path2 =
path3 =
path4 =


#appending the pics to the training data list
training_data = []
for img in os.listdir(path):
    pic = cv2.imread(os.path.join(path,img))
    pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    pic = cv2.resize(pic,(80,80))
    training_data.append([pic])

training_data2 = []
for img in os.listdir(path2):
    pic = cv2.imread(os.path.join(path2,img))
    pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    pic = cv2.resize(pic,(80,80))
    training_data.append([pic])

training_data3 = []
for img in os.listdir(path3):
    pic = cv2.imread(os.path.join(path3,img))
    pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    pic = cv2.resize(pic,(80,80))
    training_data.append([pic])

training_data4 = []
for img in os.listdir(path4):
    pic = cv2.imread(os.path.join(path4,img))
    pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    pic = cv2.resize(pic,(80,80))
    training_data.append([pic])

#converting the list to numpy array and saving it to a file using #numpy.save
np.save(os.path.join(path,'preppy'),np.array(training_data))
np.save(os.path.join(path2,'dark_ac'),np.array(training_data2))
np.save(os.path.join(path,'floral'),np.array(training_data3))
np.save(os.path.join(path,'beach_summer'),np.array(training_data4))


plt.imshow(np.array(training_data[0]).reshape(80,80,3))