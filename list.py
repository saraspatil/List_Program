## 1. interchange first and last element

l = [1,2,3,4,5,6]

res = []


#1 method: (unpacking of data)
a = [l[0]]
b= l[1:-1]
c = [l[-1]]

res = c+b+a

#2 method : (in built swap method)
l[0],l[-1]=l[-1],l[0]
l
===================================================
## 2. swap two element in a list

l

p1 = 1 
p2 = 3

#1 method:
l[p1-1],l[p2-1] = l[p2-1],l[p1-1]

#2 method:
a = []
b = []
for i in  l:
    if i == l[p1-1]:
        a.append(i)
    elif i == l[p2-1]:
        b.append(i)
l[p1-1] = b[0]
l[p2-1] = a[0]
=========================================================================
## 3. swap elements in string list

t = ['gfg','is','best','for','geek']

#1 method: list comprehension + replace()
[i.replace('g','h').replace('e','g').replace('h','e') for i in t]
==============================================================================
## 4. ways to find len of list

l

#1
len(l)

#2
l.index(l[-1])+1

#3
list(enumerate(l))[-1][0]+1

#4
c = 0
for i in l:
    c+=1
c

#5
[i for i in range(len(l)+1)][-1]

#6 
list(range(len(l)+1))[-1]
=======================================================
## 5. maximum of two numbers in python

l

a =2
b = 6

#1 method:
max(a,b)

#2 method:
sorted([a,b])[-1]
=============================================================
## 6. ways to check element is present in the list

l

e = 6

#1 conditional method:
if e not in l:
    print('not present')
else:
    print('present')

#2 method:
if l.count(e)>=1:
    print('present')
else:
    print('not present')

#3 method:
if len([i for i in l if i==e])>=1:
    print('present')
else:
    print('not present')

# 4 method:
l1 = []
for i in l:
    if i == e:
        l1.append(i)
if len(l1)>=1:
    print('present')
else:
    print('not present')
=======================================================
## 6.5 revese the list:

#1 using pop and range index
res = [l.pop() for i in range(len(l))]


res
========================================================
## 7. different way to clear a list 

l= [1,2,3,4,5,6,6]
l

#1 method:
for i in range(len(l)):
    l.pop()
l

#2 method:
l.clear()


#3 method using while loop:
while len(l)!=0:
    for i in l:
        l.remove(i)
l

#4 using '*=0' assignment operator
l*=0
l

#5 method: del it deletes object also
del(l)
==================================================
## 8. count occurance of an element

from collections import Counter

l

#1 method
[i[1] for i in list(Counter(l).items()) if i[0] == 6][0]

#2 method
for i in l:
    if i == 6:
        res = l.count(i)
res

#3 method
l.count(6)

#4 
c=0
for i in l:
    if i == 6:
        c+=1
print(c)
==============================================================
## 9. find sum and avg:

l

#1 
sum(l)

avg = sum(l)/len(l)
avg

#2 method:
import numpy as np

np.array(l).mean()

np.array(l).sum()

np.cumsum(l)[-1]

#3 method:
sum = 0
for i in l:
    sum+=i
print(sum)
print(sum/len(l))

#4 method:
import math

math.fsum(l)

math.fsum(l)/len(l)
======================================================
## 10. sum of number digit in list:

x = [11,22,33,44,55,66]

#1 for loop:
l1 = []
for i in x:
    l1.append(sum([int(j) for j in str(i)]))
l1      

#2 metho: nested list comprehension:
[sum([int(j) for j in str(i)]) for i in x]
==========================================================
## 11. multiply all numbers in a list

#1 method:
import math

math.prod(l)

#2 method:
prod = 1
for i in l:
    prod*=i
prod

#3 
import numpy as np

np.cumproduct(l)[-1]

#4 method:
from functools import reduce

reduce((lambda x,y:x*y ),l)
=================================================================
## 12. find smallest number in a list

l

#1 method
min(l)

