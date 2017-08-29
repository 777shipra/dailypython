from list_trial import list
acc_no=int(raw_input("enter the account number:"))
for dict in list:
    for keys,values in dict.iteritems():
        if dict['acc.no']==acc_no:
            print dict
            new_acc_name=raw_input("enter the name:")
            dict['acc. name']=new_acc_name
            new_acc_type=raw_input("enter the type of account:")
            dict['acc type']=new_acc_type
            print dict
            break
