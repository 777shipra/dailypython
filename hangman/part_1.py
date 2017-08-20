import random
line = random.choice(open('sowpods.txt').readlines())
print line
print "<----------welcome to HANGMAN----------->"
print "guess the word , BEWARE you just got 6 chances \n LET'S GO"
for words in line:
    print '_',



