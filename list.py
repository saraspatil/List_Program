#check whether cold is present or not :
s = 'today its very cold'

for i in s.split():
    if i == 'cold':
        print('cold is present')
    else:
        print('cold is not present')
========================================================
# WAP to get present and absent eligibility:
nm = input('Enter student name: ')
w = int(input('Enter total working days: '))
a = int(input('Enter total absent days: '))
per = float(((w-a)/w)*100)
if per >= 75:
    print((nm.title()),'you are allow to sit in exam.')
else:
    print(nm,'is not allow to sit in exam.')
=============================================================
# flow control block for percentage of number:
per = float(input('Enter the percentage: '))
if per < 25:
    print('D')
elif per >= 25 and per < 45:
    print('C')
elif per >=45 and per < 50:
    print('B')
elif per >= 50 and per < 60:
    print('B+')
elif per >= 60 and per < 80:
    print('A')
else:
    print('A+')
===============================================
# WAP to get a 10% of bouns from salary:
sal = int(input('Enter the net salary: '))
yr = int(input('Enter the service years: '))
if yr < 6:
    print('Net bonus amount is: ',(sal*0.05))
if yr >= 6 and yr <= 10:
    print('Net bonus amount is: ',(sal*0.08))
if yr > 10:
    print('Net bonus amount is: ',(sal*0.1))
=================================================
# WAP to get the amount from market price with percentage given below:
mp = int(input('Enter the marked price: '))
if mp > 10000:
    b = mp - (mp * 0.2)
if mp > 7000 and mp <= 10000:
    b = mp - (mp * 0.15)
if mp <= 7000:
    b = mp - (mp * 0.1)
print('Net amount is:',b)
=================================================
# check if tringle is equilateral, scalene or isosceles:
a = int(input('Enetr the 1st side: '))
b = int(input('Enter the 2nd side: '))
c = int(input('Enter the 3rd side: '))
if a ==b and b== c and c == a:
    print('The triangle is equilateral.')
elif a != b and b != c and c != a:
    print('The trangle is scalene')
else:
    print('The triangle is isosceles. ')
=====================================================
" WAP using flow control block to enter the operator from user and get the outpur from that one:
a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
c = input('Enter any operator: ')
if c == '+':
    z = a + b
if c == '-':
    z = a - b
if c == '*':
    z = a * b
if c == '/':
    z =  a / b
if c == '%':
    z = a % b
if c == '//':
    z = a//b
if c == '**':
    z = a ** b
print('Value is: ',z)
=======================================================
# WAP to get the wages of the workers:
a = int(input('Enter the age: '))
b = input('Enter the gender: ')
c = int(input('Enter the number of days: '))
if a>=18 and a < 30 and b.upper() == 'M':
    z = 700 * int(c)
    print('Your per day wages are:', z)
elif a >= 18 and a < 30 and b.upper() == 'F':
    z = 750 * int(c)
    print('Your per day wages are:', z)
elif a >= 30 and a <= 40 and b.upper() == 'M':
    z = 800 * int(c)
    print('Your per day wages are:', z)
elif a >= 30 and a <= 40 and b.upper() == 'F':
    z = 850 * int(c)
    print('Your per day wages are:',z)
else:
    print('Enter appropriate age.')
    ======================================================================
# use indexing to find first middle and last character
s = input('Enter any character: ')
a1 = s[0]
x = int(len(s)/2)
a2 = a1 + s[x]
a3 = a2 + s[len(s) - 1]
print('first middle & last character of str is: ',a3)
=========================================================
# WAP to get the option of the diffrent meals with avilable money:
m = int(input('Enter the available money: '))
t = input('Type of pizza: ')
if m >= 199:
    if t == 'veg':
        print('veg pizza order placed','Your available balance is',(m-199),'rupees')
    else:
        print('order for sandwitch.')
else:
    print('Go and eat vada pav')
    ===================================
# different techniques to get the mobile number separately:
s = 'my contact number is : 7741856322'
# print(s.split()[-1])
# print(s.split(':')[-1])
# print(s.find('7'))
# print(s[23:])
for i in s:
        if i.isdigit() == True:
                print(i,end='')
==========================================
# get the numeric value separate:
s = 'kjdi3ksndjk5kjsndf88knfn 9fjfn76'
a = 0
for i in s:
        if i.isdigit() == True:
                a += int(i)
print('Sum of number is:', a)
==================================
# to get the even numbers:
e = [12, 3, 45, 67, 44, 30]
for i in e:
    if i % 2 == 0:
        print(i)
====================================
# get sum of the number  from entered list:
a = 0
s = eval(input('Enetr the list: '))
for i in s:
    a += i
