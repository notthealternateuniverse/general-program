n =  int(input("n="))
x = 0
count = 0
print("the even digits in this integer are:",end='')
while n:
    x = n%10
    if x%2==0:
        print(x)
        count+=1
    n = n//10
print("no of even digits =",count)
    
