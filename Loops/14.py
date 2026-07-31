n=int(input('enter number: '))
i=1
print('factors are: ',end='')
while i<=n:
  if n%i==0:
    print(i,end=',')
  i+=1