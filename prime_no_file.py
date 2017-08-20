list=[]
for num in range(1,1000):
    if all(num%i!=0 for i in range(2,num)):
       list.append(str(num))
file=open("one.txt","w")
file.writelines(list)
file.close()