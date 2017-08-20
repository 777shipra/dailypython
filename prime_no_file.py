list=[]
for num in range(1,1000):
    if all(num%i!=0 for i in range(2,num)):

        list.append((num))
file=open("uno.txt","a")
file.writelines(str(list))
file.close()