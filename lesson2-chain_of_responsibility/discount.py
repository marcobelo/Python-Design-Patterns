
class Discount_5_items(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, budget):
        if budget.total_items >= 5:
            return budget.value * 0.1
        else:
            return self.__next_discount.calculate(budget)


class Discount_value_500(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, budget):
        if budget.value >= 500:
            return budget.value * 0.07
        else:
            return self.__next_discount.calculate(budget)

class No_discount(object):
    def calculate(self, budget):
        return 0
