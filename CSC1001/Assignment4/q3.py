#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# By Licheng Mao, 115010202@link.cuhk.edu.cn

"""
Question 3 (25% of this assignment):
Write a Python function to implement the quick sort algorithm over a singly linked list. The input of your function
should be a reference pointing to the first node of a linked list, and the output of your function should also be a
 reference to the first node of a linked list, in which the data have been sorted into the ascending order. You may
  use the LinkedQueue class we introduced in the lecture directly in your program.
"""


import SLList


def quick_sort(node_start):
    def list_quick_sort(l, low, high):
        """
        Quick sort a list.
        :param l:
        :param low:
        :param high:
        :return:
        """
        i = low
        j = high
        if i >= j:
            return l
        else:
            key = l[i]
            while i < j:
                while i < j and key <= l[j]:
                    j -= 1
                l[i] = l[j]
                while i < j and l[i] <= key:
                    i += 1
                l[j] = l[i]
            l[i] = key
        list_quick_sort(l, low, i-1)
        list_quick_sort(l, j+1, high)
        return l
    node_current = node_start
    temp_data = list()
    temp_data.append(node_start.element)
    while node_current.pointer is not None:
        temp_data.append(node_current.pointer.element)
        node_current = node_current.pointer
    result_list = list_quick_sort(temp_data, 0, len(temp_data)-1)
    result = SLList.SLList()
    for i in result_list:
        result.insert_tail(i)
    return result


def main():
    print('You are running this independently. Now in sample mode.')
    print('The following code will be executed.')
    print(
        """
    data_list = SLList.SLList()
    data_list.insert_head(1)
    data_list.insert_head(3)
    data_list.insert_head(2)
    data_list.insert_head(16)
    data_list.insert_head(8)
    data_list.insert_head(15)
    data_list.insert_head(3)
    data_list.insert_head(1)
    data_list.insert_head(9)
    data_list.insert_head(12)
    data_list.iterate()
    print('Then sort...')
    data_list = quick_sort(data_list.head)
    data_list.iterate()
        """
    )

    data_list = SLList.SLList()
    data_list.insert_head(1)
    data_list.insert_head(3)
    data_list.insert_head(2)
    data_list.insert_head(16)
    data_list.insert_head(8)
    data_list.insert_head(15)
    data_list.insert_head(3)
    data_list.insert_head(1)
    data_list.insert_head(9)
    data_list.insert_head(12)
    data_list.iterate()
    print('Then sort...')
    data_list = quick_sort(data_list.head)
    data_list.iterate()

if __name__ == '__main__':
    main()
