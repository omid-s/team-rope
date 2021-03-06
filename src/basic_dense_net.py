
# coding: utf-8

# In[2]:

import keras
import scipy as sp
import scipy.misc, scipy.ndimage.interpolation
from medpy import metric
import numpy as np
import os
from keras import losses
import tensorflow as tf
from keras.models import Model
from keras.layers import Input,merge, concatenate, Conv2D, MaxPooling2D, Activation, UpSampling2D,Dropout,Conv2DTranspose,add,multiply,Flatten,Dense
from keras.layers.normalization import BatchNormalization as bn
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.optimizers import RMSprop
from keras import regularizers 
from keras import backend as K
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
import numpy as np 
import nibabel as nib
CUDA_VISIBLE_DEVICES = [0]
os.environ['CUDA_VISIBLE_DEVICES']=','.join([str(x) for x in CUDA_VISIBLE_DEVICES])
#oasis files 1-457

path='/home/bahaa/oasis_mri/OAS1_'


# In[3]:

import numpy as np
import cv2





def UNet(input_shape,learn_rate=1e-3):
    l2_lambda = 0.0002
    DropP = 0.3
    kernel_size=3

    inputs = Input(input_shape)

    conv1a = Conv2D( 12, (kernel_size, kernel_size), activation='relu', padding='same', 
                   kernel_regularizer=regularizers.l2(l2_lambda) )(inputs)
        
    conv1a = bn()(conv1a)
    
    conv1b = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(conv1a)

    conv1b = bn()(conv1b)

    merge1=concatenate([conv1a,conv1b])
    
    conv1c = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge1)

    conv1c = bn()(conv1c)

    merge2=concatenate([conv1a,conv1b,conv1c])

    conv1d = Conv2D(32, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge2)

    conv1d = bn()(conv1d)

    
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1d)

    pool1 = Dropout(DropP)(pool1)



#############################    

    conv2a = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(pool1)
    
    conv2a = bn()(conv2a)

    conv2b = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(conv2a)

    conv2b = bn()(conv2b)

    merge1=concatenate([conv2a,conv2b])

    conv2c = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge1)

    conv2c = bn()(conv2c)

    merge2=concatenate([conv2a,conv2b,conv2c])

    conv2d = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge2)

    conv2d = bn()(conv2d)


    merge3=concatenate([conv2a,conv2b,conv2c,conv2d])



    conv2e = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge3)

    conv2e = bn()(conv2e)

    merge4=concatenate([conv2a,conv2b,conv2c,conv2d,conv2e])


    conv2f = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge4)

    conv2f = bn()(conv2f)


    merge5=concatenate([conv2a,conv2b,conv2c,conv2d,conv2e,conv2f])

    conv2g = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge5)

    conv2g = bn()(conv2g)

    merge6=concatenate([conv2a,conv2b,conv2c,conv2d,conv2e,conv2f,conv2g])


    conv2h = Conv2D(64, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge6)

    conv2h = bn()(conv2h)

    
    
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2h)

    pool2 = Dropout(DropP)(pool2)


#############################   




    conv3a = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(pool2)
    
    conv3a = bn()(conv3a)

    conv3b = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(conv3a)

    conv3b = bn()(conv3b)

    merge1=concatenate([conv3a,conv3b])

    conv3c = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge1)

    conv3c = bn()(conv3c)

    merge2=concatenate([conv3a,conv3b,conv3c])

    conv3d = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge2)

    conv3d = bn()(conv3d)


    merge3=concatenate([conv3a,conv3b,conv3c,conv3d])



    conv3e = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge3)

    conv3e = bn()(conv3e)

    merge4=concatenate([conv3a,conv3b,conv3c,conv3d,conv3e])


    conv3f = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge4)

    conv3f = bn()(conv3f)


    merge5=concatenate([conv3a,conv3b,conv3c,conv3d,conv3e,conv3f])

    conv3g = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge5)

    conv3g = bn()(conv3g)

    merge6=concatenate([conv3a,conv3b,conv3c,conv3d,conv3e,conv3f,conv3g])


    conv3h = Conv2D(128, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge6)

    conv3h = bn()(conv3h)

  

    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3h)

    pool3 = Dropout(DropP)(pool3)

