import copy


class Chessboard:
    def __init__(self, a):
        self.__size = a
        self.__data = [[False] * a for i in range(a)]
        self.__state = [[False] * a, [False] * a, [False, False]]
        self.__queen = 0
        # The order is [[row1, row2, row3...], [column1, column2, column3...], [diagonal \, diagonal /]]

    def get_index(self):
        return self.__size * self.__size

    def get_status_index(self, index):
        return self.getstatus(index//self.__size, index%self.__size)

    def put_queen_index(self, index):
        return self.put_queen(index//self.__size, index%self.__size)

    def getstatus(self, a, b):
        if a == b and a + b == self.__size-1:
            return self.__state[0][a] or self.__state[1][b] or self.__state[2][0] or self.__state[2][1]
        elif a == b:
            return self.__state[0][a] or self.__state[1][b] or self.__state[2][0]
        elif a + b == self.__size-1:
            return self.__state[0][a] or self.__state[1][b] or self.__state[2][1]
        elif a != b:
            return self.__state[0][a] or self.__state[1][b]

    def put_queen(self, a, b):
        self.__data[a][b] = True
        self.__queen += 1
        if a == b and a + b == self.__size - 1:
            self.__state[0][a], self.__state[1][b], self.__state[2][0], self.__state[2][1] = True, True, True, True
        elif a == b:
            self.__state[0][a], self.__state[1][b], self.__state[2][0] = True, True, True
        elif a + b == self.__size - 1:
            self.__state[0][a], self.__state[1][b], self.__state[2][1] = True, True, True
        elif a != b:
            self.__state[0][a], self.__state[1][b] = True, True

    def count_queen(self):
        return self.__queen

    def print(self):
        # print([(' ', 'Q')[j] for j in self.__data[2]])
        # print(['|' + '|'.join([(' ', 'Q')[j] for j in self.__data[i]]) + '|' for i in self.__data])
        print('\n'.join(['|' + '|'.join([(' ', 'Q')[j] for j in i]) + '|' for i in self.__data]))
        print()


def point_find(from_index=0, csb=Chessboard(8), no=1):
    # global count
    # print(csb.count_queen())
    if csb.count_queen() == 8:
        print('嗯,已经有8个后了,打印一下')
        csb.print()
        # count += 1
    else:
        for i in range(from_index, csb.get_index()-1):
            print('从', from_index, '到', csb.get_index()-1, '找放第',  no, '个后的位置')
            # print('查找', i)
            print(csb.count_queen())
            if csb.get_status_index(i) is False:
                print('第', no, '个后放在了', i)
                csb.put_queen_index(i)
                print('现在有', csb.count_queen(), '个后了')
                point_find(i+1, csb=copy.deepcopy(csb), no=no+1)
# count = 0
print('searching...')
point_find()
print('hello')
# print(count)
