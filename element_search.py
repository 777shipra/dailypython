def find (list):
    if value in list:
        print "TRUE"
    else:
        print "FALSE"
number=raw_input("enter the numbers")
num=number.split(",")
list=[]
for i in num :
  list.append(i)
list.sort()
value=(raw_input("enter the number to be searched"))
find(value)