file=open("a.text","r")
count=0
for lines in file :

    count=count+1
print ("names in the files are",count)

file.close()