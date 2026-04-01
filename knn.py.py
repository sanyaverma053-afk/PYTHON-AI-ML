#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report


# In[22]:


data = {
    "StudyHours": [1,2,3,4,5,6,7,8],
    "Result": [0,0,0,0,1,1,1,1]
}
df = pd.DataFrame(data)
df


# In[23]:


X = df[['StudyHours']]
y = df[['Result']]


# In[24]:


X,y


# In[25]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[26]:


knn = KNeighborsClassifier(n_neighbors=3)


# In[27]:


knn.fit(X_train,y_train)


# In[28]:


y_pred=knn.predict(X_test)


# In[29]:


y_test


# In[30]:


y_pred


# In[31]:


accuracy_score(y_test, y_pred)


# In[32]:


precision_score(y_test, y_pred)


# In[33]:


recall_score(y_test, y_pred)


# In[34]:


f1_score(y_test, y_pred)


# In[35]:


print(confusion_matrix(y_test, y_pred))


# In[36]:


print(classification_report(y_test, y_pred))


# In[ ]:




