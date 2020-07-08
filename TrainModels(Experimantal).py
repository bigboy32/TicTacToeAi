from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np


import tensorflow as tf

times = int(input("Training Epochs: "))
when_to_train = int(input("When To Train (Epochs): "))

Ai1 = Sequential()
Ai1.add(Dense(32, input_dim=10, activation="relu"))
Ai1.add(Dense(32, activation="relu"))
Ai1.add(Dense(32, activation="relu"))
Ai1.add(Dense(9, activation="softmax"))

Ai2 = Sequential()
Ai2.add(Dense(32, input_dim=10, activation="relu"))
Ai2.add(Dense(32, activation="relu"))
Ai2.add(Dense(32, activation="relu"))
Ai2.add(Dense(9, activation="softmax"))

Ai1.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

Ai2.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

class Trainer:

    def __init__(self, model):
        self.score = 0
        self.Memory = []
        self.TakenActions = []
        self.model = model
        self.prediction = None
        self.v = 0

    def train_model(self):
        self.model.fit(np.array([self.Memory]), np.array([self.TakenActions]), epochs=1)

    def predict(self, state):
        self.prediction = self.model.predict(np.array([state]))
    
    def take_res(self, state, taken_action, reward):
        self.score += reward
        if reward >= 0:
            self.Memory.append(state)
            self.TakenActions.append(taken_action)

T1 = Trainer(Ai1)
T2 = Trainer(Ai2)

t = 0

state = [0,0,0,0,0,0,0,0,0,0]
visstate = []

for x in range(times + 1):
    if t == when_to_train:
        t = 0
        T1.train_model()
        T2.train_model()
    
    T1.predict(state)
    T2.predict(state)

    T1Res = np.argmax(T1.prediction)
    T2Res = np.argmax(T2.prediction)

    r1 = 0
    r2 = 0

    visstate = [state[0:2], state[3:6], state[7:10]]

    if visstate[0][0] and visstate[1][1] and visstate[2][2] == 1:
        r1 = 1
    elif visstate[0][0] and visstate[1][1] and visstate[2][2] == 2:
        r2 = 1
    elif visstate[2][0] and visstate[1][1] and visstate[0][2] == 1:
        r1 = 1
    elif visstate[2][0] and visstate[1][1] and visstate[0][2] == 2:
        r2 = 1
    elif visstate[0][0] and visstate[0][1] and visstate[0][2] == 1:
        r1 = 1
    elif visstate[0][0] and visstate[0][1] and visstate[0][2] == 2:
        r2 = 1
    elif visstate[1][0] and visstate[1][1] and visstate[1][2] == 1:
        r1 = 1 
    elif visstate[1][0] and visstate[1][1] and visstate[1][2] == 2:
        r2 = 1
    elif visstate[2][0] and visstate[2][1] and visstate[2][2] == 1:
        r1 = 1
    elif visstate[2][0] and visstate[2][1] and visstate[2][2] == 2:
        r2 = 1

    else:
        pass

    if r1 == 1:
        T1.take_res(state, T1Res, 1)
        T1.take_res(state, T1Res, 1)
        T1.take_res(state, T1Res, 1)
    elif r2 == 1:
        T2.take_res(state, T2Res, 1)
        T2.take_res(state, T2Res, 1)
        T2.take_res(state, T2Res, 1)


    if state[T1Res] != 2:
        state[T1Res] = 1
    else:
        r1 = -1

    if state[T2Res] != 1:
        state[T2Res] = 2
    else:
        r2 = -1

    T1.take_res(state, T1Res, r1)
    T2.take_res(state, T2Res, r2)
    t += 1
    print(T1.score)
    print(T2.score)
    print("----------------------------------")
    print(state, visstate)

T1.model.save("Ai1.hdf5")
T2.model.save("Ai2.hdf5")
