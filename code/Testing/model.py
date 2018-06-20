import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from time import time
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

fr1 = pd.read_csv(r"Test.csv")
fr2 = pd.read_csv(r"outputDataSetFinal.csv")
#print(fr1)
features_train = fr2[['TankName','Weekday','Times','Day','MinutesElapsedDay']]
labels_train = fr2['Open']
features_test = fr1[['TankName','Weekday','Times','Day','MinutesElapsedDay']]
labels_test = fr2['Open']

lab = LabelEncoder()
features_train.iloc[:,:1] = lab.fit_transform(features_train.iloc[:,:1])

features_test.iloc[:,:1] = lab.fit_transform(features_test.iloc[:,:1])

clf = DecisionTreeClassifier(min_samples_split=10)
t0 = time()
clf.fit(features_train,labels_train)
t1 = time()
print("Time required in training: ", round(t1-t0,3))
pred = clf.predict(features_test)
print("Accuracy: ", accuracy_score(pred,labels_test))
