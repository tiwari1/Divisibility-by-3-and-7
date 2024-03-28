#!/usr/bin/env python
# coding: utf-8

# In[4]:


x=int(input("enter the number--> ")) #x=15 #x=21 #x=14 #x=11
if x%3==0: # 15%3==0 True # 21%3==0 True # 14%3==0 False #11%3==0 False
    if x%7==0: # 15%7==0 False  # 21%7==0 True
        print("Number is divisible by both")
    else:
        print('Number is divisible by 3 but not with 7')
elif x%7==0: #14%7==0 True # 11%7==0 False
    print('Number is divisble by 7 but not with 3')
else:
    print('Number is not divisble by both')


# In[ ]:




