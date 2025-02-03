#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def max_of_3(no1,no2,no3):
  if no1 > no3:
    if no1 > no2:
      if no2 > no3:
        return no1
      else:
        return no1
    else:
      return no2
  else:
    if no3 > no2:
      if no2 > no1:
        return no3
      else:
        return no3
    else:
      return no2
no1 = int(input("Please enter a number  "))
no2 = int(input("Please enter a number  "))
no3 = int(input("Please enter a number  "))
print(str(max_of_3(no1,no2,no3)) + " is the largest of the 3 numbers")

