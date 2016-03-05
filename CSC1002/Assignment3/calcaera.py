#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TBD:
y = -x + 1
y = 1
"""


def debug(execute):
    """
    Debug用的东西
    :param execute:
    :return:
    """
    global isDebug
    if isDebug:
        print(execute)
    else:
        pass


def array_plus(list1, list2):

    """
    就是矩阵加法啦~~
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
    矩阵减法~~
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
    矩阵乘法好伐
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
    还没打算用的
    :param list1:
    :param list2:
    :return:
    """

    return list(map(lambda x: list1[0] / list2[x] + list2[0] / list1[x], list(range(len(list1)))))


def expr_extract(expr_extracted_from):

    """
    把表达式整理成链表形式,第一个值表示数据的类型, True为运算符, 否则是字符串
    :param expr_extracted_from:
    :return:
    """

    expr_extracted_from += '\n'
    expr_extract_unit = ''
    expr_extract_result = []
    for i in expr_extracted_from:
        if i in '+-*/=\n':
            if i == '-' and len(expr_extract_unit) == 0:
                expr_extract_result.append([True, '0'])
            if len(expr_extract_unit) != 0:
                expr_extract_result.append([True, expr_extract_unit])
            if i is not '\n':
                expr_extract_result.append([False, i])
            # else:
            #     expr_extract_result.append(False, '+')
            #     expr_extract_result.append(True, '0')
            expr_extract_unit = ''
        else:
            if i is not ' ':
                expr_extract_unit += i
    return expr_extract_result


def term_unify(term_to_be_unified):
    """
    往简写的一项里面补点运算符啦
    :param term_to_be_unified:
    :return:
    """
    if term_to_be_unified.isnumeric():
        return term_to_be_unified
    elif term_to_be_unified.isalpha():
        return '1*'+term_to_be_unified
    else:
        for i in range(len(term_to_be_unified)):
            if term_to_be_unified[i].isalpha():
                return term_to_be_unified[:i] + '*' + term_to_be_unified[i:]


def expr_unify(expr_to_be_unified):
    """
    对整个式子补充运算符
    :param expr_to_be_unified:
    :return:
    """
    for i in [j for j in range(len(expr_to_be_unified)) if expr_to_be_unified[j][0]]:
        expr_to_be_unified[i][1] = term_unify(expr_to_be_unified[i][1])
    return expr_to_be_unified


def expr_variable_to_be_array(list1):
    """
    将式中变量归档存储,并用矩阵替换
    :param list1:
    :return:
    """
    variable_dictionary = {'const': 0}
    index = 1
    for i in range(len(list1)):
        term = list1[i][1]
        if term.isalpha():
            if term not in variable_dictionary:
                variable_dictionary[term] = index
                index += 1
    index -= 1
    # print(variable_dictionary)
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
    进行化简运算啦,先算乘法除法再算加法减法
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
                # if i == 0 or list1[i - 1][0] == False:
                #     list1.insert(i, [True, '0'])
                #     continue
                list1[i] = [True, array_minus(list1[i - 1][1], list1[i + 1][1])]
                del list1[i + 1]
                del list1[i - 1]
                i -= 1
        i += 1
    i = 0
    # print(list1)
    while i < len(list1):
        if not list1[i][0]:
            if list1[i][1] is '=':
                return array_minus(list1[i - 1][1], list1[i + 1][1])
        i += 1


def deal_with_input_line(input_line):
    debug('[DEBUG]: Debug mode is on...')
    debug('[DEBUG]: Raw input is: \n\t\t\'{}\''.format(input_line))
    input_line = expr_extract(input_line)
    debug('[DEBUG]: Extracted input is: \n\t\t\'{}\''.format(input_line))
    input_line = expr_unify(input_line)
    input_line = ''.join([input_line[i][1] for i in range(len(input_line))])
    input_line = expr_extract(input_line)
    debug('[DEBUG]: Extracted input(unified) is \n\t\t\'{}\''.format(input_line))
    input_line, line_dictionary = expr_variable_to_be_array(input_line)
    input_line = expr_calc(input_line)
    debug('[DEBUG]: Abstracted line is {}, \n\t\twith dictionary {}'.format(input_line, line_dictionary))
    return input_line, line_dictionary


def intersection_point_find(line1, line2):
    """

    :param line1:
    :param line2:
    :return:
    """
    a1, b1, c1 = line1
    a2, b2, c2 = line2
    if b1 == 0 or b2 == 0:
        if b1 == b2 == 0:
            return 'No intersection'
        elif b1 == 0:
            x = - c1 / a1
            y = (- c2 - a2 * x) / b2
            return x, y
        elif b2 == 0:
            x = - c2 / a2
            y = (- c1 - a1 * x) / b1
            return x, y
    else:
        a1, b1, c1 = (- a1 / b1, - 1, - c1 / b1)
        a2, b2, c2 = (a2 / b2, 1, c2 / b2)
        if a1 + a2 == 0:
            if c1 + c2 == 0:
                return 'There the same line'
            else:
                return 'No intersection'
        else:
            x = - (c1 + c2) / (a1 + a2)
            y = (- c1 - a1 * x) / b1
            return x, y


def calc_magnitude(vector1):
    from math import sqrt
    return sqrt(vector1[0] * vector1[0] + vector1[1] * vector1[1])


def calc_side_length(point1, point2, point3):

    if point1 == point2 == point3:
        return False
    return (calc_magnitude(array_minus(point1, point2)),
            calc_magnitude(array_minus(point2, point3)),
            calc_magnitude(array_minus(point1, point3)))


def calc_area(length1, length2, length3):
    p = (length1 + length2 + length3) / 2
    from math import sqrt
    return sqrt(p * (p - length1) * (p - length2) * (p - length3))

while True:
    isDebug = False
    line = [0, 0, 0]
    line_dic = [0, 0, 0]


    def if_exist(cmd):
        try:
            return eval(cmd)
        except:
            return 0

    for i in range(3):
        line[i] = input('line{}'.format(i))
        line[i], line_dic[i] = deal_with_input_line(line[i])
        print('The input is simplified as ({})x+({})y+({})=0'.format(if_exist("line[i][line_dic[i]['x']]"),
                                                                   if_exist("line[i][line_dic[i]['y']]"),
                                                                   if_exist("line[i][line_dic[i]['const']]")
                                                                   )
              )

        line[i] = (if_exist("line[i][line_dic[i]['x']]"),
                   if_exist("line[i][line_dic[i]['y']]"),
                   if_exist("line[i][line_dic[i]['const']]")
                   )
        # print(line[i])
    p1 = list(intersection_point_find(line[0], line[1]))
    p2 = list(intersection_point_find(line[1], line[2]))
    p3 = list(intersection_point_find(line[0], line[2]))
    l1, l2, l3 = calc_side_length(p1, p2, p3)
    area = calc_area(l1, l2, l3)
    print('面积估摸着大概是', area)
