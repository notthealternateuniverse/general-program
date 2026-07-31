n=int(input('enter a number: '))
x=n
i=1
sam = 0
while n:
   ones=n%10
   sam+=ones
   n=n//10
print("sum =",sam)
