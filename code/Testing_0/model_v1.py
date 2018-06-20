#from time import time
#from sklearn.metrics import accuracy_score
#from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import pandas as pd

data_test = pd.read_csv(r"G:\PS1\Testing\Test.csv")
data_train = pd.read_csv(r"G:\PS1\Testing\outputDataSetFinal.csv")
X_train = data_train[['TankName','Weekday','MinutesElapsedDay']]
y_train = data_train.iloc[:,2].values
X_test = data_test[['TankName','Weekday','MinutesElapsedDay']]
y_test = data_test.iloc[:,2].values

lab1 = LabelEncoder()
X_train.iloc[:,0] = lab1.fit_transform(X_train.iloc[:,0])
X_test.iloc[:,0] = lab1.fit_transform(X_test.iloc[:,0])
#onehotencoder = OneHotEncoder(categorical_features = [1])
#X_train = onehotencoder.fit_transform(X_train).toarray()
#X_test = onehotencoder.fit_transform(X_test).toarray()
#X_train = X_train[:,:-1]
#X_test = X_test[:,:-1]

clf = Sequential()

# Adding the input layer and the first hidden layer
clf.add(Dense(3, activation = 'relu',input_dim = 3))
# Adding the second hidden layer
clf.add(Dense(2,activation = 'sigmoid'))
# Adding the output layer
clf.add(Dense(1, activation = 'relu'))

# Compiling Neural Network
sgd = optimizers.SGD(lr = 0.5)
clf.compile(optimizer = sgd, loss = 'binary_crossentropy', metrics = ['accuracy'])

clf.fit(X_train,y_train,batch_size = 1, epochs = 20)
score = clf.evaluate(X_test,y_test, batch_size = 16)
print(score)
#y_pred = clf.predict(X_test)
#y_pred = (y_pred > 0.5)#converting output into 0 and 1
#score = accuracy_score(y_pred, y_test)*100
#print(score)