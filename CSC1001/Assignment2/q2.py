#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Question 5 (20% of this assignment): Write a program to allow a user to input an integer N, and print all the prime
#  numbers which are smaller than N. For example, when the user inputs N = 10, your program should output
# Your program should output at most 8 prime numbers in each line. Your program should also be robust enough to handle
#  the possible improper inputs (e.g. the user inputs a string).

# Answer given by tavimori


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


# n = int(input_regex('Enter a integer N: ', r'^[1-9]\d*$', 'Should be a positive integer. Try again...'))
n = 1000000
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
    if len(p) == 10000:
        break
print_a_list(p)
