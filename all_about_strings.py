str='hello world'
#accessing characters in string
print str
print str[0]
print str[2:5]
print str[2:]
print str*2
print str + 'TEST'
print str[:7]
print str[::-1]
print str[::]
print str[:2:-1]
#operations in string
list_enumerate=list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)
print len(str)
del str #delete the whole string
#format  method in string
# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')

print('\n--- Keyword Order ---')
print(keyword_order)
#some more methods used in string like replace(),find(),split(),join(),.upper(),.lower()
print 'program'.upper()
print 'SBXSVC'.lower()
print "this will split all the words into a list".split()
list=["this","will","join"]
print " ".join(list)
print "happy new year".find("ppy")
print "happy python programming".replace("happy","enjoy")



