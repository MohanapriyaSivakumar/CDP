#!/usr/bin/env python
# coding: utf-8

# # User Defined Function
# 
# * To create the function use def keyword followed by function name and () and colon
# 
# * Define it with indent
# 
# ### Example

# In[1]:


def square(x):
    return(x**2)
print(square(9))


# ## Positional Arguments
# 
# ### Example

# In[2]:



def square(*a):
    print(format(a))
square(1,2)
square(1,2,3)
square(1,2,3,4)


# ## Recursive Function
# 
# * In Python, we know that a function can call other functions. 
# * It is even possible for the function to call itself. These types of construct are termed as recursive functions.
# 
# ### Example

# In[3]:


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


# In[ ]:




