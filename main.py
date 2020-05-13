import tensorflow as tf
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
from keras.layers import *
from keras.models import *
from keras.preprocessing import image

tr_path="Dataset/train"
test_path="Dataset/test"


#CNN Model in Keras

model=Sequential()
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(224,224,3)))
model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
#model.add(Dropout(0.25))

model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))


model.add(Conv2D(128,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))


model.compile(loss=keras.losses.binary_crossentropy,optimizer='adam',metrics=['accuracy'])

print(model.summary)

#Training

train_datagen=image.ImageDataGenerator(
           rescale    =1./255,
           shear_range =0.2,
           zoom_range=0.2,
           horizontal_flip=True,
           )
test_datagen=image.ImageDataGenerator(rescale=1./255)

train_generator =train_datagen.flow_from_directory(
     tr_path,
     target_size=(224,224),
     batch_size=32,
     class_mode='binary')

test_generator =test_datagen.flow_from_directory(
	 test_path,
     target_size=(224,224),
     batch_size=32,
     class_mode='binary')


model.fit_generator(
	train_generator,
	steps_per_epoch=8,
	epochs=8,
	validation_data=test_generator,
	validation_steps=2
	)
model.save('Corona.h5')
model.save_weights('weights.h5')

	



	
















































