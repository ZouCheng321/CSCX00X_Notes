#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module for input """

__author__ = 'Licheng Mao'


def input_regex(prompt, regex, error_str):
    import re
    input_value = input(prompt)
    if re.match(regex, input_value):
        return input_value
    print(error_str)
    return input_regex(prompt, regex, error_str)