#2 method
sorted(l)[0]

#3 method
l.sort(reverse=False)
l[0]

#4 method
[i for i in l if i==min(l)][0]
==================================================================
## 13. largest number in list

#1 method:
max(l)

#2 method:
sorted(l)[-1]

#3 ethod:
l.sort(reverse=True)
l[0]

#4 method:
[i for i in l if i==max(l)][0]
====================================================================
## 14. second largest number in a list

l

#1 method:
res=set(l)
list(res)[-2]

#2 method:
l1 =[]
for i in l:
    if i not in l1:
        l1.append(i)
l1.sort()
l1[-2]
=======================================================================
## 15. print even number in a list

l

#1 list comprehension:
[i for i in l if i%2==0]

#2 for loop:
l1 =[]
for i in l:
    if i % 2==0:
        l1.append(i)
print(l1)

#3 method:
even=list(map(lambda x:x if x%2==0 else 'nan', l))

[i for i in even if type(i)== int]

#OR
import pandas as pd

e = pd.DataFrame(even)
e.dropna(inplace = True)
[int(i)for i in np.array(e)]

#4 method:
list(filter(lambda x: x%2==1,l))
=========================================================================
## 16. print odd number in python

l

#1 method:
sorted([i  for i in l if i%2==1])

#2 method:
l1 =[]
for i in l:
    if i%2==1:
        l1.append(i)
l1.sort()
l1

#3 method:
odd=list(map(lambda x: x if x%2==1 else 'n',l))

res=sorted([ i for i in odd if type(i)==int])

res

#4 method:
list(filter(lambda x: x%2==1,l))
=========================================================================
## 17. to print all even number in range:

s = 10
e = 21

#1 method:
[i for i in range(s,e) if i%2==0]

#2 for loop:
l1=[]
for i in range(s,e):
    if i % 2==0:
        l1.append(i)
l1

#3 method:
list(filter(lambda x: x%2==0 , range(s,e)))

#4 method:
e1=list(map(lambda x: x if x%2==1 else 'n',range(s,e)))

[i for i in e1 if type(i)==int]
==========================================================================
## 18. python programe to find even and odd in a list:

#1 method:
print('even is:',len([i for i in l if i%2==0]))
print('odd is:',len([i for i in l if i%2==1]))

#2 method:
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
print('eve:',len(l1),'odd:',len(l2))

#3 method:
print('even is:',len(list(filter(lambda x: x%2==0,l))))
print('odd is:',len(list(filter(lambda x: x%2==1,l))))

#4 method:
print('even is:',len([i for i in list(map(lambda x: x if x%2==0 else 'n',l)) if type(i)==int]))

print('odd is:',len([i for i in list(map(lambda x: x if x%2==1 else 'n',l)) if type(i)==int]))
======================================================================================================
## 19. print positive number in list:

li = [-1,-2,-3,-4,-5,1,2,3,4,5]

#1 method:
[i for i in li if i>0]

#2 method:
l1 = []
for i in li:
    if i>0:
        l1.append(i)
l1

#3 method:
list(filter(lambda x:x>0,li))

#4 method:
[i for i in list(map(lambda x: x if x>0 else 'n',li)) if type(i)==int]
======================================================================================================
## 20. print negative number in a list:

li

#1 method:
[i for i in li if i<0]

#2 method:
l1=[]
for i in li:
    if i<0:
        l1.append(i)
l1

#3 method:
list(filter(lambda x:x<0,li))

#4 method:
[i for i in list(map(lambda x: x if x<0 else 'n',li)) if type(i)==int]
==============================================================================================
## 21. print all positive number in a range:

s = -10
e = 11

#1 method:
[i for i in range(s,e) if i>0]

#2 method:
l1=[]
for i in range(s,e):
    if i>0:
        l1.append(i)
l1

#3 method:
list(filter(lambda x: x>0, range(s,e)))

