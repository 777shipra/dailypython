from list_trial import list
acc_no=int(raw_input("enter the account number:"))
for dict in list:
    for keys,values in dict.iteritems():
        if dict['acc.no']==acc_no:
            list.remove(dict)
            print "<------------ACCOUNT CLOSED------------->"
            exit()
        else:
            print "<----------INVALID ACCOUNT NUMBER---------->"