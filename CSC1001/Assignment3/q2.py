#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# By Licheng Mao, 115010202@link.cuhk.edu.cn

"""
Question 2 (40% of this assignment):
Write a Python class that inputs a polynomial in standard algebraic notation and outputs the first derivative of that
polynomial. Both the inputted polynomial and its derivative should be represented as strings.
For example, when the inputted polynomial is   , the output of your program should be   .
Note: (1) The inputted polynomial will contain only one variable, and the variable is not
necessarily ‘x’; (2) In the inputted polynomial, the terms are not necessarily arranged in descending or ascending
orders.
"""

import re


class Polynomial(object):
    """
    Polynomial is a class for math polynomials, whose algorithm is redefined
    """
    def __init__(self, other):
        if type(other) == Polynomial:
            # Polynomial directly
            self.__var = other.get_value()
        elif type(other) == str:
            try:
                self.__var = {'': float(other), }
                # Const
            except ValueError:
                if other[0].isalpha() and other.replace('^', 'x').isalnum():
                    # Start with alpha and all is an alnum. Exp. abc12
                    self.__var = {other: 1, }
                else:
                    term = ''
                    other += '\n'
                    other = list(other)
                    for i in range(len(other) - 1):
                        if (other[i].isdigit() or other[i] == ')') and other[i + 1].isalpha():
                            other[i] += '*'
                    other = list(''.join(other))
                    for i in range(len(other)):
                        if other[i] not in '+-*/()\n':
                            term += other[i]
                            other[i] = ''
                        else:
                            if term != '':
                                other[i] = 'Polynomial(\'' + term + '\')' + other[i]
                            term = ''
                    other = list(''.join(other))
                    other.pop(-1)
                    # print(''.join(other))
                    # pass
                    self.__var = Polynomial(eval(''.join(other))).get_value()
        elif type(other) == int or type(other) == float:
            self.__var = {'': other}
        elif type(other) == dict:
            self.__var = other

    def __add__(self, other):
        if type(other) == Polynomial:
            return_dict = {}
            for i in self.get_value():
                if i not in return_dict:
                    return_dict[i] = self.get_value()[i]
                else:
                    return_dict[i] += self.get_value()[i]
            for i in other.get_value():
                if i not in return_dict:
                    return_dict[i] = other.get_value()[i]
                else:
                    return_dict[i] += other.get_value()[i]
            return Polynomial(return_dict)
        else:
            return self + Polynomial(other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == Polynomial:
            return self + -other
        else:
            return self - Polynomial(other)

    def __rsub__(self, other):
        if type(other) == Polynomial:
            return -self + other
        else:
            return Polynomial(other) - self

    def __neg__(self):
        return_dict = {}
        for other in self.get_value():
            return_dict[other] = -self.get_value()[other]
        return Polynomial(return_dict)

    def __mul__(self, other):
        if type(other) == Polynomial:
            if other.is_number():
                other = other.get_parameter('')
                return_dict = {}
                for i in self.get_value():
                    return_dict[i] = other * self.get_value()[i]
                return Polynomial(return_dict)
            elif self.is_number():
                return other * self

        if type(other) == int or type(other) == float:
            return self * Polynomial(other)

    def __rmul__(self, other):
        return self * other

    # def __truediv__(self, other):
    #     if type(other) == int or type(other) == float:
    #         return_dict = {}
    #         for other in self.get_value():
    #             if other not in return_dict:
    #                 return_dict[other] = self.get_value()[other] / other
    #             return Polynomial(return_dict)
    #
    # def __rtruediv__(self, other):
    #     if type(other) == int or type(other) == float:
    #         return_dict = {}
    #         for other in self.get_value():
    #             if other not in return_dict:
    #                 return_dict[other] = other / self.get_value()[other]
    #             return Polynomial(return_dict)

    def __repr__(self):
        return '+'.join('' + str(self.get_value()[i]) + '' + i for i in self.get_value())

    def is_number(self):
        if len(self.get_value()) == 1 and ('' in self.get_value()):
            return True
        else:
            return False

    def get_derivative(self):
        __derivative = dict()
        for i in self.__var:
            if '^' in i:
                j = i.split('^')
                __derivative[(j[0]+'^'+str(float(j[1])-1))] = float(j[1]) * self.__var[i]
            elif i == '':
                continue
            else:
                __derivative[''] = self.get_value()[i]
        return Polynomial(__derivative)

    def derivative(self):
        self.__var = Polynomial(self.get_derivative())

    def get_value(self):
        return self.__var

    def get_parameter(self, other):
        if other in self.__var:
            return self.get_value()[other]
        else:
            return 0

    def get_magnitude(self):
        import math
        # print(self.__var)
        return math.sqrt(sum(float(self.__var[coefficient])**2 for coefficient in self.__var))


class Equation(object):
    """
    The Equation is a class of math equation, which contain two inner polynomial. the __left and __right are the
    left and right part of the equation
    """
    def __init__(self, other):
            if type(other) == str:
                other = other.split('=')
                if len(other) == 2:
                    self.__left = Polynomial(other[0])
                    self.__right = Polynomial(other[1])
                else:
                    raise ValueError
            else:
                raise ValueError

    def get_expression(self):
        return self.__left - self.__right


def main():
    print(r"You're not using this as a module, so this is an diagnose program.")
    print(r"We define a = Polynomial('x^2+2+y+x')")
    a = Polynomial('x^2+2+y+x')
    print(r"We print a.get_derivative()")
    print(a.get_derivative())
    print(r"More interesting things: You can do a = Polynomial('x'), then try a = 2 * a, a + 2, a * '2y'")
    b = input(r"Now enter a expression:")
    a = Polynomial(b)
    print('The derivative of your input is {}'.format(a.get_derivative().__repr__()))

if __name__ == "__main__":
    main()

