#!/usr/bin/env python
# coding: utf-8

# # Lambda Function
# 
# * Python supports the creation of anonymous of function (i.e. functins that are not bound to the name)
# * It is powerful when it is integrated with filter(), map() and reduce()
# * It does not have return statement
# 
# ### Example
# 

# In[1]:


g=lambda x: x**2


# In[2]:


g(4)


# In[3]:


g(8)


# ## Filter
# It creates a list of elements for which a functions returns true
# 
# ### Example
# 

# In[4]:


z=[2,18,9,22,17,24,8,12,27]
list( filter(lambda x:x%3==0,z))  #filter the number divisible by 3


# ## Map
# Map applies a function to all the items in an input_list
# 
# ### Example

# In[5]:


z=[2,18,9,22,17,24,8,12,27]
list(map(lambda x:x**2,z)) #power all the value present in z


# ## Reduce
# * It is a reall useful function for performing some computation on a list and returning the result
# * It applies a rolling computation to sequential pairs of values in a list
# 

# In[6]:


z=[2,18,9,22,17,24,8,12,27]
from functools import reduce  #import modules
p=reduce((lambda x,y:x+y),z)  #add all the value present in z
p


# 
