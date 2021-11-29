#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_request")
df = pd.read_csv('House.csv')
df2 = pd.DataFrame(columns=["Price", "Address_x","Address_y", "Bedrooms", "Baths","Area"])

for i in range(0,df.shape[0]):
    if df.loc[i,'Address'] != None:
        location = geolocator.geocode(df.loc[i,'Address'])
        if location:
            cardAddress_x = location.latitude
            cardAddress_y = location.longitude
            cardPrice = df.loc[i,'Price']
            cardBedrooms = df.loc[i,'Bedrooms']
            cardBaths = df.loc[i,'Baths']
            cardArea = df.loc[i,'Area']
            temp = pd.DataFrame([[cardPrice, cardAddress_x, cardAddress_y, cardBedrooms, cardBaths, cardArea]],columns=["Price", "Address_x","Address_y", "Bedrooms", "Baths","Area"])
            df2 = df2.append(temp)
        else:
            list = df.loc[i,'Address'].split(",")
            length =len(list)
            addressArea=list[length-2]
            print("second last array element ",list[length-2])
            location=geolocator.geocode(addressArea)
            if location:
                cardAddress_x = location.latitude
                cardAddress_y = location.longitude
                cardPrice = df.loc[i,'Price']
                cardBedrooms = df.loc[i,'Bedrooms']
                cardBaths = df.loc[i,'Baths']
                cardArea = df.loc[i,'Area']
                temp = pd.DataFrame([[cardPrice, cardAddress_x, cardAddress_y, cardBedrooms, cardBaths, cardArea]],columns=["Price", "Address_x","Address_y", "Bedrooms", "Baths","Area"])
                df2 = df2.append(temp)
            else:
                print("--ADDRESS LOCATION NOT FOUND",df.loc[i,'Address'])
                latitude = 0
                longitude = 0
                cardAddress_x = latitude
                cardAddress_y = longitude
                cardPrice = df.loc[i,'Price']
                cardBedrooms = df.loc[i,'Bedrooms']
                cardBaths = df.loc[i,'Baths']
                cardArea = df.loc[i,'Area']
                temp = pd.DataFrame([[cardPrice, cardAddress_x, cardAddress_y, cardBedrooms, cardBaths, cardArea]],columns=["Price", "Address_x","Address_y", "Bedrooms", "Baths","Area"])
                df2 = df2.append(temp)

print(df2)
df2.to_csv('House2.csv',index = False,header = True)            


# In[13]:


import numpy as np
import pandas as pd

df = pd.read_csv('House2.csv')
df3 = pd.DataFrame(columns=["Price", "Address_x","Address_y", "Bedrooms", "Baths","Area"])
#columns=["Price", "Address_x","Address_y", "Bedrooms", "Baths","Area"]

for i in range(0,df.shape[0]):
    if df.loc[i,'Price'] == None or df.loc[i,'Price'] < 1000 or np.isnan(df.loc[i,'Price']):
        pass
    elif df.loc[i,'Address_x'] == 0.0:
        pass
    else:    
        df3 = df3.append(df.loc[i])

print(df3)
Area_avg = int(np.mean(df3.loc[:,'Area']) + 0.5)
Baths_avg = int(np.mean(df3.loc[:,'Baths']) + 0.5)
Bedrooms_avg = int(np.mean(df3.loc[:,'Bedrooms']) + 0.5)

df3['Area'] = df3['Area'].fillna(Area_avg)
df3['Bedrooms'] = df3['Bedrooms'].fillna(Bedrooms_avg)
df3['Baths'] = df3['Baths'].fillna(Baths_avg)

print(df3)
df3.to_csv('House3.csv',index = False,header = True)


# In[ ]:




