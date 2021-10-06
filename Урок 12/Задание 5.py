def gold_data(data_gold):
    data_gold = data_gold.split('.')
    data1 = int(data_gold[0])
    data2 = int(data_gold[1])
    composition = int(data_gold[2]) % 100
    print(data1*data2 == composition)
data_g = input()
gold_data(data_g)
