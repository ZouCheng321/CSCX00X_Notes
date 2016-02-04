def replace_plus(target_value, find_from, known_position):
    if len(known_position) == 0:
        return ''
    else:
        print(find_from[:known_position[0]] + target_value)
        return find_from[:known_position[0]] + target_value + replace_plus(target_value, find_from[known_position[0]:], known_position[1:])


def find_plus(target_value, find_from):
    find_result = find_from.find(target_value)
    if find_result == -1:
        return []
    else:
        return [find_result] + find_plus(target_value, '*' * (find_result + 1) + find_from[find_result + 1:])


def input_plus(prompt, regex):
    if



print(input_plus(1,2))