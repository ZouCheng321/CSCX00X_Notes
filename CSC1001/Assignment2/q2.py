#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question 2 (15% of this assignment):
(Emirp) An emirp (prime spelled backward) is a nonpalindromic prime number whose reversal is also a prime. For example,
 both 17 and 71 are prime numbers, so 17 and 71 are emirps. Write a program that displays the first 100 emirps.
 Display 10 numbers per line and align the numbers properly, as follows:
"""

# !!! Some of the core algorithm is refer to the Assignment1

from math import sqrt, ceil


def sieve(sieve_num):
    coefficient = 2
    while sieve_num * coefficient <= n:
        data[sieve_num * coefficient - 1] = False
        coefficient += 1


def print_a_list(list_to_be_printed):
    for print_nth_row in range(ceil(len(list_to_be_printed) / 10)):
        list_of_nth_row = list_to_be_printed[:10]
        del list_to_be_printed[:10]
        print(''.join(map(lambda x: str(x)+'\t', list_of_nth_row)))


n = 10000
border = int(sqrt(n))
data = [True] * n
data[0] = False
for index in range(1, border):
    if not data[index]:
        continue
    sieve(index + 1)
p = []
data[n - 1] = False
for i in range(4, n):
    if data[i]:
        if int(str(i+1)[::-1])-1 != i and data[int(str(i+1)[::-1])-1]:
            p.append(i + 1)
    if len(p) == 100:
        break
print_a_list(p)
