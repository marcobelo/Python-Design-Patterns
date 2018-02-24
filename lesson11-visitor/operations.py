
class Subtraction(object):
    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def check(self):
        return self.__left_expression.check() - self.__right_expression.check()

    def accepts(self, visitor):
        visitor.subtraction_visitor(self)

    @property
    def left_expression(self):
        return self.__left_expression

    @property
    def right_expression(self):
        return self.__right_expression


class Sum(object):
    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def check(self):
        return self.__left_expression.check() + self.__right_expression.check()

    def accepts(self, visitor):
        visitor.sum_visitor(self)

    @property
    def left_expression(self):
        return self.__left_expression

    @property
    def right_expression(self):
        return self.__right_expression


class Number(object):
    def __init__(self, number):
        self.__number = number

    def check(self):
        return self.__number

    def accepts(self, visitor):
        visitor.number_visitor(self)


if __name__ == '__main__':
    from printing import Printing

    printer = Printing()

    left_expression = Sum(Number(10), Number(20))
    right_expression = Sum(Number(5), Number(2))
    score_expression = Sum(left_expression, right_expression)
    # print(score_expression.check())
    score_expression2 = Subtraction(left_expression, right_expression)
    # print(score_expression2.check())

    score_expression.accepts(printer)
    print('')
    score_expression2.accepts(printer)
    print('')
