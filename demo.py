#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=eval(input('Enter the no: '))
print(a)


# In[16]:


a=eval(input('Enter the no: '))
s=0
for x in range (2,a):
    if(a%x==0):
        s=1
        
if(s==1):
    print("Not Prime")
else:
    print("Prime")
    

