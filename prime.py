number=int(raw_input("enter the number to be checked"))
if number>1:
    for i in range(2,number):
        if number%i==0 :
            print "not prime"
    else:
            print "prime"
else:
    print "not prime"

