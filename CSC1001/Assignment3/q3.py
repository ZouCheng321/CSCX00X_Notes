#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# By Licheng Mao, 115010202@link.cuhk.edu.cn

"""
Question 3 (40% of this assignment):
Write a Python class to simulate an ecosystem containing two types of creatures, bears and fish. The ecosystem consists
of a river, which is modeled as a relatively large list. Each element of the list should be a Bear object, a Fish
object, or None. In each time step, based on a random process, each animal either attempts to move into an adjacent
list location or stay where it is. If two animals of the same type are about to collide in the same cell, then they
stay where they are, but they create a new instance of that type of animal, which is placed in a random
empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish
dies (i.e., it disappears).
Write an initializer for the ecosystem class, the initializer should allow the user to assign the initial values of
the river length, the number of fishes and the number of bears. Before the simulation, fishes and bears should be
allocated randomly into the river. The ecosystem class should also contain a simulation() method, which will simulate
the next N steps of the random moving process. N should be inputted by the user. In each step of your simulation, all
animals in the river should try to take some random moves.
For example, assume that before the simulation, the initial state of the river is:
In which, ‘F’, ‘B’ and ‘N’ denote fish, bear and empty location respectively. Assume that in the first step of
simulation, the first fish will move to the left, the first bear will move to the right, and the second bear will
remain still. Then after the first step, the state of the river is:
To generate random numbers in Python, you should import the random() function by using the following statement:
By assigning the return of the random() function to a variable, you will get a random floating point number in the
range of [0, 1]. The following code is an example of using the random() function:
"""
import random


class Ecosystem(object):
    def __init__(self, **kwargs):
        if kwargs['len'] < kwargs['F'] + kwargs['B']:
            raise Exception('The sum of creatures is smaller than the length of the river')
        self.__len = kwargs['len']
        self.__init_f = kwargs['F']
        self.__init_b = kwargs['B']
        self.__debug = kwargs['debug']
        self.__data = [Creature('F')]*self.__init_f + [Creature('B')]*self.__init_b + [Creature('N')]*\
                                                                                      (self.__len -
                                                                                       self.__init_b -
                                                                                       self.__init_f)
        random.shuffle(self.__data)
        self.__none_set = set()
        for i, item in enumerate(self.__data):
            if item.s() == 'N':
                self.__none_set.add(i)

    def simulation(self):
        for i, item in enumerate(self.__data):
            if item == 'N':
                continue
            else:
                if i == 0:
                    move = random.choice((0, 1, ))
                elif i == self.__len-1:
                    move = random.choice((0, -1, ))
                else:
                    move = random.choice((0, -1, 1, ))
                if move == 0:
                    continue
                if self.__data[i+move].s() == 'N':
                    self.__data[i+move] = Creature(item.s())
                    self.__none_set.discard(i+move)
                    self.__data[i] = Creature('N')
                    self.__none_set.add(i)
                elif self.__data[i+move].s() == 'B':
                    if item.s() == 'F':
                        self.__data[i] = Creature('N')
                        self.__none_set.add(i)
                    elif item.s() == 'B':
                        if len(self.__none_set) == 0:
                            continue
                        random_place = random.choice(list(self.__none_set))
                        self.__data[random_place] = Creature('B')
                        self.__none_set.discard(random_place)
                elif self.__data[i+move].s() == 'F':
                    if item.s() == 'B':
                        self.__data[i+move] = Creature('B')
                        self.__data[i] = Creature('N')
                        self.__none_set.add(i)
                    if item.s() == 'F':
                        if len(self.__none_set) == 0:
                            continue
                        random_place = random.choice(list(self.__none_set))
                        self.__data[random_place] = Creature('F')
                        self.__none_set.discard(random_place)
        if self.__debug:
            print(' '.join(item.s() for item in self.__data))

    def print(self):
        print(' '.join(item.s() for item in self.__data))


class Creature(object):
    def __init__(self, s = 'Unknown'):
        self.__s = s

    def s(self):
        return self.__s

    def __repr__(self):
        return self.__s


def main():
    while True:
        length = input('Please input the length of the river:')
        count_f = input('Please input the number of the fishes:')
        count_b = input('Please input the number of the bears:')
        n = input('Please input the times of simulation:')
        try:
            length = int(length)
            count_f = int(count_f)
            count_b = int(count_b)
            n = int(n)
            if (length < (count_b + count_f)) or (length <= 0) or (count_f < 0) or (count_b < 0) or (n <= 0):
                raise TypeError
            river = Ecosystem(len=length, F=count_f, B=count_b, debug=False)
            # You can change the parameter 'debug' above to see the detail of each simulation
            for i in range(n):
                river.simulation()
            print('After {} times of simulation, the result is'.format(str(n)))
            river.print()
        except TypeError:
            print("Your input is not valid, please try again.")

if __name__ == '__main__':
    main()

