def max(a,b,c):
    if (a>b) and (a>c) :
        print "greatest if",a
    elif (b>a) and (b>c) :
        print "greatest is",b
    else:
        print "greatest is",c
print "print your numbers"
a=int(raw_input("first number"))
b=int(raw_input("second number please"))
c=int(raw_input("last number"))
max(a,b,c)