#############################   
    conv4a = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(pool3)
    
    conv4a = bn()(conv4a)

    conv4b = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(conv4a)

    conv4b = bn()(conv4b)

    merge1=concatenate([conv4a,conv4b])

    conv4c = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge1)

    conv4c = bn()(conv4c)

    merge2=concatenate([conv4a,conv4b,conv4c])

    conv4d = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge2)

    conv4d = bn()(conv4d)


    merge3=concatenate([conv4a,conv4b,conv4c,conv4d])



    conv4e = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge3)

    conv4e = bn()(conv4e)

    merge4=concatenate([conv4a,conv4b,conv4c,conv4d,conv4e])


    conv4f = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge4)

    conv4f = bn()(conv4f)


    merge5=concatenate([conv4a,conv4b,conv4c,conv4d,conv4e,conv4f])

    conv4g = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge5)

    conv4g = bn()(conv4g)

    merge6=concatenate([conv4a,conv4b,conv4c,conv4d,conv4e,conv4f,conv4g])


    conv4h = Conv2D(256, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge6)

    conv4h = bn()(conv4h)

    pool4 = MaxPooling2D(pool_size=(2, 2))(conv4h)

    pool4 = Dropout(DropP)(pool4)

#############################   
    conv5a = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(pool4)
    
    conv5a = bn()(conv5a)

    conv5b = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(conv5a)

    conv5b = bn()(conv5b)

    merge1=concatenate([conv5a,conv5b])

    conv5c = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge1)

    conv5c = bn()(conv5c)

    merge2=concatenate([conv5a,conv5b,conv5c])

    conv5d = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge2)

    conv5d = bn()(conv5d)


    merge3=concatenate([conv5a,conv5b,conv5c,conv5d])



    conv5e = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge3)

    conv5e = bn()(conv5e)

    merge4=concatenate([conv5a,conv5b,conv5c,conv5d,conv5e])


    conv5f = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge4)

    conv5f = bn()(conv5f)


    merge5=concatenate([conv5a,conv5b,conv5c,conv5d,conv5e,conv5f])

    conv5g = Conv2D(12, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge5)

    conv5g = bn()(conv5g)

    merge6=concatenate([conv5a,conv5b,conv5c,conv5d,conv5e,conv5f,conv5g])


    conv5h = Conv2D(512, (kernel_size, kernel_size), activation='relu', padding='same',
                   kernel_regularizer=regularizers.l2(l2_lambda) )(merge6)

    conv5h = bn()(conv5h)


    flatten_block=Flatten()(conv5h)

    final_op=Dense(15000, activation='softmax',name='final_op')(flatten_block)
    model = Model(inputs=inputs, outputs=final_op)
    model.compile(optimizer='adadelta',loss='categorical_crossentropy',metrics=['accuracy'])
    model.summary()

    return model
 

# In[8]:


model=UNet(input_shape=(64,64,3))
print(model.summary())


# In[62]:
for i in range(0,121):
  print(i)

  X_train=np.load(("/home/rdey/dsp_final/train_np/X_train"+str(i)+".npy"))
  X_train = X_train.astype('float32')
  #X_train=X_train.reshape(X_train.shape+(1,))
  y_train=np.load(("/home/rdey/dsp_final/train_np/y_train"+str(i)+".npy"))#.reshape(X_train.shape)
  y_train=keras.utils.to_categorical(y_train, 15000)

  model.fit([X_train], [y_train],
                    batch_size=64,
                    nb_epoch=4,
                          #validation_data=([X2_validate],[y_validate]),
                    shuffle=True)
                          #callbacks=[xyz],
                          #class_weight=class_weightt)
print('last')
X_train=np.load(("/home/rdey/dsp_final/X_train_last.npy"))
X_train = X_train.astype('float32')
#X_train=X_train.reshape(X_train.shape+(1,))
y_train=np.load(("/home/rdey/dsp_final/y_train_last.npy"))#.reshape(X_train.shape)
y_train=keras.utils.to_categorical(y_train, 15000)

model.fit([X_train], [y_train],
                  batch_size=64,
                  nb_epoch=4,
                        #validation_data=([X2_validate],[y_validate]),
                  shuffle=True)
                        #callbacks=[xyz],
                        #class_weight=class_weightt)

# In[29]:



import h5py
model.save('basic_dense_net_dsp.h5')

