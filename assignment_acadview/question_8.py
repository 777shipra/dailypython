sentence=raw_input("enter your sentence :")

letters=0
digits=0
for x in sentence:
    if x.isalpha():
        letters +=1

    elif x.isdigit():
        digits +=1
print letters
print digits
