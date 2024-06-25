n=int(input())
sp=n
for i in range(1,n+1):
    for k in range(sp-1):
        print(" ",end="")
    for j in range(1,i*2):
        print("*",end="")
    print()
    sp-=1
f=2*i-2
for i in range(1,n):
    for k in range(i):
        print(" ",end="")
    for j in range(1,f):
        print("*",end="")
    print()
    f-=2
    
