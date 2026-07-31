x=int(input('enter input: '))
n=int(input('enter n: '))
i=1
a=0
while i<=n:
    a+=x/i
    i+=1
print('sum of series is',a)