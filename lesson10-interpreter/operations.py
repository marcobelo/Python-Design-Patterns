
class Subtraction(object):
    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def check(self):
        return self.__left_expression.check() - self.__right_expression.check()


class Sum(object):
    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def check(self):
        return self.__left_expression.check() + self.__right_expression.check()


class Number(object):
    def __init__(self, number):
        self.__number = number

    def check(self):
        return self.__number


if __name__ == '__main__':
    left_expression = Sum(Number(10), Number(20))
    right_expression = Sum(Number(5), Number(2))
    score_expression = Sum(left_expression, right_expression)
    print(score_expression.check())
    score_expression2 = Subtraction(left_expression, right_expression)
    print(score_expression2.check())
