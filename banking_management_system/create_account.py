def create_account():
    print "<--------WELCOME , CREATE YOUR ACCOUNT------->"
    acc_no=(raw_input("enter the account number:"))
    if (len(acc_no)>0 and len(acc_no)==10):
             acc_name=raw_input("enter the name of the account holder:")
    else:
            print "<---INVALID ACCOUNT NUMBER,PLEASE TRY AGAIN--->"
    while(len(acc_no)>0 and len(acc_no)==10):
        acc_type=raw_input("enter the type of account (C/S):")
        if (len(acc_type)==1 and acc_type=="c" or acc_type=="C" or acc_type=="S"or acc_type=="s"):
            acc_amount=int(raw_input("enter the amount \n (NOTE:amount>=500 for S and amount>=1000 for C): "))
            if ((acc_type=="s"or acc_type=="S") and acc_amount>=500) or ((acc_type=="c" or acc_type=="C") and acc_type>=1000):
                print "<-----ACCOUNT CREATED----->"
            else:
                print "<-----NOT CORRECT AMOUNT----->"
        else:
            print "<-----INVALID ACCOUNT TYPE ,TYPE AGAIN (C=current/S=saving)"


