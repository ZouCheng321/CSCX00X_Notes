#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question 4 (15% of this assignment):
(Anagrams) Write a function that checks whether two words are anagrams. Two words are anagrams if they contain the
same letters. For example, silent and listen are anagrams. The header of the function is:
"""


def is_anagram(s1, s2):
    return sorted(list(s1.lower())) == sorted(list(s2.lower()))
print('is {}an anagram'.format(('not ', '')[is_anagram(input('Word 1: '), input('Word 2: '))]))

