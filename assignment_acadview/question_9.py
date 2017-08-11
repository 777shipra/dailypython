sentence=raw_input("enter your sentence :")

uppercase_letters=0
lowercase_letters=0
for x in sentence:
    if x.isupper():
        uppercase_letters +=1

    elif x.islower():
        lowercase_letters +=1
print uppercase_letters
print lowercase_letters
