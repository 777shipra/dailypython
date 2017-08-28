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
            dict['acc amount']=dict['acc amount']+b
            break
print list
