#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:36:46 2018

@author: mahadityakaushik
"""
import pandas as pd
import numpy as np
import keras   
from keras.models import Sequential
from keras.layers import Dense
    
# Importing the datset and dataset preprocessing
#######################################################################
dataset=pd.read_excel('al1.xlsx')
df=pd.DataFrame()
dataframe=dataset.iloc[:,0]
for i in range(dataset.shape[0]):
    #ope=pd.Series([int(j) for j in str(dataframe.iloc[i,0]).split()])
    #su=sum([float(j) for j in str(dataset.iloc[i,1]).split()])
    #ope=ope.append(flo)
    #ope=ope.reset_index(drop=True)
    flo=pd.Series([float(j) for j in str(dataset.iloc[i,1]).split()])
    df=df.append(flo,ignore_index=True)
df=df.reset_index(drop=True)    
dataframe=dataframe.reset_index(drop=True) 
dataframe=pd.concat([dataframe,df],axis=1)  
dataframe=dataframe.groupby('Open',as_index=False).mean()
df=pd.DataFrame()
for i in range(dataframe.shape[0]):
    #su=sum([float(j) for j in str(dataset.iloc[i,1]).split()])
    #if su and su<14:
    #flo=pd.Series([float(j) for j in str(gari.iloc[i,1]).split()])
    #ope=ope.append(flo)
    #ope=ope.reset_index(drop=True)
    ope=pd.Series([int(j) for j in str(dataframe.iloc[i,0]).split()])
    df=df.append(ope,ignore_index=True)    
jk=dataframe.iloc[:,1:]
df=pd.concat([df,jk],axis=1)  

################################################################################

#  df is the final dataframe you get after datapreprocessing

#here we break the dataframe into 2 parts states and flowrates
X1=df.iloc[:,:21]
Y1=df.iloc[:,21:43]

  
for i in range (df.shape[0]):
    for j in range(21):
        if X1.iloc[i,j]==0:
            Y1.iloc[i,j]=0   
 
    
#here we are exporting the dataset to csv   

df.to_csv('averaged.csv')  



    
###Optional method of neural net which we are not using.

model=Sequential()
model.add(Dense(200,activation='relu',input_dim=21)) 
model.add(Dense(200,activation='relu'))
model.add(Dense(200,activation='relu'))
model.add(Dense(200,activation='relu'))
model.add(Dense(200,activation='relu'))
model.add(Dense(200,activation='relu'))
model.add(Dense(200,activation='relu'))
model.add(Dense(21))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X1, Y1, epochs=5000, batch_size=1000)
predictions = model.predict(test)
predictions=pd.DataFrame(predictions)





