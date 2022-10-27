import csv
def reader(src):
    with open(src , 'r' , encoding= 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile , delimiter = ';')
        denomination = []
        amount = []
        for i in reader:
            # print(i)
            denomination.append(i['Denomination'])
            amount.append(i['Amount'])
        return denomination , amount
all = reader("denomination_for_admin.csv")
print(all)
class Problem(Exception):
    pass
def __security(all):
    while True:
        amount_money = input('Введите банкноту: ')
        try:
            if amount_money in all[0]:
                return amount_money
            else:
                raise Problem('Пробдема!Вы ввели неправильную банкноту!')
        except Problem as pr:
            print(pr)
money = __security(all)