n=int(input('enter a number: '))
x=n
i=1
new=0
while n:
   ones=n%10
   new=new*10+ones
   n=n//10
if new==x:
 print('it is a palindrome.')
else:
 print('it is not a palindrome.')
