# -*- coding: utf-8 -*-
"""Fuzzy_C_Means.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-YJgaE1EM8SD0KaVBiMFn682EMcwEkKj
"""

from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import random

iris = datasets.load_iris()
#print(iris)
m=0.5
'''Initialize U(0) randomly or based on an approximation; initialize V (0) and calculate U(0). Set the iteration counter, t  = 1. Select the number of class centres c and choose the exponent weight m.

Compute the cluster centres. Given U(t), calculate V (t) according to eq. (2).

Update the membership values. Given V (t), calculate U(t) according to eq. (3).

Stop the iteration if else let  t=t+1 and go to step 2, where  is the pre-specified small number representing the smallest acceptable change in U.
'''
#random number initialisation for U(0)
a = random.uniform(0,1)

#iteration count
i=1
j=1
e=0
n=150
c=4
k=1

#vector uik 
#uik = np.zeros((c,n))
for k in range(0,n):
    vi = iris.data[k]

#Update the membership values
while e:
    for j in range(0,n):
        uik= [1/abs(xk-vi)^2]^(1/(m-1))/[1/abs(xk-vj)^2]^(1/(m-1))
        maxnum = max(uik - uik,uik - uik)
    if maxnum<e:
            break
    
    for j in range(0,n):
        uik=1
        
    for j in range(0,n):
        uik<n
        
        
print(iris)

