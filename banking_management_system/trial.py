list=[{
    "acc.no":1234567890,
    "acc. name":"shipra",
    "acc type":"c",
    "acc amount":1200
},
{
    "acc.no":1234567891,
    "acc. name":"raj",
    "acc type":"c",
    "acc amount":100
}]
a=int(raw_input("enter the acc no:"))
b=int(raw_input("enter the amount :"))
for dict in list:
    for keys,values in dict.iteritems():
        if dict['acc.no']==a:
            print dict
            dict['acc amount']=dict['acc amount']+b
            print "after deposit amount is :",dict['acc amount']
            break
#<----------------------------------------WITHDRAW AMOUNT----------------------------------------------------->
acc_no=int(raw_input("enter the account number:"))
acc_amount=int(raw_input("enter the amount to  withdraw:"))
for dict in list:
    for keys,values in dict.iteritems():
        if dict['acc.no']==acc_no:
            if dict['acc amount']>acc_amount:
                dict['acc amount']=dict['acc amount']-acc_amount
                print "amount after withdraw :",dict['acc amount']
            else:
                print "amount is less in account"
        else:
            print "INVALID ACCOUNT NUMBER"