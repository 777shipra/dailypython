from datetime import datetime
from datetime import datetime,timedelta

#prints current date and time
now=datetime.now()

print now
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second

#use of timedelta()
print "1 week ago was it: ", now - timedelta(weeks=1)
print "100 days ago was: ", now - timedelta(days=100)
print "1 week from now is it: ",  now + timedelta(weeks=1)
print "In 1000 days from now is it: ", now + timedelta(days=1000)
#days pending for birthday

birthday = datetime(2012,11,04)

print "Birthday in ... ", birthday - now