

def is_valid(number):
    import re
    if re.match(r'^([4-6][0-9]{12,15})|(37[0-9]{11,14})$', number):
        if (sum_of_double_even_place(number) + sum_of_odd_place(number)) % 10 == 0:
            return True
        return False
    return False


def sum_of_double_even_place(number):
    return sum(int(i) for i in ''.join(str(int(i)*2) for i in list(number)[::2]))


def sum_of_odd_place(number):
    return sum(int(i) for i in list(number)[::-2])

print(is_valid('4388576018410707'))
print(is_valid('4388576018402626'))
print(is_valid('438857601840'))
# print(is_valid(4388576018410707))
# print(is_valid(4388576018410707))

