n=int(input('enter number: '))
i=1
count=0
print('factors are: ',end='')
while i<=n:
  if n%i==0:
   print(i,end=',')
   count+=1
  i+=1
print('\nno. of factors are: ',count)