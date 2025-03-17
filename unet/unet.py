# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:19:51 2024

@author: yloghmar
"""

from tensorflow.keras.layers import Conv2D, BatchNormalization, Activation, MaxPool2D, Conv2DTranspose, Concatenate, Input
from tensorflow.keras.models import Model

#definition du block convolutionel 
def conv_block(inputs, num_filters):
    x = Conv2D(num_filters, 3, padding="same")(inputs)
    x = BatchNormalization()(x) # la normalisation pour ameliorer la perfermance
    x = Activation("relu")(x)

    x = Conv2D(num_filters, 3, padding="same")(x) # l'entre de cette couche est la sortie de la précedente 
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    return x
# l'encodeur 
def encoder_block(inputs, num_filters):
    x = conv_block(inputs, num_filters)
    p = MaxPool2D((2, 2))(x) # le maxpolling est fait 2 par 2
    return x, p

def decoder_block(inputs, skip_features, num_filters):
    x = Conv2DTranspose(num_filters, 2, strides=2, padding="same")(inputs)
    x = Concatenate()([x, skip_features])
    x = conv_block(x, num_filters)
    return x

def build_unet(input_shape):
    inputs = Input(input_shape)#Définit l'entrée du modèle avec la forme spécifiée

    s1, p1 = encoder_block(inputs, 64) # 64 est le nombre de filter 
    s2, p2 = encoder_block(p1, 128) #a chaque couche on double le nombre des filtre  
    s3, p3 = encoder_block(p2, 256)
    s4, p4 = encoder_block(p3, 512)

    # print(s1.shape, s2.shape, s3.shape, s4.shape)
    # print(p1.shape, p2.shape, p3.shape, p4.shape)

    b1 = conv_block(p4, 1024) # bloc convolutionelle 

    d1 = decoder_block(b1, s4, 512)
    d2 = decoder_block(d1, s3, 256)
    d3 = decoder_block(d2, s2, 128)
    d4 = decoder_block(d3, s1, 64)

    outputs = Conv2D(1, 1, padding="same", activation="sigmoid")(d4)

    model = Model(inputs, outputs, name="UNET")
    return model

if __name__ == "__main__":
    input_shape = (256, 256, 3)
    model = build_unet(input_shape)
    model.summary()