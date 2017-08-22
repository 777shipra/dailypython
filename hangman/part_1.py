import random
line = random.choice(open('sowpods.txt').readlines())
print line
count=0
word=[]
guess=[]
word.append(line)
print "<----------welcome to HANGMAN----------->"
print "guess the word , BEWARE you just got 6 chances \n LET'S GO"
for w in word:
    for char in w:
     guess.append("-")
print guess
your_guess=[]
a=raw_input("enter your character:")
for w in word:
    for char in w:
        if a==char:
            guess.append(char)
        else:
            guess.append("-")
print guess





