n=int(input('enter a number: '))
big = 0
while n:
   oi = n%10
   if oi>big:
      big=oi
   n=n//10
print(big)
