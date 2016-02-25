#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Question 4 (15% of this assignment): Write a program to allow a user to input a number N, and print a table with N
#  rows and 3 columns. In the mth row, your program should output three numbers: m, m+1, and mm+1. For example, when
#  the user inputs N = 5, your program should output the following:
# Your program should be robust enough to handle the possible improper inputs (e.g. the user inputs a negative N).


# Answer given by tavimori

from minput import *
n = int(input_regex('Enter a number N:',r'^[1-9]\d*|0$', 'Should be a positive integer. Try again...'))
print('m', 'm+1', 'm**(m+1)', sep='\t')
for m in range(1, n + 1):
    print(m, m + 1, m ** (m + 1), sep='\t')
