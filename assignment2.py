# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:12:16 2019

@author: Lakshay Dhiman
"""
import re
import math
import nltk
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from nltk.tokenize import sent_tokenize

file = open("31100.txt", 'r')
sentence_list = sent_tokenize(file.read())
file.close()
special_chars = re.compile('[`~!@#$%^&*()+={}|\[\]:";<>?,\./“”]')

for i in range (len(sentence_list)):
    text = sentence_list[i].replace("\n", " ")
    text = "<s> " + special_chars.sub("", text) + " </s>"
    text = text.lower()
    sentence_list[i] = ' '.join(text.split())

test = []
train = []

for i in range (len(sentence_list)):
    if (i%5 == 0):
        test.append(sentence_list[i])
    else:
        train.append(sentence_list[i])

# Function for calculating n-grams from the text and their individual as well as total count.
def n_grams(lst, n):
    count = {}
    total_count = 0
    for i in range (len(lst)):
        item=lst[i]
        x = item.split()
        for j in range(len(x)-n+1):
            y = []
            for k in range(n):
                y.append(x[j+k])
                s = " ".join(y)
            count[s] = count.get(s, 0) + 1
            total_count += 1
    return count, total_count

# Function to calculate the Maximum likelihood estimation for n-grams in the corpus.
def MLE_generation(n_grams, n_1_grams):
    MLE = {}
    for i in n_grams.keys():
        lst = i.split()
        MLE[i] = n_grams[i]/n_1_grams[' '.join(lst[:len(lst)-1])]
    return MLE 

unigrams, total_unigrams = n_grams(train, 1)
bigrams, total_bigrams = n_grams(train, 2)
trigrams, total_trigrams = n_grams(train, 3)
quadgrams, total_quadgrams = n_grams(train, 4) 

MLE_unigrams = {}
for i in unigrams.keys():
    MLE_unigrams[i] = unigrams[i]/total_unigrams
    
MLE_bigrams = MLE_generation(bigrams, unigrams)
MLE_trigrams = MLE_generation(trigrams, bigrams)
MLE_quadgrams = MLE_generation(quadgrams, trigrams)
