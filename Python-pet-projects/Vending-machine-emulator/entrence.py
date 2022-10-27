import csv
import const
import change
from product import product_can
from work_with_csv import writer , updating
def writer_products(products):
    with open('products.txt' , 'w', encoding='utf-8') as file:
        for i in products:
            file.write(i['name'] + ';')
            file.write(i['price'] + ';')
            file.write(i['quantity'] + ';')
            file.write(i['number'] + '\n')
def read_amount():
    with open('amount.txt', 'r',encoding='utf-8') as file:
        amount = file.read()
        return amount

def write_amount(amount):
    with open('amount.txt' , 'w' , encoding='utf-8') as file:
        file.write(amount)
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

def reader(src):
    with open(src , newline='' , encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=";")
        denominations = []
        amount = []
        for row in reader:
            denominations.append(row['Denomination'])
            amount.append(row['Amount'])
        return denominations , amount
all = reader('denomination_for_admin.csv')
class Problem(Exception):
    pass
def __hello():
    print("""
Добро пожаловать на наш торговый автомат!
Наши валюты:
1000
2000
5000
10000
    """)
__hello()
def __security(all):
    while True:
        amount_money = input('Введите банкноту: ')
        try:
            if amount_money in all[0]:
                return amount_money
            else:
                raise Problem('Пробдема!Вы ввели неправильную банкноту!')
        except Problem as pr:
            global __hello
            print(pr)
            __hello()
def __show_functions():
    print(
        """
1. Вставить банкноту
2. Показать доступные продукты
3. Выбрать продукт
4. Получить сдачу 
        """
    )
def chose_action():
    while True:
        action = input('Введите функцию: ')
        try:
            action = int(action)
            if action == const.BANKNOTE:
                return const.BANKNOTE
            elif action == const.SHOW_PRODUCTS:
                return const.SHOW_PRODUCTS
            elif action == const.CHOOSE_PRODUCT:
                return const.CHOOSE_PRODUCT
            elif action == const.EXCHANGE:
                return const.EXCHANGE
            else:
                int('ok')
        except:
            print('Вы выбрали неправильную функцию!Пожалуйста введите заново!')

def __products():
    with open("products.txt" , 'r' , encoding='utf-8') as file:
        for i in file:
            product = i.split(';')
            if int(product[2]) > 0 :
                print("Название продукта: "+product[0])
                print("Цена: "+product[1])
                print("Количество: "+product[2])
                print("Номер продутка: "+product[3])
def choose(amount , products):
    num = input('Введи номер продукта: ')
    while True:
        try:
            num = int(num)
            break
        except:
            print('Ошибка введите номер!!!!!!!')
            num = input('Введи номер продукта: ')
    l = const.ZERO
    n = const.ZERO
    n = 0
    n = 0
    for i in products:
        product = i
        n+=1
        if int(product['number']) == num:
            amount -= int(product['price'])
            if amount < 0 :
                amount += int(product['price'])
                print('У тебя не хвотает денег!')
                lists = [amount , products]
                return lists
            print('Name: '+ product['name'])
            print('Costs: '+ product['price'])
            print('Quantity: ' + str(int(product['quantity']) - 1))
            print('Number: '+ product['number'])
            products[n - 1]['quantity'] = str(int(product['quantity']) - 1)
            print('Your balance: '+ str(amount))
            break
    if n == len(products) and l == const.ONE:
        print('Такого номер не существует')
    lists = [amount , products]
    return lists

def see_all(AMOUNT):
    products = read('products.txt')
    while True:
        __show_functions()
        action = chose_action()
        if action == const.BANKNOTE:
            AMOUNT = int(AMOUNT)
            upgratings=updating(int(__security(reader("denomination_for_admin.csv"))),all)
            AMOUNT+=int(upgratings[1])
            writer(upgratings[0] , 'denomination_for_admin.csv')

            print(f'Ваш баланс : {AMOUNT}')
            write_amount(str(AMOUNT))
        elif action == const.SHOW_PRODUCTS:
            __products()
        elif action == const.CHOOSE_PRODUCT:
            cans=product_can(products , AMOUNT)
            if cans == "nope":
                continue
            lists = choose( int(read_amount()) , products)
            AMOUNT=lists[0]
            write_amount(str(AMOUNT))
            writer_products(lists[1])
        elif action == const.EXCHANGE:
            if AMOUNT == 0:
                print('Ваш баланс 0 мы не можем выдать сдачу!!!')
            else: change.exchange(AMOUNT)
            write_amount('0')
            AMOUNT=read_amount()
see_all(int((read_amount())))
