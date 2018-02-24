from abc import ABCMeta, abstractmethod

class Tax(object):
    def __init__(self, other_tax = None):
        self.__other_tax = other_tax

    @abstractmethod
    def calculate(self, budget):
        pass

    def calculate_other_tax(self, budget):
        if self.__other_tax is None:
            return 0
        else:
            return self.__other_tax.calculate(budget)


class Template_conditional_tax(Tax):
    __metaclass__ = ABCMeta
    def calculate(self, budget):
        if self.use_max_tax(budget):
            return self.max_tax(budget) + self.calculate_other_tax(budget)
        else:
            return self.min_tax(budget) + self.calculate_other_tax(budget)

    @abstractmethod
    def use_max_tax(self, budget):
        pass

    @abstractmethod
    def max_tax(self, budget):
        pass

    @abstractmethod
    def min_tax(self, budget):
        pass

def IPVX(func):
    def wrapper(self, budget):
        return func(self, budget) + 10000
    return wrapper

class ISS(Tax):
    @IPVX
    def calculate(self, budget):
        return budget.value * 0.1 + self.calculate_other_tax(budget)

class ICMS(Tax):
    def calculate(self, budget):
        return budget.value * 0.06 #+ self.calculate_other_tax(budget)

class ICPP(Template_conditional_tax):
    def use_max_tax(self, budget):
        return budget.value > 500

    def max_tax(self, budget):
        return budget.value * 0.07

    def min_tax(self, budget):
        return budget.value * 0.05


class IKCV(Template_conditional_tax):
    def use_max_tax(self, budget):
        return budget.value > 500 and self.__have_item_with_value_over_100(budget)

    def max_tax(self, budget):
        return budget.value * 0.1

    def min_tax(self, budget):
        return budget.value * 0.06

    def __have_item_with_value_over_100(self, budget):
        for item in budget.get_items():
            if item.value > 100:
                return True
        return False
