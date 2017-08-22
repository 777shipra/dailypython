import random
line = random.choice(open('sowpods.txt').readlines())
print line
count=0
print "<----------welcome to HANGMAN----------->"
print "guess the word , BEWARE you just got 6 chances \n LET'S GO"
for char in line:
    print "-",

guess=raw_input("enter your character:")
for char in line:
            if guess == char:
                print char,
            else:
                print "-",



