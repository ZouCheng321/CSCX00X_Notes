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


def HanoiTower(height, move_from='A', move_to='C'):
    import stack

    n_stack = stack.ListStack()
    n_stack.push((height, move_from, move_to))
    while not n_stack.is_empty():
        prev = n_stack.pop()
        if prev[0] > 1:
            # Change the procedure of move n from a to c into 3 steps.
            # (n-1) a to b; 1 a to c; (n-1) b to c
            n_stack.push((prev[0] - 1, 'ABC'.replace(prev[1], '').replace(prev[2], ''), prev[2]))
            n_stack.push((1, prev[1], prev[2]))
            n_stack.push((prev[0] - 1, prev[1], 'ABC'.replace(prev[1], '').replace(prev[2], '')))
        else:
            print(prev[1], '-->', prev[2])


def main():
    print('You are running this independently. Now in sample mode.')
    print('The following code will be executed.')
    print(
        """
        n = 6
        HanoiTower(n)
        """
    )
    n = 6
    HanoiTower(n)

if __name__ == '__main__':
    main()