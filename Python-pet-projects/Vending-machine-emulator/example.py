def read():
    with open('amount.txt', 'r',encoding='utf-8') as file:
        amount = file.read()
        print((amount))
read()
def write(amount):
    with open('amount.txt' , 'w' , encoding='utf-8') as file:
        file.write(amount)     
# write('5')
