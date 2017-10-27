from globals import Record,record
def create_account():

    print "<--------WELCOME , CREATE YOUR ACCOUNT------->"
    new_Record=Record(" ",0," ",0)
    new_Record.number=raw_input("enter the account number:")
    if (len(new_Record.number)>0 and len(new_Record.number)==10):
             new_Record.name=raw_input("enter the name of the account holder:")
    else:
            print "<---INVALID ACCOUNT NUMBER,PLEASE TRY AGAIN--->"
    if(len(new_Record.number)>0 and len(new_Record.number)==10):
        new_Record.type=raw_input("enter the type of account (C/S):")
        if (len(new_Record.type)==1 and (new_Record.type=="c" or new_Record.type=="C" or new_Record.type=="S"or new_Record.type=="s")):
            new_Record.amount=int(raw_input("enter the amount \n (NOTE:amount>=500 for S and amount>=1000 for C): "))
            if ((new_Record.type=="s"or new_Record.type=="S") and new_Record.amount>=500) or ((new_Record.type=="c" or new_Record.type=="C") and new_Record.amount>=1000):
                print "<-----ACCOUNT CREATED----->"
                record.append(new_Record)
                print str(new_Record.name)+" whose account number "+str(new_Record.number)+" of account type "+str(new_Record.type)+" with balance "+str(new_Record.amount)+" is added successfully"


            else:
                print "<-----NOT CORRECT AMOUNT----->"
        else:
            print "<-----INVALID ACCOUNT TYPE ,TYPE AGAIN (C=current/S=saving)"
def deposit_amount():
    entered_acc_no=int(raw_input("enter the account number:"))
    amount_to_deposit=int(raw_input("enter the amount to be deposit:"))
    for number in record:
        for account_number in number:
            if entered_acc_no==account_number:#problem
                print dict
                record.amount = record.amount + entered_acc_no
                print "after deposit amount is :", record.amount
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