#!/usr/bin/env python
# coding: utf-8

# # Overloading
# 
# * use +  operator for adding numbers and at the same time to concatenate strings. 
# * Defining methods for operators is known as operator overloading. 
# * For e.g. To use +  operator with custom objects  you need to define a method called __add__  .
# 
# ![](images/overl.png)

# ![](images/overl1.png)

# In[1]:



class Circle:
    def __init__(self, radius):
        self.__radius = radius
 
    def getRadius(self):
        return self.__radius
 
    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius )
 
c1 = Circle(4)
print(c1.getRadius())
 
c2 = Circle(5)
print(c2.getRadius())
c3 = c1 + c2 
# This became possible because we have overloaded + operator by adding a    method named __add__
print(c3.getRadius())


# In[ ]:




