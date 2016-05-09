#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# By Licheng Mao, 115010202@link.cuhk.edu.cn

"""
Question 2 (25% of this assignment):
An arithmetic expression can be represented by a binary tree whose leaves are associated with numbers, and whose
 internal nodes are associated with one of the operators +, −, ×, and /. For example, an expression can be represented
 by the following binary tree:
 Write a Python function to calculate the value of an arithmetic expression which is represented by a binary tree.
 In each internal node, the arithmetic operators will be represented by characters ‘+’, ‘-‘, ‘*’ and ‘/’. In each
 leaf node, the numbers may be either integer or floating point numbers. The input of the function will be a
 reference pointing to the root of the binary tree, and the output of the function should be the value of the
 arithmetic expression. (Hint: this problem can be solved by modifying the depth first search algorithm we introduced
  in the lecture)
"""


class Node:
    def __init__(self, element, parent=None, left=None, right=None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right


class LBTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def find_root(self):
        return self.root

    def parent(self, p):
        return p.parent

    def left(self, p):
        return p.left

    def right(self, p):
        return p.right

    def num_child(self, p):
        count = 0
        if p.left is not None:
            count += 1
        if p.right is not None:
            count += 1
        return count

    def add_root(self, e):
        if self.root is not None:
            print('Root already exists.')
            return None
        self.size = 1
        self.root = Node(e)
        return self.root

    def add_left(self, p, e):
        if p.left is not None:
            print('Left child already exists.')
            return None
        self.size += 1
        p.left = Node(e, p)
        return p.left

    def add_right(self, p, e):
        if p.right is not None:
            print('Right child already exists.')
            return None
        self.size += 1
        p.right = Node(e, p)
        return p.right

    def replace(self, p, e):
        old = p.element
        p.element = e
        return old

    def delete(self, p):
        old = p.parent
        if p.parent.left is p:
            p.parent.left = None
        if p.parent.right is p:
            p.parent.right = None
        return old


def calc(expression_tree, start_node=None):
    if start_node is None:
        start_node = expression_tree.find_root()
    if start_node.element in ('+', '-', '*', '/'):
        return eval(str(calc(expression_tree, start_node=start_node.left)) +
                    start_node.element + str(calc(expression_tree, start_node=start_node.right)))
    else:
        return start_node.element


print('You are running this independently. Now in sample mode.')
print('The following code will be executed.')
print(
    """
    a = LBTree()
    node_1 = Node('1')
    node_2 = Node('2')
    b = Node('-')
    b.left = node_1
    b.right = node_2
    node_1.parent = b
    node_2.parent = b
    a.root = b
    print('The calc result is ', calc(a))
    """
)
a = LBTree()
node_1 = Node('1')
node_2 = Node('2')
b = Node('-')
b.left = node_1
b.right = node_2
node_1.parent = b
node_2.parent = b
a.root = b
print('The calc result is ', calc(a))
