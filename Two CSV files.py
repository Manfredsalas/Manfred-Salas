import csv
from datetime import datetime

def read_products(filename):
    products = {}
    with open(filename, mode ='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        
        for row in reader:
            key = row[0]
            product_desc = row[1]
            product_price = row[2]
            products[key] = [product_desc, product_price]

    return products

def read_request(filename):
    product_ids = []
    quantities = []
    with open(filename, 'rt') as csv_request:
        reader = csv.reader(csv_request)
        next(reader)

        for row in reader:
            product_ids.append(row[0])
            quantities.append(row[1])
            
    return product_ids, quantities

def main():
    products = read_products('products.csv')
    product_ids = read_request('request.csv')[0]
    quantities = read_request('request.csv')[1]
    print()
    print('Super el many')
    print()

    subtotal = 0
    total_items = 0 

    for i in range(len(product_ids)):
        product = products[product_ids[i]]
        name = product[0]
        price = float(product[1])
        quantity = float(quantities[i])
        print(f'{name}: {quantity} @ {price}')
        subtotal = subtotal + ((quantity) * price)
        total_items += quantity

    print()
    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Total Items:{int(total_items)}')
    print(f'Tax: ${subtotal * 0.06:.2f}')
    print(f'Total: ${subtotal * 1.06:.2f}')

    print()
    payment = float(input('Payment: $'))
    change = payment - (subtotal * 1.06)
    if change > 0:
        print(f'Your Change is: ${change:.2f}')
        print()
        print('thanks you for you purchase!')
        current_date = datetime.now()
        print(f'{current_date:%a %b %d %Y  %H:%M:%S}')
    else:
        print('Error. You need to pay the total of this ticket.')

    

main()
read_products('products.csv')