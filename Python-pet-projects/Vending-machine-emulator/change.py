def exchange(money):
    count_10 = money // 1000
    money -= count_10 * 1000
    count_5 = money // 500
    money -= count_5 * 500
    count_2 = money // 200
    money -= count_2 * 200
    count_1 = money // 100
    money -= count_1 * 100
    count_50 = money // 50
    money -= count_50 * 50
    print(f'1000 >> {count_10} \n 500 >> {count_5} \n 200 >> {count_2} \n 100 >> {count_1} \n 50 >> {count_50}')
