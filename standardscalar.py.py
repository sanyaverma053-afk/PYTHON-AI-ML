#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
graph={
    "type_of_house":["flat","pg","flat","pg","flat"],
    "area_of_house":[55.25,77.89,82.33,49.44,50.00],
    "house_size":[2,5,10,1,2],
    "cost":[50000,80000,100000,45000,50000],
}
print("original date-\n")
df=pd.DataFrame(graph)
print(df)
print("\n")

n1=np.array(df["area_of_house"])
n2=np.array(df["cost"])
mean_n1=np.mean(n1)
mean_n2=np.mean(n2)
std_n1=np.std(n1)
std_n2=np.std(n2)
df["area_of_house"]=((df["area_of_house"]-mean_n1)/(std_n1)).round(2)
df["cost"]=((df["cost"]-mean_n2)/(std_n2)).round(2)
print("new data-\n")
print(df)


# In[ ]:




