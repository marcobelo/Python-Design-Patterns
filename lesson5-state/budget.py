from abc import ABCMeta, abstractmethod

class Budget_States(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.applied_discount = False

    @abstractmethod
    def apply_extra_discount(self, budget):
        pass

    @abstractmethod
    def approve(self, budget):
        pass

    @abstractmethod
    def disapprove(self, budget):
        pass

    @abstractmethod
    def finalize(self, budget):
        pass

class On_approval(Budget_States):
    def apply_extra_discount(self, budget):
        if not self.applied_discount:
            budget.add_extra_discount(budget.value * 0.02)
            self.applied_discount = True
        else:
            raise Exception("Discount already applied")

    def approve(self, budget):
        budget.state = Approved()

    def disapprove(self, budget):
        budget.state = Disapproved()

    def finalize(self, budget):
        raise Exception("Budget on approval can't be finalized")

class Approved(Budget_States):
    def apply_extra_discount(self, budget):
        if not self.applied_discount:
            budget.add_extra_discount(budget.value * 0.05)
            self.applied_discount = True
        else:
            raise Exception("Discount already applied")

    def approve(self, budget):
        raise Exception("Budget already approved")

    def disapprove(self, budget):
        raise Exception("Approved budget can't be disapproved")

    def finalize(self, budget):
        budget.state = Finished()

class Disapproved(Budget_States):
    def apply_extra_discount(self, budget):
        raise Exception("Disapproved budget don't recieve extra discount.")

    def approve(self, budget):
        raise Exception("Disapproved budget can't be approved")

    def disapprove(self, budget):
        raise Exception("Disapproved budget can't be disapproved again")

    def finalize(self, budget):
        budget.state = Finished()

class Finished(Budget_States):
    def apply_extra_discount(self, budget):
        raise Exception("Finished budget don't recieve extra discount.")

    def approve(self, budget):
        raise Exception("Finished budget can't be approved")

    def disapprove(self, budget):
        raise Exception("Finished budget can't be disapproved")

    def finalize(self, budget):
        raise Exception("Finished budget can't be finished again")




class Budget(object):
    def __init__(self):
        self.__items = []
        self.state = On_approval()
        self.__extra_discount = 0

    def approve(self):
        self.state.approve(self)

    def disapprove(self):
        self.state.disapprove(self)

    def finalize(self):
        self.state.finalize(self)

    def apply_extra_discount(self):
        self.state.apply_extra_discount(self)

    def add_extra_discount(self, discount):
        self.__extra_discount += discount

    @property
    def value(self):
        total = 0.0
        for item in self.__items:
            total += item.value
        return total - self.__extra_discount

    def get_items(self):
        return tuple(self.__items)

    @property
    def total_items(self):
        return len(self.__items)

    def add_item(self, item):
        self.__items.append(item)


class Item(object):

    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

if __name__ == '__main__':

    budget = Budget()
    budget.add_item(Item('item 1', 50))
    budget.add_item(Item('item 2', 25))
    budget.add_item(Item('item 3', 25))
    # budget.add_item(Item('item 4', 10))
    # budget.add_item(Item('item 5', 10))

    # print(budget.value)
    # budget.apply_extra_discount()
    print(budget.value)
    budget.apply_extra_discount()
    print(budget.value)
    budget.approve()
    budget.apply_extra_discount()
    print(budget.value)
    # budget.apply_extra_discount()
    # budget.approve()
    # budget.apply_extra_discount()
    # print(budget.value)
