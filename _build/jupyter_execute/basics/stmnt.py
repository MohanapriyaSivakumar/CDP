#!/usr/bin/env python
# coding: utf-8

# # Statements
# 
# ## Input and Output statements
# To get input from user <b>input() statement</b> will be used
# ### Example

# In[1]:


a=input()
a


# ### get the input with message as follows

# In[2]:


a=input("Enter your age")
a


# ## Print the output using print statement
# ### Example

# In[3]:


a=input("Enter your age")
print(a)


# ## Print the output with some formatting

# In[4]:


a=input("Enter your age: ")
print("your age is "+a)


# ## Print the output with some formatting with more than one variable

# In[10]:


a=int(input("Enter your age: "))
b=input("Enter your name: ")
print("your name is %s and your age is %d"%(b,a))


# ## Multiline statement
# the Continuation character (\) is used for multiline statement.
# 
# Statements continued with in the brackts [],(),{} do not need to use line continution character
# 
# ### Example:
# 
# Days=[‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’,‘Saturday’, ‘Sunday’] 
# 

# In[13]:


item_one=20
item_two=30
item_three=40
Total=item_one+item_two+item_three
Total=item_one+item_two+item_three
Total


# ## Quotation
# single, double, triple quotes to denote string literals.
# 
# Triple quotes are used to span the string across multiple lines.
# 
# Word=‘hello’
# 
# Sentence=“this is a sentence”
# 
# Paragraph=“””this is a paragraph this made up of multiple lines and strings”””
# 

# ## comments
# 
# ### Single line Comments
# 
# #This is a long comment 
# #and it extends 
# #to multiple lines 
# or
# 
# ### Multiline Comments
# """This is also a perfect 
# example of 
# multi-line comments""" 
# 

# ## Multiple statements
# 
# Multiple statements on a single line
# 
# <b>Example:</b>
#     
# Import sys; x=‘ets’ ; print x
# 

# Groups of individual statements in a single block(if,while etc.,) called <b>suits</b> 
# ![](../images/suit.jpg)

# In[ ]:




