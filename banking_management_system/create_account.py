def create_account():
    acc_no=int(raw_input("enter the account number:"))
    acc_name=raw_input("enter the name of the account holder:")
    acc_type=raw_input("enter the type of account (C/S):")
    acc_amount=int(raw_input("enter the amount \n (NOTE:amount>=500 for S and amount>=1000 for C): "))
    print "<-----ACCOUNT CREATED----->"
