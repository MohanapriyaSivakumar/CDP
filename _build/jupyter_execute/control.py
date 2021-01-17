#!/usr/bin/env python
# coding: utf-8

# # Control Statements
# 
# Control statements enable us to specify the flow of program control; ie, the order in which the instructions in a program must be executed.
# 
# ![](images/cntrl.jpg)

# ## Control flow constructs
# 1. if statements
# 2. while loop
# 3. for in loop
# 4. break statement
# 5. pass statement
# 6. continue statement
# 
# ### if statement
# 
# ![](images/ifp.png)
# 
# ### Example
# 
# Finding greatest of 2 numbers

# In[1]:


a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))

if(a>b):
    print("number1 is greater than number2")
else:
    print("number2 is greater than number1")


# ## if... elif..else
# ### Example
# finding greatest number of 3 numbers

# In[8]:


a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))
c=int(input("Enter the number3: "))

if(a>b and a>c):
    print("number1 is greater")
elif(b>a and b>c):
    print("number2 is greater")
else:
    print("number3 is greater")


# ## While loop
# * while loop Repeats a statement or group of statements while a given condition is true. 
# * It tests the condition before executing the loop body.
# 
# ### Example
# 

# In[11]:


a=0
while(a<10):
    print(a)
    a+=1


# ## For loop
# for loop Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.
# 
# ### Example

# In[14]:


for a in range(5 ,10):
    print(a)


# ## Pass Statement
# * Pass is a Placeholder for python
# 
# * If you write a code for looping but u want to implement in future.
# 
# * Empty body of loop will give an error
# 
# * So we can write pass inside it means ”does nothing”
# 
# 
# ### Example

# In[17]:


s={2,3,4,55,66}
for v in s:
    pass


# ## Continue statement
# 
# * The continue statement in C programming works somewhat like the break statement. 
# 
# * Instead of forcing termination, it forces the next iteration of the loop to take place, skipping any code in between.
# 
# ### Example
# 

# In[22]:


l=[1,2,3,4,5,6]
for i in range(len(l)):
    if(l[i]==4):
        continue
    print(l[i])


# ## Break Statement
# * The break is a keyword in C which is used to bring the program control out of the loop.
# * The break statement is used inside loops.
# * The break statement breaks the loop one by one, i.e., in the case of nested loops, it breaks the inner loop first and then proceeds to outer loops.
# 
# ### Example

# In[24]:


l=[1,2,3,4,5,6]
for i in range(len(l)):
	if(l[i]==4):
		break
	print(l[i])


# In[ ]:




