#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Question 2 (15% of this assignment): Write a program that prompts the user to enter an integer and displays the
#  number in reverse order. Here is a sample run:

# Answers given by tavimori

from minput import *


integerEnterByUser = input_regex('Enter an integer:', r'^[1-9]\d*$', 'Should be a positive integer. Try again...')
for i in integerEnterByUser:
    print(i)

