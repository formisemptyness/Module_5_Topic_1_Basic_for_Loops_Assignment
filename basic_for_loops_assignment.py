'''
Program: basic_for_loops_assignment.py
Author: Joshua M. McGinley
Last date modified: 09/28/2022

In the editor of your choice, write a Python script (.py file)

    Declare a list of floating point numbers
    Write a for loop to print each
    Write a second for loop to print the odd number descending from 99 to 33 (including 99 and 33)

Include in .py file a docstring.
'''

float_point = [6.66, 3.141592, 6.174, 7.77, 4.44, .133333, .85714286, 1.16666666666]  #list of floats declared

for x in float_point:  #for loop
    print(str(x))  #x converted to string and printed

for x in range(99, 31, -2):  #for loop and range function
    print(str(x))  #x converted to string and printed
