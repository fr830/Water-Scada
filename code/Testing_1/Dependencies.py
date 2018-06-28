import pandas as pd
from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, LassoLarsCV
from sklearn.model_selection import cross_val_score
import numpy as np
from flow import str_to_num, format_data
import matplotlib.pyplot as plt
#import flow
import matplotlib

#db0 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\ml11.xlsx')
#db1 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\ml12.xlsx')
db2 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\a10.xlsx')
db3 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\a20.xlsx')
db4 = pd.read_excel(r'G:\Water_Skada\code\Testing_1\a30.xlsx')
frames = [db2,db3,db4]
db = pd.concat(frames,ignore_index=True)

fr1 = db.iloc[:len(db),1]
fr1 = format_data(fr1,'fr', 0, len(db))


def rmse_cv(model, X_train, y_train):
    rmse= np.sqrt(-cross_val_score(model, X_train, y_train, scoring="neg_mean_squared_error", cv = 5))
    return(rmse)


def main(cols, i):
    X_train = fr1[:len(fr1),cols]
    y_train = fr1[:len(fr1),i]
    
    X_train = pd.DataFrame(X_train)
    y = pd.isnull(X_train).any(1).nonzero()[0]
    X_train.dropna(inplace=True)
    y_train = np.delete(y_train,y,0)

    y_train = np.log1p(y_train)

    #model_ridge = Ridge()

    #to pick the best alpha

    #alphas = [0.05, 0.1, 0.3, 1, 3, 5, 10, 15, 30, 50, 75]
    #cv_ridge = [rmse_cv(Ridge(alpha = alpha)).mean() 
            #for alpha in alphas]

    #cv_ridge = pd.Series(cv_ridge, index = alphas)
    #cv_ridge.plot(title = "Validation")
    #plt.xlabel("alpha")
    #plt.ylabel("rmse")
    model_lasso = LassoCV(alphas = [1, 0.1, 0.001, 0.0005]).fit(X_train, y_train)
    print(rmse_cv(model_lasso, X_train, y_train).mean())
    
    coef = pd.Series(model_lasso.coef_, index = X_train.columns)
    print("Lasso picked " + str(sum(coef != 0)) + " variables and eliminated the other " +  str(sum(coef == 0)) + " variables")
    
    imp_coef = pd.concat([coef.sort_values().head(10),coef.sort_values().tail(10)])
    
    #features coefficient
    
    matplotlib.rcParams['figure.figsize'] = (8.0, 10.0)
    imp_coef.plot(kind = "barh")
    plt.title("Coefficients in the Lasso Model")
    plt.savefig("Important features"+str(i)+".pdf")

    #residuals
    
    matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)

    preds = pd.DataFrame({"preds":model_lasso.predict(X_train), "true":y_train})
    preds["residuals"] = preds["true"] - preds["preds"]
    preds.plot(x = "preds", y = "residuals",kind = "scatter")
    plt.savefig("Residuals"+str(i)+".pdf")
    
cols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(0,len(cols)):
    