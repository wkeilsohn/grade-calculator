#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 07:37:22 2019

@author: William Keilsohn
"""

# This file only deals w/ data manipulation. 
# If you want to see a test file writen, please see the other .py file. 

# Import Packages:
import numpy as np

  
# Read in the text file:
def fileReader(file):
    data_array = np.loadtxt(file, skiprows = 1)# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.loadtxt.html
    return data_array #Above, I choise to skip the first row as np can't convert strings to numbers.
'''
Additional Note:
    The defualt of np.loadtxt() is to accept all data as float values. I did not change this default. 
    However, all the data I passed into it was int values. Therefore, I went back and tested it with float values
    and it can read them; they just get rounded later. 
'''
  

## Create The dictionary:
def dicMaker(array):
    data_dic = {}
    for i in range(len(array)): # https://stackoverflow.com/questions/30280856/populating-a-dictionary-using-for-loops-python
        data_dic[array[i, 0]] = list(array[i, 1:])
    return data_dic
    
## Calculate Grades per test:
def gradeCalculator(array):
    data_lst = list(array.mean(axis = 0))# From the text book. (Pg. 100)
    ### Note: According to the text book, this is a form of Numpy functionality.
    return data_lst

## Resolve low grades:
def gradeChecker(array):
    lst = gradeCalculator(array)
    new_array = array.astype(np.int32) # From the text book (Pg. 84-85)
    for i in lst[1:]: # Skip the student id's
        if i < 60:
            new_array[0:, lst.index(i)] += 10 # From the text book (Pg. 80).
        else:
            continue
    if sum(lst[1:]) == sum(gradeCalculator(new_array)[1:]):
        return new_array
    else:
        return gradeChecker(new_array)
            
