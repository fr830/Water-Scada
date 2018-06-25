import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras import optimizers
from keras import regularizers

d1 = pd.read_excel(r'ml11.xlsx')
d2 = pd.read_excel(r'ml12.xlsx')
frames = [d1,d2]
d1 = pd.concat(frames, ignore_index = True)
#d1 = d1.dropna()
test = pd.read_excel(r'G:\Water_Skada\code\Testing_1\a10.xlsx')
#test = test.dropna()
#print(d1)

def df_init(s):
    if s=='op':
        cols1 = [('t'+str(i)) for i in range(1,22) ]
        df1 = pd.DataFrame(cols1)
        return df1
    else:
        cols2 = [('fr1'+str(i)) for i in range(1,22)]
        df2 = pd.DataFrame(cols2)
        return df2
    
def str_to_num(l1):
    nlist = []
    for i in range(0,len(l1)):
        alp = float(l1[i])
        nlist.append(alp)
    return nlist
    
    
def format_data(dat,s, lo, hi):
    #df = df_init(s)
    #df = pd.DataFrame()#
    nd = np.empty([len(dat),21])
    k=0
    for i in range(lo,hi):
        #print(i)
        #dat[i] = dat[i].to_string()
        dat[i] = str(dat[i]).split()
        dat[i] = str_to_num(dat[i])
        #print(type(dat[i]),type(dat))
        #print(i)
        
        nd[k] = dat[i]
        k+=1
        #print(len(dat[i]))
    return nd

def create_model():
    model1 = Sequential()
    model1.add(Dense(11,activation = 'sigmoid',input_dim = 21))
    #model1.add(BatchNormalization())
    model1.add(Dense(18, activation = 'relu'))#, activation = 'sigmoid'))
    model1.add(Dense(11, activation = 'sigmoid'))
    #model1.add(Dense(19,activation = 'sigmoid'))# kernel_regularizer = regularizers.l1(0.02),bias_regularizer = regularizers.l1(0.01)))
    model1.add(Dense(21, activation = 'relu'))#,activity_regularizer = regularizers.l1(0.02)))
    #model1.add(Dropout(0.2))
    """model2 = Sequential()
    model2.add(Dense(20, activation = 'relu',input_dim = 22))
    model2.add(Dense(22, activation = 'relu'))"""
    return model1

def normalize(flow):
    for i in range(0,len(flow)):
        for j in range(0,len(flow[i])):
            print(i,j)
            if sum(flow[i]) != 0:
                flow.iloc[i,j] = flow.iloc[i,j]/sum(flow.iloc[i])
                print('hiii')
    return flow
    
"""     
opcl1 = d1.iloc[:int(len(d1)/3),0]
opcl1 = format_data(opcl1,'op', 0, len(opcl1))
print('done1')
opcl2 = d1.iloc[int(len(d1)/3):int(len(d1)/3)*2,0]
opcl2 = format_data(opcl2,'op', int(len(d1)/3), int(len(d1)/3)*2)
print('done1')
fr1 = d1.iloc[:int(len(d1)/3),1]
fr1 = format_data(fr1,'fr', 0, int(len(d1)/3))
print('done1')
fr2 = d1.iloc[int(len(d1)/3):int(len(d1)/3)*2,1]
fr2 = format_data(fr2,'fr', int(len(d1)/3), int(len(d1)/3)*2)
print('done1')
opcl3 = d1.iloc[int(len(d1)/3)*2:,0]
opcl3 = format_data(opcl3,'op', int(len(d1)/3)*2,len(d1))
fr3 = d1.iloc[int(len(d1)/3)*2:,1]
fr3 = format_data(fr3,'fr',int(len(d1)/3)*2,len(d1))
"""
opcl1 = d1.iloc[:len(d1),0]
opcl1 = format_data(opcl1,'op', 0, len(d1))
fr1 = d1.iloc[:len(d1),1]
fr1 = format_data(fr1,'fr', 0, len(d1))

fr1 = pd.DataFrame(fr1)
x = pd.isnull(fr1).any(1).nonzero()[0]
fr1.dropna(inplace=True)
opcl1 = np.delete(opcl1,x,0)

opcl3 = test.iloc[:len(test),0]
opcl3 = format_data(opcl3,'op',0,len(test))
fr3 = test.iloc[:len(test),1]
fr3 = format_data(fr3,'fr',0,len(test))

fr3 = pd.DataFrame(fr3)
y = pd.isnull(fr3).any(1).nonzero()[0]
fr3.dropna(inplace=True)
opcl3 = np.delete(opcl3,y,0)

fr1 = normalize(fr1)
fr3 = normalize(fr3)

model1= create_model()
sgd = optimizers.SGD(lr=0.0004)
ada = optimizers.Adam(clipnorm=0.5,lr=0.00004)
model1.compile(optimizer = ada, loss = 'categorical_crossentropy', metrics = ['accuracy'])

model1.fit(fr1,opcl1,batch_size = 5, epochs = 30)

#model2.compile(optimizer = optimizers.rmsprop(lr = 0.12), loss = 'categorical_crossentropy', metrics = ['accuracy'])
#model2.fit(opcl2,fr2,batch_size = 5, epochs = 25)

score1 = model1.evaluate(fr3,opcl3,batch_size = 5)
#score2 = model2.evaluate(opcl3,fr3,batch_size = 5)
print('score1: ', score1)
#print('score2: ', score2)
#92.8 % accuracy - srsr - 27 epochs


