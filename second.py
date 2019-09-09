# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:56:45 2019

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
voc=list(y)
