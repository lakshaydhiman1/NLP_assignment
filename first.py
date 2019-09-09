# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:33:12 2019

@author: Lakshay Dhiman
"""
from nltk.tokenize import TweetTokenizer
import pandas as pd
dataset = pd.read_csv('tweets-dataset.csv')
x=dataset.iloc[:,:].values
tknzr=TweetTokenizer(strip_handles=True, reduce_len=True)
y=set()
t=0
for i in range(len(x)):
    p=tknzr.tokenize(x[i][0])
    for j in range(len(p)):
        if(p[j]!='?' and p[j]!='!' and p[j]!='.' and p[j]!=','):
             y.add(p[j]) 
             t=t+1
print("Type in the whole data",end=" :")
print(len(y))
print("Token in the whole data",end=" :")
print(t)
print("type token ratio",end=" :")
print(len(y)/t)         
