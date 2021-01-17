#!/usr/bin/env python
# coding: utf-8

# # Dictionaries
# ![](images/dict.jpg)
# 
# <li> contain a set of keys, where each key points to a value and "associative arrays" Dictionaries use the curly braces ({}) like the set </li>
#     
# {"blue": 0, "red": 1, "green": 2}
# 
# {'green': 2, 'red': 1, 'blue': 0}  
# 
# Ordering is different from that supplied above.
# 
# 
# <li>"blue" is a key. Its associated value is 0.</li>
# <li>"red" is a key. Its associated value is 1.</li>
# <li>"green" is a key. Its associated value is 2.</li>
# 
# ## create dictionary phoneNumbers

# In[1]:


phoneNumbers = {}


# ### add entries to phoneNumbers

# In[2]:


phoneNumbers['Manikarnika'] = 89564875
phoneNumbers['Laxmi Bai'] = 98653255
phoneNumbers['Gangathar Roa'] = 77885544


# ### display contents of phoneNumbers

# In[3]:


phoneNumbers


# ### delete an item

# In[4]:


del phoneNumbers['Manikarnika']
phoneNumbers


# ### check wheather an item present or not

# In[5]:


'George' in phoneNumbers


# In[6]:


'Laxmi Bai' in phoneNumbers


# ### Retrieve the keys

# In[7]:


[*phoneNumbers]


# In[8]:


names =  phoneNumbers.keys()
names


# ### Retrieve the values

# In[9]:


numbers = phoneNumbers.values() 
numbers


# ## Database using dictionaries
# The information which we'd like to include is: name, age, address, phone number, hobbies. Add entries to "friends:"
# 

# In[10]:


friends = {}

friends['Bill']  = [22, 'Black Street', 1234, [None]]
friends['Alan']  = [20, 'Brown Street', 2345, ['cycling','stamp collecting']]
friends['Tim']   = [19, 'Green Street', 3456, ['parachuting', 'video games','athletics']]
friends['Linda'] = [19, 'Brown Street', 4567, ['old movies']]
friends['Jenny'] = [21, 'Grey Street',  4567, ['old movies', 'cycling', 'video games', 'genealogy']]

#Access the data in the database:
print ("Bill's age is", friends['Bill'][0])


# In[ ]:




