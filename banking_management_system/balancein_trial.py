#<------------------------------------------BALANCE ENQUIRY-------------------------------------------------->
from list_trial import list
acc_no=int(raw_input("enter the account number:"))
for dict in list:
    for keys,values in dict.iteritems():
        if dict['acc.no']==acc_no:
            print "account number of the holder:",dict['acc.no']
            print "balance in the account is :",dict['acc amount']
            exit()
        else:
            print "INVALID ACCOUNT NUMBER"
