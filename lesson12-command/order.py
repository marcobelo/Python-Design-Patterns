from datetime import date
from abc import ABCMeta, abstractmethod

class Order(object):
    def __init__(self, client, value):
        self.__client = client
        self.__value = value
        self.__status = 'NEW'
        self.__finish_date = None

    def paid(self):
        self.__status = 'PAID'

    def finish(self):
        self.__finish_date = date.today()
        self.__status = 'DELIVERED'

    @property
    def client(self):
        return self.__client

    @property
    def value(self):
        return self.__value

    @property
    def status(self):
        return self.__status

    @property
    def finish_date(self):
        return self.__finish_date


class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

class Finish_order(Command):
    def __init__(self, order):
        self.__order = order

    def execute(self):
        self.__order.finish()


class Pay_order(Command):
    def __init__(self, order):
        self.__order = order

    def execute(self):
        self.__order.paid()


class Job_queue(object):
    def __init__(self):
        self.__commands = []

    def add_command(self, command):
        self.__commands.append(command)

    def process(self):
        for command in self.__commands:
            command.execute()


if __name__ == '__main__':

    order1 = Order('marco', 200)
    order2 = Order('marco2', 400)

    job_queue = Job_queue()
    job_queue.add_command(Finish_order(order1))
    job_queue.add_command(Pay_order(order1))
    job_queue.add_command(Finish_order(order2))

    job_queue.process()
