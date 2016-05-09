#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# By Licheng Mao, 115010202@link.cuhk.edu.cn

"""
Question 4 (40% of this assignment):
The Tower of Hanoi is a mathematical game or puzzle. It consists of three rods, and a number of disks of different sizes which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape. The following figure shows the initial state of the Tower of Hanoi with 5 disks.
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1. Only one disk can be moved at a time.

2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3. No disk may be placed on top of a smaller disk.
Assume that initially all the disks are placed on rod A. Write a non-recursive Python function to print out the steps to move all the disks from rod A to rod C via rod B (Hint: a recursive algorithm can be converted into a non-recursive algorithm using stack). The header of the function is:
def HanoiTower(n)
Here n represents the number of disks. For example, when n = 3 your function should output:
"""

n = 3


def HanoiTower(n, move_to='C', move_from='A'):
    if n == 1:
        print(move_from+' --> ' + move_to)
    elif n > 1:
        HanoiTower(n-1, move_to='ABC'.replace(move_from, '').replace(move_to, ''), move_from=move_from)
        print(move_from+' --> ' + move_to)
        HanoiTower(n-1, move_from='ABC'.replace(move_from, '').replace(move_to, ''), move_to=move_to)


import stack
n_stack = stack.ListStack()
n_stack.push((n, 'A', 'C'))
while not n_stack.is_empty():
    prev = n_stack.pop()
    if prev[0] > 1:
        n_stack.push((prev[0] - 1, 'ABC'.replace(prev[1], '').replace(prev[2], ''), prev[2]))
        n_stack.push((1, prev[1], prev[2]))
        n_stack.push((prev[0] - 1, prev[1], 'ABC'.replace(prev[1], '').replace(prev[2], '')))
    else:
        print(prev[1], '-->', prev[2])



# HanoiTower(n)