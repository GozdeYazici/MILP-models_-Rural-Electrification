import pandas as pd
import gurobipy as gp
from gurobipy import GRB
import time
import math
import numpy as np


n=21
period=5

s1="CD"
s2="CGI"
s3="CGE"


N = [i for i in range(1,n+1)]
T=[j for j in range(1, period+1)]
T1=[j for j in range(1,period)]

alpha=math.floor(len(N)/len(T))

file="21_instance.xlsx"


CD_df= pd.read_excel(file, sheet_name=s1, header=None)
CD = CD_df.to_numpy()

CD=np.tile(CD,(1,period))


CGI_df= pd.read_excel(file, sheet_name=s2, header=None)
CGI = CGI_df.to_numpy()

CGI=np.tile(CGI,(1,period))


CGE_df= pd.read_excel(file, sheet_name=s3, header=None)
CGE = CGE_df.to_numpy()

CGE=np.tile(CGE,(period,1,1))


model=gp.Model('Multistage_base')

x=model.addVars(N,T, vtype=GRB.BINARY,name="x")
s=model.addVars(N,T, vtype=GRB.BINARY,name="s")
f=model.addVars(N,N,T, lb=0, vtype=GRB.CONTINUOUS,name="f")
u=model.addVars(N,N,T, vtype=GRB.BINARY,name="u")
v=model.addVars(N,T, vtype=GRB.BINARY,name="v")
q=model.addVars(N,T, lb=0, vtype=GRB.CONTINUOUS,name="q")


print("Variables created")


model.modelSense=GRB.MINIMIZE

model.setObjective(sum(s[i,t]*CD[i-1,t-1] for i in N for t in T)+sum(x[i,t]*CGI[i-1,t-1] for i in N for t in T)+sum(u[i,j,t]*CGE[t-1,i-1,j-1] for i in N for j in N for t in T))


c1=model.addConstrs(sum(x[i,t]+s[i,t] for t in T)==1 for i in N)

c2=model.addConstrs(sum(v[i,t] for i in N)<=1 for t in T)

c3=model.addConstrs(len(N)*v[i,t]>=q[i,t] for i in N for t in T)

c4=model.addConstrs(sum(f[i,j,t] for j in N)+sum(x[i,k] for k in range(1, t+1))==sum(f[l,i,t] for l in N)+q[i,t] for i in N for t in T)

c5=model.addConstrs(len(N)*sum(u[i,j,k] for k in range(1, t+1))>=f[i,j,t] for i in N for j in N for t in T)

c6=model.addConstrs(sum(u[i,j,k] for i in N for k in range(1, t+1))+v[j,t]==sum(x[j,k] for k in range(1, t+1)) for j in N for t in T)

c7=model.addConstrs(u[i,j,t] <=sum(x[i,k] for k in  range(1, t+1)) for i in N for j in N for t in T)

c8=model.addConstrs(sum(x[i,t]+s[i,t] for i in N)>=alpha for t in T1)

c9=model.addConstr(sum(x[i,len(T)]+s[i,len(T)] for i in N)==len(N)-(len(T)-1)*alpha)

c10=model.addConstrs(f[i,j,k]<=f[i,j,k+1] for i in N for j in N for k in T1)

starting_time=time.time()

model.optimize()

print("Runtime is (seconds):", time.time()-starting_time)







