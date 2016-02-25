#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Question 1 (10% of this assignment): Suppose you want to deposit a certain amount of money into a savings account with
#  a fixed annual interest rate. What amount do you need to deposit in order to have $5,000 in the account after three
#  years? The initial deposit amount can be obtained using the following formula:
# Write a program that prompts the user to enter final account value, annual interest rate in percent, and the number
#  of years, and displays the initial deposit amount. A sample run of your program:

# Answer given by tavimori


from minput import *


finalAccountValue = input_regex('Enter the final account value: ',
                                r"""
                                       ^(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$'
                                """,
                                'Should be a positive number. Try again...')
annualInterestRate = input_regex('Enter the annual interest rate: ',
                                 r'^-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0)$',
                                 'Should be a number. Try again...')
numberOfYears = input_regex('Enter the number of years: ', r'^[1-9]\d*$', 'Should be a positive integer. Try again...')
finalAccountValue = float(finalAccountValue)
annualInterestRate = float(annualInterestRate)
numberOfYears = float(numberOfYears)
initialDepositRate = finalAccountValue / (1 + annualInterestRate / 100) ** numberOfYears
print('The initial value is:', initialDepositRate)
