num = int(input("Enter the value of fibonaci: "))
n0 = 0
n1 = 1
nold = 0
nnew = 1
a = 0
nprint = 0
print(nold,nnew, sep="\n")
while a <= num:
        nprint = nnew+nold
        nold = nnew
        nnew = nprint
        print(nprint)
        a += 1