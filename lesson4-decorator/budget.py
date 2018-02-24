
class Budget(object):

    def __init__(self):
        self.__items = []

    @property
    def value(self):
        total = 0.0
        for item in self.__items:
            total += item.value
        return total

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
