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
    def __init__(self, social_name, cnpj, items, date_of_issue=date.today(), details=''):
        self.__social_name = social_name
        self.__cnpj = cnpj
        self.__date_of_issue = date_of_issue
        if len(details) > 20:
            raise Exception("Invoice details can't have more than 20 char")
        self.__details = details
        self.__items = items

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
    from invoice_creator import Invoice_creator

    items = [
            Item('item 1', 100),
            Item('item 2', 200)
            ]

    invoice = Invoice(
        social_name='FHSA Limited',
        cnpj='012345678910',
        items=items,
        date_of_issue=date.today(),
        details='details about fhsa'
    )

    invoice_from_builder = Invoice_creator().with_social_name('FHSA Limited').with_cnpj('012345678910').with_items(items).with_date_of_issue(date.today()).with_details('details about fhsa').build()
