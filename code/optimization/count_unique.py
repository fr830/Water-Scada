import pandas as pd
import numpy as np
from scipy.optimize import linprog
from numpy.linalg import solve
df=pd.read_excel('al1.xlsx')
df1=df.drop_duplicates(subset=['Open','Close'], keep='first')
df1.reset_index(drop=True,inplace=True)
tk=pd.DataFrame()
l=[]
for i in range(df1.shape[0]):
    f=[float(i) for i in df1.iloc[i,1].split()]
    # print(sum(f))
    if sum(f) and sum(f)<14: 
        l.append(f+[-1])
TankCapacity=[85,40,20,40,30,20,40,200,40,40,
              90,60,60,20,20,60,60,60, 40,40,40]
TankCapacity=[j*10 for j in TankCapacity]+[-24*60]
print(TankCapacity)
"""
PNB_AKP_OHSR_01	20
PNB_BVP_OHSR_01	60
PNB_CKD_OHSR_01	30
PNB_CNP_OHSR_01	40
PNB_CNP_SUMP_01	85
PNB_GDV_OHSR_01	40
PNB_GDV_OHSR_02	40
PNB_GDV_OHSR_03	20
PNB_IKP_GLBR_01	90
PNB_KNP_OHSR_01	60
PNB_KYP_OHSR_01	40
PNB_KYP_SUMP_01	40
PNB_MAD_OHSR_01	60
PNB_MAD_OHSR_02	60
PNB_NSP_OHSR_01	40
PNB_PNB_GLSR_01	90
PNB_PNB_GLSR_02	60
PNB_RDP_OHSR_01	200
PNB_RLP_OHSR_01	20
PNB_TNP_OHSR_01	20
PNB_TVL_OHSR_01	40
PNB_VKP_OHSR_01	40
PNB_VNP_OHSR_01	40
"""

A_ub=np.array(l).transpose()*-1
b_ub = np.array(TankCapacity)*-1

c = np.ones(A_ub.shape[1])
print(A_ub,A_ub.shape,'\n'*3,b_ub,b_ub.shape,'\n'*3,c,c.shape,'\n'*3,end='\n')
res = linprog(c, A_ub=A_ub, b_ub=b_ub,bounds=(0,None),
              options=dict(bland=True , tol=1e-1, disp=True, maxiter= 100000))
print('Optimal value:', res)
b=[]
for i in range(len(res.x)):
    if res.x[i]!=0.0:
        b.append([res.x[i],l[i]])#,[k for k in df1.iloc[i,0].split()]])

print(b,len(b))
print(A_ub.dot(res.x))