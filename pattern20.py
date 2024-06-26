n=int(input())
sp=n
for i in range(n):
    for l in range(i):
        print(" ",end=" ")
    for j in range(1,sp*2):
        print("*",end=" ")
    print()
    sp-=1
b=n-1
g=3
for i in range(b):
    for l in range(b-1):
        print(" ",end=" ")
    for j in range(g):
        print("*",end=" ")
    print()
    b-=1
    g+=2
