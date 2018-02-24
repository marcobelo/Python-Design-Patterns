from datetime import date

class Contract(object):
    def __init__(self, date, client, type):
        self.__date = date
        self.__client = client
        self.__type = type

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self.__client = client

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    def advances(self):
        if self.__type == 'NEW':
            self.__type = 'ON_PROGRESS'
        elif self.__type == 'ON_PROGRESS':
            self.__type = 'SUCCESSFUL'
        elif self.__type == 'SUCCESSFUL':
            self.__type = 'DONE'

    def save_state(self):
        return State(Contract(date=self.__date, client=self.__client, type=self.__type))

    def restore_state(self, state):
        self.__client = state.contract.client
        self.__date = state.contract.date
        self.__type = state.contract.type



class State(object):
    def __init__(self, contract):
        self.__contract = contract

    @property
    def contract(self):
        return self.__contract


class Historic(object):
    def __init__(self):
        self.__saved_states = []

    def get_state(self, index):
        return self.__saved_states[index]

    def add_state(self, state):
        self.__saved_states.append(state)


if __name__ == '__main__':
    hist = Historic()

    contract = Contract(date=date.today(), client='Marco', type='NEW')
    print(contract.type)
    hist.add_state(contract.save_state())
    contract.advances()
    hist.add_state(contract.save_state())
    print(contract.type)
    contract.advances()
    hist.add_state(contract.save_state())
    print(contract.type)
    contract.advances()
    hist.add_state(contract.save_state())
    print(contract.type)
    contract.restore_state(hist.get_state(1))
    print(contract.type)
