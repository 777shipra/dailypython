x=input("enter the number from where u want to begin the series")
y=input("enter the number where you want to end series")
even = 0
odd = 0
for a in range(x,y) :

    if a % 2 == 0 :
        even += 1
    else:
        odd += 1
print ("evens are : ",even)
print ("odd are : ",odd)
