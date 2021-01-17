#!/usr/bin/env python
# coding: utf-8

# # File
# 
# * A file is some information or data which stays in the computer storage devices.
# * Python gives you easy ways to manipulate these files.
# * Generally we divide files in two categories, text file and binary file.
# * Text files are simple text where as the binary files contain binary data which is only readable by computer.
# 
# ## Opening the file 

# In[1]:


ifile=open("test.txt")


# ## Reading the file

# In[2]:


print(ifile.read())


# ## Closing the file

# In[3]:


ifile.close()


# ## Appending the file

# In[4]:


ifile=open("test.txt",'a') # a means append
c=ifile.tell() # tells the position of pointer in file
print(c)
a="...Extra data..."
ifile.write(a)
ifile.close()


# In[5]:


ifile=open("test.txt")
print(ifile.read())
ifile.close()


# ## readline
# 
# ### Example
# 

# In[6]:


f=open('test.txt')
s=f.readline() #read line by line
print(s)


# ## Seek
# 
# seek a particular text in the file
# 
# ### syntax
# 
# f.seek(offset, from)
# 
# Here, the from parameter takes the following values:
# 
#     0 : offset calculated from the beginning
# 
#     1 : offset calculated from the current position
#     
#     2 : offset calculated from the end
# 
# Assuming that myfile.txt contains "Hello World" text, the following example demonstrates the seek() method.
# 
# 
# 
# ### Example

# In[7]:


f=open("test.txt","r+")
f.seek(46,0) #seek from 46 th letter
lines=f.readlines()
for line in lines:
    print(line)
f.close()


# ## To know the file closed or not

# In[8]:


f = open ('test.txt')
f.closed


# ## To know file readable or not
# We expect the file to be readable. It was opened without error.

# In[9]:


f.readable()


# ## To know file Seekable or not
# We can cause the file to seek to any desired position within the file
# 

# In[10]:


f.seekable()


# ## tell()
# Internal pointer is at beginning of file. This is expected after opening file.

# In[11]:


f.tell()


# ## To know file writable or not
# Not writable, opened for reading only. An attempt to write or truncate raises OSError.
# 

# In[12]:


f.writable()

