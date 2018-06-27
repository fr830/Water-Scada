import pandas as pd
from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, LassoLarsCV
from sklearn.model_selection import cross_val_score
import numpy as np
from flow import str_to_num, format_data
import matplotlib.pyplot as plt
#import flow

db0 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\ml11.xlsx')
db1 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\ml12.xlsx')
db2 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\a10.xlsx')
db3 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\a20.xlsx')
db4 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\a30.xlsx')
frames = [db0,db1,db2,db3,db4]
db = pd.concat(frames,ignore_index=True)

fr1 = db.iloc[:len(db),1]
fr1 = format_data(fr1,'fr', 0, len(db))
X_train = fr1[:len(fr1),:-1]
y_train = fr1[:len(fr1),-1]

X_train = pd.DataFrame(X_train)
y = pd.isnull(X_train).any(1).nonzero()[0]
X_train.dropna(inplace=True)
y_train = np.delete(y_train,y,0)
    
def rmse_cv(model):
    rmse= np.sqrt(-cross_val_score(model, X_train, y_train, scoring="neg_mean_squared_error", cv = 5))
    return(rmse)

model_ridge = Ridge()

#to pick the best alpha

alphas = [0.05, 0.1, 0.3, 1, 3, 5, 10, 15, 30, 50, 75]
cv_ridge = [rmse_cv(Ridge(alpha = alpha)).mean() 
            for alpha in alphas]

cv_ridge = pd.Series(cv_ridge, index = alphas)
cv_ridge.plot(title = "Validation - Just Do It")
plt.xlabel("alpha")
plt.ylabel("rmse")



