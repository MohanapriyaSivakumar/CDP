#!/usr/bin/env python
# coding: utf-8

# # Sets
# Sets are mutable sequences, like lists. 
# ![](../images/set.jpg)

# In[1]:


eggs = {1, 2, 1, 3, 5, 2, 7, 3, 4}
eggs


# ## Initialize set

# In[2]:


b = set('alacazam')
b


# ## Subset
# checks the first set is subset to next or not

# In[3]:


{'a', 'b', 'c'}.issubset( {'a', 'b', 'c', 'd'} )


# ## symmetric difference
# it leaves the identical items in both sets and returns different items in both sets

# In[4]:


newSet = {'a', 'b', 'c', 'g'}.symmetric_difference( {'a', 'b', 'h', 'i'} )
newSet


# ## difference
# it leaves the identical items in first sets and returns different items in first sets

# In[5]:


newSet = {'a', 'b', 'c', 'g','q', 'x'}.difference( {'g', 'b', 'h'},'bczg' ) 
newSet


# ## Intersection
# returns the common items in both sets

# In[6]:


newSet = {'a', 'b', 'c', 'g'}.intersection( {'g', 'b', 'h'},'abczg' )
newSet 


# ## Union
# combine both the sets

# In[7]:


newSet = {'a', 'b', 'c', 'g'}.union( {'b', 'h'},'abcz', [1,2,3] )
newSet

