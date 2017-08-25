import random
line = random.choice(open('sowpods.txt').readlines())
print line
count=0
i=0
dashes=0
word=[]
guess=[]
word.extend(line)
print word
print "<----------welcome to HANGMAN----------->"
print "guess the word , BEWARE you just got 6 chances \n LET'S GO"
for w in word:
     guess.append("-")
print guess
your_guess=[]
while count<=5:
    a=raw_input("enter your character:")
    for index,w in enumerate(word):
        for index, dashes in enumerate(guess):
            if w == a:


        else:
            for index, dashes in enumerate(guess):
                pass

    print guess






