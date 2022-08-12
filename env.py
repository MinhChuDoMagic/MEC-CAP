import pandas as pd
import numpy as np

# print(pd.read_csv('data/M15N10/f.csv').to_numpy()[5])

B = 40
P = 10
sigma2 = pow(10,-9)
k= pow(10,-27)
count = 0

def calReward(M,N, timeslot, p):
    cDir = "data/M" + str(M) + "N" + str(N)+ "/c.csv"
    dDir = "data/M" + str(M) + "N" + str(N)+ "/d.csv"
    fDir = "data/M" + str(M) + "N" + str(N)+ "/f.csv"
    f0Dir = "data/M" + str(M) + "N" + str(N)+ "/f0.csv"
    rDir = "data/M" + str(M) + "N" + str(N)+ "/r.csv"

    c = pd.read_csv(cDir).to_numpy()[timeslot]
    d = pd.read_csv(dDir).to_numpy()[timeslot]
    f = pd.read_csv(fDir).to_numpy()[timeslot]
    f = np.insert(f,0,0)
    f0 = pd.read_csv(f0Dir).to_numpy()
    r = pd.read_csv(rDir).to_numpy()

    # state = (c,d,f,p)

    # print(state)
    
    lm = np.zeros((M))
    l1 = 0
    e1 = 0
    l2 = 0
    e2 = 0
    

        
    for i in range(M):
        for j in range(1, N+1):
            e1 += P*p[i,j]*d[i]/r[i,j]
            lm[i] += p[i,j]*d[i]/r[i,j]
        l1 = max(l1,lm[i])

    lm = np.zeros((M))
    for i in range(M):
        for j in range(N+1):
            if(j==0):
                l2 = max(l2, p[i,j]*c[i]/f0[i])
                e2 += k*p[i,j]*c[i]*(f0[i]**2)
            else:
                lm[i] += p[i,j]*c[i]/f[j]
                e2 += k*p[i,j]*c[i]*(f[j]**2)
        l2 = max(l2,lm[i])

    reward = 0.5*(500*(l1+l2) +(e1*10+e2/10)/100) ##+e1*10+e2/10
    print(reward) ##, l1, l2, e1*10, e2/10
    return -reward

# p= np.zeros((10,10))
# p= np.insert(p, 0, 1, axis=1)
# print(p.shape)

# # p=[]
# # for i in range(10):
# #     p.append(np.random.dirichlet(np.ones(10+1)))
# # p = np.stack(p, axis=0)

# for i in range(3):
#     calReward(10,10,i,p)
