#!/usr/bin/env python
# coding: utf-8

# In[15]:


#2
def solve(n):
    d = {'Square': lambda a : a**2,'Cube': lambda a : a**3,'Squareroot': lambda a : a**(1/2)}
    result = 0
    for k in d.keys():
        result += d[k](n)
    return result
print(round(solve(3),2))


# In[3]:


#5
WeightOnEarth = {'John':45,'Shelly':65,'Marry':35}
GMoon = 1.622
GEarth = 9.81
dict(map(lambda x: (x,round((WeightOnEarth[x]/GEarth)*GMoon,2)),WeightOnEarth))


# In[11]:


#7
d = [[1,2,3,4,8],[2,3,8,5,6],[8,4,5,3,7],[6,9,8,3],[9,12,3,7,6,8,4,6,21,1,6]]
set(d[0]).intersection(*d)


# In[12]:


#9
x = map(lambda x:x.upper(),['True','FAlse','tRUe','False','false'])
upperlist=list(x)
print(upperlist)


# In[22]:


#8
from itertools import accumulate
result = accumulate([9,8,7,6,5],lambda x,y:(x+y)/2)
for res in result:
    print(res)


# In[20]:


#10
dateslist = ['17-12-1997','22-04-2011','01-05-1993','19-02-2020']
l=[]
for i in dateslist:
    l.append(i[6:])
print(l)


# In[ ]:




