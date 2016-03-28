#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question 6 (25% of this assignment):
(Game: Eight Queens) The classic Eight Queens puzzle is to place eight queens on a chessboard such that no two queens
can attack each other (i.e., no two queens are in the same row, same column, or same diagonal). There are many
possible solutions. Write a program that displays one such solution. A sample output is shown below:
Note: you cannot just pre-define a solution and display it. Please use algorithm to display a possible solution.
"""

import itertools
for cond in itertools.permutations(range(8)):
    if 8 == len(set([cond[i]+i for i in range(len(cond))])) == len(set([cond[i]-i for i in range(len(cond))])):
        print('\n'.join(['|'+'|'.join([(' ', 'Q')[j == cond[i]]for j in range(8)])+'|' for i in range(8)]), end='\n\n')
