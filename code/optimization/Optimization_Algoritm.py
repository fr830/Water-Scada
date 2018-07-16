#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:11:10 2018

@author: mahadityakaushik
"""
import pandas as pd
import numpy as np

def first_full_tank(row,state):
    '''this returns the min time for a state'''
    min_time=0
    index=0
    ntime=0
    time_array=pd.Series(np.zeros(row.shape[0]))
    for i in range(row.shape[0]):
        if row[i]!=0:
            ntime=(state[i])/row[i]
            #print("*")
            time_array[i]=ntime
    time=time_array[time_array>0]
    if len(time.index)!=0:
        min_time=time.min()
    ind=time_array[time_array>0]
    if len(ind.index)!=0:
        index=ind.idxmin()
    return min_time,index
            
def find_sum(dataset):
'''this returns the series with sum of the flowrate row multiplied by min 
time for each row in the dataset'''     
    row_sum_array=pd.Series(np.zeros(dataset.shape[0]))
    for i in range(dataset.shape[0]):
        row=dataset.iloc[i]
        min_time,min_index=first_full_tank(row,state)
        row=row.multiply(min_time)
        row_sum_array[i]=row.sum()
    return row_sum_array,min_time



def update_quota(dataset,index,quota):
    time,dex=first_full_tank(dataset.iloc[index],state)
    quota=quota.add(dataset.iloc[maxsum_index].multiply(time))
    return quota,dex



def full_states_updater(full_states,state):
    '''this updates the full_state series'''
    for i in range(state.shape[0]):
        if state.iloc[i]==0:
            full_states[i]=1
    return full_states

def get_index(row):
    for i in range(row.shape[0]):
        if row.iloc[i]==1:
            index=i
            row.iloc[i]=0
            return index

def states_deleter(dataset,index):
'''this deletes the states corresponding to the  tank which was recently filled'''
        dataset=dataset[dataset.iloc[:,index]==0]
        dataset=dataset.reset_index(drop=True)

        return dataset

def sunc(ds,full_states):
'''this just calls states_deleter'''
  for i in range(full_states.shape[0]):
    if full_states.iloc[i]==1:
        ds=states_deleter(ds,i)
  return ds

#############################################################################################################
#############################################################################################################
#Declarations

Final_Dataframe_X=pd.DataFrame()
Final_Dataframe_Y=pd.DataFrame()
full_states=pd.Series(np.zeros(21))
Quota_dataframe=pd.Series([40,40,20,40,30,20,40,200,40,40,90,60,60,20,20,60,60,60,40,40,40],dtype='float64')

state=Quota_dataframe

quota=pd.Series(np.zeros(21))
ds=pd.DataFrame(Y1)
ds=ds.T
ds=ds.reset_index(drop=True)
ds=ds.T
ds = ds[(ds.T != 0).any()]

##############################################################################################################
#Main function()

time=0
while(len(ds.index)!=0):
    sum_array,min_time=find_sum(ds)
    maxsum=sum_array.max()
    maxsum_index=sum_array.idxmax()
    Final_Dataframe_Y=Final_Dataframe_Y.append(Y1.iloc[maxsum_index])
    Final_Dataframe_X=Final_Dataframe_X.append(X1.iloc[maxsum_index])
    quota,dex=update_quota(ds,maxsum_index,quota)
    state=Quota_dataframe-(quota)
    full_states=full_states_updater(full_states,state)
    ds=sunc(ds,full_states)
    time=min_time+time
    print(time/6)



###Y1 is the prerequisite dataframe which has just flow rates.













