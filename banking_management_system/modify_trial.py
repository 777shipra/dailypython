from list_trial import list
acc_no=int(raw_input("enter the account number:"))
for dict in list:
    for keys,values in dict.iteritems():
        if dict['acc.no']==acc_no:
            print dict.values()
            new_acc_name=raw_input("enter the name:")
            if len(new_acc_name)>0:
               dict['acc. name']=new_acc_name
            else:
                print "<----------INVALID NAME----------->"

            new_acc_type=raw_input("enter the type of account:")
            if (len(dict['acc type']) == 1 and dict['acc type'] == "c" or dict['acc type'] == "C" or dict[ 'acc type'] == "S" or dict['acc type'] == "s"):

                dict['acc type']=new_acc_type
            else:
                print "<------------WRONG ACCOUNT TYPE--------->"
            print dict
            break
