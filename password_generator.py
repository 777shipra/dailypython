from random import randint
print "let us generate a password for you"
print "what kind of password do u want.\n 1. Strong \n 2.Weak \n choose your option "
choice=int(raw_input("enter your choice:"))
count=0
password = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
password.extend('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_-+={[}]:;,.<>?')
if choice==1:
    print "want a weak password or strong \n1.STRONG PASSWORD\n2.WEAK PASSWORD"
    choose=int(raw_input("enter your choice:"))
    if choose==1:
        while count<=10:
            generate=password[randint(0,86)]
            print generate
            count=count+1
    if choose==2:
        while count<=5:
            generate=password[randint(0,86)]
            count=count+1
elif choice==2:
    while count<=2:
        generate=password[randint(0,86)]
        print generate
        count=count+1
else:
    print "invalid option . TRY AGAIN"