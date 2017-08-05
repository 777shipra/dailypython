def add (a,b) :
    return a+b
def sub (a,b) :
    return a-b
def multiply (a,b) :
    return a*b
def divide (a,b) :
    return a/b
choice=input("enter your choice 1/2/3/4")
if choice > 4 :
    print "invalid option , optiona available till 4"
    exit()

a=int(raw_input("enter first number"))
b=int (raw_input("enter second number"))

if choice == 1 :
    print (add(a,b))
if choice == 2 :
    print (sub(a,b))
if choice == 3 :
    print (multiply(a,b))
if choice == 4 :
    print (divide(a,b))

