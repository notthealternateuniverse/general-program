n=int(input('enter no.: '))
flag=0
i=2
while i<=n-1:
    if n%i==0:
      flag=1
      break
    i+=1                                                                                
if flag==0:
    print('it is a prime.')
else:
    print('not prime.')
