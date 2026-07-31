  a=int(input('enter a 2-digit number: '))
  tens=a//10
  ones=a%10
  if tens%2==0:
    print('tens digit is even.')
  else:
    print('tens digit is odd.')
  if ones%2==0:
    print('ones digit is even.')
  else:
    print('ones digit is odd.')
  
