# -*- coding: utf-8 -*-
"""steve.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oNMpcpd8rYZJwr2LamwunkvsKyJ-b0YJ
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('/content/sample_data/california_housing_train.csv')

dat1 = data.head(50)
print(data.head())
age=dat1.housing_median_age

val=dat1.median_house_value

x = np.array(age).reshape((-1,1))
#print(x)

print(type(x))
y = np.array(val)
#print(y)
#plt.subplot(1,2,1)
plt.scatter(x,y, marker="h", color ='#003153')
plt.show

SLR=LinearRegression()
SLR.fit(x,y)
pred=SLR.predict(x)
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(x,pred)
#plt.subplot(1,2,2)
plt.plot(x,pred,color='black',marker='*')

print("mse:",mse)
print("intercept:",SLR.intercept_)
print("slope:",SLR.coef_)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5,6,7]).reshape((-1,1))
y=np.array([7,1,5,2,3,1,2])

plt.scatter(x,y)
plt.xlabel("independent")
plt.ylabel("dependent")
plt.show

from sklearn.linear_model import LinearRegression

SLR=LinearRegression()
SLR.fit(x,y)
pred=SLR.predict(x)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(x,pred)

plt.plot(x,pred,color='black',marker='*')

print("mse:",mse)
print("intercept:",SLR.intercept_)
print("slope:",SLR.coef_)

import math

a=int(input("enter a number"))
c=1
n=int(math.sqrt(a))
if a<2:
    c=0
else:
    for i in range(2,n+1):
        if a % i == 0:
            c=0
            break

if c==1:
    print("Number is prime")

else:
    if a==1:
        print("Number isn't prime or composite")
    else:
        print("Number is not prime")
    if a % 3 == 0:
      print("divisible bu 3")
    if a% 7==0:
      print("divisible by 7")
    if a%9==0:
      print("divisible by 9")
    if a%11==0:
      print("divisible by 11")
    else:
        print("Number is not divisible by one of four")

a = []

for i in range(10):
    b = int(input("enter a number: "))
    a.append(b)

c = []
d = []

for i in range(10):
    if a[i] % 2 == 0:
        c.append(a[i])
    else:
        d.append(a[i])

print("Even num=", c)
print("Odd num=", d)

a = input("input string")
b = a[::-1]



if b == a:
    print("is palindrom")
else:
    print("not palindrome")

b=int(input("enter rows"))

for i in range (0,b+1):
  print("*"*i)

import matplotlib.pyplot as plt
import numpy as np

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

import random
d=0
c=0
for x in range (5):
  f=random.randint(1,9)
  g=int(input("enter input value within 9"))
  if(f>g):
    d=d+1
    print("computer= ",f)
    print("yours= ",g)
    print("computer won")

  elif(f==g):
    print("computer= ",f)
    print("yours= ",g)
    print("tie")
  else:
    c=c+1
    print("computer= ",f)
    print("yours= ",g)
    print("you won")

print("your score=",c)
print("computer score=",d)

a=int(input("enter number"))

if a>0:
  print("positive num")
else:
  print("negative num")

a=int(input("enter num"))

if a%2:
  print("odd")
else :
  print("even")



a=7
b=9

s=a+b+a*b
print(s)

a=9
b=4
d=a/b
print(d)

import math
a=8
b=math.sqrt(a)
print(b)

import math
a=9
b=a**2
print(b)

s=0
for chad in range(1 ,7):
  s=s+5
  print("ok", chad, chad * "*")
  if s==4:
    break

print("i drive")

p=6
o=9

s=p+o
print(s)

for x in range (8):
  for y in range (8):
    print(x, y)

s=0
for chad in range(1 ,7):
  s=s+5
  print("ok", chad, chad * "*")
  if s==4:
    break

num1=input("num1 ")
num2=input("num2 ")

operation=input("operation ")

if operation=='a':
    sum = float(num1) + float(num2)
    print("sum" + str(sum))

elif operation == 'b' :
   pro=float(num1)*float(num2)
   print("product" + str(pro))

elif operation == 'c' :
   div=float(num1)/float(num2)
   print("divided" + str(div))

elif operation == 'd' :
   mod=float(num1)%float(num2)
   print("modulo" + str(mod))

elif operation == 'e' :
   diff=float(num1)-float(num2)
   print("difference" + str(diff))

i=1
n=input("num")
while i<=int(n):
  print(i)
  i=i+1
  j=i
  if j%2==0:
    print("even")
  else:
    print("odd")

for x in range (7) :
  print(x ,end='')