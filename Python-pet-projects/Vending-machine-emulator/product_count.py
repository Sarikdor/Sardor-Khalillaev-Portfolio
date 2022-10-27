

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
     
read('products.txt')




              




    


            