#4 method:
[i for i in list(map(lambda x: x if x>0 else 'n',range(s,e))) if type(i)==int]
====================================================================================
## 22. to count positive and negative element in a list

#1 method:
print('positive:',len([i for i in range(s,e) if i>=0]))
print('negative:',len([i for i in range(s,e) if i<0]))

#2 method:
l1=[]
l2=[]
for i in range(s,e):
    if i >=0:
        l1.append(i)
    else:
        l2.append(i)
print('positive:',len(l1))
print('negative',len(l2))

#3 method:
print('positive:',len(list(filter(lambda x: x>=0,range(s,e)))))
print('negative:',len(list(filter(lambda x: x<0,range(s,e)))))

#4 method:
print('positive:',len([i for i in list(map(lambda x:x if x>=0 else 'n',range(s,e))) if type(i)==int]))
print('negative:',len([i for i in list(map(lambda x:x if x<0 else 'n',range(s,e))) if type(i)==int]))
=============================================================================================================
## 23. remove multiple element from list:

l = [1,2,3,4,5,6,6]

re = [1,4]

#1 method:
[i for i in l if i not in re]

#2 method:
l1=[]
for i in l:
    if i not in re:
        l1.append(i)
l1

#3 method:
[l.remove(i) for i in re ]
l

#4 method:
list(filter(lambda x: l.remove(x),re))
l
========================================================================================================
## 24. program to remove empty tuple from a list:

t = [(),('pratik','p'),(),('santosh','s'),(),('salaskar','s'),(",")]

#1 method:
[tuple(i) for i in t if len(i)>=1]

#2 method:
l1 =[]
for i in t:
    if i !=():
        l1.append((i))
l1

#3 method
list(filter(None,t))

#4 method:
[i for i in t if i != ()]
=======================================================================================
## 25. to print duplicates in a list:
    

#1 method:
list({i for i in l if l.count(i)>1})

#2 method:
l1=[]
for i in l:
    if l.count(i)>1:
        l1.append(i)
set(l1)

#3 method:
set(filter(lambda x:l.count(x)>1,l))

#4 method:
from collections import Counter

res = Counter(l)

[i[0] for i in list(res.items()) if i[1]>1]
=======================================================================================
## 26. remove empty list from list of list:

x = [[1],[2],[3],[4],[],[]]

#1 method:
[i  for i in x if i != []]

#2 method:
l1 = []
for i in x:
    if i != []:
        l1.append(i)
l1

#3 method:
list(filter(lambda x : x!=[],x))

#4 method:
[i for i in list(map(lambda x:x if x != [] else 'n',x)) if type(i)==list or type(i)==int]
=======================================================================================
## 27. convert list to list of dictionary:

l1 = ['gfg',3,'is',8]
l2 = ['name','id']


=======================================================================================
## 28. uncommon element in list of list:

l1 = [[1,2],[3,4],[5,6]]
l2 = [[1,2],[3,4],[7,8]]


#1 method:
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
for j in l2:
    if j not in l1:
        l3.append(j)
l3

#2 method:
[i for i in l1 if i not in l2]+[j for j in l2 if j not in l1]

#3 method:
list(filter(lambda x: x not in l2,l1))+list(filter(lambda y: y not in l1,l2))

 
=======================================================================================
## 29. select random value from list of list

l1

import random

#1 method:
l3 = []
for i in l1:
    for j in i:
        l3.append(j)

random.choice(l3)

#2 method:
res = [j for i in l1 for j in i]
res

random.choice(res)

#3 method:
import numpy as np

np.random.randint(res[0],res[-1],size=(1,1))[0][0]
=======================================================================================
## 30. reverse row sort in list of list

l1

#1 method:
[[i for i in reversed(j)] for j in l1 ]

#2 method:
l3 = []
for i in l1:
    l3.append(list(reversed(i)))
l3

#3 method:
[list(reversed(i)) for i in l1]

#4 method:
list(map(lambda x: list(reversed(x)),l1))
