from datetime import date
from invoice import Invoice

class Invoice_creator(object):
    def __init__(self):
        self.__social_name = None
        self.__cnpj = None
        self.__date_of_issue = date.today()
        self.__items = None
        self.__details = ''

    def with_social_name(self, social_name):
        self.__social_name = social_name
        return self

    def with_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def with_date_of_issue(self, date_of_issue):
        self.__date_of_issue = date_of_issue
        return self

    def with_items(self, items):
        self.__items = items
        return self

    def with_details(self, details):
        self.__details = details
        return self

    def build(self):
        if self.__social_name is None:
            raise Exception("Social name cannot be empty")
        if self.__cnpj is None:
            raise Exception("Cnpj cannot be empty")
        if self.__items is None:
            raise Exception("Items cannot be empty")

        return Invoice(
            social_name=self.__social_name,
            cnpj=self.__cnpj,
            date_of_issue=self.__date_of_issue,
            items=self.__items,
            details=self.__details
            )
