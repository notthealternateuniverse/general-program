n=int(input('enter a 3-digit number: '))
i=1
new=0
while n:
     ones=n%10
     new=new*10+ones
     n=n//10
print(new)