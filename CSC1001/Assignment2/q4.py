def is_anagram(s1, s2):
    l1, l2 = list(s1), list(s2)
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False

print(is_anagram('apple','banana'))
print(is_anagram('apple','eppla'))
print(is_anagram('silent','listen'))