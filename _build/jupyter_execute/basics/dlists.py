#!/usr/bin/env python
# coding: utf-8

# # Lists
# ![](../images/list.jpg)
# 
# <li>Lists are an important data type that allows you to keep a set of iterable item(s). </li>
# <li>This literally means you can have a list of items, like 1, 2, 3 or "h", "e", "l", "l", "o", "!".</li> 
# <li>A list is denoted by square brackets[ ]</li>

# In[1]:


a=[1, 2, 3, 4 ,5]
a


# In[2]:


list(range(7,13))


# In[3]:


[1, 102, 2.22, "F", 2/2, 1+2j, False] 


# In[4]:


list("hello") #convert to list


# ## Two-dimensional array
# ![](../images/2dar.jpg)
# A list can contain a two-dimensional array

# In[5]:


a = ['a1','a2']
b = ['b1','b2'] 
c = ['c1','c2'] 
L = [a,b,c]
L 


# In[6]:


L[0]


# In[7]:


L[1]


# In[8]:


L[2] 


# In[9]:


L[0][0]


# In[10]:


L[1][1]


# In[11]:


L[2][0]


# ## Three dimensional array
# ![](../images/3dar.jpg)

# In[12]:


b = ['b1','b2'] 
c = ['c1','c2']
d = ['d1','d2']
a = [b,c,d] 
B = ['B1','B2'] 
C = ['C1','C2'] 
D = ['D1','D2']
A = [B,C,D] 
array = [a,A]
array


# In[13]:


array[1]


# In[14]:


array[1][2]


# In[15]:


array[1][2][1]


# ## List manipulations
# 
# ### append

# In[16]:


spam = [1, 2, 3, 4] 
spam.append(5)
spam


# ### delete an item

# In[17]:


juice = ["a", "b", "c"] 
print(juice)
del juice[1]
print(juice)


# ### clear

# In[18]:


eggs = [1, 2, 3]
print(eggs)
eggs.clear()
print(eggs)


# ### count
# Returns the number of times a given item x is found in list 

# In[19]:


votes = ["yes", "no", "yes", "yes", "no"]
y = votes.count("yes") 
y


# ### extend
# 

# In[20]:


bacon = [1, 2, 3]
bacon.extend([4, 5, 6])
bacon


# ### pop

# In[21]:


toast = [1, 2, 3, 4, 5, 6, 7]
jelly = toast.pop(2)
print(jelly)
print(toast)


# ### remove

# In[22]:


bacon = [1, 2, 3]
bacon.remove(2) # Item removed was not at position 2. It had value 2.
bacon


# ### reverse

# In[23]:


coke = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
coke.reverse()
coke


# ## Shallow Copy
# 
# ![](../images/shallow.jpg)

# In[24]:


child=[1,2,3]
society=child  #shallow copy


# In[25]:


child


# In[26]:


society


# In[27]:


child[1]=22  #it automatically make changes in the society :)
child 


# In[28]:


society


# ## Deep Copy
# 
# ![](../images/deep.jpg)

# In[29]:


men=[1,2,3]
society=men[:] #deep copy 


# In[30]:


society


# In[31]:


men


# In[32]:


men[1]=22  # it never make changes in the society


# In[33]:


men


# In[34]:


society

