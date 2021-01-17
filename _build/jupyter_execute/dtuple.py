#!/usr/bin/env python
# coding: utf-8

# # Tuples
# In Python, a tuple is an immutable sequence
# ![](images/tup.jpg)

# In[1]:


spam = 1, 2, 3 # default datatype is tuple
spam


# ### We cannot change the value of tuple

# In[2]:


spam=(1,2,3)
spam[1]=22


# ### To store one value in tuple

# In[12]:


b=1,
b


# ## Indexing

# In[13]:


("A", "B", "C", "D", "E", "F")[0]


# ## Slicing

# In[8]:


("A", "B", "C", "D", "E", "F")[1:]

