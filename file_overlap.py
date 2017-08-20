data1 = open("uno.txt", 'r').readline().split(',')
data2 = open("two.txt", 'r').readline().split(',')
res = list(set(data1) & set(data2))
print res