#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import reduce
from math import sqrt,ceil


def shai(shai_num):
  #  if not data[shai_num - 1]:
  #     shai(shai_num + 1)
  #  if shai_num > border:
  #      return True
    t = 2
    while shai_num * t <= n:
        data[shai_num * t - 1] = False
        t += 1
  #  shai(shai_num + 1)


def print_a_list(list_to_be_printed):
    for print_nth_row in range(ceil(len(list_to_be_printed) / 8)):
        list_of_nth_row = list_to_be_printed[:8]
        del list_to_be_printed[:8]
        print(reduce(lambda x, y: x + y, map(lambda x: str(x)+'\t', list_of_nth_row)))


n = int(input('...:'))
border = int(sqrt(n))
data = [True] * n
shai(2)
for i in range(2, border + 1):
    shai(i)
p = []
for i in range(n):
    if data[i]:
        p += [i + 1]
print_a_list(p)
