  a=int(input('enter num1: '))
  b=int(input('enter num2:'))
  c=int(input('enter num3: '))
  if a<b<c:
    print(a,b,c,'are in ascending order')
  elif a<c<b:
    print(a,c,b,'are in ascending order')
  elif b<c<a:
    print(b,c,a,'are in ascending order')
  elif b<a<c:
    print(b,a,c,'are in ascending order')
  elif c<a<b:
    print(c,a,b,'are in ascending order')
  elif c<b<a:
    print(c,b,a,'are in ascending order')
  else:
    print('all are equal')
