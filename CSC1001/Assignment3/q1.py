#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# By Licheng Mao, 115010202@link.cuhk.edu.cn

"""
Question 1 (20% of this assignment):
Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively
represent the name of the flower, its number of petals, and its price. Your class must include an initializer that
initializes each variable to an appropriate value, and your class should include methods for setting the value of each
type, and retrieving the value of each type. Your program should be robust enough to handle possible inappropriate
inputs.
"""


class Flower(object):
    def __init__(self, name='Unknown Flower', petals=0, price=0):
        self.__name = name
        self.__petals = petals
        self.__price = price

    def set_name(self, name):
        self.__name = name

    def set_petals(self, petals):
        self.__petals = petals

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def get_petals(self):
        return self.__petals

    def get_price(self):
        return self.__price


if __name__ == "__main__":
    print(r"You're not using this as a module, so this is an diagnose program.")
    print(r"We define a = Flower('Rosa multiflora', 4, 999)")
    a = Flower('Rosa multiflora', 4, 999)
    print(r"We print a.get_name(), a.get_petals() and a.get_price()")
    print(a.get_name())
    print(a.get_petals())
    print(a.get_price())
