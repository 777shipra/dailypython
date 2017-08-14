list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print list[0]
print list[1:3]
print list[2:]
print list*2
print list + list*3
print list[::]
print list[::-1]
print list[:2:-1]
print list[:-2]
#nested list can be too there
my_list=["hello",[1,2,3],"bye"]
print my_list
#append() and extend()
list.append('brother')
print list
list.extend('sister')
print list
#insert() into list at desired position
list.insert(1, "hello")
print list
list[2]=[198,112]
print list