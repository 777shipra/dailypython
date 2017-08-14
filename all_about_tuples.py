tup=(1,2,3,4)
tuplex=(5,7,8)
print tup[0]
print tup[1:2]
print len(tup)
tup3=tup+tuplex#concatination because modification cannot be done
print tup3
print tup3*3
print tup[2:]
print tup[-2]
print cmp(tup,tup3)#comparision between tuple
print max(tup3)#returns max value
print min(tup3)#returns min value
#converts list into tuple
list=["hello","world"]
atuple=tuple(list)
print atuple
