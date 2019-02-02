#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 20:22:32 2019

@author: william keilsohn
"""

# This file only writes the .txt file for the data. 
# Please see the other file for the data comprhension portion.


# Import Packages:
from random import randint

# Specify location:
path = '/home/william/Documents/Class_Scripts/HW_2_2019/' # Using Linux.

# Create some variables/values for the file:
tst = 14
# Any number can go here, but this time it represents the number of tests.
# Additionally, this is about the max number before one starts seeing text wrap. 

# Create a "Heading" Function:
def addHeaders(num):
    headers = ["Student_id"]
    for i in range(num + 1):
        headers.append("Test" + str(i))
    return headers

# Create a random class size:
def studentCounter():
    stu = randint(50, 100) # Any number could be used here. It just represents the size of the class.
    student_ids = [randint(8000, 9000) for i in range(stu + 1)] # Represents the student_ids for the class.
    # This formatting was gone over in the last semester but... #https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
    fail_data = [randint(0, 60) for i in range(stu + 1)] # Represents the guarenteed test the students failed. 
    # If the maximum range is for the random integer is 60, the average is not going to be higher.
    return student_ids, fail_data
    
# Define a cleaning function:
def fileCleaner():
    file = open(path + 'data.txt', 'w')
    file.close()   

# Define a write function:
def fileWriter(): #Not the prettiest file, but it works.
    fileCleaner()
    students = studentCounter()
    file = open(path + 'data.txt', "w")
    for x in addHeaders(tst):
        file.write(x)
    file.write('\n')
    for i in range(len(students[0])): # Writes in a "table" of all the test scores into the .txt file.
        file.write(str(students[0][i]))
        for j in range(1, len(addHeaders(tst))):
            file.write(str(randint(0 ,100)))
            file.write('\t')
        file.write(str(students[1][i]))
        file.write('\n')
    file.close()
    

# Run the file and make some data!
#fileWriter()
