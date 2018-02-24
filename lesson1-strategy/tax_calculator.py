from taxes import *

class Tax_Calculator(object):

    def calculate(self, budget, tax):
        calculated_tax = tax(budget) #The strategy is defined by the function var 'tax'
        print(calculated_tax)

if __name__ == '__main__':
    from budget import Budget
    calculator = Tax_Calculator()
    budget = Budget(500)
    calculator.calculate(budget, calculate_ISS)
