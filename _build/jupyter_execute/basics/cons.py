#!/usr/bin/env python
# coding: utf-8

# # Constructor and Destructor
# 
# ![](../images/cons.png)
# 
# * The constructor is implemented using __init__(self) 
# * which you can define parameters that follows the self.
# * The destructor is defined using __del__(self). 
# * if you comment out the last line ‘del obj’, 
# * the destructor will not be called immediately. 
# * Instead, the Garbage Collector (GC) will take care of the deletion automatically, 
# 
# ### Example

# In[1]:


class car:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
if (__name__=="__main__"):
    c=car()
    del c


# In[ ]:




