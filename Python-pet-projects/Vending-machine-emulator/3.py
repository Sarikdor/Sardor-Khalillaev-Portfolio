# def mount(products):
#     with open('products.txt' , 'w' , encoding='utf-8') as file:
import const
# from entrence import choose_product
def read(src):
    products = []
    k = 1
    with open(src , 'r' , encoding='utf-8') as file:
        
        while True:
            line = file.readline().strip().split(';')
            if len(line) == 1: 
                break
            data = {
               
               'name' : line[0],
               'price' : line[1],
               'quantity': line[2],
               'number': line[3]
            }
            products.append(data)
    return products
read('products.txt')
print(read('products.txt'))
def choose(amount , products):
    num = input('Введи номер продукта: ')
    while True:
        try:
            num = int(num)
            break
        except:
            print('Ошибка введите номер!!!!!!!')
    l = const.ZERO
    n = const.ZERO
    n=0
    for i in products:
        product = i
        n+=1
        if int(product['number']) == num:
            print('Name: '+product['name'])
            print('Costs: '+product['price'])
            print('Quantity: ' +str(int(product['quantity']) - 1))
            print('Number: '+product['number'])
            products[n-1]['quantity'] = str(int(product['quantity']) - 1)
            break
        if int(product['number']) == num and int(product['price']) > amount:
            print('У тебя не хватает денег!')
            break
    if n == len(products) and l == const.ONE:
        print('Такого номер не существует')
    return products
# print(choose(15000 ,read('products.txt') ))

def writer_products(products):
    with open('products.txt' , 'w', encoding='utf-8') as file:
        for i in products:
            file.write(i['name'] + ';')
            file.write(i['price'] + ';')
            file.write(i['quantity'] + ';')
            file.write(i['number'] + '\n')
writer_products(choose(20000 , read('products.txt')))
