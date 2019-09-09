# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:56:45 2019

@author: Lakshay Dhiman
"""
import matplotlib.pyplot as plt
from nltk.tokenize import TweetTokenizer
import pandas as pd
from nltk.corpus import wordnet
import random
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
z=list(y)
p=[]
for i in range(40000):
    h=random.randint(0,len(z)-1)
    syn=[]
    for j in wordnet.synsets(z[h]):
        for k in j.lemmas():
            if(z[h]==k.name()):
                syn.append(k.name())
    if(len(syn)>5):   
        p.append([len(syn),len(z[h])])
    if(len(p)==30):
        break
e=[]
f=[]
for i in range(len(p)):
    e.append(p[i][0])
    f.append(p[i][1]**0.5)
plt.scatter(e,f)
plt.xlabel("number of meaning")
plt.ylabel("length of token")
plt.show()   

    
       


             
