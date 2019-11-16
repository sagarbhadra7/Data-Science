#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import numpy as np
<<<<<<< HEAD
distance = [10,15,20,25,30]
=======
#distance = [10,15,20,25,30]
>>>>>>> slave
time=[0.3,0.5,0.7,0.9,0.99]
#np_distance=np.array(distance)
#np_time=np.array(time)
speed=np_distance/np_time
print(speed)


# In[3]:


#print(speed)


# In[12]:


import numpy as np
zero_v = np.zeros((3,3))
zero_v


# In[15]:


threeD= np.arange(27).reshape((3,3,3))


# In[16]:


threeD


# In[18]:


np_distance> 15


# In[19]:


np.ravel(threeD)


# In[20]:


threeD


# In[22]:


d=np.ravel(threeD)


# In[23]:


d


# In[28]:


xd=d


# In[33]:


d.resize(5,6)


# In[34]:


d.reshape(3,9)


# In[39]:


d.resize(9,3)
d


# In[43]:


np.vsplit(d,9)


# In[ ]:




