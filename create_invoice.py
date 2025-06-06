company_name = 'Company : The Clever Programmer'
company_address = 'Address : Vasavi Skycity.'
company_city = 'City : Hyderabad'
message = 'Thanks for shopping with us today!'
product1_name = 'Books     '
product1_price = 10.00
product2_name = 'Grosery   '
product2_price = 25.50
product3_name = 'Paper     '
product3_price = 5.75
print('*' * 50)
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))
print('=' * 50)
print('\tProduct Name\tProduct Price')
print('\t{}\t\t${:.2f}'.format(product1_name.title(), product1_price))
print('\t{}\t\t${:.2f}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${:.2f}'.format(product3_name.title(), product3_price))
print('=' * 50)
print('\t\t\tTotal')
total = product1_price + product2_price + product3_price
print('\t\t\t${:.2f}'.format(total))
print('=' * 50)
print('\n\t{}\n'.format(message))