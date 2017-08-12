N=int(raw_input("enter your number"))
a, b, c ,d = N % 2, N / 10 % 2, N / 100 % 2,N / 1000 % 2
if (a ^ b) or (a ^ c) or (a^d):
    print 'The number contains both even and odd digits'
elif a:
    print 'The number contains all odd digits'
else:
    print 'The number contains all even digits'