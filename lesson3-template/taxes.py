from abc import ABCMeta, abstractmethod

class Template_conditional_tax(object):
    __metaclass__ = ABCMeta
    def calculate(self, budget):
        if self.use_max_tax(budget):
            return self.max_tax(budget)
        else:
            return self.min_tax(budget)

    @abstractmethod
    def use_max_tax(self, budget):
        pass

    @abstractmethod
    def max_tax(self, budget):
        pass

    @abstractmethod
    def min_tax(self, budget):
        pass


class ISS(object):
    def calculate(self, budget):
        return budget.value * 0.1

class ICMS(object):
    def calculate(self, budget):
        return budget.value * 0.06

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
