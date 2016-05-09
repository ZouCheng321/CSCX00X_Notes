#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# By Licheng Mao, 115010202@link.cuhk.edu.cn

"""
Question 1 (10% of this assignment):
Write a Python function to implement a recursive algorithm which counts the number of nodes in a singly linked list.
The input of the function should be a reference pointing to the first node of the linked list. The output of the
 function should be the number of nodes in that linked list.
"""

import SLList


def length(node1):
    while node1.pointer is not None:
        return 1 + length(node1.pointer)
    return 1


def main():
    print('You are running this independently. Now in sample mode.')
    print('The following code will be executed.')
    print(
        """
        singly_list = SLList.SLList()
        singly_list.insert_head(1)
        singly_list.insert_head('2')
        singly_list.insert_head({'3': 1})
        singly_list.insert_head([4, 5])
        singly_list.insert_head(print)
        singly_list.insert_head('Apple')
        print('The length is %s' % length(singly_list.head))


        """
    )
    singly_list = SLList.SLList()
    singly_list.insert_head(1)
    singly_list.insert_head('2')
    singly_list.insert_head({'3': 1})
    singly_list.insert_head([4, 5])
    singly_list.insert_head(print)
    singly_list.insert_head('Apple')
    print('The length is %s' % length(singly_list.head))


if __name__ == '__main__':
    main()


