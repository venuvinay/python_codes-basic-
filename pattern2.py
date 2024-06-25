n=int(input())
sp=n
for i in range(n):
    for k in range(sp-1):
        print(" ",end="")
    for j in range(1,i+2):
        print(j,end="")
    print()
    sp-=1
