import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory
from enviroment import MecEnviroment

nb_actions = 3
M=10
N=10

model = Sequential()
model.add(Flatten(input_shape=(1, 10, 12)))

model.add(Dense(16, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='relu'))

model.add(Dense(nb_actions, activation='linear'))

model.summary()


env = MecEnviroment(M,N)
memory = SequentialMemory(limit=2000, window_length = 1)
policy = EpsGreedyQPolicy(eps=0.8)
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory,
               target_model_update=200, policy=policy, batch_size = 200)

dqn.compile(optimizer="RMSProp")

# Okay, now it's time to learn something! We visualize the training here for show, but this
# slows down training quite a lot. You can always safely abort the training prematurely using
# Ctrl + C.
dqn.fit(env, nb_steps=999, visualize=False, verbose=2)

# After training is done, we save the final weights.
dqn.save_weights(f'dqn_weights.h5f', overwrite=True)

# Finally, evaluate our algorithm for 5 episodes.
dqn.test(env, nb_episodes=100, visualize=False)