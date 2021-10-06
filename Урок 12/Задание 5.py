data_gold = input()
data_gold = data_gold.split('.')

data1 = int(data_gold[0])
data2 = int(data_gold[1])
composition = int(data_gold[2]) % 100
print(data1*data2 == composition)