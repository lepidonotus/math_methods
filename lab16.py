#!/usr/bin/env python
# coding: utf-8

# In[19]:


import math
import matplotlib.pyplot as plt
import numpy


# In[8]:


p_to_q = 3


# In[30]:


cH = 35
cM = 65




# In[38]:


p = cH / (cH + cM)
q = cM / (cH + cM)




# In[39]:


#cH = 5
#cM = 95

print("p = ", p)
print("q = ", q)


# In[40]:


p4 = p ** 4
p3q_4 = 4 * (p ** 3) * q
p2q2_6 = 6 * (p ** 2) * (q ** 2)
pq3_4 = 4 * p * (q ** 3)
q4 = q ** 4

print(p4, p3q_4, p2q2_6, pq3_4, q4)


# In[41]:


Y = [p4, p3q_4, p2q2_6, pq3_4, q4]
Y = numpy.array(Y)
Y *= 100
Y


# In[42]:


X = ['ЛДГ-1', 'ЛДГ-2', 'ЛДГ-3', 'ЛДГ-4', 'ЛДГ-5']


# In[44]:

plt.ylabel('%')
plt.subplot(121)
plt.plot(X, Y)
plt.subplot(122)
plt.bar(X, Y)
plt.show()

input()

# In[ ]:




