#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Question 3 (15% of this assignment):
(Financial: credit card number validation) Credit card numbers follow certain patterns: It must have between 13 and 16
digits, and the number must start with:
■ 4 for Visa cards
■ 5 for MasterCard credit cards ■ 37 for American Express cards ■ 6 for Discover cards
In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. The algorithm is useful to
 determine whether a card number is entered correctly or whether a credit card is scanned correctly by a scanner.
 Credit card numbers are generated following this validity check, commonly known as the Luhn check or the Mod 10 check,
 which can be described as follows (for illustration, consider the card number 4388576018402626):
"""


def is_valid(number):
    # Return true if the card is valid.
    import re
    return re.match(r'^([4-6][0-9]{12,15})|(37[0-9]{11,14})$', number) and (sodep(number) + soop(number)) % 10 == 0


def sodep(number):
    # Sum of double even place. result of step2.
    return sum(int(i) for i in ''.join(str(int(i)*2) for i in list(number)[::2]))


def soop(number):
    # Return sum of odd place digit number.
    return sum(int(i) for i in list(number)[::-2])

print('The card is {}'.format(('not valid', 'valid')[is_valid(input('Input a card number: '))]))

