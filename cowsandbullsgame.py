from random import randint
while True:
    print "lets play cows and bulls"
    print "<------ Lets Get Started ------>\n"
    print 'Hey! We Welcomes U to the Game --> cows and bulls\n'
    print 'Select your menu options Given Below:\n'
    print "Select Option:'Y' : To play the game.\n"
    print "Select Option:'N' : To exit the game.\n"
    choice =  raw_input("enter ur choice")
    if choice.upper() ==  "Y":
        print "ready set go"
        list = []
        computer = []
        count = 0
        i = 0
        j = 0
        cows = 0
        bulls = 0
        number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        while (count < 4):
            num = int(raw_input("enter the number"))
            newlist = list.append(num)
            num2 = number[randint(0, 9)]
            alist = computer.append(num2)
            count = count + 1
        print list

        for x in list:
            if list[i] == computer[j]:

                i = i + 1
                j = j + 1
                cows += 1

            else:

                i = i + 1
                j = j + 1
                bulls += 1
        print('my list was',computer)
        print ('cows are:', cows)
        print ('bulls are', bulls)
    elif choice.upper() == "N":
     exit()