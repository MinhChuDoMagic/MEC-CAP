import pandas as pd
import numpy as np

# cMin = 2
# cMax = 3
# dMin = 2
# dMax = 3
# fMin = 5
# fMax = 7
# uMin = 1.5
# uMax = 2

# c = np.random.uniform(cMin,cMax,size=(15000,15))
# d = np.random.uniform(cMin,cMax,size=(15000,15))
# f = np.random.uniform(fMin,fMax,size=15)
# f0 = np.random.uniform(uMin,uMax,size=15)
# h = np.random.normal(4, size=(15000,15))

# pd.DataFrame(c*pow(10,9)).to_csv('data/taskRequire.csv')
# pd.DataFrame(d*pow(10,8)).to_csv('data/taskSize.csv')
# pd.DataFrame(f*pow(10,9)).to_csv('data/CAP.csv')
# pd.DataFrame(f0*pow(10,9)).to_csv('data/localComputational.csv')
# pd.DataFrame(h).to_csv('data/chanelGain.csv')


B = 40*pow(10,6)
P = 10
timeslot = 15003
sigma2 = pow(10,-9)
cMin = 2
cMax = 3
dMin = 2
dMax = 3
fMin = 5
fMax = 7
f0Min = 1.5
f0Max = 2

def makingData(M,N):
    c = np.random.uniform(cMin,cMax,size=(timeslot, M))
    d = np.random.uniform(cMin,cMax,size=(timeslot,M))
    f = np.random.uniform(fMin,fMax,size=(timeslot, N))

    f0 = np.random.uniform(f0Min,f0Max,size=M)
    h = np.random.normal(4, size=(M,N))
    h = np.insert(h, 0, 0, axis=1)
    r = B*(np.log2(1+ P*(np.power(h,2))/sigma2))

    # p=[]
    # for i in range(M):
    #     p.append(np.random.dirichlet(np.ones(N+1)))
    # p = np.stack(p, axis=0)

    cDir = "data/M" + str(M) + "N" + str(N)+ "/c.csv"
    dDir = "data/M" + str(M) + "N" + str(N)+ "/d.csv"
    fDir = "data/M" + str(M) + "N" + str(N)+ "/f.csv"
    f0Dir = "data/M" + str(M) + "N" + str(N)+ "/f0.csv"
    rDir = "data/M" + str(M) + "N" + str(N)+ "/r.csv"

    pd.DataFrame(c*pow(10,9)).to_csv(cDir,index=False)
    pd.DataFrame(d*pow(10,8)).to_csv(dDir,index=False)
    pd.DataFrame(f*pow(10,9)).to_csv(fDir,index=False)
    pd.DataFrame(f0*pow(10,9)).to_csv(f0Dir,index=False)
    pd.DataFrame(r).to_csv(rDir,index=False)

makingData(10,10)
makingData(15,10)
makingData(10,15)

