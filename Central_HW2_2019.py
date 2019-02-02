#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 07:53:01 2019

@author: William Keilsohn
"""

### This File only Deals with User Input/Output ###
### To See Data Processing and File Creations, please view other Files ###

# Link to other files:
## This was done in Dr. Cassel's  class last semester, but here is a citation that explains the setup:
### https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another
### https://www.programiz.com/python-programming/methods/built-in/exec
folder_path = '/home/william/Documents/Class_Scripts/HW_2_2019/'

exec(open(folder_path + 'file_writer.py').read()) # Writes files
exec(open(folder_path + 'file_reader.py').read()) # Reads files

# Handle print out format(s):
def arrayPrinter(array):
    titles = ['Student_id']
    lst = ['Test' + str(i) for i in range(1, len(array[0, 0:]))] #Not sure if I need a citation for list formatting so:
    # https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
    for x in lst:
        titles.append(x)
    print('\n')
    for i in titles:
        print("{:^8}".format(i), end = '')
    print(end = '\n')
    for j in range(len(array)):
        for y in array[j, 0:]:
            print("{:>7}".format(y), end = ' ')
        print(end = '\n')
    print('\n')
    
def dicPrinter(dic):
    print('\n')
    print('Student_id ', 'Test_Grades')
    for k, v in dic.items(): # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
        print("{:^10}".format(k), ' ', v)
    print('\n')

def lisPrinter(lst):
    tests = addHeaders(len(lst))[2:]
    for j in tests:
        print("{:^10}".format(j), end = ' ')
    print(end = '\n')
    for i in lst:
        print("{:^10.2f}".format(i), end = ' ')
    print('\n')

# Ask the user what file they want to read:
### The file_writer.py script will randomly generate test data if the text file is not desierable.
file_runner = True

### Handle possible y/n answers:
def answerHandler(string):
    if string in ['y', 'Y', 'Yes', 'yes']:
        return True
    else:
        return False

while file_runner == True:
    file_input = input('Whould you like random data? (Y/N)' )
    if answerHandler(file_input) == True:
        fileWriter()
        data = fileReader(folder_path + 'data.txt')
    else:
        data = fileReader(folder_path + 'made_data.txt')
    print('\n')
    print('Original Data: ')
    arrayPrinter(data)
    datum_dic = dicMaker(data)
    print('Dictionary of Data: ')
    dicPrinter(datum_dic)
    scores = gradeCalculator(data)
    print('Original Test Averages: ')
    print('\n')
    lisPrinter(scores[1:])
    print('\n')
    final_grades = gradeChecker(data)
    print('Final Grades: ')
    arrayPrinter(final_grades)
    print('Final Test Averages: ')
    print('\n')
    new_scores = gradeCalculator(final_grades)
    lisPrinter(new_scores[1:])
    cont_input = input('Would you like to continue? (Y/N)')
    if answerHandler(cont_input) == True:
        print('\n')
        continue
    else:
        break
        
        