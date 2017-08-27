def create_account():
    print "<--------WELCOME , CREATE YOUR ACCOUNT------->"
    dict['acc_no']=raw_input("enter the account number:")
    if (len(dict['acc_no'])>0 and len(dict['acc_no'])==10):
             dict['acc_name']=raw_input("enter the name of the account holder:")
    else:
            print "<---INVALID ACCOUNT NUMBER,PLEASE TRY AGAIN--->"
    while(len(dict['acc_no'])>0 and len(dict['acc_no'])==10):
        acc_type=raw_input("enter the type of account (C/S):")
        if (len(dict['acc_type'])==1 and dict['acc_type']=="c" or dict['acc_type']=="C" or dict['acc_type']=="S"or dict['acc_type']=="s"):
            dict['acc_amount']=int(raw_input("enter the amount \n (NOTE:amount>=500 for S and amount>=1000 for C): "))
            if ((dict['acc_type']=="s"or dict['acc_type']=="S") and dict['acc_amount']>=500) or ((dict['acc_type']=="c" or dict['acc_type']=="C") and dict['acc_amount']>=1000):
                print "<-----ACCOUNT CREATED----->"

            else:
                print "<-----NOT CORRECT AMOUNT----->"
        else:
            print "<-----INVALID ACCOUNT TYPE ,TYPE AGAIN (C=current/S=saving)"


