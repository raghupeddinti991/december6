#!/usr/bin/env python
# coding: utf-8

# In[1]:


# printing second largest number in a list.

l=[10,20,30,40,50]
l.sort()
print('second larget number is:',l[-2])


# In[2]:


# pring 3rd largest number in a given digit.
n=input('enter the input digits:')
l=list(n)
print('third largest number in a digit:',l[-3])


# In[5]:


# printing pattern using single for loop.
n=int(input('enter input:'))
for i in range(1,n):
    print(i*10**i//9)


# In[8]:


# python program to check palindrom.
seq = input('enter input sequence:')
if (seq==seq[::-1]):
    print('Given sequence is palindrom')
else:
    print('Given sequence is not a palindrome.')
    


# In[10]:


# program for leap year or not
n=int(input('enter year:'))
if n%4==0 or n%400==0:
    print('leap year')
elif n%100==0:
    print('not leap year')
else:
    print('not leap year')


# In[ ]:




