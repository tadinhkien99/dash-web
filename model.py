#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    model.py
# @Author:      Kuro
# @Time:        10/31/2022 3:25 PM

from keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam


def build_model(hidden_layers, lr, dropout):
    model = Sequential()
    model.add(Dense(256, input_shape=(21,), activation='relu'))
    # Hidden Layer
    for layer in range(hidden_layers):
        model.add(Dense(256, activation='relu'))

    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    if dropout == "Yes":
        model.add(Dropout(0.15))
    # Output layer
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer=Adam(learning_rate=lr), loss='mse', metrics='mae')
    return model
