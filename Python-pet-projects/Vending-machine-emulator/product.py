def product_can(products,amount):
    can = 0
    for i in products:
        if int(i['quantity'])>0 and int(i['price'])<=amount:
            print("Название продукта: "+i['name'])
            print("Цена: "+i['price'])
            print("Количество: "+i['quantity'])
            print("Номер продутка: "+i['number']+'\n')
            can +=1
    if can == 0:
        print('Прости но у тебя не хвотает денег ни на что!!!')
        return "nope"
