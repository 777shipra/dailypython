from random import randint
while True:
    print "lets play rock paper and scissor"
    print "<------ Lets Get Started ------>\n"
    print 'Hey! We Welcomes U to the Game --> Rock Paper And Scissor\n'
    print 'Select your menu options Given Below:\n'
    print "Select Option:'Y' : To play the game.\n"
    print "Select Option:'N' : To exit the game.\n"
    choice =  raw_input("enter ur choice")
    if choice.upper() ==  "Y":
        print "ready set go"
        print "type r for rock , p for paper and s for scissor"
        user = ["r", "p", "s"]
        computer = user[randint(0, 2)]
        count_win = 0
        for x in user:
            user = raw_input("type:")
            if user == computer:
                print "tie"
            elif user == "r":
                if computer == "p":
                    print "you win"
                    count_win += 1
                else:
                    print "you loose"
            elif user == "p":
                if computer == "r":
                    print "you win"
                    count_win += 1
                else:
                    print "you loose"
            elif user == "s":
                if computer == "p":
                    print "you win"
                    count_win += 1
                else:
                    print "you loose"
        for x in user:
            if count_win == 2:
                print "you won overall"
            else:
                print "better luck next time"

    elif choice.upper() == "N":
        exit()