print('Sum of number is: ',a)
=========================
n = 5
while n > 0:
    print(n)
    n -= 1
    =======================
# to get number of occurances from the list:
n = eval(input('Enter the list of four number: '))
a = 0
count = 0
while count < 4:
    a += n[count]
    count += 1
print('Addition of given number',n,'is',a)
=============================================

for i in range(10):

    if i <= 6:
        break
    else:
        print(i)
        ===================================
for i in range(10):

    if i <= 6:
        continue
    else:
        print(i)
=====================================

# s = [1, 2, 3, 4]
for i in range(1,6):
    print(i**2)
====================================
# WAP to square of the list from range 1 to 6
ls = []
for i in range(1,6):
    ls.append(i**2)
print(ls)
=======================================
# WAP to square the list of range 1 to 7 using list comprehension:
# syntax : [Expression for i in list/sequence if condition]
print([i**2 for i in range(1, 8)])
=======================================
# WAP to square the list of range 1 to 6 using list comprehension only for even number:
print([i**2 for i in range(1, 7) if i % 2 == 0])
=====================================
name = ['pratik','rohit','pradeep','amol']
# print([word[0] for word in name])
# i want to initialize only worg starting with 'p':
print([word[0] for word in name if word.startswith('p')])
========================================
n1 = [10, 20, 30, 40]
n2 = [1, 4, 20, 30]
print([i for i in n1 if i  in n2])
============================
name = ['pratik','rohit','pradeep','amol']
print([(i.upper(), len(i)) for i in name  ])
==============================================

a = 0
b = 1
for i in range(1, 5):
    a += i
    print(a)
    b += i
    print(b)
==============================================
# WAP to execute dic with number as key and value as square od that number from range 1 to 10.
# expected output is : { (1: 1), (2:4),......}
print({i: i**2 for i in range(1, 11)})
====================================================
# WAP to swap the number
a = int(input('enter the value of a: '))
b = int(input('enter the value of b: '))
a, b = b, a
print('value of a after swapping: ',a)
print('value of b after swapping: ',b)
==========================================
WAP to get the expected output as:
[10, 40, 1, 4]
n1 = [10, 20, 30, 40]
n2 = [1, 20, 30, 4]
print([i for i in n1 + n2 if i not in set(n1).intersection(n2)])
=============================================================

a = 'pratikjdhejbncnc'
print('first number is: ', a[0], 'position of this word in given string: ', a.find(a[0]))
print('last number is: ', a[-1], 'position of this word in given string: ', a.find(a[-1]))
print('middle number is:', a[len(a) // 2], 'position of this word in given string: ', a.find(a[len(a) // 2]))
print('length of the string is: ', len(a))
===============================================================================================================

# WAP to process atm machine:
import time
nm = input('Enter your name: ')
p = int(input('Enter the password: '))
b = 5000
if p == 1234:
    print('its processing.....')
    time.sleep(3)
    print(' 1. mini statement.','\n','2. balance enquiry.','\n','3. withdrawal.')
    c = int(input('Enetr the number from option: '))
    if c == 1:
        print('your last five transactions are in the receipt &', b, 'is your available balance')
    elif c == 2:
        print('your balance is: ',b)
    elif c == 3:
        w = int(input('Enter the amount: '))
        if w <= b:
            print(w, 'withdrawal is successful, your balance is: ', int(b - w))
        else:
            print('Insufficient balance.')
    else:
        print('Please enter the number between 1 to 3.')
else:
    print('its processing.....')
    time.sleep(3)
    print('incorrect pin')
============================================================================================================

# expected output - [0, 30, 6, 30]

k = []
def add(*args):

    a = 0
    for val in args:
       a += val
    k.append(a)
    print('addition is: ', a)
add()
add(10, 20)
add(1, 2, 3)
add(12, 3, 4, 5, 6)
print('final list of addition is:', k)

# expected o/p --> [[10, 20, 30],[3, 4, 5],[200, 300]]
l1 = []
def sample(**k):
    for key in list(k.values()):
        l1.append(key)
sample(x1=10, x2=20, x3=30)
l2 = []
def sample(**k):
    for key in list(k.values()):
        l2.append(key)
sample(x1=3, x2=4, x3=5)
l3 = []
def sample(**k):

    for key in list(k.values()):
         l3.append(key)
sample(x1=200, x2=300)
print([l1, l2, l3])

#
# WA lambda fuction to calculate cub of a number
c = lambda x : x ** 3
cube = c(9)
print('cube of a number is', cube)

# WA lambda function to get even number
s = lambda x, y: x == y
k = s(1, 11)
print('is numbers are equal: ',k)
