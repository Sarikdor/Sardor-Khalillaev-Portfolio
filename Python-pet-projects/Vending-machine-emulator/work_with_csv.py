from asyncore import write
import csv
# def reader(src):
#     with open(src , 'r' , encoding= 'utf-8') as csvfile:
#         reader = csv.DictReader(csvfile , delimiter = ';')
#         denomination = []
#         amount = []
#         for i in reader:
#             # print(i)
#             denomination.append(i['Denomination'])
#             amount.append(i['Amount'])
#         return denomination , amount
# all = reader("denomination_for_admin.csv")
# print(all)
# class Problem(Exception):
#     pass
# def __security(all):
#     while True:
#         amount_money = input('Введите банкноту: ')
#         try:
#             if amount_money in all[0]:
#                 return amount_money
#             else:
#                 raise Problem('Пробдема!Вы ввели неправильную банкноту!')
#         except Problem as pr:
#             print(pr)
# # money = __security(all) 
def updating(money , all):
    for i in all:
        for ii in i :
            if int(ii) == money:
                index = i.index(ii)
                ko= int(all[1][index])
                ko+=1
                all[1][index] = str(ko)
            
        break
    lists = [all , money]
    return lists
# updating(money  , all)
def writer(all , src):
    with open(src , 'w' ,newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile , delimiter = ';')
        writer.writerow(
            ('Denomination' , 'Amount')
        )
        denominate = all[0]
        amount = all[1]
        for i in range(len(denominate)):
            user1 = []
            denominate[i].strip()
            amount[i].strip()
            user1.append(denominate[i])
            user1.append(amount[i])
            # print(user1)
            writer.writerow(
                user1
            )
    
# writer(all , 'denomination_for_admin.csv')
