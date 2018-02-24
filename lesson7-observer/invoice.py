from datetime import date

class Item(object):
    def __init__(self, description, value):
        self.__description = description
        self.__value = value

    @property
    def description(self):
        return self.__description

    @property
    def value(self):
        return self.__value


class Invoice(object):
    def __init__(self, social_name, cnpj, items, date_of_issue=date.today(), details='', observers=[]):
        self.__social_name = social_name
        self.__cnpj = cnpj
        self.__date_of_issue = date_of_issue
        if len(details) > 20:
            raise Exception("Invoice details can't have more than 20 char")
        self.__details = details
        self.__items = items

        for observer in observers:
            observer(self)

        # print_invoice(self)
        # send_email(self)
        # save_to_db(self)

    @property
    def social_name(self):
        return self.__social_name

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def details(self):
        return self.__details


if __name__ == '__main__':
    from observer import print_invoice, send_email, save_to_db

    items = [
            Item('item 1', 100),
            Item('item 2', 200)
            ]

    invoice = Invoice(
        social_name='FHSA Limited',
        cnpj='012345678910',
        items=items,
        date_of_issue=date.today(),
        details='details about fhsa',
        observers= [print_invoice, send_email, save_to_db]
    )
