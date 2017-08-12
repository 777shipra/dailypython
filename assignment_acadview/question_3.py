square={}
key=int(raw_input("enter the number:"))
for i in range(0,key+1):
    value=i*i
    square.update({i:value})
print square

