#!/usr/bin/env python
# coding: utf-8

# # Exception Handling
# 
# * We don’t live in the perfect world
# * Computers can crash, monitors can short, hard drives can corrupt
# * To fix the problem
# 
# ![](../images/excep.png)
# 
# ## Name Error

# In[1]:


try:
    print(spam)
except:
    print("spam isnt defected")


# ## Else statement
# 
# * Python has built in 20 exceptions each problem can be addressed
# * i.e. unicode decode error, type error, timeout error..,
# * Else statement like while or for loop
# 

# In[2]:


try:
    sp=7
    print("sp:%d"%(sp))
except:
    print("some error")
else:
    print("everthing is fine")


# ## Finally statement
# 
# It executes after try statement fails or ends
# 

# In[3]:


try:
    print("soda")
except:
    print("some error")
finally:
    print("cleaning")


# ## Some exceptions
# 
# * Name error: a==6 anot defined
# * Syntax error: if a==6 print
# * Type error: str not int
# * Index error: list index out of range
# * Value error: ’maybe ‘ is not in list
# * Key error
# * Overflowerror: int greater than maxmium
# * Zerodivisionerror: 2/0
# 

# In[ ]:




