#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Question 3 (15% of this assignment): Write a program to allow a user to input a number m, and then use a while loop
#  to find the smallest integer n such that n2 is greater than m. For example, if the user inputs m = 10, your program
#  should output n = 4.

# Answer given by tavimori


from minput import *


m = input_regex('Enter a positive number:', r'^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$',
                'Should be a positive integer. Try again...')
n = 0
while n * n <= m:
    n += 1
print('n =', n)
