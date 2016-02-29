#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
lalalalala
"""


def array_plus(list1, list2):

    """
    :param list1:
    :param list2:
    :return:
    """

    if type(list1) == list and type(list2) == list:
        return list(map(lambda x: list1[x] + list2[x], list(range(len(list1)))))
    else:
        return float(list1) + float(list2)


def array_minus(list1, list2):

    """
    :param list1:
    :param list2:
    :return:
    """

    if type(list1) == list and type(list2) == list:
        return list(map(lambda x: list1[x] - list2[x], list(range(len(list1)))))
    else:
        return float(list1) - float(list2)


def array_multi(list1, list2):

    """

    :param list1:
    :param list2:
    :return:
    """
    # print(list(map(lambda x: list1[0] * list2[x] + list2[0] * list1[x], list(range(len(list1))))))
    if list1[0] != 0 and list2[0] != 0:
        return list(map(lambda x: list1[x] * list2[x], list(range(len(list1)))))
    elif list1[0] != 0:
        return list(map(lambda x: list1[0] * list2[x], list(range(len(list1)))))
    elif list2[0] != 0:
        return list(map(lambda x: list1[x] * list2[0], list(range(len(list1)))))
    else:
        return list(map(lambda x: list1[x] * list2[x], list(range(len(list1)))))


def array_divide(list1, list2):

    """

    :param list1:
    :param list2:
    :return:
    """

    return list(map(lambda x: list1[0] / list2[x] + list2[0] / list1[x], list(range(len(list1)))))


def expr_extract(expr_extracted_from):

    """

    :param expr_extracted_from:
    :return:
    """

    expr_extracted_from += '\n'
    expr_extract_unit = ''
    expr_extract_result = []
    for i in expr_extracted_from:
        if i not in '+-*/=\n':
            if i is not ' ':
                expr_extract_unit += i
        else:
            expr_extract_result.append([True, expr_extract_unit])
            if i is not '\n':
                expr_extract_result.append([False, i])
            expr_extract_unit = ''
    return expr_extract_result


def term_unify(term_to_be_unified):
    if term_to_be_unified.isnumeric():
        return term_to_be_unified
    elif term_to_be_unified.isalpha():
        return '1*'+term_to_be_unified
    else:
        for i in range(len(term_to_be_unified)):
            if term_to_be_unified[i].isalpha():
                return term_to_be_unified[:i] + '*' + term_to_be_unified[i:]


def expr_unify(expr_to_be_unified):
    for i in [j for j in range(len(expr_to_be_unified)) if expr_to_be_unified[j][0]]:
        expr_to_be_unified[i][1] = term_unify(expr_to_be_unified[i][1])
    return expr_to_be_unified


def expr_variable_to_be_array(list1):
    variable_dictionary = {'const': 0}
    index = 1
    for i in range(len(list1)):
        term = list1[i][1]
        if term.isalpha():
            if term not in variable_dictionary:
                variable_dictionary[term] = index
                index += 1
    index -= 1
    print(variable_dictionary)
    # blank_list = [0]*(index + 1)
    # print(blank_list)
    for i in range(len(list1)):
        if list1[i][0]:
            term = list1[i][1]
            if term.isalpha():
                var_as_array = [0]*(index + 1)
                var_as_array[variable_dictionary[term]] = 1
                list1[i][1] = var_as_array
            else:
                var_as_array = [0]*(index + 1)
                var_as_array[variable_dictionary['const']] = float(term)
                list1[i][1] = var_as_array
    return list1, variable_dictionary


def expr_calc(list1):

    """

    :param list1:
    :return:
    """
    i = 0
    while i < len(list1):
        if not list1[i][0]:
            if list1[i][1] is '*':
                list1[i] = [True, array_multi(list1[i - 1][1], list1[i + 1][1])]
                # print(list1[i][1])
                del list1[i + 1]
                del list1[i - 1]
                i -= 1
            elif list1[i][1] is '/':
                list1[i] = [True, array_divide(list1[i - 1][1], list1[i + 1][1])]
                del list1[i + 1]
                del list1[i - 1]
                i -= 1
        i += 1
    i = 0
    while i < len(list1):
        if not list1[i][0]:
            if list1[i][1] is '+':
                list1[i] = [True, array_plus(list1[i - 1][1], list1[i + 1][1])]
                del list1[i + 1]
                del list1[i - 1]
                i -= 1
            elif list1[i][1] is '-':
                list1[i] = [True, array_minus(list1[i - 1][1], list1[i + 1][1])]
                del list1[i + 1]
                del list1[i - 1]
                i -= 1
        i += 1
    i = 0
    print(list1)
    while i < len(list1):
        if not list1[i][0]:
            if list1[i][1] is '=':
                return array_minus(list1[i - 1][1], list1[i + 1][1])
        i += 1

while True:
    a = input('Any expr:').lower()
    # a = '2x= 5y+1'
    b = expr_extract(a)
    b = expr_unify(b)
    b = ''.join([b[i][1] for i in range(len(b))])
    print(b)
    b = expr_extract(b)
    b, dictionary = expr_variable_to_be_array(b)
    print(b)
    b = expr_calc(b)
    print(b)
    for i in dictionary:
        # print(i, '=', b[dictionary[i]])
        pass
    print('The input is simplified as ',
          b[dictionary['x']], 'x+',
          b[dictionary['y']], 'y+',
          b[dictionary['const']], '=0',
          sep='')
