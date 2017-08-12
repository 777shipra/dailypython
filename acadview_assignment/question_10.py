list=[1,2,3,4,5,6,7,8,9]
alist=[]
for x in list:
    if not(x%2==0):
        c=x*x

        alist.append(str(c))
print ','.join(alist)