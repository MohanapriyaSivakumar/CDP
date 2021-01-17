#!/usr/bin/env python
# coding: utf-8

# # Strings
# 
# 
# <li>String written in quotes and double quotes and triple quotes</li>
# 
# <li>To concatenate use + sign</li>
# 
# ![](../images/strhello.png)
# 
# ## Indexing
# 
# 

# In[1]:


"Hello, world!"[1] 


# In[2]:


spam = "Hello, world!" 
spam[1]


# In[3]:


spam[-1]


# ## Inserting

# In[4]:


spam = "Hello, world!" 
spam = spam[:6] + " Py-" + spam[7:] 
spam


# ## Slincing

# In[5]:


spam = "I love Python." 


# In[6]:


spam[0:1]


# In[7]:


spam[2:6]


# In[8]:


spam[7:13]


# ## More operations on strings
# ### left fill with zeroes

# In[9]:


'abc def'.zfill(30) 


# ### remove leading and trailing whitespace 

# In[10]:


' 1234 '.strip()


# ### retain non-whitespace in a list 

# In[11]:


' 1234 456 23456 '.split() 


# ### split into 3 around string supplied 

# In[12]:


' 1234.567e-45 '.partition('e') 


# ### methods may be chained. 

# In[13]:


' 1234.567e-45 '.strip().partition('e') 


# ### to check the datatypes

# In[14]:


'123456'.isnumeric() 


# In[15]:


'01234567'.isdecimal() 


# In[16]:


'abcd123efg789abc'.isalnum() 


# ### Expand tabs

# In[17]:


'\t2345\t56\t678'.expandtabs() 


# In[18]:


'\t2345\t56\t678'.expandtabs(12) 


# ### fill with specified character

# In[19]:


' abcd '.center(30,'+') 


# ### Find the specified character

# In[20]:


' abcd efg abc '.find('c') 


# In[21]:


' abcd efg abc '.find('x') 


# In[22]:


' abcd efg abc '.find('c',7,13) 


# ### replace the word

# In[23]:


' The quick brown fox had a quick lunch .... '.replace('quick','lazy')

