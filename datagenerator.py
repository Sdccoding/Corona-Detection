import os
import numpy as np
import shutil

# # Creating Train / Val / Test folders (One time use)
root_dir = 'Dataset'
posCls = '/Covid'
negCls = '/Non-Covid'
y1=root_dir +'/train' + posCls
y2=root_dir +'/train' + negCls
y3=root_dir +'/test' + posCls
y4=root_dir +'/test' + negCls
list =[y1,y2,y3,y4]
for i in range(4): 
   if not os.path.exists(list[i]):  #Checking if the directory exists,if n't create
     os.mkdir(list[i])
#os.makedirs(root_dir +'/train' + posCls)
#os.makedirs(root_dir +'/train' + negCls)
#os.makedirs(root_dir +'/test' + posCls)
#os.makedirs(root_dir +'/test' + negCls)

# Creating partitions of the data after shuffeling
l2=[posCls,negCls]
for i in range(2):
  currentCls = l2[i]
  src = "Dataset"+currentCls # Folder to copy images from

  allFileNames = os.listdir(src)
  np.random.shuffle(allFileNames)
  train_FileNames,test_FileNames = np.split(np.array(allFileNames),[int(len(allFileNames)*0.80)])
  train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
  test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

  print('Total images: ', len(allFileNames))
  print('Training: ', len(train_FileNames))
  print('Testing: ', len(test_FileNames))
  for name in train_FileNames:
    shutil.copy(name, "Dataset/train"+currentCls)
  for name in test_FileNames:
    shutil.copy(name, "Dataset/test"+currentCls)
print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Testing: ', len(test_FileNames))
