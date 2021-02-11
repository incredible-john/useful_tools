import os
import numpy as np
import shutil

# # Creating Train / Val / Test folders (One time use)
images_dir = 'plane_dataset/images'
labels_dir = 'plane_dataset/labels'

allFileNames = os.listdir(images_dir)
np.random.shuffle(allFileNames)
train_FileNames, test_FileNames = np.split(np.array(allFileNames), [int(len(allFileNames)*0.7)])
# train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
#                                                           [int(len(allFileNames)*0.7), int(len(allFileNames)*0.85)])

train_labels = [labels_dir + '/' + name.replace('.tif', '.txt') for name in train_FileNames.tolist()]
test_labels = [labels_dir + '/' + name.replace('.tif', '.txt') for name in test_FileNames.tolist()]
train_FileNames = [images_dir + '/' + name for name in train_FileNames.tolist()]
test_FileNames = [images_dir + '/' + name for name in test_FileNames.tolist()]

print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Testing: ', len(test_FileNames))

if not os.path.exists('plane_dataset/images/train'):
    os.makedirs('plane_dataset/images/train')
    os.makedirs('plane_dataset/images/test')
    os.makedirs('plane_dataset/labels/train')
    os.makedirs('plane_dataset/labels/test')

# Copy-pasting images
for name in train_FileNames:
    shutil.copy(name, "plane_dataset/images/train")
for name in test_FileNames:
    shutil.copy(name, "plane_dataset/images/test")
for name in train_labels:
    shutil.copy(name, "plane_dataset/labels/train")
for name in test_labels:
    shutil.copy(name, "plane_dataset/labels/test")