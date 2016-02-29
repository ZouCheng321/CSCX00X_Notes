def load_dic():
    dic_handle = open('dic.dic', 'r')
    comment = []
    dic_data = []
    for line in dic_handle:
        if line.startswith('#'):
            comment.append(line)
        else:
            dic_data.append(line)
    return comment, dic_data

