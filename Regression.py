#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
x=np.array([10,20,30,40,50]).reshape(-1,1)
y=np.array([5,10,15,20,25])
model=LinearRegression()
model.fit(x,y)
y_predict=model.predict(x)
print("slope(m):",model.coef_[0])
print("intercept(c):",model.intercept_)
plt.scatter(x,y,color="blue")
plt.plot(x,y_predict,color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("linear regression")
plt.show()


# In[ ]:




