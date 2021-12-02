#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error ,r2_score


# In[12]:


df =pd.read_csv("House.csv")
df.columns= ['price','lattitude','longitude','bedrooms','bathrooms','area']

latitude=df.iloc[:,1]
longitude=df.iloc[:,2]
bedrooms = df.iloc[:,3] ## bedrooms
bathrooms = df.iloc[:,4] ## bathrooms
area = df.iloc[:,5] ## area m2
price= np.array(df.iloc[:,0])
features= np.column_stack((latitude,longitude,bedrooms,bathrooms,area))


# In[13]:




actualY = []
predictedY =[]
featuresCollected=[]
kf = KFold(n_splits=2)

for train,test in kf.split(features):
    
        modelBaseline = DummyRegressor(strategy ="mean").fit(features[train],price[train])
        predY = modelBaseline.predict(features[test])
        
        
        fig,ax = plt.subplots()
        ax.set_title("Features versus Price")
        ax.plot(features[test],price[test],'+',color='green',label='Actual Price')
        ax.plot(features[test],predY,'o',color='red',label='Predicted price')
        plt.xlabel('Features')
        plt.ylabel('Price')
        leg=ax.legend()
        plt.show()
        
        roundedY = [np.round(y) for y in predY]

        predictedY = predictedY +roundedY
        actualY =  actualY + price[test].tolist()
  
    
MSE = mean_squared_error(actualY,predictedY)
r2 =r2_score(actualY,predictedY)
    
print("Value of mse ", MSE)
print("Value of r2 score",r2 )


# In[ ]:




