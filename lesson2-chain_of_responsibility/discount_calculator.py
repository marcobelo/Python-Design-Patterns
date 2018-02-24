from discount import *

class Discount_Calculator(object):

    def calculate(self, budget):
        discount = Discount_5_items(
            Discount_value_500(No_discount())
        ).calculate(budget)
        # if discount == 0:
        #     discount = Discount_value_500().calculate(budget)
        return discount


if __name__ == '__main__':
    from budget import Budget, Item

    budget = Budget()
    budget.add_item(Item('item 1', 100))
    budget.add_item(Item('item 2', 50))
    budget.add_item(Item('item 3', 10))
    budget.add_item(Item('item 4', 10))
    budget.add_item(Item('item 5', 10))

    print(budget.value)

    discount = Discount_Calculator()
    discount_total = discount.calculate(budget)
    print(discount_total)
