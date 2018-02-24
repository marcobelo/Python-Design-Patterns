def print_invoice(invoice):
    print('Printing the invoice: {}'.format(invoice.cnpj))

def send_email(invoice):
    print('Sending by email the invoice: {}'.format(invoice.cnpj))

def save_to_db(invoice):
    print('Saving to db the invoice: {}'.format(invoice.cnpj))
