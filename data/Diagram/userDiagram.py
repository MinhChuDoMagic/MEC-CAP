import matplotlib
import numpy as np
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/Diagram/user.csv')

yDQNAgent = df.loc[:,"DQNAgent"].to_numpy()
yDoubleDQN = df.loc[:,"DoubleDQN"].to_numpy()
yDuelingDQN = df.loc[:,"DuelingDQN"].to_numpy()
x = np.array([10, 11, 12, 13, 14, 15])

plt.plot(x, yDQNAgent, label="DQNAgent")    
plt.plot(x, yDoubleDQN, label="DoubleDQN")  
plt.plot(x, yDuelingDQN, label="DuelingDQN")  

plt.xlabel('User')
plt.ylabel('Cost of Linear function')

plt.legend()

#Two  lines to make our compiler able to draw:
plt.savefig("userDiagram.png")