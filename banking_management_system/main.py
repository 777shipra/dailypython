record=[]
def create_account():
    dict={
        "account number":0,
        "account holder name":"",
        "account type":"",
        "account amount":0,

    }
    print "<--------WELCOME , CREATE YOUR ACCOUNT------->"
    dict['acc_no']=raw_input("enter the account number:")
    if (len(dict['acc_no'])>0 and len(dict['acc_no'])==10):
             dict['acc_name']=raw_input("enter the name of the account holder:")
    else:
            print "<---INVALID ACCOUNT NUMBER,PLEASE TRY AGAIN--->"
    if(len(dict['acc_no'])>0 and len(dict['acc_no'])==10):
        dict['acc_type']=raw_input("enter the type of account (C/S):")
        if (len(dict['acc_type'])==1 and dict['acc_type']=="c" or dict['acc_type']=="C" or dict['acc_type']=="S"or dict['acc_type']=="s"):
            dict['acc_amount']=int(raw_input("enter the amount \n (NOTE:amount>=500 for S and amount>=1000 for C): "))
            if ((dict['acc_type']=="s"or dict['acc_type']=="S") and dict['acc_amount']>=500) or ((dict['acc_type']=="c" or dict['acc_type']=="C") and dict['acc_amount']>=1000):
                print "<-----ACCOUNT CREATED----->"
                record.append(dict)
                print record


            else:
                print "<-----NOT CORRECT AMOUNT----->"
        else:
            print "<-----INVALID ACCOUNT TYPE ,TYPE AGAIN (C=current/S=saving)"
def deposit_amount():
    entered_acc_no=int(raw_input("enter the account number:"))
    amount_to_deposit=int(raw_input("enter the amount to be deposit:"))
    for dict in record:
        for key,values in dict:
            if entered_acc_no==dict['acc_no']:
                print dict
                dict['acc_amount'] = dict['acc_amount'] + entered_acc_no
                print "after deposit amount is :", dict['acc_amount']
                break
            else:
                print "<-----INVALID ACCOUNT NUMBER----->"
print "Welcome to BANKING MANAGEMENT SYSTEM \n <---------------MAIN MENU--------------->"
while True:
    print "\t 1:NEW ACCOUNT \n \t 2:DEPOSIT AMOUNT \n\t 3:WITHDRAW AMOUNT \n\t 4:BALANCE ENQUIRY \n\t 5:ALL ACCOUNT HOLDER LIST \n\t 6:CLOSE AN ACCOUNT \n\t 7:MODIFY AN ACCOUNT \n\t 8:EXIT"
    choice=int(raw_input("Make your choice (1-8):"))
    if choice==1:
       create_account()
    elif choice==2:
       deposit_amount()
    elif choice==3:
        print "code"
    elif choice==4:
        print "code"
    elif choice==5:
        print "code"
    elif choice==6:
        print "code"
    elif choice==7:
        print "code"
    elif choice==8:
        print "code"
    else:
        print "INVALID CHOICE. Please choose between (1-8)"