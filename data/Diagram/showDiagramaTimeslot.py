import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/Diagram/data.csv')

yDQNAgent = df.loc[:,"DQNAgent"].to_numpy()
yDoubleDQN = df.loc[:,"DoubleDQN"].to_numpy()
yDuelingDQN = df.loc[:,"DuelingDQN"].to_numpy()
x= df.loc[:,"Time slot"].to_numpy()

plt.scatter(x, yDQNAgent, s=1, label="DQNAgent")
plt.scatter(x, yDoubleDQN, s=1, label="DoubleDQN")
plt.scatter(x, yDuelingDQN, s=1, label="DuelingDQN")

plt.xlabel('Time slot')
plt.ylabel('Cost of Linear function')

plt.legend()

#Two  lines to make our compiler able to draw:
plt.savefig("Diagram.png")