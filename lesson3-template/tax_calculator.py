from taxes import *

class Tax_Calculator(object):

    def calculate(self, budget, tax):
        calculated_tax = tax.calculate(budget)
        print(calculated_tax)

if __name__ == '__main__':
    from budget import Budget, Item

    calculator = Tax_Calculator()
    budget = Budget()
    budget.add_item(Item('item 1', 50))
    budget.add_item(Item('item 2', 200))
    budget.add_item(Item('item 3', 250))
    # budget.add_item(Item('item 4', 10))
    # budget.add_item(Item('item 5', 10))

    print('iss e icms')
    calculator.calculate(budget, ISS())
    calculator.calculate(budget, ICMS())

    print('icpp e ikcv')
    calculator.calculate(budget, ICPP())
    calculator.calculate(budget, IKCV())
