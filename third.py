# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:52:18 2019

@author: Lakshay Dhiman
"""

import matplotlib.pyplot as plt
from nltk.tokenize import TweetTokenizer
import pandas as pd
dataset = pd.read_csv('tweets-dataset.csv')
x=dataset.iloc[:,:].values
tknzr=TweetTokenizer(strip_handles=True, reduce_len=True)
y=set()
t=0
l=list()
o=list()
for i in range(len(x)):
    p=tknzr.tokenize(x[i][0])
    for j in range(len(p)):
        if(p[j]!='?' and p[j]!='!' and p[j]!='.' and p[j]!=','):
            y.add(p[j]) 
            t=t+1
            l.append(t)
            o.append(len(y))
plt.plot(l,o)
plt.xlabel("Size: N")
plt.ylabel("Vocaulary: V")
plt.title("Heap's Law")