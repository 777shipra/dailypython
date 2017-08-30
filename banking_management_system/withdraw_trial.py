#<----------------------------------------WITHDRAW AMOUNT----------------------------------------------------->
from list_trial import list
acc_no=int(raw_input("enter the account number:"))
acc_amount=int(raw_input("enter the amount to  withdraw:"))
for dict in list:
    for keys,values in dict.iteritems():
        if dict['acc.no']==acc_no:
            if dict['acc amount']>acc_amount:
                dict['acc amount']=dict['acc amount']-acc_amount
                print "amount after withdraw :",dict['acc amount']
                exit()
            else:
                print "amount is less in account"
                exit()
        else:
            print "INVALID ACCOUNT NUMBER"
            exit()