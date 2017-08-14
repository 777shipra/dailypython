dictionary={
    "ram":"kumar"
}
key=raw_input("enter name")
value=raw_input("enter value")
dictionary.update({key:value})
print dictionary
print dictionary.keys()#get all the keys
print dictionary.values()#get all the values
print dictionary["ram"]#get the corresponding value
del dictionary["ram"]#del the mentioned key
print dictionary
dictionary.clear()#clear all the contents of the dictionary
print dictionary
del dictionary#deletes the entire dictionary
dict1={
    "name":"shipra",
    "college":"mmu",
    "course":"cse",
    "rollno":"11142501"
}
dict2={
    "name":"shipra",
    "friend":"ruhi",
    "course":"mech"
  }
print cmp(dict1,dict2)#campare the two dictionary ,return 0 if the length is same 1 if the dict1>dict2 and -1 if opposite
dict2=dict1.copy()#copies the content of one into another
print dict2
#the following code is to give multiple keys with same values
seq=("fruit","glass","chemical")
value=(10,20,30)
dict2=dict2.fromkeys(seq,value)
print dict2
print dict2.get("chemical")#get the corresponding value
print dict1.items()#returns a list of tuples containing the details
