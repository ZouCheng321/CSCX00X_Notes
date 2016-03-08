class CalcError(Exception):
    pass


class Polynomial(object):
    """
    Polynomial is a class for math polynomials, whose algorithm is redefined
    """
    def __init__(self, other):
        if type(other) == Polynomial:
            self.__var = other.get_value()
        elif type(other) == str:
            try:
                self.__var = {'': float(other), }
            except ValueError:
                if other[0].isalpha() and other.isalnum():
                    self.__var = {other: 1, }
                else:
                    term = ''
                    other += '\n'
                    other = list(other)
                    for i in range(len(other) - 1):
                        if (other[i].isdigit() or other[i] == ')') and other[i + 1].isalpha():
                            other[i] += '*'
                    other = list(''.join(other))
                    for i in range(len(other)):
                        if other[i] not in '+-*/()\n':
                            term += other[i]
                            other[i] = ''
                        else:
                            if term != '':
                                other[i] = 'Polynomial(\'' + term + '\')' + other[i]
                            term = ''
                    other = list(''.join(other))
                    other.pop(-1)
                    # print(''.join(other))
                    # pass
                    self.__var = Polynomial(eval(''.join(other))).get_value()
        elif type(other) == int or type(other) == float:
            self.__var = {'': other}
        elif type(other) == dict:
            self.__var = other

    def __add__(self, other):
        if type(other) == Polynomial:
            return_dict = {}
            for i in self.get_value():
                if i not in return_dict:
                    return_dict[i] = self.get_value()[i]
                else:
                    return_dict[i] += self.get_value()[i]
            for i in other.get_value():
                if i not in return_dict:
                    return_dict[i] = other.get_value()[i]
                else:
                    return_dict[i] += other.get_value()[i]
            return Polynomial(return_dict)
        else:
            return self + Polynomial(other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == Polynomial:
            return self + -other
        else:
            return self - Polynomial(other)

    def __rsub__(self, other):
        if type(other) == Polynomial:
            return -self + other
        else:
            return Polynomial(other) - self

    def __neg__(self):
        return_dict = {}
        for other in self.get_value():
            return_dict[other] = -self.get_value()[other]
        return Polynomial(return_dict)

    def __mul__(self, other):
        if type(other) == Polynomial:
            if other.is_number():
                other = other.get_parameter('')
                return_dict = {}
                for i in self.get_value():
                    return_dict[i] = other * self.get_value()[i]
                return Polynomial(return_dict)
            elif self.is_number():
                return other * self

        if type(other) == int or type(other) == float:
            return self * Polynomial(other)

    def __rmul__(self, other):
        return self * other

    # def __truediv__(self, other):
    #     if type(other) == int or type(other) == float:
    #         return_dict = {}
    #         for other in self.get_value():
    #             if other not in return_dict:
    #                 return_dict[other] = self.get_value()[other] / other
    #             return Polynomial(return_dict)
    #
    # def __rtruediv__(self, other):
    #     if type(other) == int or type(other) == float:
    #         return_dict = {}
    #         for other in self.get_value():
    #             if other not in return_dict:
    #                 return_dict[other] = other / self.get_value()[other]
    #             return Polynomial(return_dict)

    def __repr__(self):
        return '+'.join('' + str(self.get_value()[i]) + '' + i for i in self.get_value())

    def is_number(self):
        if len(self.get_value()) == 1 and ('' in self.get_value()):
            return True
        else:
            return False

    def get_value(self):
        return self.__var

    def get_parameter(self, other):
        if other in self.__var:
            return self.get_value()[other]
        else:
            return 0

    def get_magnitude(self):
        import math
        # print(self.__var)
        return math.sqrt(sum(float(self.__var[coefficient])**2 for coefficient in self.__var))
        

class Equation(object):
    """
    The Equation is a class of math equation, which contain two inner polynomial. the __left and __right are the
    left and right part of the equation
    """
    def __init__(self, other):
            if type(other) == str:
                other = other.split('=')
                if len(other) == 2:
                    self.__left = Polynomial(other[0])
                    self.__right = Polynomial(other[1])
                else:
                    raise ValueError
            else:
                raise ValueError
        
    def get_expression(self):
        return self.__left - self.__right


def input_terminate(*args, **kwargs):
    """
    This function works the same like 'input', except for 'terminate' support.
    :param args:
    :param kwargs:
    :return:
    """
    input_value = input(*args, **kwargs)
    if input_value == 'terminate':
        exit()
    else:
        return input_value


def intersection_point_find(line1, line2):
    """
    This function can be used to find an intersection of two lines. It will raise an error in some occasion.
    :param line1: line1 as a Polynomial
    :param line2: line2 as a Polynomial
    :return:
    """
    a1, b1, c1 = line1.get_parameter('x'), line1.get_parameter('y'), line1.get_parameter('')
    a2, b2, c2 = line2.get_parameter('x'), line2.get_parameter('y'), line2.get_parameter('')
    if b1 == 0 or b2 == 0:
        if b1 == b2 == 0:
            raise CalcError('No intersection between two line.')
        elif b1 == 0:
            x = - c1 / a1
            y = (- c2 - a2 * x) / b2
            return {'x': x, 'y': y}
        elif b2 == 0:
            x = - c2 / a2
            y = (- c1 - a1 * x) / b1
            return {'x': x, 'y': y}
    else:
        a1, b1, c1 = (- a1 / b1, - 1, - c1 / b1)
        a2, b2, c2 = (a2 / b2, 1, c2 / b2)
        if a1 + a2 == 0:
            if c1 + c2 == 0:
                raise CalcError('The same line is found.')
            else:
                raise CalcError('No intersection between two line.')
        else:
            x = - (c1 + c2) / (a1 + a2)
            y = (- c1 - a1 * x) / b1
            return {'x': x, 'y': y}


def calc_area(list1):
    p = (sum(list1)) / 2
    if 0.0 in list1:
        raise CalcError('No triangle found.')
    import math
    return math.sqrt(p * (p - list1[0]) * (p - list1[1]) * (p - list1[2]))


def main():
    while True:
        try:
            print('---------------------------------------------------------------------------')
            print('This programme can calculate the area of triangle generated be three lines.')
            print('Enter \'terminate\' to terminate at any time')
            line = []
            intersection_point = []
            side = []
            # Load the lines...
            for i in range(3):
                line.append(Equation(input_terminate('The line{} is:'.format(i + 1))).get_expression())
                print('\t-- which can be unified as {}=0'.format(line[i]))
            # Load the intersections.
            for i in range(3):
                intersection_point.append(Polynomial(intersection_point_find(line[i-1], line[i])))
            # Load the sides.
            for i in range(3):
                side.append((intersection_point[i-1]-intersection_point[i]).get_magnitude())
            print('\nThe size is {0:g}'.format(calc_area(side)))
        except CalcError as e:
            print('\n[ERROR]:', e, 'Try again...')
        except ValueError:
            print('\n[ERROR]:', 'Unknown value error.', 'Try again...')
        except AttributeError:
            print('\n[ERROR]:', 'Unknown attribute error.', 'Try again...')

if __name__ == "__main__":
    main()



