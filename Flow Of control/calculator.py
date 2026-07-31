  a=int(input('enter num1 : '))
  b=int(input('enter num2: '))
  op=input('enter operator [+,-,*,/]: ')
  if op == '+':
    print(a,'+',b,'=',a+b)
  elif op == '-':
    print(a,'-',b,'=',a-b)
  elif op=='*':
    print(a,'x',b,'=',a*b)
  elif op=='/':
    print(a,'/',b,'=',a/b)
  else:
    print('invalid operator')
