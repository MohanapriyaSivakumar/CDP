#!/usr/bin/env python
# coding: utf-8

# # Threads
# 
# Using threads allows a program to run multiple operations concurrently in the same process space.
# 
# ![](../images/thread.png)
# 
# 
# ### Example

# In[1]:


import threading
def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


# ## Synchronizing Threads
# 
# * Synchronizing threads is through using a Condition object.
# * Because the Condition uses a Lock,
# * It can be tied to a shared resource, 
# * Allowing multiple threads to wait for the resource to be updated. 
# 
# ![](../images/sync.png)
# 
# ## The methods provided by the Thread class
# 
# * run() − The run() method is the entry point for a thread.
# * start() − The start() method starts a thread by calling the run method.
# * join([time]) − The join() waits for threads to terminate.
# * isAlive() − The isAlive() method checks whether a thread is still executing.
# * getName() − The getName() method returns the name of a thread.
# * setName() − The setName() method sets the name of a thread.
# 
# Synchronizing threads is through using a Condition object. 
# Because the Condition uses a Lock, it can be tied to a shared resource, allowing multiple threads to wait for the resource to be updated. 
# In this example, the consumer() threads wait for the Condition to be set before continuing. 
# The producer() thread is responsible for setting the condition and 
# notifying the other threads that they can continue.
# 

# In[2]:


import logging
import threading
import time

def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')

def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',)

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer,args=(condition,))
c2 = threading.Thread(name='c2', target=consumer,args=(condition,))
p = threading.Thread(name='p', target=producer,args=(condition,))

c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()


# In[ ]:




