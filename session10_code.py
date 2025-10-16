###Session 10: coding in Python
l = []
type(l) #list
l = [1, 2, 3] #list of integers
type (l)

l = [1, 2.2, "apple", True, [1, "green", False]] #list of mixed types
l[1:3] #gives second and third elements of the list
l[-1] #gives last element of the list
l[-1][1] #gives second element of the last element of the list

l.reverse() #reverse the list
l #shows the reversed list

l1 = ['d', 's', 'a', 'o']
l1.sort() #sort the list
l1 #shows the sorted list

for element in l:
    print(element) #print each element of the list

print(l) #print the whole list

start = 10
stop = 20
step = 2
list(range(start, stop, step)) #gives list of numbers from start to stop with step size

list(range(10)) #gives list of numbers from 0 to 9
list(range(1,11)) #gives list of numbers from 1 to 10

l2 = [] #empty list
l2.append(1) #append 1 to the list
l2.append('red') #append 'red' to the list
l2.append(False)
l2

l3 = l1+l2 #concatenate two lists
l3

#length
len(l) #gives length of the list
len(l[0]) #gives length of the first element of the list

#remove elements from the list:
l.remove("apple") #removes 'apple' from the list
l

del l[0] #deletes the first element of the list

#joining elements of the list:
print('+'.join(l1)) #joins elements of the list with '+' as separator

###Tuples
#Tuple is similar to list but it is immutable, i.e. you cannot change the elements of the tuple

height_and_weight = (165, 60) #tuple of height and weight
type(height_and_weight)

height_and_weight2 = 165,60
print(height_and_weight2)
print(type(height_and_weight2)) #tuple without parentheses

height_and_weight[0] #gives first element of the tuple
#height_and_weight[0] = 170 #gives error, because tuple is immutable

for paramenter in height_and_weight:
    print(paramenter) #print each element of the tuple

height, weight = height_and_weight #unpacking the tuple
print(height) 
print(weight)

###Dictionaries
#Dictionary is a collection of key-value pairs, where each key is unique. Example: a dictionary of student names and their ages

class_size = {
    'Macro': 34, 
    'Micro':30, 
    'Metrics': 25
} #dictionary of class sizes
type(class_size)

class_size['Macro'] #gives value of the key 'Macro'
'Coding' in class_size.keys() #check if 'Coding' is a key in the dictionary, gives False
class_size.get('Coding', 0) #gives value of the key 'Coding', if not found gives 0

for key, value in class_size.items():
    print('The number of students in', key, 'is', value, '.') #print each key-value pair in the dictionary
    print(key)

###Sets 
#Set is a collection of unique elements, unordered and unindexed, and they cannot be changed and have duoplicates

ls_a = ['a', 'b', 'a', 3.4, 1000]
st_a = set(ls_a) #convert list to set
st_a #shows the set, duplicates are removed

st_b = {'d', 1000, 'pineapple', 'a'}
st_a | st_b #union of two sets
st_a & st_b #intersection of two sets
st_a - st_b #elements in st_a but not in st_b
st_b - st_a #elements in st_b but not in st_a
st_b - st_b #elements in st_b but not in st_b, gives empty set

### Modules
#Module is a file containing Python code, which can be imported and used in other Python files

import math #importing math module
#now we can use functions and constants from math module

math.cos(0)
math.cos(2*math.pi)

from math import * #importing all functions and constants from math module
cos(pi) #now we can use functions and constants from math module without prefixing with math.

#from numpy import ceil, floor #importing specific functions from numpy module
#print(ceil(5.5))
#print(floor(5.5))

import pandas as pd #importing pandas module with alias pd
import numpy as np #importing numpy module with alias np

np.pi #using pi constant from numpy module

data = [1,2,3,4]
series = pd.Series(data) #creating a pandas Series from a list
print(data)
print(series)

import os #importing os module to interact with the operating system
current_directory = os.getcwd()
current_directory
files = os.listdir(current_directory) #list all files in the current directory
files
type (files) #gives type of files, which is list