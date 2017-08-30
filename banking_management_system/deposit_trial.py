#<-------------------------------------DEPOSIT AMOUNT-------------------------------------------------->
from list_trial import list
a=int(raw_input("enter the acc no:"))
b=int(raw_input("enter the amount :"))
for dict in list:
    for keys,values in dict.iteritems():
        if dict['acc.no']==a:
                    print dict
                    dict['acc amount']=dict['acc amount']+b
                    print "after deposit amount is :",dict['acc amount']
                    exit()
        else:
                    print "<----------INVALID ACCOUNT NUMBER------------>"
