n=int(input('enter a number: '))
count=0
while n:
    n=n//10
    count+=1
print('no. of digits is',count)
