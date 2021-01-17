#!/usr/bin/env python
# coding: utf-8

# # Numbers
# 
# ![](images/num.png)   
# 
# ### Examples
# 
# <li> 7, 0, -11, 2, and 5 are integers.</li> 
# 
# <li>3.14159, 0.0001, 11.11111, and even 2.0 are floats </li>
# 
# ## Divmod Function
# This built-in function returns both quotient and remainder of the 2 numbers after division

# In[1]:


divmod(7,3) 


# In[2]:


(q,r) = divmod(7,3)
q,r


# ## Binary Numbers
# 
# <li>0b or 0B is the prefix which indicates the binary number</li>
# <li>The value returned by bin() is a string. </li>
# <li>The underscore (_) may be used to make numbers more readable.</li>
# 

# In[3]:


0B11 


# In[4]:


0B1 + 0B1 


# In[5]:


bin(2345) 


# In[6]:


0b_111_0101_0011 


# ## Octal Numbers
# 
# <li>0o or 0O is the prefix which indicates the Octal number</li>
# <li>The value returned by oct() is a string. </li>
# <li>The underscore (_) may be used to make numbers more readable.</li>
# 

# In[7]:


0o3


# In[8]:


0o12 


# In[9]:


0o12 + 0o10 


# In[10]:


oct(1_234_987)


# ## HEXADECIMAL NUMBER

# <li>0x or 0X is the prefix which indicates the Hexadecimal number</li>
# <li>The value returned by hex() is a string. </li>
# <li>The underscore (_) may be used to make numbers more readable.</li>

# In[11]:


0xF


# In[12]:


hex(1_234_987) 


# ## Complex number
# 
# ![](images/cmplx.png)
# 
# A complex number is represented as a+bi where a and b are real numbers, like 7 or 12, and i is an imaginary number

# In[13]:


1+2j


# In[14]:


complex(3,-2)


# ## Number convertions
# 
# ### Examples

# In[15]:


int(9.6)


# In[16]:


float(8)


# In[17]:


complex(3,4)


# In[18]:


bin(5)


# In[ ]:




