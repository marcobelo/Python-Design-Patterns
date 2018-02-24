
class Printing(object):
    def sum_visitor(self, sum):
        print('(',end='')
        sum.left_expression.accepts(self)
        print('+',end='')
        sum.right_expression.accepts(self)
        print(')',end='')

    def subtraction_visitor(self, subtraction):
        print('(',end='')
        subtraction.left_expression.accepts(self)
        print('-',end='')
        subtraction.right_expression.accepts(self)
        print(')',end='')

    def number_visitor(self, number):
        print(number.check(),end='')

class Printing2(object):
    def sum_visitor(self, sum):
        print('+(',end='')
        sum.left_expression.accepts(self)
        print(',',end='')
        sum.right_expression.accepts(self)
        print(')',end='')

    def subtraction_visitor(self, subtraction):
        print('-(',end='')
        subtraction.left_expression.accepts(self)
        print(',',end='')
        subtraction.right_expression.accepts(self)
        print(')',end='')

    def number_visitor(self, number):
        print(number.check(),end='')
