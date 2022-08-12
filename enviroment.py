import pandas as pd
import numpy as np
from gym import Env
from gym.spaces import Discrete, Box
import random

from env import calReward

# print(pd.read_csv('data/M15N10/f.csv').to_numpy()[5])



class MecEnviroment(Env):

    k= pow(10,-27)
    B = 40
    P = 10
    sigma2 = pow(10,-9)

    def __init__(self, M, N):
        self.M = M
        self.N = N
        self.cDir = "data/M" + str(self.M) + "N" + str(self.N)+ "/c.csv"
        self.dDir = "data/M" + str(self.M) + "N" + str(self.N)+ "/d.csv"
        self.fDir = "data/M" + str(self.M) + "N" + str(self.N)+ "/f.csv"
        self.f0Dir = "data/M" + str(self.M) + "N" + str(self.N)+ "/f0.csv"
        self.rDir = "data/M" + str(self.M) + "N" + str(self.N)+ "/r.csv"

        # self.f0 = pd.read_csv(self.f0Dir).to_numpy()
        # self.r = pd.read_csv(self.rDir).to_numpy()
        self.p= np.zeros((self.M, self.N))
        self.p= np.insert(self.p, 0, 1, axis=1)
        # self.c = pd.read_csv(self.cDir).to_numpy()[0]
        # self.d = pd.read_csv(self.dDir).to_numpy()[0]
        # self.f = pd.read_csv(self.fDir).to_numpy()[0]
        # self.f = np.insert(self.f,0,0)

        self.state = self.p
        self.timeslot = 0
        self.action_space = Discrete(3, start = -1)

        self.k= pow(10,-27)
        self.B = 40
        self.P = 10
        self.sigma2 = pow(10,-9)
    

    def reset(self):
        self.p= np.zeros((self.M, self.N))
        self.p= np.insert(self.p, 0, 1, axis=1)
        # self.c = pd.read_csv(self.cDir).to_numpy()[0]
        # self.d = pd.read_csv(self.dDir).to_numpy()[0]
        # f = pd.read_csv(self.fDir).to_numpy()[0]
        # f = np.insert(f,0,0)
        state = self.p
        self.timeslot = 0
        return state

        
    def step(self, action):
        randomM = random.randint(0,self.M-1)
        randomN = random.randint(1,self.N)
        if self.p[randomM][randomN] + action*0.01 >= 0 and self.p[randomM][0] - action*0.01 >= 0 :
            self.p[randomM][randomN] += action*0.01
            self.p[randomM][0] -= action*0.01
        self.state = self.p
        self.timeslot += 1
        reward = calReward(self.M,self.N, self.timeslot, self.p)

        if self.timeslot >= 1000: 
            done = True
        else:
            done = False
        
        info = {}

        return self.state, reward, done, info

    # def reward(self,timeslot, p):
    #     # cDir = "data/M" + str(self.M) + "N" + str(self.N)+ "/c.csv"
    #     # dDir = "data/M" + str(self.M) + "N" + str(self.N)+ "/d.csv"
    #     # fDir = "data/M" + str(self.M) + "N" + str(self.N)+ "/f.csv"
    #     # f0Dir = "data/M" + str(self.M) + "N" + str(self.N)+ "/f0.csv"
    #     # rDir = "data/M" + str(self.M) + "N" + str(self.N)+ "/r.csv"

    #     # c = pd.read_csv(cDir).to_numpy()[timeslot]
    #     # d = pd.read_csv(dDir).to_numpy()[timeslot]
    #     # f = pd.read_csv(fDir).to_numpy()[timeslot]
    #     # f = np.insert(f,0,0)
    #     # f0 = pd.read_csv(f0Dir).to_numpy()
    #     # r = pd.read_csv(rDir).to_numpy()


        
    #     lm = np.zeros((self.M))
    #     l1 = 0
    #     e1 = 0
    #     l2 = 0
    #     e2 = 0

            
    #     for i in range(self.M):
    #         for j in range(1, N+1):
    #             e1 += P*p[i,j]*d[i]/r[i,j]
    #             lm[i] += p[i,j]*d[i]/r[i,j]
    #         l1 = max(l1,lm[i])

    #     lm = np.zeros((self.M))
    #     for i in range(self.M):
    #         for j in range(self.N+1):
    #             if(j==0):
    #                 l2 = max(l2, p[i,j]*c[i]/f0[i])
    #                 e2 += k*p[i,j]*c[i]*(f0[i]**2)
    #             else:
    #                 lm[i] += p[i,j]*c[i]/f[j]
    #                 e2 += k*p[i,j]*c[i]*(f[j]**2)
    #         l2 = max(l2,lm[i])

    #     print(l1, l2, e1, e2)
    #     return 0.5*(l1+l2+e1+e2)

# p= np.zeros((10,10))
# p= np.insert(p, 0, 1, axis=1)

# p=[]
# for i in range(10):
#     p.append(np.random.dirichlet(np.ones(10+1)))
# p = np.stack(p, axis=0)

