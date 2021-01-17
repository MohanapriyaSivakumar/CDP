#!/usr/bin/env python
# coding: utf-8

# # Classes and Objects
# 
# ![](../images/oop2.jpg)
# 
# ## creating classes and objects

# In[1]:


class Car:
    def brake(self):
        print ("Brakes")

    def accelerate(self):
        print ("Accelerating")


# ## Creating Objects

# In[2]:



car1 = Car() # car 1 is my instance for the first car
car2 = Car()


# ## And use the object methods like
# 

# In[3]:


car1.brake()
car1.accelerate()


# In[ ]:




