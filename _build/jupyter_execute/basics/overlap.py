#!/usr/bin/env python
# coding: utf-8

# # Overlapping
# 
# ![](../images/over.png)
# Overlapping[function has same name]

# In[1]:


class Person:

    def name(self):
        print("person")

class Employee(Person):

    def name(self):
        super().name()

        print("employee")

y = Employee()
y.name()


# In[ ]:




