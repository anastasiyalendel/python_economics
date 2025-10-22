print("Hello world")
lambda_new = 1
print (lambda_new) #printing the lambda new variable

#How to name our vairables in Python
a = 3 #assign value of 3 to a
print(type(a)) #print the type of value of this object
b = 1.2
print(type (b))
c = 'a'
d = "abc"
e = "dsfs"
type(c)
float (a) #change the type of a to float
str (a) #change the type of a to string
int (b) #change the type of b to integer
float(int(b)) #change the type of b to integer and then to float
#B = int(b)

#Fundamental types of variables
# Integers, float, string, boolean, complex numbers
i=True
j=False
print(i+j) #True is 1 and False is 0
print (i*j) #True is 1 and False is 0

#Operators
3.0 // 2.0 #integer division, gives 1.0
10//6 #gives 1, because 6 fits into 10 only once
2**3 #2^3 = 8
2**0.5 #square root of 2
2/1 #always gives float value

True and False #gives False because both are not True
True or False #gives True because one of them is True
not False #gives True

#for comparison
x=2
y=3
z=3


z==y #True, because z is equal to y, z=y assignment operator so be careful
y is z #True, because both are pointing to same object in memory

#strings
s = "Hello Monty!"
print(s) #print the string
len(s) #gives length of the string
print(s.replace("Monty", "Python")) #replace Monty with Python
s[0:5] #shows firsts 5 characters of the string
s[-6:] #shows last 6 characters of the string
s[:] #shows the whole string
s[::2] #shows every second character of the string
s2 = "Hello Monty Python!"
s2.split(' ') #split the string at space
s2.split(' ')[1] #gives second word of the string
s2.split('o') #gives list of strings split at 'o'

print('Hello \n world!') #\n is new line character
print('Hello \\n world!') #\\n is printed as it is

'Monty' + 'Python' #string concatenation
' '.join(['Monty', 'Python']) #join the list of strings with '' as separator 
'+'.join(['Monty', 'Python']) #join the list of strings with '+' as separator 

print("hello", a) #print hello and value of a
print("The outcome of interest is", a) #print the outcome of interest is 3

print("The outcome of interest is %f", a) #print the outcome of interest is 3.000000
print ('Hello, my name is %s and I am %d years old.' % ('John', 23)) #string formatting
#%s is for string, %d is for integer, %f is for float

name = 'Anastasiya'
session_number = 9
print('My name is {name} and I am attending today\'s session {session_number}'.format(name=name, session_number=session_number)) #string formatting
#Extra:  \ is used to escape special characters like ' in today's
print('{} divided by {} is {}.'.format(2000, 1500, 2000/1500)) #string formatting)
print('{:,d} divided by {:,.0f} is {:,.2f}.'.format(2000, 1500, 2000/1500)) #string formatting with precision
print(type(a).__name__) #gives the type of variable a as string

import math
print(math.pi)
import numpy as np
print(np.pi)
import matplotlib.pyplot as plt
