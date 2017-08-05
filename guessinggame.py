print "let's play"
print "so, this is what it's all about"
print "i choosed a number from 1 to 10  and u have to guess it "
print "but u just have 2 turns"
user = [1,2]
for a in user :
    a=raw_input("enter your guessed number or type exit for quitting")
    if (a>7 or a<3) :
        print "u are going away"
    if (a == 6 or a == 7 or a==4 or a == 3):
       print "u are close"
    if (a==5 ):
       print "u guessed it , congrats"
    if (a=='exit'):
        exit()


