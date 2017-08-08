def prime(a) :
    i=range(2,100)
    if (a%a==0 and a%1==0) :
        return "prime"
    elif a%i==0 :
        return "not"
a=input("enter the number")
print (prime(a))

