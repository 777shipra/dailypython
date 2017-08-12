number=raw_input("enter the numbers")
num=number.split(",")
list=[]
for i in num :
  list.append(i)
print list
print  tuple(number.split(","))