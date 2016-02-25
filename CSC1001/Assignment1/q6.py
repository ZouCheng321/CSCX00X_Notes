#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Question 6 (25% of this assignment): Given a function f(x), and a real interval [a, b], the numerical integration of
#  f(x) over interval [a, b] can be calculated as:

# In equation (1), n represents the number of sub-intervals into which the interval [a, b] will be divided; and it
#  controls the accuracy of numerical integration.

# Write a program to allow the user to specify a trigonometric function f (f can only be sin, cos or tan), and input
#  the interval end points a, b and number of sub-intervals n. Your program should then calculate the numerical
#  integration of f over [a, b] using equation (1), and output the result. Your program should be robust enough to
#  handle possible improper inputs (e.g. the user inputs a floating point number as n).
# Python has built-in trigonometric functions. To call them, use the following statement in your program to import
#  them from the math package:
# You can then invoke the trigonometric functions like the following examples:

# Written by tavimori

from minput import *


givenFunction = input_regex('Enter f(x)= ')
a = float(input_regex('Enter the lower bound of integration: ', r'^-*[0-9,\.]+$',
                      'Should be a number. Try again...'))
b = float(input_regex('Enter the upper bound of integration: ', r'^-*[0-9,\.]+$',
                      'Should be a number. Try again...'))
n = int(input_regex('Enter the number of sub-intervals: ', r'^[1-9]\d*$', 'Should be a positive integer. Try again...'))
# Initializing the result
integrationResult = 0
if n > 10000:
    print('It may takes a while...')
try:
    for i in range(1, n + 1):
        # print(i)
        x = a + (b - a) / n * (i - 1 / 2)
        integrationResult += (b - a) / n * eval(givenFunction)
    print('The numerical integration is ', integrationResult)
except:
    print('A math error occurred. It may caused by a wrong function input.')
