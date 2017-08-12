my_str = raw_input("enter your sentence")
words = my_str.split()
words.sort()
list=[]
print("The sorted words are:")
for word in words:
   list.append(str(word))
print ','.join(list)