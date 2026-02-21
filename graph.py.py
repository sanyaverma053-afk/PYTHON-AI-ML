#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,25]
plt.plot(x,y)
plt.show()


# In[4]:


names=['A','B','C']
marks=[80,90,70]
plt.bar(names,marks)
plt.show()


# In[5]:


marks=[45,55,65,75,85,95]
plt.hist(marks)
plt.show()


# In[6]:


x=[1,2,3,4]
y=[10,15,20,25]
plt.scatter(x,y)
plt.show()


# In[9]:


labels=['CS','IT','ECE']
students=[40,35,25]
plt.pie(students,labels=labels)
plt.show()


# In[ ]:




