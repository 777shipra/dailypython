from random import randint
print "lets play rock paper and scissor"
print "ready set go"
print "type r for rock , p for paper and s for scissor"
user=["r","p","s"]
computer=user[randint(0,2)]
count_win = 0
for x in user :
    user=raw_input("type:")
    if user == computer :
        print "tie"
    elif user=="r":
        if computer == "p":
            print "you win"
            count_win +=1
        else:
            print "you loose"
    elif user == "p":
        if computer =="r":
            print "you win"
            count_win +=1
        else:
            print "you loose"
    elif user == "s" :
        if computer == "p":
            print "you win"
            count_win +=1
        else:
            print "you loose"
for x in user :
    if count_win==2 :
      print "you won overall"
    else:
        print "better luck next time"




